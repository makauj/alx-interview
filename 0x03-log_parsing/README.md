# Log Parsing

## Log Parsing Basics

---

### What is Log Parsing?

**Log parsing** means **reading and extracting meaningful information** from log files. Logs are text files that record events, errors, or actions in a system, such as web requests, user logins, or system errors.

Here's a simple log line (from a web server):

```
127.0.0.1 - [2025-05-08 12:34:56.789] "GET /index.html HTTP/1.1" 200 1024
```

This line contains:

* IP address: `127.0.0.1`
* Date/time: `[2025-05-08 12:34:56.789]`
* HTTP method and path: `"GET /index.html HTTP/1.1"`
* Status code: `200`
* File size: `1024`

---

### How to Parse Logs with Python

#### Step 1: Read the File

```python
with open("log.txt", "r") as f:
    for line in f:
        print(line.strip())
```

This opens a log file and reads it line by line.

#### Step 2: Use `split()` or Regex to Extract Data

**Simple Example (no regex):**

```python
line = '127.0.0.1 - [2025-05-08 12:34:56.789] "GET /index.html HTTP/1.1" 200 1024'
parts = line.split()
ip = parts[0]
status = parts[-2]
size = parts[-1]
print(ip, status, size)
```

**Advanced Example (with regex):**

```python
import re

log_pattern = re.compile(
    r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET (.*?) HTTP/1\.1" (\d{3}) (\d+)$'
)

match = log_pattern.match(line)
if match:
    ip, date, path, status, size = match.groups()
    print(ip, date, path, status, size)
```

---

### Use Case: Count Requests by Status Code

```python
from collections import defaultdict

status_counts = defaultdict(int)

with open("log.txt") as f:
    for line in f:
        match = log_pattern.match(line)
        if match:
            status = match.group(4)
            status_counts[status] += 1

for code, count in status_counts.items():
    print(f"{code}: {count}")
```

---

### Summary:

* **Log parsing** lets you extract useful info from system logs.
* You can use basic string methods or `re` (regular expressions) for pattern matching.
* Python's `collections` module is great for summarizing data (e.g., counting status codes).
