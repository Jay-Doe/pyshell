import os
import subprocess
from pathlib import Path


PATHS: list[str] = os.environ.get("PATH", "").split(os.pathsep)

def find_exe(name: str)-> str:
    for p in PATHS:
        full = Path(p) / name
        if full.exists() and os.access(full, os.X_OK):
            return str(full)
    return ""
