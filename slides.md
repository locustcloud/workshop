---
marp: true
class: invert
---
<!--
animate: false
header: ''
-->
# Write Load Tests in Python and Run Them in the Cloud

- Write and and run your first load tests using Locust
- Scale and simplify test runs by using Locust Cloud
- Interpret test results and do basic root cause analysis
- Avoid common pitfalls when designing/running load test scenarios

---

## Welcome!

<!-- 
I hope you're all having a good conference!

Me: Maintainer of Locust & founder of Locust Technologies.
My colleagues will be in the room 
-->

---
<!--
header: ''
-->
<!-- 
How many have run a load tests before
How many have used locust?
FOSS, MIT License
Downloaded 50M times, 25k stars on GitHub
-->
![bg h:90%](locust_github_page.png)

---
<!--
header: '![](logo_header.png)'
-->
## What is Locust anyway?
<!--
complex flows like loops or conditional behaviour. 

generate test data on the fly or do any processing that would normally happen on your clients

Tests can be version controlled & diffed. Easier to collaborate

Reusing code between test cases is as simple as importing a module.
-->

- User behaviour defined in plain Python code
* Supports most Python libraries and protocols (WebSockets, gRPC, Kafka, MQTT, ...)
* Distributed
* CLI + WebUI
* No client side JavaScript etc

---

## Write and and run your first load tests using Locust

- Clone the workshop repo: https://github.com/locustcloud/locust-workshop
* Demo! (and then follow the instructions in the readme)
&nbsp;
&nbsp;
&nbsp;

---

## How did it go?

- Were you able to test stuff
- Comments, feedback
&nbsp;
&nbsp;
&nbsp;
---

## Locust Cloud

- Run Locust on our servers
  * No need to set up and coordinate load generators
  * Persistent reports you can go back to and compare
  * CI runs using Github Actions or web hook
  * Easier/deeper analysis with built-in OTEL support
  * Same syntax as "local" Locust-runs

---

## Locust Cloud

- Start as low as $149/mo, scales as high as 5M concurrent users
* Commercial support
&nbsp;
&nbsp;
&nbsp;

---

## Run your first test in the cloud

- Register: https://locust.cloud/signup
- Use access code: !LARRY@PYCON!
- Confirm your email and follow the instructions to set username and password
- Run it, together with your own mock server instance for testing:

```
> locust-cloud --users 100 --mock-server
[LOCUST-CLOUD] INFO: Authenticating (eu-north-1, v1.9.1)
...
[2024-11-10 15:47:12,111] master-.../INFO/locust.main: Starting web interface at https://locust.webui.locust.cloud/<your id>
```

---

## More tests in the cloud

Run a more advanced test (locustfile_advanced.py) against the mock server:

```
locust-cloud -f locustfile_advanced.py --users 100 --rate 5 --mock-server
```

* Analyze the results
  - Peak throughput that the mock can handle?
  - Which requests are slow?
  - Are there any periodic variations?
  - ...

---

## Understanding test results

Debug your application

* Which requests are slow? What is the difference between them?
* Is there a periodic behaviour? (could be due to background jobs, DB analysis etc)
* Resource metrics (CPU, network, connection pool usage etc)
* Internal response times (tracing, OTEL)
* ...
* https://medium.com/locust-cloud/

---

## Understanding test results

Debug your load generation

* Make sure you have launched enough Users
* If you use IP-based load balancing you might not hit all instances (use X-Forwarded-For or additional loadgen IP:s)
* Check your load test code for loops/heavy things
* Check your logs for CPU usage warnings (maybe you need to run distributed or need more servers)
* Is it slow from another location/browser? (if not, then it could be throttling/DDoS protection)

---

## Advanced scenarios

* on_start
* Early exit
* Weights
* https://docs.locust.io / examples here https://github.com/locustio/locust

---
<!--
* User behaviour defined in plain Python code
* Supports most Python libraries and protocols (WebSockets, gRPC, Kafka, MQTT, ...)

* Distributed load generation out of the box
* Persistent reports
* Deeper analysis (built-in OTEL)
* Automation (using GitHub Actions or plain POST)
* Support
* You can get started cheap and grow as you need it. Free tier is coming
-->
## Recap

* Locust
* Locust Cloud
* https://medium.com/locust-cloud
* Questions?
* One more thing...

---
<!-- excellent rubber duck -->
## One more thing...

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![h:350](locust_plush_stock.png) ![h:350](locust_plush_on_screen.png)
