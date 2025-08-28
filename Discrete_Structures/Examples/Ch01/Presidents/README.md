# Presidents (Text-Based Card Game)

## Quick Start
1. **Run setup once (creates venv, installs deps, sanity-checks):**
   ```bash
   ./setup.sh
   ```
2. Run tests (uses the project’s Python 3.11 automatically):
   ```bash
   ./runtests.sh -q
   ```
3. Run the CLI demo:
   ```bash
   ./.venv/bin/python cli_demo.py
   ```
If pytest ever complains about Python 3.9 vs 3.11, use:
   ```bash
   ./runtests.sh -q
   ```
