"""
GitHub CI tool handler.

This module implements the runtime-callable handler for the github_ci tool.
The runtime loads tool.yaml for schema validation and progressive disclosure,
then calls this handler at execution time.
"""

import httpx
from zerohuman_runtime import ToolContext


async def handle(ctx: ToolContext, operation: str, repo: str, payload: dict | None = None) -> dict:
    """Execute a GitHub CI operation.

    Args:
        ctx: Runtime context providing auth, policy checks, and artifact emission.
        operation: One of the operations declared in tool.yaml interface.
        repo: Repository in owner/repo format.
        payload: Operation-specific parameters.

    Returns:
        dict with ok, result, and optional error fields matching output_schema.
    """
    base_url = "https://api.github.com"
    headers = {"Authorization": f"Bearer {ctx.get_secret('GITHUB_TOKEN')}"}

    async with httpx.AsyncClient(base_url=base_url, headers=headers) as client:
        if operation == "trigger_workflow":
            workflow_id = payload.get("workflow_id", "ci.yml")
            ref = payload.get("ref", "main")
            resp = await client.post(
                f"/repos/{repo}/actions/workflows/{workflow_id}/dispatches",
                json={"ref": ref, "inputs": payload.get("inputs", {})},
            )
            return {"ok": resp.status_code == 204, "result": {"dispatched": True}}

        elif operation == "get_run_status":
            run_id = payload.get("run_id")
            resp = await client.get(f"/repos/{repo}/actions/runs/{run_id}")
            data = resp.json()
            return {"ok": resp.is_success, "result": {"status": data.get("status"), "conclusion": data.get("conclusion")}}

        elif operation == "get_run_logs":
            run_id = payload.get("run_id")
            resp = await client.get(f"/repos/{repo}/actions/runs/{run_id}/logs")
            return {"ok": resp.is_success, "result": {"logs_url": str(resp.url)}}

        elif operation == "list_check_runs":
            ref = payload.get("ref", "main")
            resp = await client.get(f"/repos/{repo}/commits/{ref}/check-runs")
            data = resp.json()
            return {"ok": resp.is_success, "result": {"check_runs": data.get("check_runs", [])}}

        elif operation == "create_check_run":
            resp = await client.post(
                f"/repos/{repo}/check-runs",
                json=payload,
            )
            return {"ok": resp.is_success, "result": resp.json()}

        else:
            return {"ok": False, "error": f"Unknown operation: {operation}"}
