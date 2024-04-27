import disnake
from disnake.ext import commands


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def профиль(self, interaction):
        embed = disnake.Embed(title="Название профиля", description="Описание профиля", color=0x00ff00)
        embed.add_field(name="Название поля 1", value="Значение поля 1", inline=False)
        embed.add_field(name="Название поля 2", value="Значение поля 2", inline=False)
        embed.add_field(name="Название поля 3", value="Значение поля 3", inline=False)
        embed.set_footer(text="Нижний колонтитул")
        embed.set_author(name="Автор профиля")
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Embed(bot))