import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.bgcolor = "#2d2d22d"
    page.window.width = 350
    page.window.height = 470
    page.padding = 10
    
    result_text = ft.Text(value="0", size=40, color="white", text_align="right")
    
    display = ft.Container(
        content=result_text,
        bgcolor="#3d3d3d",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right,
    )
    
    page.add(
        
        ft.Column(
            [
              display,
              ft.Row(
                  [
                      ft.ElevatedButton("7", on_click=lambda _: result_text.update(value="7")),
                      ft.ElevatedButton("8", on_click=lambda _: result_text.update(value="8")),
                      ft.ElevatedButton("9", on_click=lambda _: result_text.update(value="9")),
                      ft.ElevatedButton("/", on_click=lambda _: result_text.update(value="/"))
                  ]
              ),    
                
            ],
        )
    )
ft.app(target=main)