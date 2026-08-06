const ctx = document.getElementById("cpuChart");

const cpuChart = new Chart(ctx, {
    type: "line",

    data: {
        labels: [],
        datasets: [{
            label: "CPU Usage(%)",
            data: [],
            borderWidth: 2,
            tension: 0.3    
        },
        {
            label: "Memory Usage(%)",
            data: [],
            borderWidth: 2,
            tension: 0.3
        },
        {
            label: "Disk Usage(%)",
            data: [],
            borderWidth: 2,
            tension: 0.3
        }]
    },

    options: {
        responsive: true,

        scales: {
            y: {
                min: 0,
                max: 100
            }
        }
    }
});

// 依數值判斷卡片狀態 (normal / warning / danger)
function getStatusClass(value) {
    if (value >= 90) return "danger";
    if (value >= 70) return "warning";
    return "normal";
}

function updateCard(id, value) {
    const card = document.getElementById(id + "-card");
    const valueEl = document.getElementById(id);

    valueEl.textContent = value + "%";

    card.classList.remove("normal", "warning", "danger");
    card.classList.add(getStatusClass(value));
}

function updateWarning(cpu, memory, disk) {
    const warningEl = document.getElementById("warning");
    const alerts = [];

    if (cpu >= 90) alerts.push("⚠ CPU usage is critically high!");
    if (memory >= 90) alerts.push("⚠ Memory usage is critically high!");
    if (disk >= 90) alerts.push("⚠ Disk usage is critically high!");

    warningEl.textContent = alerts.join("  ");
}

function updateTable(timeHistory, cpuHistory, memoryHistory, diskHistory) {
    const tbody = document.getElementById("table-body");
    tbody.innerHTML = "";

    // 顯示最新的資料在最上面
    for (let i = timeHistory.length - 1; i >= 0; i--) {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${timeHistory[i]}</td>
            <td>${cpuHistory[i]}</td>
            <td>${memoryHistory[i]}</td>
            <td>${diskHistory[i]}</td>
        `;
        tbody.appendChild(row);
    }
}

function updateChart(timeHistory, cpuHistory, memoryHistory, diskHistory) {
    cpuChart.data.labels = timeHistory;
    cpuChart.data.datasets[0].data = cpuHistory;
    cpuChart.data.datasets[1].data = memoryHistory;
    cpuChart.data.datasets[2].data = diskHistory;
    cpuChart.update();
}

async function fetchData() {
    try {
        const response = await fetch("/data");
        const data = await response.json();

        // monitor.csv 是空的，或還沒有資料
        if (!data || Object.keys(data).length === 0) {
            console.warn("No data available yet.");
            return;
        }

        updateCard("cpu", data.CPU);
        updateCard("memory", data.Memory);
        updateCard("disk", data.Disk);

        updateWarning(data.CPU, data.Memory, data.Disk);

        updateTable(data.TimeHistory, data.CPUHistory, data.MemoryHistory, data.DiskHistory);
        updateChart(data.TimeHistory, data.CPUHistory, data.MemoryHistory, data.DiskHistory);

        document.getElementById("update-time").textContent = new Date().toLocaleTimeString();

    } catch (err) {
        console.error("Failed to fetch monitoring data:", err);
    }
}

// 立即抓一次資料，之後每 3 秒更新一次
fetchData();
setInterval(fetchData, 3000);