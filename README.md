# PrepMate AI Agent 🤖

PrepMate AI Agent is an AI-powered interview preparation application built with **Streamlit**, **LangChain**, and **Ollama**.

The application acts as an AI interviewer and generates interview questions based on the interview type requested by the user.

Currently, the agent supports:

* 👔 **HR Interviews**
* 💻 **Technical Interviews**

The application uses the **Qwen 3 1.7B** model through Ollama to generate interview questions and responses locally.

---

## 🚀 Features

* AI-powered interview preparation
* HR interview mode
* Technical interview mode
* Generates **5 interview questions** based on the requested interview type
* Conversational chat interface
* Maintains chat history using Streamlit session state
* Runs the Qwen model locally through Ollama
* No external LLM API key required

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** — Web application interface
* **LangChain** — LLM application framework
* **LangChain Ollama** — Integration with Ollama
* **Ollama** — Local LLM runtime
* **Qwen3 1.7B** — Language model

---

## 📁 Project Structure

```text
PrepMate-AI/
│
├── app.py
├── README.md
├── requirements.txt
└── venv/
```

> `venv/` should normally be excluded from Git using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ChandanKhode290503/PrepMate-AI.git
```

Navigate into the project:

```bash
cd PrepMate-AI
```

---

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

---

### 3. Install dependencies

Install the required Python packages:

```bash
pip install streamlit langchain-ollama langchain-core
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 🦙 Install Ollama

PrepMate AI uses Ollama to run the language model locally.

Download and install Ollama from:

[Ollama Official Website](https://ollama.com/?utm_source=chatgpt.com)

After installing Ollama, download the Qwen model:

```bash
ollama pull qwen3:1.7b
```

You can verify that the model is installed with:

```bash
ollama list
```

You should see something similar to:

```text
qwen3:1.7b
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to start using PrepMate AI.

---

## 💬 How to Use

After starting the application, enter your desired interview type in the chat box.

### HR Interview

Example:

```text
I want an HR interview
```

The AI interviewer will generate HR-related interview questions.

Examples of HR topics include:

* Tell me about yourself.
* What are your strengths?
* What are your weaknesses?
* Why should we hire you?
* Where do you see yourself in five years?

---

### Technical Interview

Example:

```text
I want a Technical interview
```

The AI will generate technical interview questions relevant to the requested interview.

Technical questions can cover topics such as:

* Programming
* Data Structures
* Algorithms
* Python
* Databases
* APIs
* Software Development

---

## 🧠 How It Works

The application uses a `SystemMessage` to define the behavior of the AI interviewer.

The system instructs the model to:

1. Determine the interview type from the user's input.
2. Conduct an **HR interview** when HR is requested.
3. Conduct a **Technical interview** when Technical is requested.
4. Generate exactly **5 questions**.
5. Avoid mixing HR and Technical questions unless explicitly requested.
6. Maintain a conversational interview experience.

The user's message is passed to the Qwen model using LangChain:

```python
response = model.invoke([
    system_message,
    human_message
])
```

The response is then displayed in the Streamlit chat interface.

---

## 💾 Chat History

The application uses Streamlit's session state to maintain the conversation:

```python
st.session_state.chat
```

User and assistant messages are stored as:

```python
st.session_state.chat.append(("user", question))
st.session_state.chat.append(("assistant", response.content))
```

This allows previous messages to be displayed when the Streamlit application reruns.

---

## 🔐 Privacy

PrepMate AI uses a locally running Ollama model.

Your prompts are processed by the local model rather than requiring an external LLM API service.

However, make sure you do not commit sensitive information such as:

* API keys
* Passwords
* `.env` files
* Personal credentials

---

## 🔮 Future Improvements

Possible future improvements include:

* 🎯 Interview difficulty selection
* 📊 Interview performance scoring
* 📝 Answer evaluation
* 🎤 Voice-based interviews
* ⏱️ Timed interview sessions
* 📈 Performance analytics
* 🧑‍💼 Multiple job roles
* 💻 Programming/coding interview mode
* 📚 Question categories
* 🔄 Follow-up questions
* 🏆 Interview score and feedback
* 🌐 Deployment to Streamlit Cloud

---

## 🤝 Contributing

Contributions are welcome!

To contribute:

```bash
git clone https://github.com/ChandanKhode290503/PrepMate-AI.git
```

Create a new branch:

```bash
git checkout -b feature/new-feature
```

Make your changes, commit them:

```bash
git add .
git commit -m "Add new feature"
```

Push your branch:

```bash
git push origin feature/new-feature
```

Then open a Pull Request on GitHub.

---

## 📄 License

This project is intended for educational and interview-preparation purposes.

---

## 👨‍💻 Author

**Chandan Khode**

GitHub: [ChandanKhode290503](https://github.com/ChandanKhode290503?utm_source=chatgpt.com)

---

⭐ If you find this project useful, consider giving the repository a star!
