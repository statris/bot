import datetime

import disnake
from disnake.ext import commands


class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def мьют(self, interaction, пользователь: disnake.Member, время: int, причина: str):
        if пользователь == interaction.author:
            return await interaction.response.send_message(
                "Вы не можете замьютить самого себя",
                ephemeral=True
            )

        if время < 1:
            return await interaction.response.send_message(
                "Вы не можете замьютить пользователя на меньше 1 минуты",
                ephemeral=True
            )

        time = datetime.datetime.now() + datetime.timedelta(minutes=время)
        await пользователь.timeout(until=time, reason=причина)
        cool_time = disnake.utils.format_dt(time, style="F")
        embed = disnake.Embed(
            title="Мьют",
            description=f"Пользователь {пользователь.mention} был замьючен. Причина: {причина}. "
                        f"Мьют будет снят в {cool_time}",
            color=0x2F3136
        ).set_thumbnail(url=пользователь.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.slash_command()
    async def размьют(self, interaction, пользователь: disnake.Member):
        await пользователь.timeout(until=None, reason=None)
        await interaction.response.send_message(
            f"Мьют с пользователя {пользователь.mention} был снят",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Timeout(bot))