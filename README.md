# 🎬 MovieVerse: Distributed Streaming Platform Clone

**MovieVerse** is a microservices-based movie recommendation system designed for scalability, regional content filtering, and observability. Built using **Flask**, **MySQL**, **Docker**, **Kubernetes**, **Kong API Gateway**, and **Prometheus**, it serves personalized movie content tailored to region-specific availability.

---

## 🧠 Project Summary

MovieVerse allows users to fetch movie data specific to their region — **India**, **USA**, or **UK**. It integrates modern DevOps practices with a containerized architecture, enabling modular development, monitoring, and automated scaling.

---

## 🧱 Tech Stack

| Component         | Technology       |
|------------------|------------------|
| Backend Service  | Flask            |
| Database         | MySQL            |
| API Gateway      | Kong             |
| Containerization | Docker           |
| Orchestration    | Kubernetes       |
| Monitoring       | Prometheus       |

---

## 📌 Features

- 🎯 **Region-based Filtering**: Routes movie data based on geographical regions.
- 🔒 **API Gateway Security**: Uses Kong to manage authentication, rate limiting, and request routing.
- 📊 **Monitoring with Prometheus**: Tracks service uptime, request rates, and system performance.
- 🚀 **Scalable Deployment**: Kubernetes manages Dockerized services for high availability and load balancing.

---

## 📁 Repository Structure

├── promtherservice.yaml # Prometheus monitoring service configuration
├── docker-compose.yaml # Docker setup for local dev (if added)
├── kubernetes/ # Kubernetes deployment files
├── flask-service/ # Flask-based microservices
├── sql/ # MySQL initialization scripts
└── README.md # You're here!


---

## 🌍 Region-Based Services

Kong routes incoming traffic to the following region-specific services:

- 🇮🇳 **India Service** → `localhost:8050`
- 🇺🇸 **USA Service**   → `localhost:8051`
- 🇬🇧 **UK Service**    → `localhost:8052`

Each of these services is independently deployed via Kubernetes and communicates with the central MySQL database.

---

## 🛡️ Kong API Gateway

Kong is used to:

- Route traffic to appropriate microservices
- Apply rate limiting and OAuth2 authentication
- Enable observability plugins for logging and monitoring

---

## 📈 Monitoring with Prometheus

Prometheus collects metrics from all services and provides insights via:

- Service health graphs
- Request counts and response rates
- Real-time visual dashboards

Refer to `promtherservice.yaml` for Prometheus setup.

---

## 🚀 Getting Started

1. **Clone the repository**:

    ```bash
    git clone https://github.com/keya714/DistributedStreamingPlatformClone.git
    cd DistributedStreamingPlatformClone
    ```

2. **Deploy with Kubernetes**:

    ```bash
    kubectl apply -f kubernetes/
    ```

3. **Access endpoints**:

    - India: `http://localhost:8050`
    - USA: `http://localhost:8051`
    - UK: `http://localhost:8052`

4. **Monitor with Prometheus**:

    - Open: `http://localhost:9090`

---
