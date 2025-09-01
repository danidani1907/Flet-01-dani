import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.padding = 20

    # Caixa colorida
    caixa_colored = ft.Container(
        content=ft.Text(
            "Escolha uma cor! 🎨",
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor=ft.Colors.GREY,
        width=300,
        height=100,
        border_radius=10,
        alignment=ft.alignment.center
    )

    # Função executada quando escolhe a cor
    def cor_selecionada(evento):
        cor_escolhida = evento.control.value

        cores_disponiveis = {
            "Azul": ft.Colors.BLUE,
            "Verde": ft.Colors.GREEN,
            "Vermelho": ft.Colors.RED,
            "Roxo": ft.Colors.PURPLE,
            "Laranja": ft.Colors.ORANGE,
            "Rosa": ft.Colors.PINK
        }

        caixa_colored.bgcolor = cores_disponiveis[cor_escolhida]
        caixa_colored.content.value = "Cor selecionada: " + cor_escolhida + " ✨"

        page.update()

    # Dropdown
    seletor_cor = ft.Dropdown(
        label="Escolha uma cor",
        width=200,
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Rosa"),
        ],
        on_change=cor_selecionada
    )

    # Elementos na tela
    page.add(
        ft.Text("Seletor de Cores Mágico! ✨", size=24, weight=ft.FontWeight.BOLD),
        seletor_cor,
        caixa_colored
    )

ft.app(target=main)
