# port-scan
## Port Scanner API
A simple Flask-based REST API that scans a given IP or domain for open ports between a defined range. This project is ideal for learning cybersecurity, Python networking, and API deployment with Docker.

## Features
Scan open ports on a target host (IP/domain)

Configurable port range (default: 1–1024)

Built using Flask

Dockerized for easy deployment

Returns a list of open ports in JSON format

## Requirements
Docker (recommended)

OR Python 3.10+ with pip install -r requirements.txt

## Run Locally with Docker

### Build the image
docker build -t port-scanner-api .

### Run the container
docker run -p 5000:5000 port-scanner-api