import sys
import pytest

def pytest_sessionstart(session):
    required = (3, 12)
    if sys.version_info < required:
        pytest.exit(f"Python {required[0]}.{required[1]}+ required, found {sys.version_info.major}.{sys.version_info.minor}")

