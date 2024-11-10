# Locust Cloud Workshop (part 1)

## 1. Installation & creating your first test

```bash
> pip install locust-cloud
...
> locust -V
locust 2.32.2 from /Users/.../locust (Python 3.12.2)
```

Alternatively (standing in this repo):

```bash
> uv sync
...
> uv run locust -V
locust 2.32.2 from /Users/.../workshop/.venv/.../locust (Python 3.12.2)
```

If you have issues, see https://docs.locust.io/en/stable/installation.html

---

Create a file called locustfile.py:

```python
from locust import HttpUser, task

class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        self.client.get("/products/42")
```

---

## 2. Running your first test

```bash
> locust -H https://<test server>
[2024-11-10 15:59:26,604] lars-mbp/INFO/locust.main: Starting Locust 2.32.2
[2024-11-10 15:59:26,608] lars-mbp/INFO/locust.main: Starting web interface at http://0.0.0.0:8089
```

Open the web ui and try running it! Just use a single user for now, you'll get your own target server later.

## 3. Use regular programming constructs in your test

```python
from locust import HttpUser, task

class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        for i in range(5):
            self.client.get(f"/products/{i}")
```

## 4. Use the debugger to run a single user

```python
from locust import HttpUser, run_single_user, task

class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        for i in range(5):
            response = self.client.get(f"/products/{i}")
        self.client.get("/this_does_not_exist")

if __name__ == "__main__":
    run_single_user(MyUser)
```

If you're in VSCode, just launch the "Run current file" configuration.

* Try setting a breakpoint
* Examine the response object

## 5. Use the catch_response flag to validate responses

```python
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
```

* Try running this with a changed username and password.
