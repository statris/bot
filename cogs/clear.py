import disnake
from disnake.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def удалить(self, interaction, количество: int):
        embed = disnake.Embed(title="Очистка", description=f"Вы удалили {количество} сообщений.", color=0x00ff00)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.purge(limit=количество + 1)


def setup(bot):
    bot.add_cog(Clear(bot))