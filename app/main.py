from flask import Flask, Response
import time
import requests
import ssl
import socket
from prometheus_client import CollectorRegistry, Gauge, Counter, generate_latest, CONTENT_TYPE_LATEST

TARGET_URL = "https://www.vogue.com"
HTTP_TIMEOUT = 5

app = Flask(__name__)
registry = CollectorRegistry()

probe_success = Gauge("vogue_probe_success", "1 if probe success else 0", registry=registry)
probe_duration_seconds = Gauge("vogue_probe_duration_seconds", "Probe duration in seconds", registry=registry)
probe_http_status = Gauge("vogue_probe_http_status", "HTTP status code", registry=registry)
ssl_cert_expiry = Gauge("vogue_ssl_cert_expiry_timestamp", "SSL cert expiry timestamp", registry=registry)


def check_ssl_expiry(hostname):
    ctx = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with ctx.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            return ssl.cert_time_to_seconds(cert["notAfter"])


@app.route('/probe')
def probe():
    start = time.time()
    status = 0

    try:
        r = requests.get(TARGET_URL, timeout=HTTP_TIMEOUT)
        duration = time.time() - start
        status = r.status_code

        probe_success.set(1)
        probe_duration_seconds.set(duration)
        probe_http_status.set(status)

    except Exception as e:
        duration = time.time() - start

        probe_success.set(0)
        probe_duration_seconds.set(duration)
        probe_http_status.set(0)
        app.logger.debug(f"Probe error: {e}")

    
    hostname = TARGET_URL.replace("https://", "").split("/")[0]
    try:
        expiry_ts = check_ssl_expiry(hostname)
        ssl_cert_expiry.set(expiry_ts)
    except:
        ssl_cert_expiry.set(0)

    return ("OK\n", 200)



@app.route('/metrics')
def metrics():
    probe()
    data = generate_latest(registry)
    return Response(data, mimetype=CONTENT_TYPE_LATEST)



@app.route('/')
def index():
    return ("Vogue monitor running. Visit /metrics for Prometheus metrics.\n", 200)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
