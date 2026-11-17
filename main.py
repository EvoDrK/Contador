import flet as ft


def main(page: ft.Page):
    # 1. Configuración de la ventana
    page.title = "Contador con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    contador = 0
    texto = ft.Text(value="0", size=60)

    # 2. Función que responde al evento
    def incrementar(e):
        nonlocal contador
        contador += 1
        texto.value = str(contador)
        page.update()  # 3. Refresca la interfaz

    boton = ft.IconButton(ft.Icons.ADD, on_click=incrementar)

    page.add(texto, boton)


ft.run(main)