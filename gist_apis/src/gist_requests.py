from email import header
from faulthandler import is_enabled
from wsgiref import headers
from pytest import param
import requests
import requests_cache
import json

from gist_apis.config import ENV


class Request:

     
    def create_gist(url,headers,params,payload):
        URL = url+params
        return requests.post(URL,headers=headers,data=json.dumps(payload))
     
    def delete_a_gist(url,headers,params,gist_id):
        URL = url+params+gist_id
        return requests.delete(URL,headers=headers)
        
    def get_a_gist(url,headers,params,gist_id):
        URL = url+params
        return requests.get(URL+gist_id,headers=headers)
 
    def update_a_gist(url,headers,params,payload,gist_id):
        URL = url+params+gist_id
        return requests.patch(URL,headers=headers,data=json.dumps(payload))

    def get_list_of_gist_for_all_user(url,params,header):
        URL = url + params
        return requests.get(URL,headers=header)

    def get_public_gists_for_a_user(url,params,user_name):
        URL = url+'/users/'+user_name+params
        return requests.get(URL)
