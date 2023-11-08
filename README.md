# calculator

A simple parser written in python for evaluating expressions and sub-expressions consisting of arithmetic operations (`plus`, `minus`, `multiplication` and `division` and `parenthesis`) involving `int`.


# Usage

```python

$ python calculator.py
(3+4)*3/2
Evaluation of expression: (3+4)*3/2 is 10.5

```

# Dependencies

* python 3.9+
* pip
* poetry
* hypothesis (to run property based test suite)
* conda/venv for virtual environment creation and maintenance

```python
# assuming virtual environment is activated from here onwards
$ pip install poetry
$ poetry install
```

# Test

```python

# To run simple unit test.

$ pytest tests/unit.py

```

```python

# To run hypothesis (property based testing) suite.

$ pytest tests/property.py --hypothesis-show-statistics

```
