from locust import HttpUser, between, task

from configs.config import get_environment
from actions import post_actions as posts
from faker import Faker

fake = Faker()


class PostPerformanceTests(HttpUser):

    wait_time = between(0.3, 0.8)

    @task
    def get_all_posts(self):
        posts.get_posts(client=self.client, catch_response=True)

    @task
    def create_and_delete_post(self):
        user_id = 1
        post_title = fake.name()
        post_body = fake.sentence()

        # Create post
        with posts.create_posts(
            post_title, post_body, user_id, client=self.client, catch_response=True
        ) as response:
            self.post_id = response.json()["id"]
            print(self.post_id)

        # Delete post
        posts.delete_post(self.post_id, client=self.client, catch_response=True)
