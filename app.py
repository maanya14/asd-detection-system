import os
import uuid
import streamlit as st
import matplotlib.pyplot as plt

from VideoProcessing import process_single_video

st.set_page_config(layout="wide")
st.title("🧠 ASD Multimodal Overload Detection")

if "df" not in st.session_state:
    st.session_state.df = None

uploaded_video = st.file_uploader(
    "Upload a video",
    type=["mp4", "mov", "avi", "mkv"],
    accept_multiple_files=False
)

if st.button("▶ Run Analysis"):

    if not uploaded_video:
        st.error("Please upload a video.")
        st.stop()

    run_dir = f"video_{uuid.uuid4().hex[:6]}"
    os.makedirs(run_dir, exist_ok=True)

    video_path = os.path.join(run_dir, uploaded_video.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_video.read())

    with st.spinner("Processing video..."):
        df = process_single_video(video_path)

    if df is None or df.empty:
        st.error("No valid analysis windows produced.")
        st.stop()

    st.session_state.df = df
    st.success("Analysis completed!")

# ================= DISPLAY =================
if st.session_state.df is not None:
    df = st.session_state.df

    st.subheader("Preview")
    st.dataframe(df.head(20))

    def ts_to_sec(t):
        h, m, s = map(int, t.split(":"))
        return h * 3600 + m * 60 + s

    df["time"] = df["timestamp"].apply(ts_to_sec)
    state_map = {"Calm": 0, "Moderate Overload": 1, "Severe Overload": 2}
    df["state_level"] = df["overall_state"].map(state_map)

    fig, ax = plt.subplots(figsize=(7, 3))

    ax.plot(df["time"], df["state_level"], marker="o")

    ax.scatter(
        df[df["overload_flag"] == 1]["time"],
        df[df["overload_flag"] == 1]["state_level"],
        color="red",
        label="Overload"
    )

    ax.scatter(
        df[df["distress_flag"] == 1]["time"],
        df[df["distress_flag"] == 1]["state_level"],
        color="orange",
        label="Distress"
    )

    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["Calm", "Moderate", "Severe"])
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("State")
    ax.legend()

    st.pyplot(fig)

    st.download_button(
        "⬇ Download CSV",
        df.to_csv(index=False),
        "multimodal_output.csv"
    )
