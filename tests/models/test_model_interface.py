import inspect
from abc import ABCMeta

from app.models.model_interface import ModelInterface


def test_model_interface_should_be_subclass_of_abcmeta():
    assert issubclass(type(ModelInterface), ABCMeta)


def test_model_interface_has_model_path_parameter():
    constructor_parameters = inspect.signature(
        ModelInterface.__init__
    ).parameters

    assert "model_path" in constructor_parameters


def test_model_interface_has_classes_names_parameter():
    constructor_parameters = inspect.signature(
        ModelInterface.__init__
    ).parameters

    assert "classes_names" in constructor_parameters


def test_model_interface_has_model_path_attribute():
    model_interface = ModelInterface(model_path='dummy_model_path', classes_names=['dummy', 'dummy', 'dummy'])
    assert hasattr(model_interface, "model_path")


def test_model_interface_has_classes_names_attribute():
    model_interface = ModelInterface(model_path='dummy_model_path', classes_names=['dummy', 'dummy', 'dummy'])
    assert hasattr(model_interface, "model_path")


def test_model_interface_has_start_method():
    model_interface = ModelInterface(model_path='dummy_model_path', classes_names=['dummy', 'dummy', 'dummy'])
    assert hasattr(model_interface, "predict")


def test_predict_has_image_parameter():
    constructor_parameters = inspect.signature(
        ModelInterface.predict
    ).parameters

    assert "image" in constructor_parameters

