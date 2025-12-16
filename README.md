🧠 ASD Multimodal Overload Detection System

📌 Overview
This project presents a multimodal AI-based system designed to analyze sensory overload and distress indicators, with a focus on Autism Spectrum Disorder (ASD). The system integrates video, audio, and environmental context to infer high-level human states such as Calm, Moderate Overload, and Severe Overload.
The project was developed as a Minor Project and follows a step-by-step evolution, starting from basic image-based emotion analysis and gradually extending to a more comprehensive multimodal pipeline.

🎯 Motivation

Individuals with ASD often experience sensory overload due to environmental stimuli such as noise, motion, lighting, or social interaction. Early detection of distress or overload can help caregivers and clinicians intervene appropriately.
This project aims to explore how AI-driven perception systems can assist in understanding such states using non-invasive, interpretable, and ethically designed techniques.

🧩 System Components

1️⃣ Video Analysis (Computer Vision)

Frame-level analysis using OpenCV
Features extracted:
-Motion intensity
-Brightness variations
-Facial emotion cues (happy, sad, angry, surprised)
-Face detection using Haar Cascades
-Temporal aggregation using sliding windows

2️⃣ Audio Analysis (Signal Processing)

Audio extracted directly from video
Features extracted:
-RMS intensity
-Spectral flux
-Spectral bandwidth
-Detection of high auditory stimulation levels

3️⃣ Environmental Context

Weather information (temperature, humidity, UV index, air quality)
Integrated as a contextual risk factor

4️⃣ Multimodal Risk Assessment

Rule-based fusion of audio, video, and environment features

Generation of:
-total_risk
-overall_state (Calm / Moderate Overload / Severe Overload)
-Alert flags (distress_flag, overload_flag)
-Human-readable alerts

⚙️ Methodology

-Sliding Window Analysis
-Window size: 10 seconds
-Step size: 5 seconds
-Multimodal Fusion Strategy
-Each modality contributes an independent risk score
-Final decision made using interpretable, rule-based logic
-Design Philosophy
-Explainable and transparent AI
-Robust to missing modalities
-Suitable for healthcare-oriented applications

🖥️ Frontend Interface

A Streamlit-based web interface allows users to:
-Upload video files
-Run multimodal analysis
-Visualize overall state over time
-Highlight distress and overload segments
-Download results as a CSV file

🛠️ Technologies Used

-Python
-OpenCV
-Librosa
-PyAV
-Pandas & NumPy
-Streamlit
-WeatherAPI

🚀 How to Run

1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
streamlit run app.py

3️⃣ Upload video(s)
Supported formats: .mp4, .mov, .avi, .mkv
Recommended length: 30–90 seconds
