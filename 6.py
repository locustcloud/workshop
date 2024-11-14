from locust import HttpUser, run_single_user, task


class MyUser(HttpUser):
    @task
    def t(self):
        with self.client.post(
            "/authenticate", json={"username": "foo", "password": "bar"}, catch_response=True
        ) as response:
            if err := response.json().get("error"):
                response.failure(err)


if __name__ == "__main__":
    run_single_user(MyUser)
