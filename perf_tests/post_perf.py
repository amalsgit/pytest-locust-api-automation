from locust import HttpUser, between, task

from configs.config import get_environment


class PostPerformanceTests(HttpUser):

    wait_time = between(0.3, 0.8)

    env = get_environment()
    host_url = env.get("host_url")

    @task
    def get_posst(self):
        with self.client.get(self.host_url + "posts", catch_response=True) as response:
            if response.status_code == 200:
                response.success
                print("request passed")
            else:
                response.failure(response.status_code)
                print("request failed")
