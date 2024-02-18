# re module

    >>> import re

# RE methods


# Match object methods

    >>> m = re.search(r"\d", "one: 1, two: 2")
    >>> m
    <re.Match object; span=(5, 6), match='1'>
    >>> m.string
    'one: 1, two: 2'
    >>> m.span()
    (5, 6)
    >>> m.group()
    '1'

## Re syntax
 - Repetitions with star *

    >>> re.search(r'ettttttt', "Now is bettttttter than never.")
    <re.Match object; span=(8, 16), match='ettttttt'>
    >>> re.search(r'et*', "Now is bettttttter than never.")
    <re.Match object; span=(8, 16), match='ettttttt'>
    >>> re.search(r'et*', "Now is beer than never.")
    <re.Match object; span=(8, 9), match='e'>

 - Repetitions with plus +

    >>> re.search(r't+', "Now is better than never.")
    <re.Match object; span=(9, 11), match='tt'>

findall() method is used to search for “all” occurrences that match a given pattern. 
In contrast, search() module will only return the first occurrence that matches the specified pattern.


## re.search

    >>> regex = r"\d"
    >>> test_str = "one: 1, two: 2"

    >>> re.search(regex, test_str)
    <re.Match object; span=(5, 6), match='1'>

## re.findall

    >>> re.findall(regex, test_str)
    ['1', '2']

# Search Star/Plus


# Word Boundaries

The metacharacter \b is an anchor like the caret and the dollar sign. It matches at a position that is called a “word boundary”. This match is zero-length.

There are three different positions that qualify as word boundaries:


Before the first character in the string, if the first character is a word character.
After the last character in the string, if the last character is a word character.
Between two characters in the string, where one is a word character and the other is not a word character.

    >>> re.search(r"\bare\b", "word boundaries are odd")
    <re.Match object; span=(16, 19), match='are'>


# Flags/Inline flags


    >>> re.search(r'now', "Now is better than never.")

- (?aiLmsux)

    (One or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x'.) The group matches the empty string; the letters set the corresponding flags for the entire regular expression

    >>> re.search(r'(?i)now', "Now is better than never.")
    <re.Match object; span=(0, 3), match='Now'>

- re.I (ignore case)
    >>> re.search(r'now', "Now is better than never.", re.I)
    <re.Match object; span=(0, 3), match='Now'>