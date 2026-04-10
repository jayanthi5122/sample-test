# Bug Report

## 1. Missing Authentication Enforcement
- API: ReqRes
- Issue: Requests without API key return 401
- Severity: High
- Impact: Unauthorized access prevention
- Fix: Require x-api-key header

## 2. Data Inconsistency
- Issue: Order references non-existent userId
- Severity: High
- Impact: Data integrity issue

## 3. GraphQL Error Handling
- Issue: Invalid query returns 200 instead of proper error code
- Severity: Medium
- Impact: Silent failures possible

## 4. No Rate Limiting
- Issue: API allows repeated requests
- Severity: Medium
- Impact: Risk of abuse

## 5. Performance Delay
- Issue: Delay endpoint shows slow response
- Severity: Low
- Impact: User experience degradation