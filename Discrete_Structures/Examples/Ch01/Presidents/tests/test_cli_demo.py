# tests/test_cli_demo.py
def test_cli_demo_imports():
    import cli_demo
    assert callable(cli_demo.run_cli_demo)

