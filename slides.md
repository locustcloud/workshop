---
marp: true
class: invert
header: '![](logo_header.png)'
---

# Write Load Tests in Python and Run Them in the Cloud

* Write and and run your first load tests using Locust
* Interpret test results and do basic root cause analysis
* Avoid common pitfalls when designing/running load test scenarios
* Scale and simplify test runs by using Locust Cloud

---

## Welcome!

---
<!--
header: ''
-->
<!-- 
I hope you're all having a good conference and that you enjoyed lunch
How many have run a load tests before
How many have used locust?
FOSS, MIT License
Downloaded 50M times, 25k stars on GitHub
-->

<!-- <style>
img {
  display: block;
  margin: auto;
  max-width: 100%; /* Ensures the image does not overflow */
  max-height: 70%; /* Ensures the image does not overflow */
}
</style> -->
![bg h:90%](image-1.png)
<!-- ![center:100%](image-1.png) -->

---
<!--
header: '![](logo_header.png)'
-->
## Step 1: Locust & locustfile basics

* Clone the workshop repo: https://github.com/locustcloud/locust-workshop

* Follow the instructions there

---

## Step 2: Register for Locust Cloud (free) and run your tests in the cloud

* Register for Locust Cloud: https://locust.viewer.locust.cloud/signup
* Use access code: !LARRY@PYCON!
* Confirm your email and follow the instructions to set username and password
* Run it:

```bash
> locust-cloud --users 50 -H http://test-target-mock
[LOCUST-CLOUD] INFO: Authenticating (eu-north-1, v1.9.1)
...
[2024-11-10 15:47:12,111] master-.../INFO/locust.main: Starting web interface at https://locust.webui.locust.cloud/<your id>
```

* Follow the link to the web interface and launch a test!

---

1. Run your tests from the Cloud
1. Explore the reports (what can we say about the performance of the system under test?)

---

## Step 3: Analyze and

Divide and conquer
* Which requests are slow?
* Is it slow in a regular browser too?
* Resource metrics (CPU, network, connection pools etc)
* Internal response times (tracing, OTEL)

* configuration


---

* Debugging tests
* Improving your tests (assertions, early exit, loops & weights, etc)
* Q&A

## Further reading

The Locust Cloud blog:

1. [Breaking your website for fun and profit, an experienced load tester’s guide](https://www.locust.cloud/blog/performance-testing-part-1)

2. [Smoke, stress, spike, soak, and recovery: 5 essential load test profiles](https://www.locust.cloud/blog/5-essential-load-test-profiles)

3. [Locusts and Honey Badgers — Closed vs Open Workload Models in Load Testing](https://www.locust.cloud/blog/closed-vs-open-workload-models)

4. [Garbage In, Garbage Out: Your Load Test Results Are Only as Reliable as Your Test Environment](https://www.locust.cloud/blog/performance-test-environments)

5. [16 ways to improve your load test scenarios](https://www.locust.cloud/blog/16-ways-to-improve-your-load-test-scenarios)