# aplicativo.py
import flet as ft
# pip install flet
def main(page: ft.Page):
    page.title = "Exemplo Educacional - Senac" # Titulo
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Column(
            [
                ft.Text("Olá, Flet no navegador!"),
                ft.ElevatedButton("Clique aqui", on_click=lambda e: page.snack_bar.open and None),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
 
if __name__ == "__main__":
    # use a enum atual:
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)