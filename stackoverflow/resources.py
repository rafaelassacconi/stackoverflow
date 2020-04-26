import requests


ENDPOINTS = {
    "question_list": {
        "path": "questions",
        "method": requests.get,
    },
    "tags_related": {
        "path": "/tags/{tags}/related",
        "method": requests.get,
    }
}
