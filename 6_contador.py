#contador

import flet as ft

def main(page: ft.Page):
    page.title = "Contador Simples"
    page.padding = 20

    # Texto que exibe o valor do contador
    display_contador = ft.Text(
        value="0",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
        text_align=ft.TextAlign.CENTER
    )

    

  