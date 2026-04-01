# 🤖 Jayam AI Chatbot (Offline AI Assistant)

## 📌 Description

Jayam AI is a locally running AI chatbot built using Flask and Ollama.
It provides a ChatGPT-like interface with chat history, multiple chat sessions, and a modern UI — all running offline without internet dependency.

---

## 🚀 Features

* 💬 ChatGPT-style user interface
* 🧠 Offline AI using local models (TinyLlama via Ollama)
* 📂 Multiple chat sessions (New Chat + History sidebar)
* 🎨 Modern UI with background image & glass effect
* ⚡ Real-time responses with “Jayam is thinking...” animation
* 🔒 Fully offline (no API required)

---

## 🛠️ Technologies Used

* Python (Flask)
* HTML, CSS, JavaScript
* Ollama (Local LLM runner)
* TinyLlama model

---

## 💻 How to Run Locally

1. Install Ollama

2. Run the model:

   ```bash
   ollama run tinyllama
   ```

3. Start the Flask server:

   ```bash
   python app.py
   ```

4. Open in browser:

   ```text
   http://127.0.0.1:5000
   ```

---

## 🌐 Live Demo

👉 (Add your GitHub Pages link here)

⚠️ Note: The live version shows only the UI.
To use full AI features, run the project locally.

---

## 📁 Project Structure

offline-ai-ui/
│── app.py
│── index.html
│── static/
│   └── bg.jpg

---

## 🎯 Future Improvements

* Voice input support 🎤
* File upload (PDF, DOC) 📄
* Mobile responsive design 📱
* Cloud deployment with API

---

## 👨‍💻 Author

Prakash (Second Year CSE Student)

---

## ⭐ Conclusion

This project demonstrates how a fully functional AI chatbot can be built and run locally using open-source tools, without relying on cloud APIs.
