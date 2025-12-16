'''

i got this error so am not using this file:
[ty@archlinux ~]$ pip install pytest
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try 'pacman -S
    python-xyz', where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Arch-packaged Python package,
    create a virtual environment using 'python -m venv path/to/venv'.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip.
    
    If you wish to install a non-Arch packaged Python application,
    it may be easiest to use 'pipx install xyz', which will manage a
    virtual environment for you. Make sure you have python-pipx
    installed via pacman.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
[ty@archlinux ~]$ 



'''

# test_2.py
"""
Unit tests for the `example` function defined in 2.py.

Run the tests with:
    pytest test_2.py
"""

import builtins
import pytest

# Import the function you want to test.
# If 2.py is in a package, adjust the import accordingly,
# e.g. `from mypackage.two import example`.
from 2 import example


def test_example_returns_expected_value():
    """
    Replace the body of this test with the actual expectations
    for `example()`. For illustration we assume it returns an integer.
    """
    result = example()
    # Example assertion – change to match your real contract.
    assert isinstance(result, int), "example() should return an integer"
    # Add more specific checks, e.g.:
    # assert result == 42


def test_example_handles_edge_cases():
    """
    If `example` accepts arguments, test boundary conditions here.
    If it takes no arguments, you can still test its behaviour
    under different global states or mocked inputs.
    """
    # Example of mocking built‑ins or external calls:
    # with unittest.mock.patch('builtins.open', ...) as mock_open:
    #     ...

    # For a no‑arg function, you might just call it again:
    result = example()
    # Replace with whatever edge‑case behavior you expect.
    assert result is not None