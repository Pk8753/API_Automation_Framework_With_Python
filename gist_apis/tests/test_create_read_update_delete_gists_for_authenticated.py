
from gist_apis.src.gist_requests import Request
from gist_apis.schema import get_gist_schema
from gist_apis.schema import create_and_update_gists_schema
from gist_apis.config import ENV
from gist_apis.src.asserts import Asserts

class Test_CRUD_API_For_Authenticated_User():

    URL = ENV.BASE_URL
    gist_id = ""

    def test_create_a_gist_with_correct_data(self):
        headers={'Authorization':f'token {ENV.API_TOKEN}'}
        params='/gists'
        payload={"description":"GIST created by python code",
                "public":True,
                "files":{"python request module":
                        {"content":"Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"
                        }
                        }
                        }

        response = Request.create_gist(Test_CRUD_API_For_Authenticated_User.URL,headers,params,payload)
        Test_CRUD_API_For_Authenticated_User.gist_id = response.json()['id']
        Asserts.assert_code_status(response, 201)
        Asserts.assert_header_value_by_key(response,'Content-Type','application/json; charset=utf-8')
        Asserts.assert_header_value_by_key(response,'Server','GitHub.com')
        Asserts.assert_valid_schema(response.json(),create_and_update_gists_schema.create_gist_response_schema)
        

    def test_get_gist_with_correct_gistId(self):
        headers={'Authorization':f'token {ENV.API_TOKEN}'}
        params='/gists/'
        response = Request.get_a_gist(Test_CRUD_API_For_Authenticated_User.URL,headers,params,Test_CRUD_API_For_Authenticated_User.gist_id)
        # print(response.json())
        Asserts.assert_code_status(response, 200)
        Asserts.assert_json_has_key(response.json(),"id")
        Asserts.assert_valid_schema(response.json(),get_gist_schema.get_response_schema)
       
      

    def test_update_a_gist_with_correct_data(self):
        headers={'Authorization':f'token {ENV.API_TOKEN}'}
        params='/gists/'
        payload={"description":"GIST updated by python code",
                "public":True,
                "files":{"python request module":
                        {"content":"Python requests has 3 parameters: 1)Request URL\n 2)Header Fields\n 3)Parameter \n4)Request body"
                        }
                        }
                        }

        response = Request.update_a_gist(Test_CRUD_API_For_Authenticated_User.URL,headers,params,payload,Test_CRUD_API_For_Authenticated_User.gist_id)
        # print(response.json())
        Asserts.assert_code_status(response, 200)
        Asserts.assert_header_value_by_key(response,'Vary','Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding, Accept, X-Requested-With')
        Asserts.assert_valid_schema(response.json(),create_and_update_gists_schema.create_gist_response_schema)


    def test_get_gists_list_for_authenticated_user(self):
        header={'Authorization':f'token {ENV.API_TOKEN}'}
        params='/gists'
        response = Request.get_list_of_gist_for_all_user(Test_CRUD_API_For_Authenticated_User.URL,params,header)
        Asserts.assert_code_status(response, 200)
        Asserts.assert_header_value_by_key(response,'Content-Type','application/json; charset=utf-8')
        Asserts.assert_header_value_by_key(response,'Content-Encoding','gzip')
        for i in response.json():
            Asserts.assert_equals(i['owner']['login'],ENV.USERNAME,'Found different login user')
      
    def test_delete_a_gist_with_correct_data(self):
        headers={'Authorization':'token %s'%ENV.API_TOKEN}
        params='/gists/'
        response = Request.delete_a_gist(Test_CRUD_API_For_Authenticated_User.URL,headers,params,Test_CRUD_API_For_Authenticated_User.gist_id)
        Asserts.assert_code_status(response, 204)

