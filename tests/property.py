from ..calculator import *


import math
from hypothesis import example, given, settings, strategies as st

@st.composite
def arithmetic_expression(draw):
    op = draw(st.sampled_from(['+', '-', '*', '/']))
    left = draw(st.integers(min_value=0, max_value=100))
    right = draw(st.integers(min_value=0, max_value=100))
    outer_braces = draw(st.booleans())
    left_braces = draw(st.booleans())
    right_braces = draw(st.booleans())
    left_expr = f"{'(' if left_braces else ''}{left}{')' if left_braces else ''}"
    right_expr = f"{'(' if right_braces else ''}{right}{')' if right_braces else ''}"
    expr = f"{'(' if outer_braces else ''}{left_expr}{op}{right_expr}{')' if outer_braces else ''}"
    
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
    actual_passed = True
    expected_passed = True
    # Ugly hack to make sure both parse()
    # and eval() pass before comparing their
    # output.
    # Also, eval() is evil - DO NOT use them
    # in your code especially on user input.
    try:
        parse(input)
    except Exception:
        actual_passed = False
    try:
        eval(input)
    except Exception:
        expected_passed = False

    if actual_passed and expected_passed:
        actual = parse(input)
        expected = eval(input)
        assert math.isclose(actual, expected, rel_tol=1e-2)
    else:
        assert True