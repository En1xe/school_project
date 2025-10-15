from tkinter import OptionMenu, Frame, PhotoImage, Label, StringVar

from constants import ICONS_DIR, CATEGORY_OPTIONS, FONT, ADVICE_PAGE_STYLE
from core.common import create_btn
from core.main import on_selected_option_change, change_current_image


current_style = ADVICE_PAGE_STYLE
widgets_list = []

def create_main_page_widgets(root):
    """Создает виджеты основной рабочей страницы"""
    global main_page, selected_option, image_label, previous_image_btn, next_image_btn

    main_page = Frame(root, pady=20)

    left_arrow_picture = PhotoImage(file=str(ICONS_DIR / 'arrow-left.png'))
    right_arrow_picture = PhotoImage(file=str(ICONS_DIR / 'arrow-right.png'))

    image_label = Label(main_page)
    image_label.pack(pady=20, padx=40)

    previous_image_btn = create_btn(
        master=main_page,
        text='Начать',
        style=current_style,
        image=left_arrow_picture,
        pady=30,
        padx=30,
        state='disabled'
    )
    previous_image_btn.pack(side='left', expand=True)
    widgets_list.append(previous_image_btn)

    selected_option = StringVar(main_page)
    selected_option.trace_add(
        'write', 
        lambda *args: on_selected_option_change(
            selected_option, 
            next_image_btn, 
            previous_image_btn,
            image_label,
            main_page
        )
    )

    option_menu = OptionMenu(
        main_page, 
        selected_option, 
        *CATEGORY_OPTIONS,
    )
    option_menu.config(
        bg=current_style['widgets_bg'],
        activebackground=current_style['widgets_bg_active'],
        activeforeground=current_style['widgets_fg_active'],
        font=FONT,
        bd=0,
    )
    option_menu.pack(side='left', expand=True)
    widgets_list.append(option_menu)

    next_image_btn = create_btn(
        master=main_page,
        text='Начать',
        style=current_style,
        image=right_arrow_picture,
        pady=30,
        padx=30,
    )
    next_image_btn.pack(side='left', expand=True)
    widgets_list.append(next_image_btn)

    next_image_btn.config(command=lambda: change_current_image(
        previous_image_btn, 
        next_image_btn, 
        'next'
    ))
    previous_image_btn.config(command=lambda: change_current_image(
        previous_image_btn, 
        next_image_btn, 
        'previous'
    ))

    selected_option.set(CATEGORY_OPTIONS[0])