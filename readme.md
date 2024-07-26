# Average Calculator HTTP Microservice

This project is a Django-based microservice that calculates the average of numbers fetched from an external test server. The microservice exposes a REST API that accepts qualified number IDs and performs the necessary calculations.

## Features

- Fetches numbers based on qualified IDs:
  - `p` for prime
  - `f` for Fibonacci
  - `e` for even
  - `r` for random
- Configurable window size (default: 10)
- Ensures stored numbers are unique, disregarding duplicates
- Handles server response times and retries
- Maintains quick response times, never exceeding 500 milliseconds

## API Endpoints

### GET `/numbers/<type>/`

Fetches numbers based on the type specified in the URL and calculates the average.

**Request:**

```bash
GET /numbers/e/
```
