# Simple Log Parser

A Python script designed to analyze server log files, summarize traffic, and detect suspicious behavioral patterns using automated regex extraction.

## Features
- **Regex Extraction:** Pulls IP addresses and HTTP status codes from raw logs.
- **Request Counting:** Aggregates total requests per unique IP.
- **Security Alerting:** Flags IPs with more than 3 suspicious responses (401, 403, or 404).

## Usage
The script requires the path to a log file and supports optional thresholding and data export.

**1. Basic Run (Default threshold = 3):**
```bash
python parser.py server.log
```

**2. Custom Threshold (e.g., alert after 10 hits):**
```bash
python parser.py server.log 10
```

**3. Export Results to JSON:**
To save the analysis for use in other tools, add the `--export` flag.
```bash
python parser.py server.log --export
```