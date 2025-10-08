from tkinter import Button, OptionMenu, Frame, PhotoImage, Label, StringVar

from constants import HOME_PAGE_STYLE, IMAGES_DIR, ICONS_DIR, FONT, CATEGORY_OPTIONS, ADVICE_PAGE_STYLE
from actions import btn_bg_change


def create_btn(master, bg, hover_bg, active_bg, active_fg, text='', image='', pady=0, padx=0):
    btn = Button(
        master, 
        text=text, 
        font=FONT, 
        background=bg,
        activebackground=active_bg,
        activeforeground=active_fg,
        bd=0,
        image=image,
        pady=pady,
        padx=padx
    )
    btn.bind('<Enter>', btn_bg_change(btn, hover_bg))
    btn.bind('<Leave>', btn_bg_change(btn, bg))

    if image:
        btn.image = image

    return btn


def create_home_page_widgets(root):
    home_page = Frame(root, background=HOME_PAGE_STYLE['bg'])
    home_page.pack(fill='both', expand=True)

    readme_text = Frame(home_page, background='white', width=300, height=200)
    readme_text.pack(pady=20)

    start_btn = create_btn(
        master=home_page,
        text='Начать',
        bg=HOME_PAGE_STYLE['widgets_bg'],
        hover_bg=HOME_PAGE_STYLE['widgets_bg_hover'],
        active_bg=HOME_PAGE_STYLE['widgets_bg_active'],
        active_fg=HOME_PAGE_STYLE['widgets_fg_active'],
    )
    start_btn.pack(expand=True, pady=20)


def create_main_page_widgets(root):
    root.configure(bg='#88C6B6')
    main_page = Frame(root, background='#88C6B6', pady=20)
    main_page.pack(fill='both', expand=True)

    main_picture = PhotoImage(file=str(IMAGES_DIR / 'Image.png'))
    left_arrow_picture = PhotoImage(file=str(ICONS_DIR / 'arrow-left.png'))
    right_arrow_picture = PhotoImage(file=str(ICONS_DIR / 'arrow-right.png'))

    image_label = Label(main_page, image=main_picture)
    image_label.image = main_picture
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
    )
    previous_image_btn.pack(side='left', expand=True)

    selected_option = StringVar(main_page)
    selected_option.set(CATEGORY_OPTIONS[0])

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