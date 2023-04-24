from PIL import Image


# функция, возвращающая измененное фото по запросу пользователя
def photoshop(picture, choice):
    im = Image.open(picture)
    pixels = im.load()
    x, y = im.size
    index = picture.find('.')

    # чб фильтр
    if choice == 1:
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                bw = (r + g + b) // 3
                pixels[i, j] = bw, bw, bw
        im.save(f"{picture[::index]}_black_white.jpg")

    return im
