import disnake
from disnake.ext import commands


class RecruitementModal(disnake.ui.Modal):
    def __init__(self, arg):
        self.arg = arg

        components = [
            disnake.ui.TextInput(label="Ваше имя", placeholder="Введите ваше имя", custom_id="name"),
            disnake.ui.TextInput(label="Ваш возраст", placeholder="Введите ваш возраст", custom_id="age")
        ]

        if self.arg == "модератор":
            title = "Набор на должность модератора"
        else:
            title = "Набор на должность ведущего"

        super().__init__(title=title, components=components, custom_id="recruitementModal")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        name = interaction.text_values["name"]
        age = interaction.text_values["age"]

        embed = disnake.Embed(color=0x2F3136, title="Заявка отправлена!")
        embed.description = f"{interaction.author.mention}, Благодарим вас за **заявку**! " \
                            f"Если вы нам **подходите**, администрация **свяжется** с вами в ближайшее время."
        embed.set_thumbnail(url=interaction.author.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)

        channel = interaction.guild.get_channel(1233597087371890762)
        await channel.send(f"Заявка на должность {self.arg} от {name} {interaction.author.mention} ({age} лет)")


class RecruitementSelect(disnake.ui.Select):
    def __init__(self):

        options = [
            disnake.SelectOption(label="Модератор", value="модератор", description="Модератор сервера"),
            disnake.SelectOption(label="Ведущий", value="ведущий", description="Ведущий мероприятий"),
        ]

        super().__init__(
            placeholder="Выбери желаемую роль", options=options, min_values=0, max_values=1, custom_id="recruitement"
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_modal(RecruitementModal(interaction.values[0]))


class Recruitement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    @commands.command()
    async def заявка(self, ctx):
        view = disnake.ui.View()
        view.add_item(RecruitementSelect())

        await ctx.send('Выбери желаемую роль', view=view)

    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(RecruitementSelect())

        self.bot.add_view(view, message_id=1233598284967317534)


def setup(bot):
    bot.add_cog(Recruitement(bot))