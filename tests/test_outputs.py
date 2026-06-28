import json
from pathlib import Path


def test_report_exists():
    """1. The agent produced a report file at /app/report.json."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_total_requests():
    """2. total_requests is the correct integer count of all log lines."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """3. unique_ips is the correct count of distinct client IP addresses."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """4. top_path is the URL path with the most requests."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )