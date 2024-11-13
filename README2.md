# Locust Cloud Workshop (part 2)

Run a test against your own mock server:

```bash
locust-cloud --users 100 --mock-server
```

Run a more [advanced test](locustfile_advanced.py) against the mock server:

```bash
locust-cloud -f locustfile_advanced.py --users 100 --rate 5 --mock-server
```

* Analyze the results
  * Peak throughput that the mock can handle?
  * Which requests are slow?
  * Are there any periodic variations?
  * ...
