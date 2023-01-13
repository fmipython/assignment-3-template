"""
GitHub Proxy API
"""

def create_app():
    """
    Creates a Flask API

    The Flask configuration must be loaded from the file
    pointed by the environment variable FLASK_CONFIG_PATH

    Return the Flask app

    Routes:
    /
        Returns the string "Ok"
        Always succeeds with response code 200

    /health
        Returns the string "Ok"
        Always succeeds with response code 200

    /config
        Returns the server configuration, which was loaded from the FLASK_CONFIG_PATH variable
        The SECRET_KEY field of the config is removed.
        Always succeeds with response code 200

    /metrics
        Returns the recorder metrics by the server.
        The result excludes the data for the current call to /metrics
        An example of the metrics is:
        {
            'calls': 7,
            'errors': 3,
            'sent_bytes': 26,
            'last_clear': 1.0,
            'endpoints': {
                'health': {
                    'calls': 4,
                    'errors': 0,
                    'sent_bytes': 8,
                    'response_codes': {200: 4}
                },
                'fail': {
                    'calls': 3,
                    'errors': 3,
                    'sent_bytes': 18,
                    'response_codes': {418: 2, 404: 1}
                }
            },
        }

        The fields (schema of the metrics):
        * calls: int
            Total number of calls to all endpoints of the server
        * errors: int
            Total errors from calls to the server
            An error is any response with 4XX or 5XX error code
            It holds true that errors <= calls
        * sent_bytes: int
            Total bytes returned by the server from all endpoints
        * last_clear: float
            Time in seconds since the epoch as a floating point number
            This field records the last time when a metrics reset occurs
            (by the /reset_metrics endpoint)
        * endpoints: dict[endpoint name] -> dict
            For each endpoint of the server EN, we record individual metrics:
            * calls: int
                Number of calls to endpoint EN
            * errors
                Number of errors for the endpoint EN
            * sent_bytes
                Total number of bytes sent as responses from endpoint EN
            * response_codes: dict[response code] -> int
                A collection of counts for each response code that endpoint EN has returned
                If you collect all response codes, this field will be a Counter of them

    /reset_metrics
        Resets the metrics of the server to the default state
        {
            'endpoints': {},
            'calls': 0,
            'errors': 0,
            'sent_bytes': 0,
            'last_clear': # Current EPOCH timestamp
        }

    /fail
        Endpoint that always fails with error code 418
        This endpoint is implemented only when we are running in 'test' ENV
        The ENV is provided to flask from the config


    /repos/<user>
        Returns the names of all public repositories for the specified user
        The user is specified as a GET parameter <user>

        Uses:
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-a-user
        If the request to github fails an error is returned with response code 502

        Expects the 'token' header to be populated with the GITHUB_TOKEN of the user
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
        If it's an invalid (empty) token, it's ignored

        Returns a JSON object with 1 key: result, which has a list of all repositories
        e.g.
        {
            'result': [
                'fmipython/lectures',
                'fmipython/exam-cheatsheet'
            ]
        }

    /languages/<user>/<repo>
        Returns the languages for a user's repository
        The languages is a dictionary of language name and
        number of bytes of code written in that language
        The user is specified as a GET parameter <user>
        The repository is specified as a GET parameter <repo>

        Uses:
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-languages
        Should work with Api-Version 2022-11-28
        If the request to github fails an error is returned with response code 502

        Expects the 'token' header to be populated with the GITHUB_TOKEN of the user
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
        If it's an invalid (empty) token, it's ignored

        Returns a JSON object with 1 key: result, which has the result returned from GitHub
        e.g.
        {
            'result': {
                "C": 78769,
                "Python": 7769
            }
        }

    /repo/<user>/<repo>
        Returns the repository information for a user
        The repository information is the same as what's returned by
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository

        The user is specified as a GET parameter <user>
        The repository is specified as a GET parameter <repo>

        Uses:
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository
        Should work with Api-Version 2022-11-28
        If the request to github fails an error is returned with response code 502

        Expects the 'token' header to be populated with the GITHUB_TOKEN of the user
        https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
        If it's an invalid (empty) token, it's ignored

        Returns a JSON object with 1 key: result, which has the result returned from GitHub
        e.g.
        {
            'result': {
                "id": 1296269,
                "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
                ...
            }
        }

    """
    pass


if __name__ == '__main__':
    create_app().run()
