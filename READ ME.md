## 📊 Vogue Monitor

Vogue Monitor is a small SRE project designed to monitor the availability and performance of Vogue.com. It uses a minimal Flask app to expose Prometheus metrics, integrates with Kubernetes, and visualizes results in Grafana.

## 🧠 Project Title
Website Availability and Performance Monitoring for Vogue.com

## 🎯 Project Goal
To design and implement a monitoring system that tracks the availability, latency, and reliability of Vogue.com, with alerting and dashboards that reflect real-world SRE observability practices.

## 🛠️ Tools & Stack
Purpose	Tool
Metric collection	Prometheus
Uptime & latency probe	Prometheus Blackbox Exporter
Visualization	Grafana
Alerting	Alertmanager (Slack/email notifications)
Optional scripting	Python for custom probes (SSL/DNS checks)

## 📂 Repository Structure
    app/main.py → Flask app exposing /metrics
    Dockerfile → Container build
    k8s/ → Kubernetes manifests (Deployment + Service)
    prometheus/ → prometheus.yml + alert rules
    alertmanager/ → alertmanager.yml
    grafana/ → Dashboard JSON to import

## 📊 Grafana Dashboard

    Import grafana/dashboard_vogue.json into Grafana.
    Grafana UI: http://192.168.49.2:30400/

Panels include:
    Uptime %
    Average latency (ms)
    Response code distribution
    SSL expiry countdown


## ✅ Wrap-Up

This project demonstrates how to apply SRE principles to monitor a real-world, high-traffic website like Vogue.com. By combining tools like Prometheus, Blackbox Exporter, Grafana, and Alertmanager, you’ve built a complete observability pipeline that tracks:

    Availability (uptime checks)
    Performance (latency, response codes)
    Reliability (alerting and dashboards)
    Security (SSL expiry monitoring)

Whether you're showcasing this for a course, portfolio, or job interview, it reflects practical skills in:

    Kubernetes deployment
    Monitoring and alerting setup
    Dashboard design
    Real-world SRE metrics
    
## 🧠 Final Thought 
Monitoring isn’t just about uptime — it’s about understanding how systems behave in production. This project gives you a solid foundation in building resilient, observable infrastructure.
