import pytest
from stackoverflow.api import StackOverflow


@pytest.fixture
def stackoverflow():
    """ Returns the client """
    return StackOverflow()
