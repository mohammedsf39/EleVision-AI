from abc import ABCMeta


class ModelInterface(metaclass=ABCMeta):
    def __init__(self, model_path: str, classes_names: list[str]) -> None:
        self.model_path: str = model_path
        self.classes_names: list[str] = classes_names

    def predict(self, image) -> str:
        pass
