from pyparsing import empty
from gist_apis.src.gist_requests import Request
from gist_apis.config import ENV
from gist_apis.src.asserts import Asserts


class Test_CRUD_API_For_Unauthenticated_User():

    URL = ENV.BASE_URL
    gist_id = ""

    def test_create_a_gist_with_incorrect_token(self):
        headers={'Authorization':f'token {ENV.FAKE_TOKEN}'}
        params='/gists'
        payload={"description":"GIST created by python code using fake token",
                "public":True,
                "files":{"python request module":
                        {"content":"Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"
                        }
                        }
                        }

        response = Request.create_gist(Test_CRUD_API_For_Unauthenticated_User.URL,headers,params,payload)
        Asserts.assert_code_status(response, 401)
        Asserts.assert_json_value_by_key(response,'message','Bad credentials')

    def test_create_a_gist_with_incorrect_endpoint(self):
        headers={'Authorization':f'token {ENV.API_TOKEN}'}
        params='/gists/Test404'
        payload={"description":"GIST created by python code",
                "public":True,
                "files":{"python request module":
                        {"content":"Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"
                        }
                        }
                        }
        response = Request.create_gist(Test_CRUD_API_For_Unauthenticated_User.URL,headers,params,payload)
        Asserts.assert_code_status(response, 404)
        Asserts.assert_json_value_by_key(response,'message','Not Found')

    def test_get_gists_list_for_unauthenticated_user(self):
        params='/gists'
        response = Request.get_list_of_gist_for_all_user(Test_CRUD_API_For_Unauthenticated_User.URL,params,header={})
        Asserts.assert_code_status(response, 200)
        Asserts.assert_header_value_by_key(response,'Content-Type','application/json; charset=utf-8')
        Asserts.assert_header_value_by_key(response,'Content-Security-Policy',"default-src 'none'")

    def test_get_public_gists_for_specified_user_unauthenticated_user(self):
        params='/gists'
        response = Request.get_public_gists_for_a_user(Test_CRUD_API_For_Unauthenticated_User.URL,params,ENV.USERNAME)
        Asserts.assert_code_status(response, 200)
        if (response.json()) != empty: #for empty response api should return 204 but it is retuning 200
            for i in response.json():
                Asserts.assert_equals(i['owner']['login'],ENV.USERNAME,'Found different login user')