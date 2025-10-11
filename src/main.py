from tkinter import Tk
from widgets import create_home_page_widgets, create_main_page_widgets


root = Tk()
root.title('Title')
root.minsize(500, 400)

create_main_page_widgets(root)
create_home_page_widgets(root)

if __name__ == '__main__':
    root.mainloop()