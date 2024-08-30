"""
GitHub-related utils.
"""

from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import requests


def download_and_extract(url: str, output_path: Path) -> Path:
    """
    Download and extract zip file with stubs from GitHub URL.
    """
    response = requests.get(url, timeout=60)
    zipfile = ZipFile(BytesIO(response.content))

    if not response.ok:
        raise RuntimeError(f"Failed to download URL {url}: {response.status_code} {response.text}")

    project_roots = [
        Path(i).parent.as_posix() for i in zipfile.namelist() if Path(i).name == "py.typed"
    ]
    if len(project_roots) != 1:
        raise ValueError(f"Failed to detect project root: {project_roots}")

    project_root = project_roots[0]

    for member in zipfile.namelist():
        if not member.startswith(project_root):
            continue
        zipfile.extract(member, output_path)

    return output_path / project_root
