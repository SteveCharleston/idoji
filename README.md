# IDoji

[![Lint](https://github.com/SteveCharleston/idoji/actions/workflows/lint.yaml/badge.svg)](https://github.com/SteveCharleston/idoji/actions/workflows/lint.yaml)
[![Unittests](https://github.com/SteveCharleston/idoji/actions/workflows/tests.yaml/badge.svg)](https://github.com/SteveCharleston/idoji/actions/workflows/tests.yaml)
[![codecov](https://codecov.io/gh/SteveCharleston/idoji/branch/master/graph/badge.svg?token=WTIMZT5852)](https://codecov.io/gh/SteveCharleston/idoji)

[![pypi](https://img.shields.io/pypi/v/idoji)](https://pypi.org/project/idoji/)
[![python](https://img.shields.io/pypi/pyversions/idoji)](https://pypi.org/project/idoji/)
[![license](https://img.shields.io/github/license/SteveCharleston/idoji)](https://github.com/SteveCharleston/idoji/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


What if you could combine the magical fun of emojis and the unique uniqueness
power of UUIDs.

What if you had a format to label objects, so powerful and elegant, that you
enjoy sending those over your favorite messenger.

What if you had a small python package, providing you all of that and much more.

Welcome to *IDoji*.

# Installation
Installation can be done via `pip`
```sh
pip3 install idoji
```

# Usage

IDoji can be used as a superior alternative to UUIDs. Common
functionality provided by UUIDs can be found in IDojis, as well as facilities
to mix both types or convert between them.

## Instantiate them

It is possible to instantiate a completely random IDoji as well as using values
of the type `str`, `int` or even `UUID`.

```python
>>> from idoji import IDoji
>>> idoj = IDoji()
>>> print(idoj)
🦟🦄😗😅-🥽🦄-🙌🦩-🥳🥱-🧊🥖-🤭🦝🦲😒
```

It is also possible to use existing UUIDs in several forms.

```python
>>> from uuid import uuid4
>>> uuidval = uuid4()
>>> print(uuidval)
e4f4d80c-01f4-4504-b18b-6061bb619aa3
>>> idoj_from_uuid = IDoji(uuidval)
>>> print(idoj_from_uuid)
🦳🧃🦧😌-😁🧃-🙅😄-🦀🥙-🤜🤝-🦊🤝🥨🥱
>>> repr(idoj_from_uuid)
"IDoji('e4f4d80c-01f4-4504-b18b-6061bb619aa3')"
>>> idoj_from_uuid_str = IDoji("e4f4d80c-01f4-4504-b18b-6061bb619aa3")
>>> print(idoj_from_uuid_str)
🦳🧃🦧😌-😁🧃-🙅😄-🦀🥙-🤜🤝-🦊🤝🥨🥱
```

And of course, if you get an IDoji string from somewhere, you can use that to
instantiate an object as well.

```python
>>> idoj = IDoji("🦳🧃🦧😌-😁🧃-🙅😄-🦀🥙-🤜🤝-🦊🤝🥨🥱")
>>> print(idoj)
🦳🧃🦧😌-😁🧃-🙅😄-🦀🥙-🤜🤝-🦊🤝🥨🥱
>>> repr(idoj)
"IDoji('e4f4d80c-01f4-4504-b18b-6061bb619aa3')"
```

## Compare them

IDojis can be compared against each other as well as UUIDs.

Comparison against IDoji objects as well as their string representation is
available.

```python
>>> idoj = IDoji()
>>> idoj_same = IDoji(idoj.uuid)
>>> idoj_diff = IDoji()
>>> print("{} -- {} -- {}".format(idoj, idoj_same, idoj_diff))
🤪🦞🤳🥔-🦏🥎-🙄🦣-🦌😶-😨😯-🦹🦣😄🥞 -- 🤪🦞🤳🥔-🦏🥎-🙄🦣-🦌😶-😨😯-🦹🦣😄🥞 -- 🦪🤜🦒🦵-🤏🧃-🙋🥓-🥟🥧-🦁🦹-🥪😎🧡🦗
>>> idoj == idoj_same
True
>>> idoj == idoj_diff
False
>>> idoj == "🤪🦞🤳🥔-🦏🥎-🙄🦣-🦌😶-😨😯-🦹🦣😄🥞"
True
>>> idoj == "🦪🤜🦒🦵-🤏🧃-🙋🥓-🥟🥧-🦁🦹-🥪😎🧡🦗"
False
```

Also comparison against UUIDs and their string representation is possible as
well.

```python
>>> uuidval = uuid4()
>>> print(uuidval)
627adf41-739a-4b5a-b727-d8add4124884
>>> idoj_from_uuid = IDoji(uuidval)
>>> idoj_from_uuid == uuidval
True
>>> idoj_from_uuid == "627adf41-739a-4b5a-b727-d8add4124884"
True
```

