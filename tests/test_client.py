import pytest
from stackoverflow.api import StackOverflow
from stackoverflow.exceptions import StackOverflowError


def test_client_with_not_found_version():
    """ Call question search method with no parameters"""
    client = StackOverflow(version="99.9")

    with pytest.raises(StackOverflowError) as excinfo:
        client.search_questions("python")

    assert "Bad Request" in str(excinfo.value)
