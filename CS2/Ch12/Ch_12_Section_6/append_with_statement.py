from datetime import datetime

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")

log_event("System started.")
log_event("All good things come to those who code.")
