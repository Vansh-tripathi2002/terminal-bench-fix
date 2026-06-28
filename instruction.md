# Log Report Task

You are given an Apache-style access log located at:

/app/access.log

Your task is to analyze the log and generate a JSON report at:

/app/report.json

The JSON file must contain exactly these fields:

- total_requests: total number of log lines in the file
- unique_ips: number of distinct client IP addresses
- top_path: the most frequently requested URL path

The output must be valid JSON and written exactly to `/app/report.json`.
