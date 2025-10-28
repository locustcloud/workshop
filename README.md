# Welcome to the Locust Tutorial

## 1. Set up Locust

Option 1: Run locally

```bash
> pip install locust
...
> locust -V
locust 2.42.1 from /Users/.../locust (Python 3.12.2)
```

Option 2: Run on [Locust Cloud](https://auth.locust.cloud/signup) (no setup needed)

## 2. Creating your first test

Open [locustfile.py](locustfile.py) (locally or in the [hosted test editor](https://auth.locust.cloud/editor))

```python
from locust import HttpUser, task

class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        self.client.get("/product/42")
```

## 3. Running your first test

Now, run your first test against a mock web shop hosted by us:

```bash
> locust --host https://mock-test-target.eu-north-1.locust.cloud
[2024-11-10 15:59:26,604] lars-mbp/INFO/locust.main: Starting Locust 2.42.1
[2024-11-10 15:59:26,608] lars-mbp/INFO/locust.main: Starting web interface at http://0.0.0.0:8089
```

Open the web ui and try running it! Just use a single user for now to not spam the service.

## 4. Use regular programming constructs in your test

```python
import time
from locust import HttpUser, task

class MyUser(HttpUser):
    @task
    def t(self):
        self.client.get("/")
        for i in range(5):
            time.sleep(1)
            self.client.get(f"/product/{i}")
```

* It is probably fairly obvious what this does, but go ahead and try it out anyway!

## 5. Use the debugger to run a single user

```python
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
```

If you're in VSCode, just launch the "Run current file" configuration.

Then you can:

* Try setting a breakpoint & examine the response object in real time

## 6. Use the catch_response flag to validate responses

```python
from locust import HttpUser, run_single_user, task

class MyUser(HttpUser):
    def t(self):
        with self.client.post(
            "/authenticate", json={"username": "foo", "password": "bar"}, catch_response=True
        ) as response:
            if err := response.json().get("error"):
                response.failure(err)

if __name__ == "__main__":
    run_single_user(MyUser)
```

* Try running this with a changed password and examine the results.

## 7. Use Locust Cloud from the terminal

Locust Cloud tests can are executed in the same way as local load tests.

Register for [Locust Cloud](https://auth.locust.cloud/signup) if you haven't already. When you are done, log in to the service:

```bash
locust --cloud --login
```

And then run your first test.

```bash
locust --cloud --host https://mock-test-target.eu-north-1.locust.cloud --users 100
```

Run a more [advanced test](locustfile_advanced.py) against the mock server:

```bash
locust --cloud --host https://mock-test-target.eu-north-1.locust.cloud -f locustfile_advanced.py --users 100 --rate 5
```

* Analyze the results
  * Peak throughput that the mock can handle?
  * Which requests are slow?
  * Are there any periodic variations?
  * ...

## References:

[Increase the request rate in tests](https://docs.locust.io/en/stable/increasing-request-rate.html)

The Locust Cloud blog:

1. [Breaking your website for fun and profit](https://locust.cloud/blog/performance-testing-part-1)

2. [Smoke, stress, spike, soak, and recovery: 5 essential load test profiles](https://locust.cloud/blog/5-essential-load-test-profiles)

3. [Closed vs Open Workload Models in Load Testing](https://locust.cloud/blog/closed-vs-open-workload-models)

4. [Garbage In, Garbage Out: Your Load Test Results Are Only as Reliable as Your Test Environment](https://locust.cloud/blog/performance-test-environments)

5. [16 ways to improve your load test scenarios](https://locust.cloud/blog/16-ways-to-improve-your-load-test-scenarios)

## Screenshots:

![alt text](https://cdn.prod.website-files.com/66596d70fa45b7e4c8ec4997/6731d678eab6e1028e060332_closed_load_rampup.png)
Notice how as new users are added, the response times start increasing and throughput starts to flatten, but the system is not completely overwhelmed.

![alt text](https://cdn.prod.website-files.com/66596d70fa45b7e4c8ec4997/6731d677f7c25db1c8ea12cd_closed_load_variations.png)
Closed load: Variations in response times cause variations in throughput

![alt text](https://cdn.prod.website-files.com/66596d70fa45b7e4c8ec4997/6731d677110f61ca6749f8a3_open_load_stable_throuhgput.png)
Open load: Stable throughput despite variations in response times

Add image showing difference in response time for different requests.