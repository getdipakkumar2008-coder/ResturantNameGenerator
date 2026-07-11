# 🗺️ Project Plan — Restaurant Name Generator

## Project Goal
Build and deploy an AI-powered restaurant name and menu generator using LangChain + Streamlit, iterating from a basic prototype to a polished, extensible app.

---

## Phase 1 — Core Setup ✅

| Task | Status |
|---|---|
| Set up Python virtual environment | ✅ Done |
| Install LangChain, Streamlit, OpenAI dependencies | ✅ Done |
| Create `secret_key.py` for API key management | ✅ Done |
| Verify OpenAI API connection | ✅ Done |

---

## Phase 2 — LangChain Logic ✅

| Task | Status |
|---|---|
| Create `PromptTemplate` for restaurant name generation | ✅ Done |
| Create `PromptTemplate` for menu item generation | ✅ Done |
| Build `name_chain` using LCEL pipe (`\|`) | ✅ Done |
| Build sequential chain with `RunnableParallel` | ✅ Done |
| Fix import errors and duplicate code | ✅ Done |
| Fix env variable name (`OPENAI_API_KEY`) | ✅ Done |
| Fix function name typo (`generate_restaurant_name_and_items`) | ✅ Done |

---

## Phase 3 — Streamlit UI ✅

| Task | Status |
|---|---|
| Create `main.py` with Streamlit layout | ✅ Done |
| Add sidebar cuisine selector | ✅ Done |
| Display restaurant name as header | ✅ Done |
| Display menu items as bullet list | ✅ Done |
| Connect UI to `langchain_helper.generate_restaurant_name_and_items()` | ✅ Done |

---

## Phase 4 — Version Control ✅

| Task | Status |
|---|---|
| Create `.gitignore` (exclude `.venv`, `secret_key.py`, etc.) | ✅ Done |
| Initialize git repository | ✅ Done |
| Make initial commit | ✅ Done |
| Create GitHub repository | ✅ Done |
| Push code to remote | ✅ Done |

---

## Phase 5 — Documentation ✅

| Task | Status |
|---|---|
| Write `README.md` (setup, usage, architecture) | ✅ Done |
| Write `Agent.md` (LangChain chain design) | ✅ Done |
| Write `specification.md` (functional & technical spec) | ✅ Done |
| Write `Plan.md` (this file) | ✅ Done |

---

## Phase 6 — Future Improvements 🔜

| Task | Priority | Notes |
|---|---|---|
| Add more cuisines (Italian, Japanese, French, etc.) | High | Extend the selectbox list |
| Add error handling for API failures | High | Try/except + Streamlit `st.error()` |
| Add loading spinner during API call | Medium | `st.spinner()` |
| Cache results with `@st.cache_data` | Medium | Avoid redundant API calls |
| Add restaurant tagline generation | Low | Third chain step |
| Add cuisine image or emoji display | Low | UI enhancement |
| Deploy to Streamlit Cloud | High | `streamlit deploy` or GitHub integration |
| Add unit tests for `langchain_helper.py` | Medium | Mock LLM responses |

---

## Timeline

```
Week 1  ██████████  Phases 1–3 (Core build)        ✅
Week 2  ████████    Phases 4–5 (Git + Docs)         ✅
Week 3  ░░░░░░░░    Phase 6    (Improvements)       🔜
```
