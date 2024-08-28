import psutil
import time

# Define the CPU usage threshold percentage
THRESHOLD = 80.0

def monitor_cpu(threshold):
    # Initial CPU usage measurement
    cpu_usage = psutil.cpu_percent(interval=None)
    
    while True:
        # Get the current CPU usage as a percentage with a 1-second interval
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Check if the CPU usage exceeds the specified threshold
        if cpu_usage > threshold:
            # Print an alert message if the threshold is exceeded
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        
        # Pause briefly before the next check to avoid overwhelming the CPU
        time.sleep(1)

if __name__ == "__main__":
    # Start monitoring the CPU usage with the specified threshold
    monitor_cpu(THRESHOLD)

import psutil
import time

# Define the CPU usage threshold percentage
THRESHOLD = 80.0

def monitor_cpu(threshold):
    # Initial CPU usage measurement
    cpu_usage = psutil.cpu_percent(interval=None)
    
    while True:
        # Get the current CPU usage as a percentage with a 1-second interval
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Check if the CPU usage exceeds the specified threshold
        if cpu_usage > threshold:
            # Print an alert message if the threshold is exceeded
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        
        # Pause briefly before the next check to avoid overwhelming the CPU
        time.sleep(1)

if __name__ == "__main__":
    # Start monitoring the CPU usage with the specified threshold
    monitor_cpu(THRESHOLD)
