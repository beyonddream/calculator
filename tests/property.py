from ..calculator import *

import math
from hypothesis import example, given, settings, strategies as st

@st.composite
def arithmetic_expression(draw):
    op = draw(st.sampled_from(['+', '-', '*', '/']))
    left = draw(st.integers(min_value=0, max_value=100))
    right = draw(st.integers(min_value=0, max_value=100))
    outer_exp_braces = draw(st.booleans())
    left_exp_braces = draw(st.booleans())
    right_exp_braces = draw(st.booleans())
    left_expr = f"{'(' if left_exp_braces else ''}{left}{')' if left_exp_braces else ''}"
    right_expr = f"{'(' if right_exp_braces else ''}{right}{')' if right_exp_braces else ''}"
    expr = f"{'(' if outer_exp_braces else ''}{left_expr}{op}{right_expr}{')' if outer_exp_braces else ''}"
    
    return f"{expr}"


@given(arithmetic_expression())
@settings(max_examples=500)
@example('3+4*3/2')
@example('(3+4)*3/2')
@example('20*4+5*3/3')
@example('(3+4)*3/2+2')
@example('((3+4)*3/2)+2')
@example('3+4*3/(3+2)')
@example('3+4*3/(3+2)*(1+1)')
@example('0-0+1')
@example('0-0-1')
@example('1+1+1/3-1+0+0+0')
def test_calculator(input):
    try:
        # eval() is evil esp. for arbitrary user inputs.
        # Here, hypothesis generates input that are only
        # capable of being arithmetic expressions.
        expected = eval(input)
        actual = parse(input)
        assert math.isclose(actual, expected, rel_tol=1e-2)
    except ZeroDivisionError:
        # skip if hypothesis creates division by 0 scenario
        # This scenario is handled directly in unit.py
        assert True
    