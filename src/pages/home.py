from tkinter import Frame, Label

from constants import HOME_PAGE_STYLE
from core.common import create_btn, switch_to_other_page


def create_home_page_widgets(root):
    """Создаёт виджеты стартовой страницы"""
    from .main import main_page

    global home_page

    with open('README.md') as readme:
        readme_text = readme.read()

    home_page = Frame(root, background=HOME_PAGE_STYLE['bg'])
    home_page.pack(fill='both', expand=True)

    readme_frame = Frame(
        home_page, 
        background=HOME_PAGE_STYLE['widgets_bg'], 
        width=300, 
        height=200,
    )
    readme_frame.pack(fill='both', pady=20, padx=80, expand=True)

    readme_text = Label(
        readme_frame,
        text=readme_text,
        background=HOME_PAGE_STYLE['widgets_bg'],
        anchor='nw',
        justify='left'
    )
    readme_text.pack(fill='both', expand=True, anchor='nw')

    start_btn = create_btn(
        master=home_page,
        text='Начать',
        style=HOME_PAGE_STYLE,
        command=switch_to_other_page(home_page, main_page)
    )
    start_btn.pack(expand=True, pady=20)