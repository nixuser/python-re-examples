# How to use doctest
```
python3 -m doctest word_bundary.py
python3 -m doctest -v word_bundary.py
```

# How to integrate with pytest

```
pytest --doctest-modules  word_bundary.py
```

# How to integrate with unittest
```
python3 -m unittest test_word_bundary.py
python3 -m unittest -v test_word_bundary.py
```