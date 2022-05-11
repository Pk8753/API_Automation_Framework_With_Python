
## Instruction To Run Test ##


*For virtualenv To Install All Library/Dependency From requirement.txt File.*

1. cd to the directory where requirements.txt is located.

2. activate your virtualenv

3. run: pip install -r requirement.txt in your shell


*Update Config File Before Running Test*

1. USERNAME = '<git user_name>'
2. API_TOKEN = '<git token>'
3. FAKE_TOKEN = '<Any random string>'
4. BASE_URL = 'https://api.github.com'



*Run Test From Commnad Line*

1. Go to project folder.
2. run single test file.
`python3 -m pytest -v gist_apis/tests/test_create_read_update_delete_gists_for_unauthenticated.py `

3. run all the test from all test file 
`python3 -m pytest -v gist_apis/tests `

