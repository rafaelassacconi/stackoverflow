# Python Stack Overflow Wrapper

Python Wrapper for Stack Exchange API.

- API Documentation in [api.stackexchange.com/docs](https://api.stackexchange.com/docs)
- API Version: 2.2
 
### How to use
Install this package:
```
pip install git+https://github.com/rafaelassacconi/stackoverflow.git
```

Example of searching questions by tag:
```
from stackoverflow.api import StackOverflow

stackoverflow = StackOverflow()
result_list = stackoverflow.search_questions("python")

for item in result_list:
    print(item["title"])
    print(item["link"])
```

Example of searching questions by multiple tags and max number of results:
```
stackoverflow.search_questions(tags="python;test;tdd", max=5)
```

### Methods
The first version of this wrapper contains one method:
| Method | Description |
| --- | --- |
| `search_questions` | Returns a list of questions related with the tags used in searching |

### Tests
For run the tests, install the `pytest` package and run the command bellow:
```
pytest
```