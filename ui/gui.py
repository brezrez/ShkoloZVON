from data.сall_schedule import get_all_schedule, create_schedule, return_bells
from logic.timer import TimerMusic
from logic.music_player import MusicPlayer
from data.music import MusicHandler

import flet as ft


def main(page: ft.Page):
    page.title = 'ШколоZVOн'

    global tim

    timetable = ft.TextField(label='Название нового расписания')
    schedule_zvonkov = get_all_schedule()
    print(schedule_zvonkov)
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

    def close_dialog(e):
        page.close(dialog_window)

    dialog_window = ft.AlertDialog(
        title=ft.Text("Редактировать задание"),
        content=bell_list,
        actions=[
            ft.Button("Отмена", on_click=close_dialog),
            ft.Button("Сохранить", on_click=lambda e: new_timetable(e)),
        ],
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

    def change(e):
        global tim
        if e.control.value:
            tim = TimerMusic(MusicPlayer().play_music, [MusicHandler().random_music(), 15],
                             list_time_music=return_bells(e.control.data))
            tim.start()
        else:

            tim.stop()

    def start():
        schedule.clear()  # Очищаем старый список перед пересборкой
        for i in schedule_zvonkov:
            schedule.append(ft.Container(
                ft.Row(
                    controls=[
                        ft.Checkbox(value=False, on_change=change, data=i),
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

            list_bells = []

            for i in bell_list.controls[2:]:
                if i.value:
                    list_bells.append(i.value)

            create_schedule(timetable.value, list_bells)

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
            main_column,
            ft.Row([ft.FilledButton("Создать новое расписание", on_click=get_clicked)],
                   alignment=ft.MainAxisAlignment.END, )
        ]
    )

    # Добавляем на страницу сам интерфейс И диалоговое окно (один раз!)
    page.add(view_schedule, dialog_window)


ft.app(target=main)
