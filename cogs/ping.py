import disnake
from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def пинг(self, interaction: disnake.CommandInteraction):
        await interaction.response.send_message("понг!")


def setup(bot):
    bot.add_cog(Ping(bot))