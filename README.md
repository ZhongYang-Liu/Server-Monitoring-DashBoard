# 🖥 Server Monitoring Dashboard

A real-time server monitoring dashboard built with **Python**, **Flask**, and **Chart.js** for monitoring CPU, Memory, and Disk usage through an interactive web interface.

---

## 📸 Dashboard Preview

<img width="1753" height="907" alt="image" src="https://github.com/user-attachments/assets/7d3bfc54-b458-40dd-97b4-a631795fb529" />


```markdown
![Dashboard](screenshots/dashboard.png)
```

---

# 📌 Project Introduction

Server Monitoring Dashboard is a lightweight web-based monitoring system developed using **Python** and **Flask**.

The application continuously collects system resource information, including **CPU**, **Memory**, and **Disk** usage, then visualizes the data on a real-time dashboard using **Chart.js**.

This project was developed to practice backend development, RESTful API integration, and real-time data visualization while learning Python web development.

---

# ✨ Features

- 📊 Real-time CPU usage monitoring
- 💾 Real-time Memory usage monitoring
- 🗄️ Real-time Disk usage monitoring
- 📈 Dynamic charts powered by Chart.js
- 🔄 Automatic data refresh
- ⚠️ Warning notification when resource usage exceeds the threshold
- 🌐 Responsive web dashboard
- 📁 CSV data logging for monitoring records

---

# 🛠 Technologies

### Backend

- Python
- Flask
- psutil
- pandas

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

---

# 🏗️ System Architecture

```
+---------------------+
|     Web Browser     |
+----------+----------+
           |
           v
+---------------------+
|      Flask API      |
+----------+----------+
           |
           v
+---------------------+
|      psutil         |
+----------+----------+
           |
           v
+---------------------+
| CPU | Memory | Disk |
+---------------------+
```

---

# 📂 Project Structure

```
server-monitoring-dashboard/
│
├── main.py
├── monitor.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
    ├── css/
    │   └── style.css
    ├── js/
        └── dashboard.js

```

---

# 🚀 Installation

Clone this repository

```bash
git clone https://github.com/ZhongYang-Liu/Server-Monitoring-DashBoard.git
```

Move into the project directory

```bash
cd Server-Monitoring-DashBoard
```

Install required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 📖 Usage

The dashboard automatically updates system resource information every few seconds.

You can monitor:

- CPU Usage
- Memory Usage
- Disk Usage
- Resource Usage Trend
- Warning Notifications

---

# 💡 Skills Demonstrated

This project demonstrates the following technical skills:

- Python programming
- Flask web development
- RESTful API integration
- System resource monitoring using psutil
- Data visualization with Chart.js
- HTML / CSS / JavaScript integration
- Real-time dashboard development

---

# 🚀 Future Improvements

- User authentication
- Historical data analysis
- SQLite/MySQL database support
- Docker deployment
- Email alert notification
- Dark / Light mode switch


# 👨‍💻 Author

**Zhong Yang Liu**

Department of Computer Science and Information Engineering

National Formosa University

GitHub:
https://github.com/ZhongYang-Liu

# 🖥 伺服器監控儀表板 (Server Monitoring Dashboard)

一套基於 **Python**、**Flask** 與 **Chart.js** 開發的即時伺服器監控系統，透過互動式網頁介面監控 CPU、Memory 與 Disk 使用狀況。

---

## 📸 儀表板預覽

<img width="1753" height="907" alt="image" src="https://github.com/user-attachments/assets/7d3bfc54-b458-40dd-97b4-a631795fb529" />

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

# 📌 專案介紹

Server Monitoring Dashboard 是一套使用 **Python** 與 **Flask** 開發的輕量化網頁監控系統。

此系統會持續收集電腦系統資源資訊，包括：

* **CPU 使用率**
* **Memory 使用率**
* **Disk 使用率**

並透過 **Chart.js** 將資料以即時圖表方式呈現在網頁 Dashboard 上。

本專案主要用於學習 Python Web 開發、後端 API 建置以及即時資料視覺化技術。

---

# ✨ 功能特色

* 📊 即時 CPU 使用率監控
* 💾 即時 Memory 使用率監控
* 🗄️ 即時 Disk 使用率監控
* 📈 使用 Chart.js 動態產生監控圖表
* 🔄 自動更新系統監控資料
* ⚠️ 當資源使用率超過設定門檻時提供警告通知
* 🌐 支援響應式網頁 Dashboard
* 📁 將監控紀錄儲存至 CSV 檔案

---

# 🛠 使用技術

## Backend

* Python
* Flask
* psutil
* pandas

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

---

# 🏗️ 系統架構

```
+---------------------+
|      Web 瀏覽器      |
+----------+----------+
           |
           v
+---------------------+
|     Flask API       |
+----------+----------+
           |
           v
+---------------------+
|      psutil         |
+----------+----------+
           |
           v
+---------------------+
| CPU | Memory | Disk |
+---------------------+
```

---

# 📂 專案結構

```
server-monitoring-dashboard/
│
├── main.py
├── monitor.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
    ├── css/
    │   └── style.css
    ├── js/
        └── dashboard.js

```

---

# 🚀 安裝方式

## 1. Clone 專案

```bash
git clone https://github.com/ZhongYang-Liu/Server-Monitoring-DashBoard.git
```

## 2. 進入專案資料夾

```bash
cd Server-Monitoring-DashBoard
```

## 3. 安裝所需套件

```bash
pip install -r requirements.txt
```

## 4. 執行程式

```bash
python main.py
```

## 5. 開啟瀏覽器

```
http://127.0.0.1:5000
```

---

# 📖 使用方式

啟動系統後，Dashboard 會每隔數秒自動更新系統資源資訊。

可以監控：

* CPU 使用率
* Memory 使用率
* Disk 使用率
* 資源使用趨勢
* 系統資源警告通知

---

# 💡 技術能力展示

本專案展示以下技術能力：

* Python 程式開發
* Flask Web 後端開發
* RESTful API 串接與設計
* 使用 psutil 進行系統資源監控
* 使用 Chart.js 進行資料視覺化
* HTML / CSS / JavaScript 前後端整合
* 即時 Dashboard 開發

---

# 🚀 未來改善方向

* 使用者登入驗證系統
* 歷史監控資料分析
* SQLite / MySQL 資料庫整合
* Docker 容器化部署
* Email 警示通知功能
* 深色 / 淺色模式切換

---

# 👨‍💻 作者

**劉仲洋**

國立虎尾科技大學
資訊工程系

GitHub:

https://github.com/ZhongYang-Liu
