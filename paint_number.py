from tkinter import *
from PIL import Image, ImageDraw


def paint_app():
    def save():
        filename = 'image.jpg'
        image1.save(filename)

    def paint(event):
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x + 1), (event.y + 1)
        cv.create_oval((x1, y1, x2, y2), fill='black', width=10)
        draw.line((x1, y1, x2, y2), fill='black', width=10)

    root = Tk()
    cv = Canvas(root, width=280, height=280, bg='white', highlightthickness=0)
    image1 = Image.new('RGB', (280, 280), 'white')
    draw = ImageDraw.Draw(image1)
    cv.bind('<B1-Motion>', paint)
    cv.pack(expand=True, fill=BOTH)
    btn_save = Button(text="save", command=save)
    btn_save.pack()
    root.mainloop()
    return "Image saved"



