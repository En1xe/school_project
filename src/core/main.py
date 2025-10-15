from tkinter import messagebox
from PIL import Image, ImageTk

from .common import widget_bg_hover, switch_to_other_page
from constants import (
    SUPPORT_IMAGES_LIST, 
    ADVICE_IMAGES_LIST, 
    MEMES_IMAGES_LIST, 
    ADVICE_PAGE_STYLE, 
    SUPPORT_PAGE_STYLE, 
    MEMES_PAGE_STYLE,
    CONTENT_IMAGE_WIDTH, 
    CONTENT_IMAGE_HEIGHT,
    CATEGORY_OPTIONS,
    PHRASES_LIST
)


current_images_list = []
current_image_index = 0    


def set_current_image(img_label):
    """Устанавливает текущее изображение в виджет Label с фиксированным размером"""

    try:
        image_path = current_images_list[current_image_index]
    except IndexError:
        from pages.main import main_page, selected_option
        from pages.home import home_page

        messagebox.showerror('Ошибка!', 'Картинка не была найдена')
        img_label.after(100, lambda: switch_to_other_page(main_page, home_page)())
        selected_option.set(CATEGORY_OPTIONS[0])
        return
        
    image = Image.open(image_path)

    image_copy = image.copy()
    image_copy.thumbnail(
        (CONTENT_IMAGE_WIDTH, CONTENT_IMAGE_HEIGHT), 
        Image.Resampling.LANCZOS
    )

    current_image_tk = ImageTk.PhotoImage(image_copy)
    
    img_label.configure(image=current_image_tk)
    img_label.image = current_image_tk


def change_current_image_and_text(
        prev_btn, 
        next_btn, 
        selected_option, 
        label_under_image, 
        btn_type
    ):
    """
    Переключает текущее изображение в зависимости от типа кнопки (вперед или назад), 
    отключает состояние кнопок при достижение границ списка изображений.
    """
    from pages.main import image_label

    global current_image_index

    step = 1 if btn_type == 'next' else -1
    index = current_image_index + step
    current_image_index = index

    if index >= len(current_images_list) - 1:
        next_btn.config(state='disabled')
    else:
        next_btn.config(state='normal')

    if index <= 0:
        prev_btn.config(state='disabled')
    else:
        prev_btn.config(state='normal')

    if selected_option.get() == 'Советы':
        label_under_image.config(text=PHRASES_LIST[current_image_index])

    set_current_image(image_label)


def update_widgets_style(widgets_list, current_style):
    """Обновляет цветовую схему виджетов согласно текущему стилю"""
    for widget in widgets_list:
        widget.config(
            background=current_style['widgets_bg'],
            activebackground=current_style['widgets_bg_active'],
            activeforeground=current_style['widgets_fg_active'],
        )
        widget.bind('<Enter>', widget_bg_hover(widget, current_style['widgets_bg_hover']))
        widget.bind('<Leave>', widget_bg_hover(widget, current_style['widgets_bg']))


def on_selected_option_change(
        selected_option, 
        next_image_btn, 
        previous_image_btn,
        image_label,
        main_page,
        label_under_image,
        label_under_image_frame
    ):
    """
    Обрабатывает изменение выбранной категории
    
    Обновляет стиль интерфейса, список изображений и состояние кнопок. 
    Сбрасывает индекс текущей изображения и применяет новую цветовую схему.
    """
    from pages.main import current_style, widgets_list

    global current_image_index, current_images_list

    new_value = selected_option.get()

    label_under_image_text = ''

    match new_value:
        case 'Мемы':
            current_style = MEMES_PAGE_STYLE
            current_images_list = MEMES_IMAGES_LIST

            label_under_image_bg = current_style['bg']
        case 'Советы':
            current_style = ADVICE_PAGE_STYLE
            current_images_list = ADVICE_IMAGES_LIST

            label_under_image_text = PHRASES_LIST[current_image_index]
            label_under_image_bg = current_style['widgets_bg']
        case 'Поддержка':
            current_style = SUPPORT_PAGE_STYLE
            current_images_list = SUPPORT_IMAGES_LIST

            label_under_image_bg = current_style['bg']


    current_image_index = 0

    next_image_btn.config(state='normal')
    previous_image_btn.config(state='disabled')
    
    main_page.config(background=current_style['bg'])
    image_label.config(background=current_style['bg'])
    label_under_image_frame.config(background=current_style['bg'])
    label_under_image.config(background=label_under_image_bg)

    label_under_image.config(text=label_under_image_text)

    update_widgets_style(
        widgets_list,
        current_style
    )
    set_current_image(image_label)