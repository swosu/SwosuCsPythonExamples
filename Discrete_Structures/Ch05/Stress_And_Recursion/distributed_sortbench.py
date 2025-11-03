import os, paramiko, pandas as pd
from datetime import datetime
import getpass

# 🔧 configuration
MACHINES = {
    "local": {"host": "localhost"},
    "ken":   {"host": "156.110.41.141", "user": "jevert"},
    "brandy":{"host": "10.2.0.18", "user": "jevert"},
}

REMOTE_PATH = "~/git/SwosuCsPythonExamples/Discrete_Structures/Ch05/Stress_And_Recursion"
RESULT_FILE = "results.csv"
FINAL_MERGE = "results_all.csv"


def connect_with_key(ssh, host, user, keyfile):
    try:
        ssh.connect(host, username=user, key_filename=keyfile)
    except paramiko.ssh_exception.PasswordRequiredException:
        pw = getpass.getpass(f"🔐 Enter passphrase for {keyfile}: ")
        ssh.connect(host, username=user, key_filename=keyfile, passphrase=pw)


def run_remote_bench(name, conf):
    """Run benchmark remotely and copy back results."""
    if conf["host"] == "localhost":
        print(f"⚙️ Running locally on {name}...")        
        local_path = os.path.dirname(os.path.abspath(__file__))
        os.system(f'python "{os.path.join(local_path, "main.py")}"')
        os.rename(RESULT_FILE, f"{name}_{RESULT_FILE}")
        return

    host, user = conf["host"], conf["user"]
    print(f"🚀 Running on {name} ({host})...")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, key_filename=os.path.expanduser("~/.ssh/id_ed25519"))



    # Run the experiment remotely
    cmd = f"cd {REMOTE_PATH} && source venv/bin/activate && python3 main.py"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode(), end="")
    err = stderr.read().decode()
    if err:
        print(f"⚠️ {name} stderr:\n{err}")

    # SFTP to copy results.csv
    sftp = ssh.open_sftp()
    local_filename = f"{name}_{RESULT_FILE}"
    sftp.get(os.path.join(REMOTE_PATH, RESULT_FILE), local_filename)
    sftp.close()
    ssh.close()
    print(f"✅ Collected {local_filename}")


def merge_results():
    """Combine all CSVs into one master file with a 'machine' column."""
    frames = []
    for name in MACHINES:
        fname = f"{name}_{RESULT_FILE}"
        if os.path.exists(fname):
            df = pd.read_csv(fname)
            df["machine"] = name
            frames.append(df)
    merged = pd.concat(frames)
    merged["timestamp"] = datetime.now().isoformat()
    merged.to_csv(FINAL_MERGE, index=False)
    print(f"\n🧾 Merged results saved as {FINAL_MERGE}")


if __name__ == "__main__":
    for name, conf in MACHINES.items():
        run_remote_bench(name, conf)

    merge_results()
