from locust import HttpUser, task


class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        self.client.get("/product/42")
