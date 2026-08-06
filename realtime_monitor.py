import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots(figsize=(10,5))


def update(frame):

    try:

        df = pd.read_csv("monitor.csv")


        if df.empty:
            return


        df["Time"] = pd.to_datetime(df["Time"])


        # 最近50筆
        df = df.tail(50)


        ax.clear()


        ax.plot(
            df["Time"],
            df["CPU"],
            label="CPU"
        )


        ax.plot(
            df["Time"],
            df["Memory"],
            label="Memory"
        )


        ax.plot(
            df["Time"],
            df["Disk"],
            label="Disk"
        )


        ax.set_title(
            "Real-Time Server Monitoring"
        )

        ax.set_xlabel(
            "Time"
        )

        ax.set_ylabel(
            "Usage (%)"
        )


        ax.legend()


        plt.xticks(rotation=45)

        plt.tight_layout()


    except Exception as e:

        print("Error:", e)



anim = FuncAnimation(
    fig,
    update,
    interval=5000,
    cache_frame_data=False
)


plt.show()