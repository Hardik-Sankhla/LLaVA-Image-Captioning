# 📸 AI Image Caption Generator (LLaVA + Ollama)

This project allows you to **upload an image** and receive an **AI-generated caption** using the powerful **LLaVA (Large Language and Vision Assistant)** model via **Ollama**.

Built with:
- 🖥 **FastAPI** backend (API for caption generation)
- 🌐 **Streamlit** frontend (beautiful user interface)
- 🚀 **Ollama** for running LLaVA locally

---

## 📷 Demo Preview

<p align="center">
  <img src="https://raw.githubusercontent.com/Hardik-Sankhla/Markdown-Resources/main/Image/Screenshot%202025-04-30%20174111.png" alt="Demo Screenshot" width="600"/>
</p>



---

## 📦 Project Structure

```
LLaVA-Image-Captioning/
├── backend/
│   ├── app/
│   │   ├── utils.py      # 🛠️ Helper functions
│   │   ├── model.py      # 🤖 Ollama model interaction
│   │   └── __init__.py   # (optional for package)
│   ├── main.py           # 🚀 FastAPI app
│   ├── requirements.txt  # 📦 Backend requirements
├── frontend/
│   ├── app.py            # 🌐 Streamlit UI
│   ├── requirements.txt  # 📦 Frontend requirements
├── Dockerfile            # 🐳 Backend Dockerfile
├── docker-compose.yml    # 🛠️ Compose backend + frontend (optional)
├── README.md             # 📖 Project guide
├── .env.example          # 🔑 Example env (optional)
└── demo.gif              # 🎥 GIF demo (optional)

```

---

## 🌟 Features

- Upload any image (.jpg, .jpeg, .png)
- Get high-quality, AI-generated captions
- FastAPI backend API
- Streamlit easy-to-use frontend
- Public API access for developers
- Local or cloud deployment support

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/llava-caption-api.git
cd llava-caption-api
```

### 2️ Run the Project (Three-Terminal Setup)

**Terminal 1: Start Ollama with LLaVA**
```
$ ollama run llava
$ ollama pull llava #If not already pulled:
```
**Terminal 2: Run the FastAPI Backend**

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
*API will be available at: http://localhost:8000*

**Terminal 3: Run the Streamlit Frontend**

```
cd frontend
pip install -r requirements.txt
streamlit run app.py
```
*Streamlit UI will open in your browser: http://localhost:8501*

### 📋 API Documentation

- Once backend is running, access the auto docs at:

*🔗 http://localhost:8000/docs*

### Example Request
- POST /caption
- Form field: file (image)

```
{
  "caption": "A beautiful sunset over the mountains."
}
```
--- 

✨ Future Improvements
- Add multi-language captioning

- Add multiple caption styles (e.g., poetic, short, storytelling)

- Host a free public demo

---

🤝 Contributing
Pull requests are welcome! Feel free to open an issue or suggest features.

---

📜 License
This project is licensed under the MIT License.

