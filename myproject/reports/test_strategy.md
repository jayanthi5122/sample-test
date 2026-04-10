# QA + AI Assessment – Test Strategy

## 1. Objective
The objective of this testing effort is to evaluate a distributed system composed of independent services including REST APIs, GraphQL, and performance endpoints. 

The focus is to identify risks related to:
- Data consistency
- Authentication and security
- API reliability
- Performance under latency
- Failure handling

---

## 2. Test Approach

A **risk-based testing approach** was adopted to prioritize critical areas of the system.

### Focus Areas:
- Authentication and authorization validation
- Data consistency across services
- API correctness and error handling
- GraphQL query validation
- Performance under delayed conditions
- Failure and chaos scenarios

---

## 3. Scope of Testing

### Included:
- REST API testing (ReqRes, JSONPlaceholder)
- GraphQL testing (Countries API)
- Data validation testing using simulated dataset
- Performance testing using httpbin delay endpoint
- Security testing (authentication behavior)

### Excluded:
- Full UI automation
- Real system integration (services are independent)

---

## 4. End-to-End Workflow Simulation

Since the services are not integrated, a simulated workflow was created:

User → ReqRes (User Service) → JSONPlaceholder (Orders)
→ GraphQL (Geo Enrichment) → Data Validation → Performance Layer

### Success Criteria:
- Valid user exists
- Order correctly mapped to user
- Country data retrieved successfully
- No data inconsistencies

---

## 5. Key Risks Identified

### 1. Data Inconsistency (High)
Orders may reference users that do not exist, leading to broken relationships.

### 2. Authentication Gaps (High)
Inconsistent enforcement of API authentication across endpoints.

### 3. Silent Failures (Medium)
GraphQL returns HTTP 200 even when errors occur.

### 4. Performance Bottlenecks (Medium)
Latency in one service can affect the entire workflow.

---

## 6. Test Coverage

### API Testing
- Status code validation
- Schema validation
- Negative testing (invalid inputs)

### GraphQL Testing
- Valid queries
- Invalid queries
- Error response validation

### Data Validation
- Referential integrity checks
- Detection of invalid user-order mapping

### Performance Testing
- Delayed response simulation using httpbin
- Response time observation

### Security Testing
- Authentication validation using API key
- Unauthorized access scenarios
- API misuse checks

---

## 7. Assumptions

- Services are independent and not integrated
- Data flow is simulated
- Public APIs represent real-world systems

---

## 8. Tools Used

- pytest (automation framework)
- requests (API testing)
- pandas (data validation)
- curl (manual API testing)

---

## 9. Conclusion

This test strategy demonstrates a structured and risk-based approach to testing a distributed system. The focus on data consistency, authentication, and performance highlights real-world QA challenges and system-level risks.