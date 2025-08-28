# Presidents/check_env.py
import sys, os
REQUIRED_MAJOR, REQUIRED_MINOR = 3, 11

def main():
    major, minor = sys.version_info[:2]
    if (major, minor) < (REQUIRED_MAJOR, REQUIRED_MINOR):
        print(f"❌ Your Python is {major}.{minor}. This project requires {REQUIRED_MAJOR}.{REQUIRED_MINOR}+.")
        here = os.path.dirname(__file__) or "."
        print("Run the bootstrap script:")
        print(f"   cd {here} && ./setup.sh")
        sys.exit(1)
    else:
        print(f"✅ Python {major}.{minor} looks good!")

if __name__ == "__main__":
    main()

