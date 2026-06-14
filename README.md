# 🐍 payment-service

Python Flask backend service for PaymentOS — created automatically via the IDP Lab Backstage golden path template.

## What it does

Provides an encryption API that the `payment-ui` frontend calls. Returns encrypted text along with Kubernetes metadata proving the request was processed by a real pod inside the cluster.

## How it was created

A developer opened Backstage, clicked **Create → New Service**, selected:
- Language: **Python**
- Starter: **Full Sample App**
- Namespace: **dev**
- Team: **team-backend**

Backstage automatically created this repo, CI pipeline, and deployment — zero manual Kubernetes work.

## API

### `POST /api/encrypt`

```bash
curl -X POST http://localhost:8082/api/encrypt \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from the demo!"}'
```

Response:
```json
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

## Tech Stack

- **Runtime:** Python 3.11 + Flask + flask-cors
- **Deployed to:** Kubernetes `dev` namespace
- **CI:** GitHub Actions → `sky2108/payment-service` on Docker Hub
- **CD:** ArgoCD (GitOps via idp-lab-gitops)

## Running Locally

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:8080
```

## CI/CD Flow

Every merge to `main`:
1. GitHub Actions builds Docker image
2. Pushes `sky2108/payment-service:<sha>` to Docker Hub
3. Updates `apps/payment-service/deployment.yaml` in idp-lab-gitops
4. ArgoCD detects change → redeploys automatically

Part of [idp-lab-org](https://github.com/idp-lab-org) — built by [@sky2194](https://github.com/sky2194)
