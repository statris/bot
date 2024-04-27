import disnake
from disnake.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def бан(self, interaction, пользователь: disnake.User, причина: str):
        await interaction.guild.ban(пользователь, reason=причина)
        await interaction.response.send_message(
            f"Пользователь {пользователь.mention} был забанен по причине: {причина}",
            ephemeral=True
        )

    @commands.slash_command()
    async def разбан(self, interaction, пользователь: disnake.User):
        await interaction.guild.unban(пользователь)
        await interaction.response.send_message(
            f"Пользователь {пользователь.mention} был разбанен.",
            ephemeral=True
        )


def setup(bot):
    bot.add_cog(Ban(bot))