class DatasetModel:
    def __init__(self):
        self.x_trains: list = list()
        self.y_trains: list = list()

    def set_x_trains(self, array_train: list) -> None:
        self.x_trains = array_train

    def set_y_trains(self, array_train: list) -> None:
        self.y_trains = array_train