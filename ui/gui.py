import flet as ft


def main(page: ft.Page):
    page.title = 'ШколоZVOн'

    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def click_schedule(e):

        for i in view_schedule.controls[0].controls:
            if i.data == e.control.data:
                i.content.controls[0].value = not i.content.controls[0].value
        page.update()
        pass

    schedule_ZVOnkov = ["1 расписание", "2 расписание", "3 расписание"]
    schedule = []

    for i in schedule_ZVOnkov:
        print(schedule_ZVOnkov.index(i))
        schedule.append(ft.Container(
            ft.Row(
                controls=[ft.Checkbox(value=False),
                          ft.Text(spans=[ft.TextSpan(i, on_click=lambda e: click_schedule(e), data=i)])]
            ),
            width=400,
            alignment=ft.alignment.Alignment(0, 0),
            border_radius=24,
            padding=20,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER),
            bgcolor="white",
            data=i
        ))

    view_schedule = ft.Row(
        [
            ft.Column(
                controls=schedule
            ),
            ft.Row([ft.FilledButton("Создать новое расписание")], alignment=ft.MainAxisAlignment.END)
        ]
    )

    page.add(
        view_schedule
    )


ft.app(target=main)
