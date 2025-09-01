# layout basico

import flet as ft

def main(page: ft.Page):
    page.title = "Layout Básico"
    page.padding = 20

    # Título
    titulo = ft.Text(
        "Deixando organizado! 📐",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    # Linha horizontal com 3 botões
    linha_botoes = ft.Row(
        controls=[
            ft.ElevatedButton(text="Botão", bgcolor=ft.Colors.PURPLE, color=ft.Colors.WHITE, width=100),
            ft.ElevatedButton(text="Botão", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE, width=100),
            ft.ElevatedButton(text="Botão", bgcolor=ft.Colors.PINK, color=ft.Colors.WHITE, width=100),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # Caixas coloridas
    caixa1 = ft.Container(
        content=ft.Text("Caixa 1", color=ft.Colors.WHITE, size=18, text_align=ft.TextAlign.CENTER),
        bgcolor=ft.Colors.ORANGE,
        width=150,
        height=100,
        alignment=ft.alignment.center,
        border_radius=10
    )

    caixa2 = ft.Container(
        content=ft.Text("Caixa 2", color=ft.Colors.WHITE, size=18, text_align=ft.TextAlign.CENTER),
        bgcolor=ft.Colors.GREEN,
        width=150,
        height=100,
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Coluna com as caixas
    coluna_caixas = ft.Column(
        controls=[caixa1, caixa2],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    # Layout principal
    layout_principal = ft.Column(
        controls=[
            titulo,
            ft.Text("Usando Colunas e Linhas para organizar a tela", size=18, text_align=ft.TextAlign.CENTER),
            linha_botoes,
            ft.Text("Caixas coloridas organizadas em coluna:", size=18, text_align=ft.TextAlign.CENTER),
            coluna_caixas,
            ft.Text("Fim do layout básico! 🎉", size=18, text_align=ft.TextAlign.CENTER)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30
    )

    # Adicionando o layout principal na página
    page.add(layout_principal)

ft.app(target=main)

