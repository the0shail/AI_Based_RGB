import random
import matplotlib.pyplot as plt
from classes.DatasetModel import DatasetModel


def generate_random_color():
    """Генерирует случайный цвет в формате RGB."""
    r = round(random.random() * 255)
    g = round(random.random() * 255)
    b = round(random.random() * 255)
    return [r, g, b]


def show_color(color):
    """Отображает цвет на графике."""
    plt.imshow([[color]])
    plt.axis('off')
    plt.show()


def create_trains(iteration: int = 1) -> DatasetModel:
    train = DatasetModel()
    x_trains, y_trains = list(), list()

    for i in range(iteration):
        rgb = generate_random_color()
        # show_color(rgb) # For debug
        lardingColor = rgb.index(max(rgb))
        x_trains.append(rgb)
        if lardingColor == 0:
            y_trains.append([1, 0, 0])
        elif lardingColor == 1:
            y_trains.append([0, 1, 0])
        elif lardingColor == 2:
            y_trains.append([0, 0, 1])
        else:
            raise IndexError(f"InputBoundsException: {lardingColor}")

    train.set_x_trains(x_trains)
    train.set_y_trains(y_trains)
    return train
