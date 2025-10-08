def btn_bg_change(btn, bg_color):
    def wrapper(e):
        btn.configure(bg=bg_color)

    return wrapper