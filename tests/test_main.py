import pytest
from main import generate_password
import string

# Define test cases using named tuples for better readability
from collections import namedtuple

TestParameters = namedtuple("TestParameters", ["length", "use_uppercase", "use_number", "use_symbols"])

test_cases = [
    TestParameters(length=8, use_uppercase=True, use_number=True, use_symbols=True),
    TestParameters(length=12, use_uppercase=False, use_number=True, use_symbols=True),
    TestParameters(length=16, use_uppercase=True, use_number=False, use_symbols=False),
    TestParameters(length=10, use_uppercase=False, use_number=False, use_symbols=False),
]

@pytest.mark.parametrize("params", test_cases)
def test_generate_password_length(params):
    password = generate_password(params.length, params.use_uppercase, params.use_number, params.use_symbols)

    # Check the length of the generated password
    assert len(password) == params.length

@pytest.mark.parametrize("params", test_cases)
def test_generate_password_uppercase(params):
    if params.use_uppercase:
        password = generate_password(params.length, params.use_uppercase, params.use_number, params.use_symbols)
        # Check if uppercase characters are included if required
        assert any(c.isupper() for c in password)

@pytest.mark.parametrize("params", test_cases)
def test_generate_password_number(params):
    if params.use_number:
        password = generate_password(params.length, params.use_uppercase, params.use_number, params.use_symbols)
        # Check if at least one number is included if required
        assert any(c.isdigit() for c in password)

@pytest.mark.parametrize("params", test_cases)
def test_generate_password_symbols(params):
    if params.use_symbols:
        password = generate_password(params.length, params.use_uppercase, params.use_number, params.use_symbols)
        # Check if symbols are included if required
        assert any(c in string.punctuation for c in password)
