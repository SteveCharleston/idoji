"""Fixtures for testing."""
import os
import sys
from collections import namedtuple

import pytest

# Add src directory to search path
code = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, code + "/../src/")


@pytest.fixture()
def uuididoji():
    """Return a namedtuple with uuid and corresponding idoji."""
    holder = namedtuple("UuidIdojiHolder", "uuid idoji")
    return holder(
        "67b8660e-831c-4f13-8fe9-dfa20d5fbbb5",
        "🤣🦇🤢😎-🥑😜-🙏😓-🥝🦸-🦮🥰-😍🤛🦊🦄",
    )
