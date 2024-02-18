r"""
>>> import re
>>> re.search(r"\bare\b", "word boundaries are odd")
<re.Match object; span=(16, 19), match='are'>
"""

# one more test

r"""
>>> 2 + 2
7
"""

def add(a, b):
    """Compute and return the sum of two numbers.

    Usage examples:
    >>> add(4.0, 2.0)
    6.0
    >>> add(4, 2)
    8.0
    """
    return float(a + b)