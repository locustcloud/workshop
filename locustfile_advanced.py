import itertools
import random
import time

from locust import FastHttpUser, constant, run_single_user, task

users = itertools.cycle(
    [
        ("foo1", "bar"),
        ("foo2", "bar"),
        ("foo3", "bar"),
        # ... normally you'd be reading this from a database or csv file
    ]
)
product_ids = [1, 2, 42, 4711]


class MyUser(FastHttpUser):
    @task
    def t(self):
        username, password = next(users)

        # log in using rest() wrapper method
        with self.rest(
            "POST", "/authenticate", json={"username": username, "password": password}
        ) as resp:
            if err := resp.js.get("error"):
                resp.failure(err)

        # view and add two random products to cart
        for product_id in random.sample(product_ids, 2):
            time.sleep(1)
            self.client.get(f"/product/{product_id}")
            # use .rest method for built in response checking and better type hints
            with self.rest("POST", "/cart/add", json={"productId": product_id}) as resp:
                if error := resp.js.get("error"):
                    resp.failure(error)

        # place order
        with self.rest("POST", "/checkout/confirm") as resp:
            if not resp.js.get("orderId"):
                resp.failure("orderId missing")

        self.client.get("/intermittent-spikes")


class JustBrowsingUser(FastHttpUser):  # this user is just looking at stuff
    wait_time = constant(5)  # sleep 5s between iterations

    @task
    def t(self):
        self.client.get("/")

        for product_id in random.sample(product_ids, 2):
            self.client.get(f"/product/{product_id}")


if __name__ == "__main__":
    run_single_user(MyUser)
