"""Test that the package can be imported."""

import importlib

import pytest


def test_package_import():
    """Test that pyclaude can be imported."""
    module = importlib.import_module("pyclaude")
    assert hasattr(module, "Client")
    assert hasattr(module, "__version__")
    assert module.__version__ == "0.1.0"