# QA + AI Assessment – Distributed System Testing

## 📌 Overview
This project demonstrates a QA testing approach for a distributed system using multiple independent public services.

The goal is to simulate real-world system behavior and identify risks related to:
- API interactions
- Authentication
- Data consistency
- Performance
- Security
- Failure scenarios

---

## 🏗️ System Under Test

The system is composed of:

- User Service → ReqRes API  
- Orders Service → JSONPlaceholder  
- Geo Service → GraphQL Countries API  
- Performance Layer → httpbin  
- Data Validation → Simulated dataset  

---

## 🧪 Test Coverage

This project includes:

### ✔ API Testing
- ReqRes user API
- JSONPlaceholder orders API

### ✔ GraphQL Testing
- Valid and invalid queries
- Error handling

### ✔ Data Validation
- Cross-service consistency checks

### ✔ Performance Testing
- Latency simulation using httpbin

### ✔ Security Testing
- Authentication behavior
- API access without API key

---

## 📂 Project Structure
