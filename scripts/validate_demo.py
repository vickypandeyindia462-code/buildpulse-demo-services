"""Validate that service ownership, runbooks, KB and scenarios remain connected."""

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    catalog = yaml.safe_load((ROOT / "service-catalog.yaml").read_text(encoding="utf-8"))
    service_ids = {service["id"] for service in catalog["services"]}
    assert len(service_ids) == 4
    for service in catalog["services"]:
        assert (ROOT / service["path"]).is_dir()
        for reference in service["runbooks"] + service["kb"]:
            assert (ROOT / reference).is_file(), reference
    scenarios = json.loads((ROOT / "demo-data/failure-scenarios.json").read_text(encoding="utf-8"))
    assert scenarios
    assert {item["service"] for item in scenarios}.issubset(service_ids)
    print(f"validated {len(service_ids)} services and {len(scenarios)} failure scenarios")


if __name__ == "__main__":
    main()
