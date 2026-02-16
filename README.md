# Simple Log Parser

A Python script that analyzes `server.log` files to summarize traffic and detect suspicious activity.

## Features
- **Regex Extraction:** Pulls IP addresses and HTTP status codes from raw logs.
- **Request Counting:** Aggregates total requests per unique IP.
- **Security Alerting:** Flags IPs with more than 3 suspicious responses (401, 403, or 404).

## Usage
1. Place `server.log` in the project directory.
2. Run the script:
   ```bash
   python parser.py