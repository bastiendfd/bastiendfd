import subprocess
import sys
from pathlib import Path


def test_profile_validator_accepts_current_readme() -> None:
    root = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, "scripts/validate_profile.py"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    assert "Profile validation passed" in completed.stdout
