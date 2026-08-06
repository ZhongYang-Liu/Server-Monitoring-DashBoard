import os
import time
import psutil
import alert
import pandas as pd
from datetime import datetime
from line_bot import send_line

cpu_warning_time = None
memory_warning_time = None
disk_warning_time = None

def start():

    print("Server Monitor Start")
    print("Press Ctrl + C to stop")


    global cpu_warning_time 
    global memory_warning_time 
    global disk_warning_time 

    file = "monitor.csv"
    if not os.path.exists(file):
        df = pd.DataFrame(
            columns=[
                "Time",
                "CPU",
                "Memory",
                "Disk"
            ]
        )
        df.to_csv(
            file,
            index=False
        )
    try:
        while True:

            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            result = {
                "Time": datetime.now(),
                "CPU": cpu,
                "Memory": memory,
                "Disk": disk
            }
            df = pd.DataFrame([result])
            df.to_csv(
                file,
                mode="a",
                index=False,
                header=False
            )
            message = ""
            if cpu > 80:

                if cpu_warning_time is None:
                    cpu_warning_time = time.time()
                elif time.time() - cpu_warning_time > 10:
                    message += (
                        "⚠ CPU Usage High\n"
                        f"CPU: {cpu}%\n\n"
                    )
                    send_line(message)
                    cpu_warning_time = None
            else:
                cpu_warning_time = None
            if memory > 80:
                if memory_warning_time is None:
                    memory_warning_time = time.time()
                elif time.time() - memory_warning_time > 10:
                    message += (
                        "⚠ Memory Usage High\n"
                        f"Memory: {memory}%\n\n"
                    )
                    send_line(message)
                    memory_warning_time = None
            else:
                memory_warning_time = None
            if disk > 80:
                if disk_warning_time is None:
                    disk_warning_time = time.time()
                elif time.time() - disk_warning_time > 10:
                    message += (
                        "⚠ Disk Usage High\n"
                        f"Disk: {disk}%\n\n"
                    )
                    send_line(message)
                    disk_warning_time = None
            else:
                disk_warning_time = None
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nServer Monitor stopped")