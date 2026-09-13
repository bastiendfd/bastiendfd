import subprocess
import sys
import unittest
from pathlib import Path


class ProfileValidatorTests(unittest.TestCase):
    def test_profile_validator_accepts_current_readme(self) -> None:
        root = Path(__file__).resolve().parents[1]
        completed = subprocess.run(
            [sys.executable, "scripts/validate_profile.py"],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("Profile validation passed", completed.stdout)


if __name__ == "__main__":
    unittest.main()
