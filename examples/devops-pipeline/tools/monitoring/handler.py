"""
Monitoring tool handler.

Queries production health, alerts, and metrics.
The runtime loads tool.yaml for schema validation and calls this at execution time.
"""

import httpx
from zerohuman_runtime import ToolContext


async def handle(ctx: ToolContext, operation: str, payload: dict | None = None) -> dict:
    """Execute a monitoring operation.

    Args:
        ctx: Runtime context providing auth, policy checks, and artifact emission.
        operation: One of the operations declared in tool.yaml interface.
        payload: Operation-specific parameters.

    Returns:
        dict with ok, result, and optional error fields matching output_schema.
    """
    base_url = ctx.get_config("MONITORING_API_URL")
    headers = {"X-Monitor-Key": ctx.get_secret("MONITORING_API_KEY")}

    async with httpx.AsyncClient(base_url=base_url, headers=headers) as client:
        if operation == "check_health":
            service = payload.get("service", "all")
            resp = await client.get(f"/health/{service}")
            return {"ok": resp.is_success, "result": resp.json()}

        elif operation == "get_alerts":
            time_range = payload.get("time_range", "1h")
            severity = payload.get("severity", "all")
            resp = await client.get("/alerts", params={"range": time_range, "severity": severity})
            return {"ok": resp.is_success, "result": resp.json()}

        elif operation == "get_metrics":
            service = payload.get("service")
            metric = payload.get("metric")
            resp = await client.get(f"/metrics/{service}/{metric}", params=payload.get("params", {}))
            return {"ok": resp.is_success, "result": resp.json()}

        elif operation == "acknowledge_alert":
            alert_id = payload.get("alert_id")
            resp = await client.post(f"/alerts/{alert_id}/ack", json={"note": payload.get("note", "")})
            return {"ok": resp.is_success, "result": resp.json()}

        else:
            return {"ok": False, "error": f"Unknown operation: {operation}"}
