def assert_response(response, status_code):
    """Assert response code for api calls made during locust runs"""
    if response.status_code == status_code:
        response.success
        print("request passed")
    else:
        response.failure(response.status_code)
        print("request failed")