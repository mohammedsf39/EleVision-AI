import inspect
from abc import ABCMeta

import pytest

from app.image_detecting_ui.image_detecting_ui_interface import (
    ImageDetectingUiInterface,
)
from tests.image_detecting_ui.model_dummy import ModelDummy


def test_image_detecting_ui_interface_should_be_subclass_of_abcmeta():
    assert issubclass(type(ImageDetectingUiInterface), ABCMeta)


def test_image_detecting_ui_interface_has_app_title_parameter():
    constructor_parameters = inspect.signature(
        ImageDetectingUiInterface.__init__
    ).parameters

    assert "app_title" in constructor_parameters


def test_image_detecting_ui_interface_has_model_parameter():
    constructor_parameters = inspect.signature(
        ImageDetectingUiInterface.__init__
    ).parameters

    assert "model" in constructor_parameters


@pytest.mark.parametrize("model", ["Not int", 2.12, [0, 2], True, "100", "-2"])
def test_model_should_be_of_type_model_interface(model):
    with pytest.raises(TypeError) as exception:
        ImageDetectingUiInterface(app_title="dummy_app_title", model=model)

        assert str(exception.value) == "model parameter must be of type ModelInterface."


def test_image_detecting_ui_interface_has_app_title_attribute():
    model_interface = ImageDetectingUiInterface(
        app_title="dummy_app_title",
        model=ModelDummy(
            model_path="dummy_model_path", classes_names=["dummy", "dummy", "dummy"]
        ),
    )
    assert hasattr(model_interface, "app_title")


def test_model_interface_has_model_attribute():
    model_interface = ImageDetectingUiInterface(
        app_title="dummy_app_title",
        model=ModelDummy(
            model_path="dummy_model_path", classes_names=["dummy", "dummy", "dummy"]
        ),
    )
    assert hasattr(model_interface, "model")
