# Web Shell Finder

Web Shell Finder is a Python tool for scanning multiple URLs to detect potential web shells. It uses threading to efficiently handle large lists of URLs and shell paths, enabling fast detection across multiple endpoints.

## Features
- Scans multiple URLs for potential web shells using a wordlist.
- Utilizes threading to perform HTTP requests in parallel, improving speed and efficiency.

## Requirements
- **Python 3.x**
- **Requests library**  
  You can install the `requests` library via pip:
  ```bash
  pip install requests

## Usage
  ```bash
  python3 checkshell.py
