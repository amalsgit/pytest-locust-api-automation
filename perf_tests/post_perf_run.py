from locust import HttpUser, between, task

from configs.config import get_environment
from api_helpers import posts
from perf_tests import perf_base


class PostPerformanceTests(HttpUser):

    wait_time = between(0.3, 0.8)

    env = get_environment()
    host_url = env.get("host_url")

    @task
    def get_post(self):
        with posts.get_posts(client=self.client, catch_response=True) as response:
            perf_base.assert_response(response, 200)
