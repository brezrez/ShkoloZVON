import flet as ft


def main(page: ft.Page):
    page.title = 'ШколоZVOн'

    timetable = ft.TextField(label='Название нового расписания')
    schedule_zvonkov = ['Полное расписание', 'Сокращенное расписание', 'Залупа']
    schedule = []

    # Перенесли определение bell_list и dialog_window наверх, чтобы функции их видели
    bell_list = ft.Column(
        [
            ft.TextField(label='Название расписания'),
            ft.Button('Добавить звонок', on_click=lambda e: new_bell(e))
        ],
        spacing=15,
        width=450,
        height=450,
        scroll=ft.ScrollMode.AUTO
    )


    def get_clicked(e):
        bell_list.controls = [timetable, ft.Button('Добавить звонок', on_click=new_bell)]
        dialog_window.open = True
        page.update()

    def new_bell(e):
        bell_list.controls.append(ft.TextField(label='Время', width=100))
        # Достаточно обновить только страницу, Flet обновит и диалог
        page.update()

    def click_schedule(e):

        for i in view_schedule.controls[0].controls:
            if i.data == e.control.data:
                i.content.controls[0].value = not i.content.controls[0].value
        page.update()
        pass


    schedule_zvonkov = ['Полное расписание', 'Сокращенное расписание', 'Залупа']


    def new_timetable(e):
        schedule_zvonkov.append(timetable.value)
        view_schedule = ft.Row(
            [
                ft.Column(
                    controls=start()
                ),
                ft.Row([ft.FilledButton("Создать новое расписание", on_click=get_clicked)],
                       alignment=ft.MainAxisAlignment.END, )
            ]
        )
        page.clean()
        page.add(view_schedule)
        print(schedule)
        page.update()
        page.close(dialog_window)
        timetable.value = ''
        schedule = []


    global bell_list
    bell_list = ft.Column([ft.TextField(label='Название расписания'), ft.Button('Добавить звонок', on_click=new_bell)], spacing=15, width=450, height=450, scroll=ft.ScrollMode.AUTO)

    dialog_window = ft.AlertDialog(
        title=ft.Text("Редактировать задание"),
        content=bell_list,
        actions=[
            ft.Button("Отмена",on_click = lambda e: page.close(dialog_window)),
            ft.Button("Сохранить", on_click=new_timetable),
        ],
    )
    global schedule

    schedule = []
    def start():
        for i in schedule_zvonkov:
            schedule.append(ft.Container(
                ft.Row(
                    controls=[
                        ft.Checkbox(value=False),
                        # Используем e.control.data, который передаем при клике
                        ft.Text(spans=[ft.TextSpan(i, on_click=click_schedule, data=i)], size=20),
                    ]
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
        return schedule

    def new_timetable(e):
        if timetable.value:
            schedule_zvonkov.append(timetable.value)

        # Вместо создания нового ft.Row, мы просто обновляем список элементов внутри main_column!
        main_column.controls = start()

        page.close(dialog_window)
        timetable.value = ''
        page.update()

    # Создаем фиксированную колонку для расписаний
    main_column = ft.Column(controls=start())

    # Главный каркас страницы, который мы НЕ меняем динамически, а только обновляем его внутренности
    view_schedule = ft.Row(
        [
            ft.Column(
                controls=start()
            ),
            ft.Row([ft.FilledButton("Создать новое расписание",on_click=get_clicked)], alignment=ft.MainAxisAlignment.END,)
        ]
    )



ft.app(target=main)

