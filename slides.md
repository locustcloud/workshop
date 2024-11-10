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
I hope you're all having a good conference and that you enjoyed lunch.

Me: Maintainer of Locust & founder of Locust Technologies
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
![bg h:90%](image-1.png)

---
<!--
header: '![](logo_header.png)'
-->
## Step 1: Locust & locustfile basics

- Clone the workshop repo: https://github.com/locustcloud/locust-workshop
- Follow the instructions there

---

## Step 2: Register for Locust Cloud and run your tests in the cloud

- Register for Locust Cloud: https://locust.viewer.locust.cloud/signup
- Use access code: !LARRY@PYCON!
- Confirm your email and follow the instructions to set username and password
- Run it:

```bash
> locust-cloud --users 50 -H http://test-target-mock
[LOCUST-CLOUD] INFO: Authenticating (eu-north-1, v1.9.1)
...
[2024-11-10 15:47:12,111] master-.../INFO/locust.main: Starting web interface at https://locust.webui.locust.cloud/<your id>
```

- Follow the link to the web interface and launch a test!

---

## Step 3: Understanding test results

Debug your application

- Which requests are slow? What is the difference? (example using Locust Cloud)
- Resource metrics (CPU, network, connection pool usage etc)
- Internal response times (tracing, OTEL)
- ...

---

## Step 3: Understanding test results

Debug your load generation

- Make sure you have launched enough Users
- If you use IP-based load balancing you might not hit all instances (use X-Forwarded-For or additional loadgen IP:s)
- Check your load test code for loops/heavy things
- Check your logs for CPU usage warnings (maybe you need to run distributed or need more servers)
- Is it slow from another location/browser? (if not, then it could be throttling/DDoS protection)

---

## To infinity and beyond!

- https://medium.com/locust-cloud/16-ways-to-improve-your-load-test-scenarios-a90372db283a
- Q&A

---
<!-- excellent rubber duck -->
## One more thing...

![h:300](image-7.png)

![h:300](image-6_small.png)
