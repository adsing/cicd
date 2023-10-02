Testing Github actions CI with previously simple module (includes tests).

Pytest: Had to add __init__.py under tests to get around ModuleNotFoundError for "mymodule". Alternatively, add conftest.py to update sys.path. 

Pytest hack from https://stackoverflow.com/questions/20971619/ensuring-py-test-includes-the-application-directory-in-sys-path