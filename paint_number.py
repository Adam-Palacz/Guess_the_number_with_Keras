from tkinter import *
from PIL import Image, ImageDraw


def paint_app():
    def save():
        filename = f'image.png'
        image.save(filename)

    def activate_paint(event):
        global last_x, last_y
        cv.bind('<B1-Motion>', paint)
        last_x, last_y = event.x, event.y

    def paint(event):
        global last_x, last_y
        x, y = event.x, event.y
        cv.create_line((last_x, last_y, x, y), fill='black', width=30, capstyle=ROUND)
        draw.line((last_x, last_y, x, y), fill='black', width=30)
        last_x, last_y = x, y

    root = Tk()

    last_x, last_y = None, None

    cv = Canvas(root, width=280, height=280, bg='white')
    image = Image.new('RGB', (280, 280), 'white')
    draw = ImageDraw.Draw(image)

    cv.bind('<1>', activate_paint)
    cv.pack(expand=YES, fill=BOTH)

    btn_save = Button(text="save", command=save)
    btn_save.pack()

    root.mainloop()
    return "Image saved"

