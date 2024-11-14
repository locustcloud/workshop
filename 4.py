import time

from locust import HttpUser, task


class MyUser(HttpUser):
    host = "https://mock-test-target.eu-north-1.locust.cloud"

    @task
    def t(self):
        self.client.get("/")
        for i in range(5):
            time.sleep(1)
            self.client.get(f"/product/{i}")
