# calculator

A simple parser written in python for evaluating expressions and sub-expressions consisting of arithmetic operations (`plus`, `minus`, `multiplication` and `division`) involving `numbers`.


# Usage

```python

$ python calculator.py
(3+4)*3/2
Evaluation of expression: (3+4)*3/2 is 10.5

```

# Dependencies

* python 3.9+
* pip
* hypothesis (to run property based test suite)

```python

$ pip install -r requirements.txt

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