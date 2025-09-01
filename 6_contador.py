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

    info_contador = ft.Text(
        value="Contador iniciado em 0",
        size=20,
        color=ft.Colors.PURPLE,
        text_align=ft.TextAlign.CENTER
    )

    def atualizar_display():
        # Atualiza o texto do display com o valor atual do contador
        display_contador.value = str(valor_contador)

        if valor_contador > 0:
           display_contador.value = "Contador positivo! 🎉"
        info_contador.color = ft.Colors.GREEN


  