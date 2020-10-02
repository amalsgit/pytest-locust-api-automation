import requests
import allure
from configs.config import get_environment


env = get_environment()
host_url = env.get("host_url")


def get(client, path, **kwargs):
    """Http GET method"""
    result = client.get(host_url + path, **kwargs)
    if client == requests:
        save_request_details(result.request)
        save_response_details(result)
    return result


def post(client, path, **kwargs):
    """Http POST method"""
    result = client.post(host_url + path, **kwargs)
    if client == requests:
        save_request_details(result.request)
        save_response_details(result)
    return result


def put(client, path, **kwargs):
    """Http PUT method"""
    result = client.put(host_url + path, **kwargs)
    if client == requests:
        save_request_details(result.request)
        save_response_details(result)
    return result


def delete(client, path, **kwargs):
    """Http DELETE method"""
    result = client.delete(host_url + path, **kwargs)
    if client == requests:
        save_request_details(result.request)
        save_response_details(result)
    return result


def patch(client, path, **kwargs):
    """Http PATCH method"""
    result = client.patch(host_url + path, **kwargs)
    if client == requests:
        save_request_details(result.request)
        save_response_details(result)
    return result


def save_request_details(request):
    """Attach request details to test report"""
    allure.attach(
        "\n{}\n{}\n\n{}\n\n{}\n".format(
            "-----------Request----------->",
            request.method + " " + request.url,
            "\n".join("{}: {}".format(k, v) for k, v in request.headers.items()),
            request.body,
        ),
        "Request details",
    )


def save_response_details(response):
    """Attach response details to test report"""
    allure.attach(
        "\n{}\n{}\n\n{}\n\n{}\n".format(
            "<-----------Response-----------",
            "Status code:" + str(response.status_code),
            "\n".join("{}: {}".format(k, v) for k, v in response.headers.items()),
            response.text,
        ),
        "Response details",
    )