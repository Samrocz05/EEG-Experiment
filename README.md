# 🧠 PsychoPy EEG Digit Imagination Experiment

This project replicates an EEG digit imagination experiment using **PsychoPy** based on a guided procedure. It is designed for collecting EEG data during mental imagery tasks where participants imagine digits from 0 to 9.

---

## 📋 Overview

This experiment consists of:

1. **Meditation Sessions**: To help the subject relax.
2. **Task 1 (Ordered Digits)**: Observe and visualize digits 0–9 sequentially.
3. **Task 2 (Shuffled Digits)**: Observe and visualize digits 0–9 in random order.
4. **Beep Cues**: Indicate the end of each visualization period.
5. **End Screen**: Thanks the participant for completion.

---

## 🎬 Experiment Flow

Each digit involves:
- **10 seconds of visual observation**
- **10 seconds of mental imagery with eyes closed**
- A **beep sound** to signal the end of the imagination period

Total flow:
- Welcome & Instruction screens
- Meditation (1 minute)
- Task 1: Digits 0–9 (in order)
- Meditation (1 minute)
- Task 2: Digits 0–9 (shuffled)
- Thank you screen

---

## 📁 Project Structure

psyco-eeg-digit-imagination/
├── README.md
├── requirements.txt
├── LICENSE
└── experiment/
├── main.py
└── meditation.mp3 (optional, you can use your own audio)

yaml


---

## 🚀 How to Run

### 1. Clone the Repository

```
git clone https://github.com/your-username/psyco-eeg-digit-imagination.git
cd psyco-eeg-digit-imagination
2. Install Dependencies

pip install -r requirements.txt
3. Run the Experiment

cd experiment
python main.py
✅ Tip: Press any key to navigate through screens. You’ll need to keep the screen fullscreen for best results.

🔈 Optional: Add Meditation Audio
If you'd like real meditation music:

Replace meditation.mp3 with your own relaxing 1-minute audio clip.

The script will automatically play the file if named correctly and placed in experiment/.

💻 Requirements
Python 3.7+

PsychoPy

Sound playback library (automatically installed with PsychoPy)

Install manually if needed:

pip install psychopy sounddevice
🧪 Designed For
EEG Experiments using Emotiv, OpenBCI, Muse, etc.

Cognitive science and BCI tasks

Mental imagery research (digits 0–9)

📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Sam D
LinkedIn | YouTube: Sam Explorer
Built with ❤️ using Python and PsychoPy

🙋‍♂️ Contributions
Feel free to fork, improve, and submit pull requests to expand this EEG tool!

🧠 Related Topics
EEG Signal Processing

Brain-Computer Interface (BCI)

Neurofeedback and Mental Task Classification

yaml
---

Let me know if:
- You want a **`.zip` file** of this repo for direct upload
- You’d like help uploading this to **GitHub with commit history**
- Or you'd like to **connect EEG hardware** (e.g., Emotiv or OpenBCI) to collect real-time data while this script runs

Ready to generate your `.zip` folder?

<img width="1978" height="1100" alt="image" src="https://github.com/user-attachments/assets/614feb3b-9099-48f1-a5fc-c3edf58070fa" />

