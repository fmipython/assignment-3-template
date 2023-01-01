import os


# Provide command line/environment variables to tests
# These variables are:
# - token: a GITHUB token, used to access the GH API
def pytest_addoption(parser):
    parser.addoption("--token", action="store", default=None)


def pytest_generate_tests(metafunc):
    if 'token' in metafunc.fixturenames:  # if the test requires the token
        option_value = metafunc.config.option.token
        if option_value is not None:  # if passed as cmd argument --token ...
            metafunc.parametrize("token", [option_value])
        else:
            token = os.getenv('GITHUB_TOKEN')
            metafunc.parametrize("token", [token])
