from abc import ABCMeta

from app.models.model_interface import ModelInterface


class ImageDetectingUiInterface(metaclass=ABCMeta):
    def __init__(self, app_title: str, model: ModelInterface):
        def validate_model_type(_model):
            if not isinstance(_model, ModelInterface):
                raise TypeError(
                    "model parameter must be of type ModelInterface."
                )

        validate_model_type(model)
        self.app_title: str = app_title
        self.model: ModelInterface = model
