from pathlib import Path


BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / 'assets' / 'images'
ICONS_DIR = BASE_DIR / 'assets' / 'icons'

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

MEMES_PAGE_STYLE = {
    'bg': '#6C91B2',
    'widgets_bg': '#F0EAD6',
    'widgets_bg_hover': "#E7E3D6",
    'widgets_bg_active': "#D8D2C0",
    'widgets_fg_active': "#474747",
}

SUPPORT_PAGE_STYLE = {
    'bg': '#D7B19D',
    'widgets_bg': '#FAF6F0',
    'widgets_bg_hover': "#F1EEE9",
    'widgets_bg_active': "#E4E1DC",
    'widgets_fg_active': "#474747",
}

ADVICE_FOLDER_PATH = Path(IMAGES_DIR / 'advice').resolve()
MEMES_FOLDER_PATH = Path(IMAGES_DIR / 'memes').resolve()
SUPPORT_FOLDER_PATH = Path(IMAGES_DIR / 'support').resolve()

ADVICE_IMAGES_LIST = [str(item.resolve()) for item in ADVICE_FOLDER_PATH.iterdir()]
MEMES_IMAGES_LIST = [str(item.resolve()) for item in MEMES_FOLDER_PATH.iterdir()]
SUPPORT_IMAGES_LIST = [str(item.resolve()) for item in SUPPORT_FOLDER_PATH.iterdir()]

CONTENT_IMAGE_WIDTH = 400
CONTENT_IMAGE_HEIGHT = 300