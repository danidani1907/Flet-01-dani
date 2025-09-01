#primeiro programa em python com flet
import flet as ft 

def main(page: ft.Page):

    #configurações da página
    page.title = " Meu primeiro App flet"
    page.padding = 20 # espaçamento interno

    #criando um texto
    meu_texto = ft.Text(
        value="Olá, Mundo!",
        size=24, 
        color=ft.Colors.BLUE, 
        weight=ft.FontWeight.BOLD, 
        text_align=ft.TextAlign.CENTER
    )
    
    #adicionando o texto na página
    page.add(meu_texto)

    #atualizando a página
    page.add(
        ft.Text("bem-vindo ao mundo do desenvolvimento de apps com flet!", size=16),
        ft.Text("texto 2", size=16, color=ft.Colors.GREEN)
    )


ft.app(target=main)

  
