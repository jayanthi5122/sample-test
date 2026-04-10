## Performance Testing – Delayed Response Simulation

### Endpoint Tested
GET https://httpbin.org/delay/2

### Objective
To simulate network latency and evaluate system behavior under slow downstream service conditions.

### Observation
- The API response was intentionally delayed by ~2 seconds
- Response returned successfully with status 200
- No failure occurred, but latency is clearly visible

### Risk
In a distributed system:
- Slow downstream services can delay the entire workflow
- Multiple chained API calls can amplify latency
- This can impact user experience and increase timeout risk

### Conclusion
The system must handle delays using:
- timeouts
- retries with backoff
- async processing (queues)
- caching where possible

### Evidence
See: evidence/screenshots/performance_delay.png