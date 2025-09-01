#primeiro botão

import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão"
    page.padding = 20

    # Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo! 👇",
        size=20,
        text_align = ft.TextAlign.CENTER
    )

    # Função que será chamada quando o botão for clicado
    def botao_clicado(evento):
        mensagem.value = "🎉 Parabéns! Você clicou no botão!"
        mensagem.color = ft.Colors.GREEN
        page.update()  # Atualiza a interface

    # Criando o botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!",    # Texto no botão
        on_click=botao_clicado,   # Função executada ao clicar
        width=200,                # Largura
        height=50,                # Altura
        bgcolor=ft.Colors.BLUE,   # Cor de fundo
        color=ft.Colors.WHITE     # Cor do texto
    )

    # Adicionando os elementos na página
    page.add(mensagem)
    page.add(meu_botao)

# Executa a aplicação
ft.app(target=main)
