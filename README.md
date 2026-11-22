# Automatic Indian Sign Language (ISL) Translator (Hearing Impairment Assistant)

A Python-based **Speech-to-Indian Sign Language (ISL)** translator designed as a Hearing Impairment Assistant[cite: 3, 4]. The application captures live voice input through a microphone, converts the spoken audio into text, and displays either a corresponding animated ISL GIF for recognized words/phrases or spells out unrecognized words letter-by-letter using ISL alphabet images[cite: 3, 6].

---

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Prerequisites & Dependencies](#prerequisites--dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Vocabulary](#supported-vocabulary)

---

## Features
- **Live Voice Recognition:** Captures real-time speech via microphone with automatic ambient noise adjustment[cite: 3, 6].
- **Dual Speech Recognition Engines:**
  - **Online Recognition (`main2.py` / `speech.py`):** Uses Google Speech Recognition (`recognize_google`) for high accuracy[cite: 4, 6].
  - **Offline Recognition (`main1.py`):** Uses CMU PocketSphinx (`recognize_sphinx`) for offline voice-to-text conversion[cite: 3].
- **Phrase & Word GIF Translation:** Matches spoken words and common conversational phrases against a predefined ISL dictionary and renders animated `.gif` files in a Tkinter window[cite: 3, 6, 8].
- **Fingerspelling Fallback:** Automatically breaks down words not found in the GIF dictionary into individual letters (`a–z`) and displays sequential ISL alphabet images (`.jpg`) using Matplotlib[cite: 1, 3, 6].
- **Graphical User Interface (GUI):** Provides an interactive `easygui` launcher menu (`HEARING IMPAIRMENT ASSISTANT`) featuring a custom sign language banner (`signlang.png`)[cite: 2, 3, 4, 5].
- **Agent-Based Simulation (`imageLabel.py`):** Includes a multi-agent grid simulation built with `Mesa` (`SignLanguageModel` and `SignLanguageAgent`) alongside the custom Tkinter GIF renderer[cite: 2].

---

## How It Works
1. **Launch:** Running `main2.py` (or `main1.py`) opens the **Hearing Impairment Assistant** GUI prompt[cite: 3, 4].
2. **Listen:** Selecting **"Live Voice"** activates the microphone, calibrates for background noise, and listens for spoken input[cite: 3, 4, 6].
3. **Process & Match:**
   - The recognized speech is converted to lowercase and stripped of punctuation[cite: 3, 6].
   - If the phrase is `"goodbye"`, `"good bye"`, or `"bye"`, the listening session terminates[cite: 3, 6].
   - If the phrase exists in `words.py` (`isl_gif`), the corresponding `ISL_Gifs/<phrase>.gif` animation is played in a Tkinter window[cite: 3, 6, 8].
   - Otherwise, each character in the recognized text is matched against `alphabets.py` (`a–z`) and displayed sequentially from `letters/<letter>.jpg` at 0.8-second intervals[cite: 1, 3, 6].

---

## Project Structure
```text
Automatic-Indian-Sign-Language-Translator-ISL-master-main/
│
├── main2.py                   # Primary modular entry point (uses Google Speech API)[cite: 4, 6]
├── main1.py                   # Standalone entry point (uses offline PocketSphinx)[cite: 3]
├── speech.py                  # Core speech-to-ISL translation logic[cite: 6]
├── words.py                   # Dictionary list of supported ISL words and phrases[cite: 8]
├── alphabets.py               # List of lowercase alphabet characters (a–z)[cite: 1]
├── imageLabel.py              # Custom Tkinter GIF player widget & Mesa agent simulation[cite: 2]
├── speech_recongisation.py    # Utility script to list available system microphones[cite: 7]
├── signlang.png               # UI banner graphic for the EasyGUI prompt
