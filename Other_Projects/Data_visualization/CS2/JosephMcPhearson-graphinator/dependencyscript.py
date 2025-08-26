import subprocess
import sys

def install_dependencies():
    required_packages = ['pandas', 'matplotlib']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package} has been successfully installed.")

if __name__ == "__main__":
    print("Checking and installing required dependencies...")
    install_dependencies()
    print("\nAll dependencies are ready! You can now run your Graphinator 3000 program.")