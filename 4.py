import time

from locust import HttpUser, task


class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        for i in range(5):
            time.sleep(1)
            self.client.get(f"/product/{i}")
