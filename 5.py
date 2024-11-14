from locust import HttpUser, run_single_user, task


class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        for i in range(5):
            response = self.client.get(f"/product/{i}")
        self.client.get("/this_does_not_exist")


if __name__ == "__main__":
    run_single_user(MyUser)
