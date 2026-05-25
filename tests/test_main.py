# Unit tests

from first_app.main import run


def test_run_returns_expected_string():
    assert run() == "Hello from first_app!"
