# calculadora com operação quadrado
import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Campos de entrada
    numero1 = ft.TextField(label="Número 1", width=150, keyboard_type=ft.KeyboardType.NUMBER)
    numero2 = ft.TextField(label="Número 2", width=150, keyboard_type=ft.KeyboardType.NUMBER)
    operacao = ft.Dropdown(
        label="Operação",
        width=150,
        options=[
            ft.dropdown.Option("Somar"),
            ft.dropdown.Option("Subtrair"),
            ft.dropdown.Option("Multiplicar"),
            ft.dropdown.Option("Dividir"),
            ft.dropdown.Option("Elevado ao quadrado")
        ]
    )

    resultado = ft.Text(value="Resultado: ", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)

    # Função de cálculo
    def calcular(e):
        try:
            num1 = float(numero1.value)
            num2 = float(numero2.value) if numero2.value else 0
            op = operacao.value

            if not op:
                resultado.value, resultado.color = "‼️Resultado: Selecione uma operação", ft.Colors.GREY_600
            elif op == "Dividir" and num2 == 0:
                resultado.value, resultado.color = "‼️Resultado: Divisão por zero não é permitida", ft.Colors.RED
            else:
                simbolos = {
                    "Somar": ("+", num1 + num2),
                    "Subtrair": ("-", num1 - num2),
                    "Multiplicar": ("*", num1 * num2),
                    "Dividir": ("/", num1 / num2),
                    "Elevado ao quadrado": ("²", num1 ** 2)
                }

                simbolo, res = simbolos[op]

                if op == "Elevado ao quadrado":
                    resultado.value, resultado.color = f"✅Resultado: {num1}² = {res:.2f}", ft.Colors.GREEN
                else:
                    resultado.value, resultado.color = f"✅Resultado: {num1} {simbolo} {num2} = {res:.2f}", ft.Colors.GREEN

        except ValueError:
            resultado.value, resultado.color = "‼️Resultado: Insira números válidos", ft.Colors.RED

        page.update()

    # Função limpar
    def limpar(e):
        numero1.value = ""
        numero2.value = ""
        operacao.value = ""
        resultado.value, resultado.color = "🧽 Limpo", ft.Colors.PINK
        page.update()

    # Layout
    page.add(
        ft.Column(
            controls=[
                ft.Text("🧮 Calculadora Simples", size=24, weight=ft.FontWeight.BOLD),
                numero1,
                numero2,
                operacao,
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="Calcular", on_click=calcular, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, width=150),
                        ft.ElevatedButton(text="🧽 Limpar", on_click=limpar, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE, width=150),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Divider(),
                resultado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )

ft.app(main)
