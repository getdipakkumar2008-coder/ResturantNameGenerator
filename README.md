# 🍽️ Restaurant Name Generator

An AI-powered web app that generates creative restaurant names and menu items based on a selected cuisine, built with **LangChain**, **OpenAI GPT-4o-mini**, and **Streamlit**.

---

## 🚀 Features

- Select a cuisine from the sidebar (Indian, Chinese, Mexican)
- AI generates a fancy restaurant name
- AI suggests a list of menu items for that restaurant
- Clean, interactive Streamlit UI

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| LangChain (LCEL) | LLM chain orchestration |
| OpenAI GPT-4o-mini | Language model |
| Streamlit | Web UI |

---

## 📁 Project Structure

```
ResturantNameGenerator/
├── main.py               # Streamlit UI
├── langchain_helper.py   # LangChain logic
├── secret_key.py         # API key (not committed)
├── .gitignore
├── README.md
├── Agent.md
├── specification.md
└── Plan.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/getdipakkumar2008-coder/ResturantNameGenerator.git
cd ResturantNameGenerator
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies
```bash
pip install streamlit langchain langchain-openai langchain-core
```

### 4. Add your OpenAI API key
Create a `secret_key.py` file in the project root:
```python
openapi_key = "sk-your-openai-api-key-here"
```

### 5. Run the app
```bash
streamlit run main.py
```

---

## 🔐 Security Note

`secret_key.py` is listed in `.gitignore` and will **never** be committed to the repository. Never share your API key publicly.

---

## 📸 How It Works

1. User picks a cuisine from the sidebar dropdown
2. `langchain_helper.py` builds a sequential LCEL chain:
   - **Chain 1** → Generates a restaurant name from the cuisine
   - **Chain 2** → Generates menu items from the restaurant name
3. Results are displayed in the Streamlit app

---

## 📄 License

MIT License
