# Context- and Confidence-Aware Speech-Controlled FSM System

This project implements a real-time speech-controlled control system that
integrates speech signal processing with a finite state machine (FSM)
using confidence-aware and context-aware decision logic.

The goal is to design a reliable command-based control system that
reduces false activations and invalid state transitions.

---

## 🔍 System Overview

The system processes live microphone input and converts spoken commands
into FSM-compatible digital control signals.

Pipeline:
Audio Input → Speech Activity Detection → Feature Extraction →
Command Recognition → Confidence & Context Validation → FSM Output

---

## ⭐ Key Features

- Energy-based speech activity detection (silence filtering)
- MFCC + delta feature extraction
- Distance-based command recognition with confidence estimation
- Unknown command rejection
- Context-aware FSM validation
- Binary command encoding for FSM interface

---

## 🛠️ Technologies Used

- Python
- Librosa
- NumPy
- Speech Signal Processing
- Finite State Machines (FSM)
- VS Code

---

## 📂 Project Structure

speech-controlled-fsm/
│
├── audio_gate.py
├── features.py
├── recognizer.py
├── decision_manager.py
├── fsm_interface.py
├── requirements.txt
└── diagrams/

## 🚧 Project Status

This project is under active development.
Additional modules such as logging, performance evaluation,
and deep learning-based keyword spotting will be added.
