from tkinter import OptionMenu, Frame, PhotoImage, Label, StringVar

from constants import *
from actions import show_main_page, update_colours, set_image, create_btn, change_img


current_images_list = []
current_image_index = 0
current_bg = ''
current_widgets_bg = ''
current_widgets_bg_hover = ''
current_widgets_bg_active = ''
current_widgets_fg_active = ''
widgets_list = []


def set_current_index(value):
    global current_image_index
    current_image_index = value


def create_home_page_widgets(root):
    global home_page

    home_page = Frame(root, background=HOME_PAGE_STYLE['bg'])
    home_page.pack(fill='both', expand=True)

    readme_text = Frame(home_page, background='white', width=300, height=200)
    readme_text.pack(fill='both', pady=20, padx=80, expand=True)

    start_btn = create_btn(
        master=home_page,
        text='Начать',
        bg=HOME_PAGE_STYLE['widgets_bg'],
        hover_bg=HOME_PAGE_STYLE['widgets_bg_hover'],
        active_bg=HOME_PAGE_STYLE['widgets_bg_active'],
        active_fg=HOME_PAGE_STYLE['widgets_fg_active'],
        command=show_main_page(home_page, main_page)
    )
    start_btn.pack(expand=True, pady=20)


def create_main_page_widgets(root):
    global main_page, selected_option, image_label, previous_image_btn, next_image_btn

    main_page = Frame(root, pady=20)

    left_arrow_picture = PhotoImage(file=str(ICONS_DIR / 'arrow-left.png'))
    right_arrow_picture = PhotoImage(file=str(ICONS_DIR / 'arrow-right.png'))

    image_label = Label(main_page)
    image_label.pack(pady=20, padx=40)

    previous_image_btn = create_btn(
        master=main_page,
        text='Начать',
        bg=ADVICE_PAGE_STYLE['widgets_bg'],
        hover_bg=ADVICE_PAGE_STYLE['widgets_bg_hover'],
        active_bg=ADVICE_PAGE_STYLE['widgets_bg_active'],
        active_fg=ADVICE_PAGE_STYLE['widgets_fg_active'],
        image=left_arrow_picture,
        pady=30,
        padx=30,
        state='disabled'
    )
    previous_image_btn.pack(side='left', expand=True)
    widgets_list.append(previous_image_btn)

    selected_option = StringVar(main_page)
    selected_option.trace_add('write', on_selected_option_change)

    option_menu = OptionMenu(
        main_page, 
        selected_option, 
        *CATEGORY_OPTIONS,
    )
    option_menu.config(
        bg=ADVICE_PAGE_STYLE['widgets_bg'],
        activebackground=ADVICE_PAGE_STYLE['widgets_bg_active'],
        activeforeground=ADVICE_PAGE_STYLE['widgets_fg_active'],
        font=FONT,
        bd=0,
    )
    option_menu.pack(side='left', expand=True)
    widgets_list.append(option_menu)

    next_image_btn = create_btn(
        master=main_page,
        text='Начать',
        bg=ADVICE_PAGE_STYLE['widgets_bg'],
        hover_bg=ADVICE_PAGE_STYLE['widgets_bg_hover'],
        active_bg=ADVICE_PAGE_STYLE['widgets_bg_active'],
        active_fg=ADVICE_PAGE_STYLE['widgets_fg_active'],
        image=right_arrow_picture,
        pady=30,
        padx=30,
    )
    next_image_btn.pack(side='left', expand=True)
    widgets_list.append(next_image_btn)

    next_image_btn.config(command=lambda: change_img(previous_image_btn, next_image_btn, 'next'))
    previous_image_btn.config(command=lambda: change_img(previous_image_btn, next_image_btn, 'previous'))

    selected_option.set(CATEGORY_OPTIONS[0])


def on_selected_option_change(*args):
    global current_bg, current_widgets_bg, current_widgets_bg_active, main_page
    global current_widgets_bg_hover, current_widgets_fg_active, current_image_index
    global current_images_list, previous_image_btn, next_image_btn

    new_value = selected_option.get()

    match new_value:
        case 'Мемы':
            current_bg = MEMES_PAGE_STYLE['bg']
            current_widgets_bg = MEMES_PAGE_STYLE['widgets_bg']
            current_widgets_bg_hover = MEMES_PAGE_STYLE['widgets_bg_hover']
            current_widgets_bg_active = MEMES_PAGE_STYLE['widgets_bg_active']
            current_widgets_fg_active = MEMES_PAGE_STYLE['widgets_fg_active']
            current_images_list = MEMES_IMAGES_LIST
        case 'Советы':
            current_bg = ADVICE_PAGE_STYLE['bg']
            current_widgets_bg = ADVICE_PAGE_STYLE['widgets_bg']
            current_widgets_bg_hover = ADVICE_PAGE_STYLE['widgets_bg_hover']
            current_widgets_bg_active = ADVICE_PAGE_STYLE['widgets_bg_active']
            current_widgets_fg_active = ADVICE_PAGE_STYLE['widgets_fg_active']
            current_images_list = ADVICE_IMAGES_LIST
        case 'Поддержка':
            current_bg = SUPPORT_PAGE_STYLE['bg']
            current_widgets_bg = SUPPORT_PAGE_STYLE['widgets_bg']
            current_widgets_bg_hover = SUPPORT_PAGE_STYLE['widgets_bg_hover']
            current_widgets_bg_active = SUPPORT_PAGE_STYLE['widgets_bg_active']
            current_widgets_fg_active = SUPPORT_PAGE_STYLE['widgets_fg_active']
            current_images_list = SUPPORT_IMAGES_LIST

    current_image_index = 0
    next_image_btn.config(state='normal')
    previous_image_btn.config(state='disabled')
    main_page.config(background=current_bg)
    update_colours(
        widgets_list,
        current_widgets_bg,
        current_widgets_bg_hover,
        current_widgets_bg_active,
        current_widgets_fg_active
    )
    set_image(current_images_list, current_image_index, image_label)