import importlib
from pathlib import Path


def load_all_tasks() -> list[dict]:
    tasks = []
    pkg_dir = Path(__file__).parent
    for path in sorted(pkg_dir.glob("*.py")):
        if path.name == "__init__.py":
            continue
        mod = importlib.import_module(f"a360_packages.{path.stem}")
        for act in mod.ACTIONS:
            tasks.append({
                "package": mod.PACKAGE_NAME,
                "action": act["action"],
                "data_item_name": act["data_item_name"],
                "description": act.get("description", ""),
            })
    return tasks