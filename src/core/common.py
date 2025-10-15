from tkinter import Button

from constants import FONT


def widget_bg_hover(widget, bg_color):
    """Обновляет стиль виджета при наведение"""
    def wrapper(e):
        widget.configure(bg=bg_color)

    return wrapper


def create_btn(master, style, image='', **kwargs):
    """Создаёт стилизованную кнопку с эффектом наведения"""
    btn = Button(
        master, 
        font=FONT, 
        background=style['widgets_bg'],
        activebackground=style['widgets_bg_active'],
        activeforeground=style['widgets_fg_active'],
        bd=0,
        image=image,
        **kwargs
    )
    btn.bind('<Enter>', widget_bg_hover(btn, style['widgets_bg_hover']))
    btn.bind('<Leave>', widget_bg_hover(btn, style['widgets_bg']))

    if image:
        btn.image = image

    return btn


def switch_to_other_page(current_page, new_page):
    """Переключает страницу с одной на другую"""
    def wrapper():
        current_page.pack_forget()
        new_page.pack(fill='both', expand=True)
    
    return wrapper