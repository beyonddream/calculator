from ..calculator import *

import pytest
import math

@pytest.mark.parametrize("input, expected", [
    ('3+4*3/2', 9.0),
    ('(3+4)*3/2', 10.5),
    ('20*4+5*3/3', 85.0),
    ('(3+4)*3/2+2', 12.5),
    ('((3+4)*3/2)+2', 12.5),
    ('3+4*3/(3+2)', 5.4),
    ('3+4*3/(3+2)*(1+1)', 7.8),
    ('0-0+1', 1),
    ('0-0-1', -1),
    ('1+1+1/3-1+0+0+0', 1.33)
])
def test_calculator(input, expected):
        actual = parse(input)
        assert math.isclose(actual, expected, rel_tol=1e-2)