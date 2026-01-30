# Deployment Guide for Coolify

This guide explains how to deploy the Aki Forwarder Backend on Coolify.

## Prerequisites

- A Coolify instance
- A Telegram bot token (get one from [@BotFather](https://t.me/botfather))

## Deployment Steps

### 1. Create a New Service in Coolify

1. Go to your Coolify dashboard
2. Create a new service
3. Select "Docker" as the deployment type
4. Connect your Git repository

### 2. Configure Environment Variables

In Coolify, set the following environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `TOKEN` | Your Telegram bot token | `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz` |
| `PORT` | Port the app listens on | `8000` (default) |
| `HOST` | Host to bind to | `0.0.0.0` (default) |
| `DEBUG` | Debug mode | `False` (production) |

**Important:** The `TOKEN` variable is required for the bot to function.

### 3. Port Configuration

- The application listens on port `8000` by default
- Coolify will automatically map this to your domain
- If you need to change the port, set the `PORT` environment variable

### 4. Build Configuration

Coolify will automatically:
- Detect the `Dockerfile` in the repository root
- Build the Docker image
- Deploy the container

### 5. Health Check

After deployment, verify the service is running by accessing:
```
https://your-domain.com/
```

You should see:
```json
{"message": "Aki-Forwarder Backend"}
```

## Environment Variable Loading

The application uses `python-dotenv` to load environment variables. In Docker/Coolify:

1. Environment variables set in Coolify are automatically available to the container
2. The `.env` file is **not** included in the Docker image (see `.dockerignore`)
3. All configuration is loaded from environment variables at runtime

## CORS Configuration

The application is configured to allow requests from:
- `http://localhost:5173` (development)
- `https://aki.rian.moe` (production frontend)

To add additional origins, modify the `origins` list in `main/__main__.py`.

## Troubleshooting

### Bot not responding
- Verify the `TOKEN` environment variable is set correctly
- Check the Coolify logs for any errors

### Connection issues
- Ensure the `HOST` is set to `0.0.0.0` (not `localhost`)
- Verify the port mapping in Coolify

### File upload issues
- The application accepts files up to 8 MB
- Ensure your reverse proxy (if any) allows this file size

## Architecture

- **FastAPI** serves HTTP endpoints and WebSocket connections
- **Aiogram** runs the Telegram bot in polling mode
- Both run concurrently in the same container using asyncio
