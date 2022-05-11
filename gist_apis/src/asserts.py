import json
from requests import Response
from jsonschema import validate


class Asserts:
     
    def assert_valid_schema(data, schema_file):
            return validate(data, schema_file)

    def assert_equals(val1, val2, error_massage: str = ""):
        assert val1 == val2, f"Failed assertion that {val1} is equals {val2}. {error_massage}"

     
    def assert_code_status(response: Response, expected_code: int, message: str = ""):
        assert response.status_code == expected_code, \
            f'Expected status code {expected_code}, but got {response.status_code}. {message}'

     
    def assert_response_text(response: Response, expected_text: str, message: str = ""):
        assert response.json() == expected_text, \
            f'Expected response text "{expected_text}", but got "{response.text}". {message}'

     
    def assert_json_value_by_key(response: Response, key: str, val: str):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.text}"'

        assert key in response_as_dict, \
            f'Response json does\'n have key "{key}"'

        assert response_as_dict[key] == val, \
            f'Response key "{key}" has value {response_as_dict[key]} but expected is {val}'

     
    def assert_json_has_key(response: Response, key: str):
        assert key in response, \
            f'Response json does not have a key "{key}" which is expected. JSON text: "{response}"'

     
    def assert_response_has_headers(response: Response, key: str):
        assert key in response.headers, \
            f'Cannot find header with name {key} in the response. All headers in the response: ' \
            + str(response.headers)

    def assert_header_value_by_key(response: Response, key: str, val: str):
        try:
            response_as_dict = response.headers
        except json.decoder.JSONDecodeError:
            assert False, f'Response is not in JSON format. Response text is "{response.headers}"'

        assert key in response_as_dict, \
            f'Response json does\'n have key "{key}"'

        assert response_as_dict[key] == val, \
            f'Response key "{key}" has value {response_as_dict[key]} but expected is {val}'
