import app
import monitor
import threading
import pandas as pd

monitor_thread = threading.Thread(
    target= monitor.start
)

monitor_thread.daemon = True

monitor_thread.start()

app.app.run(
    host = "0.0.0.0",
    port = 5000
)

