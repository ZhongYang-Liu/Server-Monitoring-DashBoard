import os
import csv
import time
import threading
from datetime import datetime

import psutil
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

CSV_FILE = "monitor.csv"
UPDATE_INTERVAL = 5      # 每幾秒抓一次系統資訊 (秒)
MAX_ROWS = 200           # CSV 最多保留幾筆資料，避免無限增長

csv_lock = threading.Lock()


def init_csv():
    """如果 CSV 不存在，先建立含表頭的檔案"""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Time", "CPU", "Memory", "Disk"])


def trim_csv():
    """只保留最後 MAX_ROWS 筆資料，避免檔案無限變大"""
    df = pd.read_csv(CSV_FILE)
    if len(df) > MAX_ROWS:
        df.tail(MAX_ROWS).to_csv(CSV_FILE, index=False)


def collect_loop():
    """背景執行緒：每隔 UPDATE_INTERVAL 秒抓一次系統資訊並寫入 CSV"""
    init_csv()

    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with csv_lock:
            with open(CSV_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([now, cpu, memory, disk])
            trim_csv()

        time.sleep(UPDATE_INTERVAL - 1)  


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():
    with csv_lock:
        df = pd.read_csv(CSV_FILE)

    if df.empty:
        return jsonify({})

    latest = df.iloc[-1]
    history = df.tail(20)

    return jsonify({
        "CPU": latest["CPU"],
        "Memory": latest["Memory"],
        "Disk": latest["Disk"],

        "TimeHistory": history["Time"].tolist(),
        "CPUHistory": history["CPU"].tolist(),
        "MemoryHistory": history["Memory"].tolist(),
        "DiskHistory": history["Disk"].tolist()
    })


if __name__ == "__main__":
    # 背景執行緒負責持續收集資料寫入 CSV
    collector_thread = threading.Thread(target=collect_loop, daemon=True)
    collector_thread.start()

    app.run(debug=True, use_reloader=False)