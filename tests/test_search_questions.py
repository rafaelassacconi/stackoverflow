import pytest


def test_search_questions_no_parameters(stackoverflow):
    """ Call question search method with no parameters"""
    with pytest.raises(TypeError) as excinfo:
        stackoverflow.search_questions()

    assert "missing 1 required positional argument" in str(excinfo.value)

def test_search_questions_result_structure(stackoverflow):
    """ Check the json structure of the response """
    result = stackoverflow.search_questions(tags="python")

    assert type(result) == list
    assert len(result) == 10

    item = result[0]    

    keys = [
        "tags", 
        "owner", 
        "is_answered", 
        "view_count", 
        "protected_date", 
        "accepted_answer_id", 
        "answer_count", 
        "score", 
        "last_activity_date", 
        "creation_date", 
        "last_edit_date", 
        "question_id", 
        "link", 
        "title",
    ]

    for key in keys:
        assert key in item

def test_search_questions_many_tags(stackoverflow):
    """ Serch with more than one tag """
    max_results = 2
    result = stackoverflow.search_questions(tags="python;django;rest", max=max_results)

    assert type(result) == list
    assert len(result) == max_results

def test_search_questions_not_found_tag(stackoverflow):
    """ Search with a tag that not exists """
    result = stackoverflow.search_questions(tags="tagtestnotfoundstackwrapper")

    assert type(result) == list
    assert len(result) == 0
