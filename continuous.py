import time
from datetime import datetime

def main():
    print("Script started. Running continuously...")
    print(f"PID: {os.getpid()}")
    
    counter = 0
    while True:
        counter += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write to a log file so we can monitor it
        with open("./script.log", "a") as f:
            f.write(f"[{timestamp}] Iteration {counter}\n")
        
        # Sleep for 10 seconds between iterations
        time.sleep(10)

if __name__ == "__main__":
    import os
    main()