# Simple Log Parser

A Python script designed to analyze server log files, summarize traffic, and detect suspicious behavioral patterns using automated regex extraction.

## Features
- **Regex Extraction:** Pulls IP addresses and HTTP status codes from raw logs.
- **Request Counting:** Aggregates total requests per unique IP.
- **Security Alerting:** Flags IPs with more than 3 suspicious responses (401, 403, or 404).

## Usage
The script requires the path to a log file as the first argument and accepts an optional second argument to set a custom alert threshold.

**Basic Run (Default threshold = 3):**
```bash
python parser.py server.log
```

**Custom Threshold (e.g., alert after 10 suspicious hits):**
```bash
python parser.py server.log 10
```