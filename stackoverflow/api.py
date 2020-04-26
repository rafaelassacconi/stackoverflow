from stackoverflow.resources import ENDPOINTS
from stackoverflow.exceptions import StackOverflowError


class StackOverflow:
    """ Simple wrapper for Stack Overflow REST API """

    def __init__(self, version="2.2"):
        self.base_url = "https://api.stackexchange.com" 
        self.version = version

    def __make_request(self, service: str, payload: dict = {}) -> dict:
        """
        Make a basic request for the API

        Parameters:
        - service: the name of the API service
        - payload: dict with data of request

        Returns the response.content data
        """
        endpoint = ENDPOINTS[service]
        url = "/".join([self.base_url, self.version, endpoint["path"]])

        try:
            response = endpoint["method"](url, data=payload)
        except Exception as e:
            raise StackOverflowError(str(e))

        if not response.ok:
            raise StackOverflowError(
                "%s: %s" % (response.reason, response.json().get("error_message", ""))
            )

        return response.json()

    def search_questions(self, tags: str, max: int = 10) -> list:
        """
        Calls API endpoint: /questions
        This method allows you make flexible queries of questions.
        Doc: https://api.stackexchange.com/docs/questions

        Parameters:
        - tags: tags that will be used in the search (semi-colon delimited)
        - max: max results in the response

        Returns a list of questions.
        """
        data = {
            "order": "desc",
            "sort":"votes",
            "site": "stackoverflow",
            "pagesize": str(max),
            "tagged": tags,
        }

        result = self.__make_request("question_list", data)
        return result.get("items", [])
