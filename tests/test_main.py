import pytest

from main import SinValidator


@pytest.mark.parametrize(
    "string, expected",
    [
        ("   test  string", "teststring"),
        ("foobar", "foobar"),
        ("foo1    2bar", "foo12bar"),
    ],
)
def test_string_space_clean(string, expected):
    assert SinValidator.string_space_clean(string=string) == expected


@pytest.mark.parametrize("string, expected", [("123", False), ("123456789", True), ("", False)])
def test_len_validator(string, expected):
    assert SinValidator._lenght_validator(sin_string=string) == expected


@pytest.mark.parametrize(
    "num, expected",
    [
        (1, 2),
        (5, 1),
        (9, 9),
    ],
)
def test_sum_multiply_method(num, expected):
    assert SinValidator._sum_multiply_method(num=num) == expected


@pytest.mark.parametrize("num, expected", [(i, False) for i in range(1, 100, 2)])
def test_non_divisible_divisible_validator(num, expected):
    assert SinValidator._divisible_validator(num=num) == expected


@pytest.mark.parametrize("num, expected", [(i, True) for i in range(0, 100, 10)])
def test_divisible_divisible_validator(num, expected):
    assert SinValidator._divisible_validator(num=num) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("046454286", True),
        ("046454296", False),
        ("000000000", True),
    ],
)
def test_sum_validator(string, expected):
    assert SinValidator._sum_validator(sin_string=string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [("046454286", True), ("046454296", False), ("000000000", True), ("123", False)],
)
def test_validate(string, expected):
    assert SinValidator.validate(sin_string=string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("1234a6789", False),
        ("000 000 000", False),
        ("000000000", True),
    ],
)
def test_guarantee_only_digits(string, expected):
    assert SinValidator._guarantee_only_digits(string=string) == expected
