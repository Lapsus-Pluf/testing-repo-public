# ======================================================================================================================
# IMPORTS
# ======================================================================================================================
# Standard library imports
# N/A

# Related third party imports
# N/A

# Local application/library specific imports
from app_name.file_to_test import sum_values


# ======================================================================================================================
# TESTS
# ======================================================================================================================
def test_sum_typical_values():
    assert sum_values(2, 3) == 5
    assert sum_values(-1, 1) == 0
    assert sum_values(0, 0) == 0
    assert sum_values(-2, -3) == -5


def test_sum_float_values():
    assert sum_values(2.5, 3.5) == 6.0
    assert sum_values(-1.0, 1.0) == 0.0
    assert sum_values(0.0, 0.0) == 0.0
    assert sum_values(-2.5, -3.5) == -6.0


def test_sum_mixed_types_values():
    assert sum_values(2, 3.5) == 5.5
    assert sum_values(-1.0, 1) == 0.0
    assert sum_values(0, 0.0) == 0.0
    assert sum_values(-2, -3.5) == -5.5


def test_sum_large_number_values():
    assert sum_values(1_000_000, 2_000_000) == 3_000_000
    assert sum_values(-1_000_000, 1_000_000) == 0
    assert sum_values(0, 1_000_000) == 1_000_000
    assert sum_values(-2_000_000, -3_000_000) == -5_000_000
