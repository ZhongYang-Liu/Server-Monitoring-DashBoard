# 🖥 Server Monitoring Dashboard

A real-time server monitoring dashboard built with **Python**, **Flask**, and **Chart.js** for monitoring CPU, Memory, and Disk usage through an interactive web interface.

---

## 📸 Dashboard Preview

> **(Add your dashboard screenshot here)**

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
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── dashboard.js
│   └── images/
│
└── screenshots/
    └── dashboard.png
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
python app.py
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

---

# 📷 Screenshots

## Dashboard

> Add dashboard screenshot here

---

## Resource Usage Chart

> Add chart screenshot here

---

## Terminal

> Add terminal execution screenshot here

---

# 👨‍💻 Author

**Alan Liu**

Department of Computer Science and Information Engineering

National Formosa University

GitHub:
https://github.com/ZhongYang-Liu
