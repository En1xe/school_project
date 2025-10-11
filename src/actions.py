from tkinter import Button
from PIL import Image, ImageTk

from constants import FONT


def btn_bg_change(btn, bg_color):
    def wrapper(e):
        btn.configure(bg=bg_color)

    return wrapper


def show_main_page(home_page, main_page):
    def wrapper():
        home_page.pack_forget()
        main_page.pack(fill='both', expand=True)
    
    return wrapper


def change_img(prev_btn, next_btn, btn_type):
    from widgets import set_current_index, current_image_index, current_images_list, image_label

    step = 1 if btn_type == 'next' else -1
    index = current_image_index + step
    set_current_index(index)

    if index >= len(current_images_list) - 1:
        next_btn.config(state='disabled')
    else:
        next_btn.config(state='normal')

    if index <= 0:
        prev_btn.config(state='disabled')
    else:
        prev_btn.config(state='normal')

    set_image(current_images_list, index, image_label)


def update_colours(
    widgets_list,
    widgets_bg,
    widgets_bg_hover,
    widgets_bg_active,
    widgets_fg_active
):
    for widget in widgets_list:
        widget.config(
            background=widgets_bg,
            activebackground=widgets_bg_active,
            activeforeground=widgets_fg_active,
        )
        widget.bind('<Enter>', btn_bg_change(widget, widgets_bg_hover))
        widget.bind('<Leave>', btn_bg_change(widget, widgets_bg))


def set_image(img_list, img_index, img_label):
    image_path = img_list[img_index]
    image = Image.open(image_path)

    image_copy = image.copy()
    image_copy.thumbnail((400, 300), Image.Resampling.LANCZOS)

    current_image_tk = ImageTk.PhotoImage(image_copy)
    
    img_label.configure(image=current_image_tk)
    img_label.image = current_image_tk


def create_btn(master, bg, hover_bg, active_bg, active_fg, image='', **kwargs):
    btn = Button(
        master, 
        font=FONT, 
        background=bg,
        activebackground=active_bg,
        activeforeground=active_fg,
        bd=0,
        image=image,
        **kwargs
    )
    btn.bind('<Enter>', btn_bg_change(btn, hover_bg))
    btn.bind('<Leave>', btn_bg_change(btn, bg))

    if image:
        btn.image = image

    return btn