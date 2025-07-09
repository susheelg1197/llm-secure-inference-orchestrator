# LLM Secure Inference Orchestrator 🚀

A production-ready, secure, multi-tenant LLM inference serving infrastructure built for scale and observability.

---

## 🧠 Architecture Overview

```
Client
  |
  v
[Envoy Gateway] ---> [Auth + Rate Limiting]
  |
  v
[Inference Server Pods (FastAPI)]
  |
  v
[Model Backends - Mistral, Falcon, etc.]
  |
  v
[Prometheus, Loki, CloudWatch for Observability]
```

---

## 🔐 Features

- **Multi-tenant support** via API key validation
- **Envoy Gateway** to route and filter traffic
- **FastAPI-based inference layer**
- **Prometheus/Grafana integration** for request metrics
- **Kubernetes-native deployments** with auto-scaling support

---

## 🛠️ Stack

- **API Layer**: FastAPI, Python
- **Gateway**: Envoy
- **Platform**: Kubernetes, Helm, Terraform (infra optional)
- **Observability**: Prometheus, Grafana, FluentBit (optional)

---

## 🚀 Deployment

### 1. Start FastAPI App (locally for test)
```bash
uvicorn inference-server.main:app --host 0.0.0.0 --port 8000
```

### 2. Deploy to Kubernetes
```bash
kubectl apply -f k8s/manifests/
```

### 3. Run Envoy Proxy
```bash
docker run -v $(pwd)/auth-gateway/envoy-config.yaml:/etc/envoy/envoy.yaml   -p 8080:8080 envoyproxy/envoy:v1.18.3
```

---

## 📈 Example Request

```bash
curl -X POST http://localhost:8080/infer \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "def add(a, b): return a + b",
    "tenant_id": "client_123",
    "api_key": "secure_dummy_key"
  }'
```

---

## 📌 Future Enhancements

- Add token metering for billing
- Integrate real LLM inference with HuggingFace or vLLM
- Add per-tenant Prometheus metrics

---