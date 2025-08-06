import flet as ft
import re

def main(page: ft.Page):
    page.title = "Beautiful Calculator"
    page.bgcolor = "#1a1a2e"
    page.window.width =  400
    page.window.height = 620
    page.padding = 20
    page.update()

    all_values = ""

    result_text = ft.Text(
        value="0", 
        size=32, 
        color="white",
        text_align="right",
        weight=ft.FontWeight.W_300
    )

    def delete_last(e):
        nonlocal all_values
        all_values = all_values[:-1]
        result_text.value = all_values if all_values else "0"
        page.update()

    def entering_values(e):
        nonlocal all_values
        t = str(e.control.text)
        
        if t == ".":
            parts = re.split(r"[+\-*/%]", all_values)
            if "." in (parts[-1] if parts else ""):
                return
        all_values += t
        result_text.value = all_values
        page.update()

    def clear_screen(e):
        nonlocal all_values
        all_values = ""
        result_text.value = "0"
        page.update()

    def safe_eval(expr):
        expr = re.sub(r"(\d+(\.\d+)?)%", r"(\1/100)", expr)
        if not re.fullmatch(r"[\d\.\+\-\*/\(\) ]+", expr):
            raise ValueError("Invalid input")
        return eval(expr)

    def calculate(e):
        nonlocal all_values
        try:
            expression = all_values
            result = safe_eval(expression)
            result_text.value = str(result)
            all_values = str(result)
            result_text.color = "white"
        except:
            result_text.value = "Error"
            result_text.color = "#ff6b6b"
            all_values = ""
        page.update()

    display = ft.Container(
        content=result_text,
        bgcolor="#2c3e50",
        padding=20,
        border_radius=15,
        height=80,
        alignment=ft.alignment.center_right,
        border=ft.border.all(2, "#34495e"),
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color="#00000040",
            offset=ft.Offset(0, 5)
        )
    )

    number_style = {
        "height": 65,
        "bgcolor": "#34495e",
        "color": "white",
        "expand": 1,
    }
    operator_style = {
        "height": 65,
        "bgcolor": "#f39c12",
        "color": "white", 
        "expand": 1,
    }
    clear_style = {
        "height": 65,
        "bgcolor": "#e74c3c",
        "color": "white",
        "expand": 1,
    }
    equal_style = {
        "height": 65,
        "bgcolor": "#27ae60",
        "color": "white",
        "expand": 1,
    }

    button_grid = [
        [
            ("C", clear_style, clear_screen),
            ("DEL", clear_style, delete_last),
            ("%", operator_style, entering_values),
            ("/", operator_style, entering_values),
        ],
        [
            ("7", number_style, entering_values),
            ("8", number_style, entering_values),
            ("9", number_style, entering_values),
            ("*", operator_style, entering_values),
        ],
        [
            ("4", number_style, entering_values),
            ("5", number_style, entering_values),
            ("6", number_style, entering_values),
            ("-", operator_style, entering_values),
        ],
        [
            ("1", number_style, entering_values),
            ("2", number_style, entering_values),
            ("3", number_style, entering_values),
            ("+", operator_style, entering_values),
        ],
        [
            ("0", {**number_style, "expand": 2}, entering_values),
            (".", number_style, entering_values),
            ("=", equal_style, calculate),
        ],
    ]

    buttons = []
    for row in button_grid:
        row_controls = []
        for text, style, handler in row:
            btn = ft.ElevatedButton(
                text=text,
                on_click=handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=12),
                    padding=0,
                    elevation=3,
                    shadow_color="#00000030"
                )
            )
            row_controls.append(btn)
        buttons.append(ft.Row(row_controls, spacing=8))

    main_container = ft.Container(
        content=ft.Column([
            ft.Row([ft.Text("Calculator", size=24, color="white", weight="bold")],
                   alignment="center"),
            display,
            ft.Container(height=15),
            ft.Column(buttons, spacing=10)
        ], spacing=5),
        bgcolor="#16213e",
        padding=20,
        border_radius=20,
        border=ft.border.all(1, "#0f3460"),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color="#00000050",
            offset=ft.Offset(0, 8)
        ),
    )

    page.add(main_container)

ft.app(target=main)