from pathlib import Path


BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / 'images'
ICONS_DIR = BASE_DIR / 'icons'

FONT = ('Arial', 20)

CATEGORY_OPTIONS = ['Советы', 'Мемы', 'Поддержка']

HOME_PAGE_STYLE = {
    'bg': '#E6D2AA',
    'widgets_bg': '#FAF6F0',
    'widgets_bg_hover': "#EEE9E3",
    'widgets_bg_active': "#E4DFDA",
    'widgets_fg_active': "#474747",
}

ADVICE_PAGE_STYLE = {
    'bg': '#88C6B6',
    'widgets_bg': '#F8F4E9',
    'widgets_bg_hover': "#F0ECE0",
    'widgets_bg_active': "#E0DDD3",
    'widgets_fg_active': "#474747",
}