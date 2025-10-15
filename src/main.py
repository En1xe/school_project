from tkinter import Tk
from PIL import Image, ImageTk

from pages import create_home_page_widgets, create_main_page_widgets


root = Tk()
root.title('Без паники')
root.minsize(500, 400)
root.resizable(False, False)

empty_icon = Image.new('RGBA', (1, 1), (240, 244, 249, 0))
photo = ImageTk.PhotoImage(empty_icon)
root.iconphoto(True, photo)

create_main_page_widgets(root)
create_home_page_widgets(root)

if __name__ == '__main__':
    root.mainloop()