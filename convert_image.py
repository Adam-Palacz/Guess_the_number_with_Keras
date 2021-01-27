from PIL import Image, ImageFilter


def convert_app(image_name):
    image = Image.open(image_name).convert('L')
    width = int(image.size[0])
    height = int(image.size[1])
    new_image = Image.new('L', (28, 28), 255)
    new_width = int(round((20.0 / height * width), 0))

    if (new_width == 0):
        new_width = 1

    resized_image = image.resize((new_width, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
    vertical_position = int(round(((28 - new_width) / 2), 0))
    new_image.paste(resized_image, (vertical_position, 4))

    pixel_values = list(new_image.getdata())

    result = [(255 - x) * 1.0 / 255.0 for x in pixel_values]
    return result

