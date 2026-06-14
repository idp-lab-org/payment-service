# 🐍 payment-service

Backend service for PaymentOS — a sample Internal Developer Platform demo application.

## What is this?

This service was created automatically via the **IDP Lab Backstage golden path template**. A developer filled a form in Backstage and this entire repo — including CI pipeline and Kubernetes deployment — was generated automatically.

## Features

- **`POST /api/encrypt`** — accepts a message, returns it encrypted with metadata
- Returns pod name, namespace, processing time, and timestamp
- Proves real backend processing inside Kubernetes

## Tech Stack

- **Runtime:** Python + Flask
- **Deployed to:** Kubernetes (`dev` namespace)
- **CI:** GitHub Actions → Docker Hub
- **CD:** ArgoCD (GitOps)

## API

### `POST /api/encrypt`

```json
// Request
{ "message": "Hello from the demo!" }

// Response
{
  "success": true,
  "encrypted": "b2xsZUg=...",
  "message_id": "MSG-4821",
  "key_id": "KEY-DB99B2DC",
  "algorithm": "AES-256-CBC (mock)",
  "processed_by": "payment-service-7dbf6c4d77-2dh6s",
  "namespace": "dev",
  "processing_time_ms": 8.1,
  "timestamp": "2026-06-14 03:24:28 UTC"
}
```

### `GET /health`

```json
{ "status": "healthy", "pod": "payment-service-xxx" }
```

## Running locally

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:8080
```

## CI/CD

Every push to `main`:
1. GitHub Actions builds Docker image
2. Pushes to `sky2108/payment-service:<sha>` on Docker Hub
3. Updates `apps/payment-service/deployment.yaml` in idp-lab-gitops
4. ArgoCD detects change and redeploys automatically

Part of [idp-lab-org](https://github.com/idp-lab-org) — Mini IDP portfolio project.
