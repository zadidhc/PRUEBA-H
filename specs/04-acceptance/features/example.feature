@spec-first
Feature: Service Health and Readiness
  As a client or system operator
  I want to check the health endpoint
  So that I know the service is running and ready to accept traffic

  Scenario: Health check returns status OK
    Given the service is initialized and running
    When a GET request is made to "/health"
    Then the response status code should be 200
    And the response body should match the schema:
      """json
      {
        "status": "ok"
      }
      """
