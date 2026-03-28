"""
Deployment tool handler.

Manages release creation, environment promotion, and rollbacks.
The runtime loads tool.yaml for schema/approval gates and calls this at execution time.
"""

import httpx
from zerohuman_runtime import ToolContext


async def handle(ctx: ToolContext, operation: str, payload: dict | None = None) -> dict:
    """Execute a deployment operation.

    Args:
        ctx: Runtime context providing auth, policy checks, and artifact emission.
        operation: One of the operations declared in tool.yaml interface.
        payload: Operation-specific parameters.

    Returns:
        dict with ok, result, and optional error fields matching output_schema.
    """
    base_url = ctx.get_config("DEPLOY_API_URL")
    headers = {"X-Deploy-Key": ctx.get_secret("DEPLOY_API_KEY")}

    async with httpx.AsyncClient(base_url=base_url, headers=headers) as client:
        if operation == "create_release":
            version = payload.get("version")
            resp = await client.post("/releases", json={"version": version, "artifacts": payload.get("artifacts", [])})
            return {"ok": resp.is_success, "result": resp.json()}

        elif operation == "promote_to_staging":
            version = payload.get("version")
            resp = await client.post(f"/releases/{version}/promote", json={"environment": "staging"})
            return {"ok": resp.is_success, "result": resp.json()}

        elif operation == "promote_to_production":
            version = payload.get("version")
            resp = await client.post(f"/releases/{version}/promote", json={"environment": "production"})
            return {"ok": resp.is_success, "result": resp.json()}

        elif operation == "rollback":
            environment = payload.get("environment", "production")
            target_version = payload.get("target_version")
            resp = await client.post(f"/environments/{environment}/rollback", json={"target_version": target_version})
            return {"ok": resp.is_success, "result": resp.json()}

        elif operation == "get_deploy_status":
            environment = payload.get("environment", "production")
            resp = await client.get(f"/environments/{environment}/status")
            return {"ok": resp.is_success, "result": resp.json()}

        else:
            return {"ok": False, "error": f"Unknown operation: {operation}"}
