from environs import Env

env = Env()
env.read_env()

environments = {
    "local": {
        "host_url": "https://jsonplaceholder.typicode.com/",
    },
    "development": {
        "host_url": "https://jsonplaceholder.typicode.com/",
    },
    "staging": {
        "host_url": "https://jsonplaceholder.typicode.com/",
    },
    "production": {
        "host_url": "https://jsonplaceholder.typicode.com/",
    },
}


def get_environment():
    app_env = environments.get(env("app_env", "local"))
    print(f"""Tests will be run against {app_env} environment""")
