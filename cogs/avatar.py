import disnake
from disnake.ext import commands


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def аватар(self, interaction, пользователь: disnake.Member = None):
        member = пользователь or interaction.author
        embed = disnake.Embed(
            title=f"Аватар – {member}",
            color=0x2F3136
        )
        embed.set_image(url=member.display_avatar)
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Avatar(bot))