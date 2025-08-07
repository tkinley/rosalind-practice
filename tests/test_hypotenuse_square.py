import importlib
from pathlib import Path
import sys
import pytest

# Ensure repository root is on sys.path so modules with hyphenated names can be imported
sys.path.append(str(Path(__file__).resolve().parent.parent))

hypotenuse_square = importlib.import_module(
    'python-village.INI2-variables-and-some-arithmetic.solution'
).hypotenuse_square


def test_typical_values():
    assert hypotenuse_square(3, 4) == 25


@pytest.mark.parametrize("a, b, expected", [(0, 0, 0), (0, 5, 25), (5, 0, 25)])
def test_zero_length_sides(a, b, expected):
    assert hypotenuse_square(a, b) == expected


@pytest.mark.parametrize("a, b", [(-3, -4), (-3, 4), (3, -4)])
def test_negative_inputs(a, b):
    assert hypotenuse_square(a, b) == 25
