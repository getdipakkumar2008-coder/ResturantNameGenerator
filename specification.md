# 📋 Technical Specification — Restaurant Name Generator

## 1. Purpose

Generate AI-powered restaurant names and menu suggestions based on user-selected cuisine using a Streamlit UI backed by LangChain and OpenAI.

---

## 2. Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | User can select a cuisine from a predefined list via a sidebar dropdown |
| FR-02 | App generates a unique, fancy restaurant name for the selected cuisine |
| FR-03 | App generates a list of relevant menu items for the generated restaurant |
| FR-04 | Restaurant name is displayed as a header in the UI |
| FR-05 | Menu items are displayed as a bullet list |
| FR-06 | Results update automatically when cuisine selection changes |

---

## 3. Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-01 | Response should be generated within 10 seconds under normal network conditions |
| NFR-02 | API keys must never be committed to version control |
| NFR-03 | App must run on Python 3.10+ |
| NFR-04 | Code must be modular — UI and LLM logic in separate files |
| NFR-05 | LLM temperature set to 0.7 for creative but coherent output |

---

## 4. System Architecture

```
┌──────────────┐      ┌──────────────────────┐      ┌───────────────┐
│   main.py    │ ───▶ │  langchain_helper.py  │ ───▶ │  OpenAI API   │
│  (Streamlit) │      │  (LCEL Chain Logic)   │      │ (GPT-4o-mini) │
└──────────────┘      └──────────────────────┘      └───────────────┘
```

---

## 5. Inputs & Outputs

### Input
| Parameter | Type | Source | Values |
|---|---|---|---|
| `cuisine` | `str` | Streamlit sidebar | `"Indian"`, `"Chinese"`, `"Mexican"` |

### Output
| Key | Type | Description |
|---|---|---|
| `restaurant_name` | `str` | AI-generated fancy restaurant name |
| `menu_items` | `str` | Comma-separated list of menu suggestions |

---

## 6. File Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Streamlit UI — renders sidebar, header, and menu list |
| `langchain_helper.py` | LangChain LCEL chain — prompts, model calls, output parsing |
| `secret_key.py` | Stores `openapi_key` (excluded from version control) |
| `.gitignore` | Prevents secrets and environment files from being committed |

---

## 7. API & Model

| Property | Value |
|---|---|
| Provider | OpenAI |
| Model | `gpt-4o-mini` |
| Temperature | `0.7` |
| Auth | Environment variable `OPENAI_API_KEY` |
| Chain Type | LCEL Sequential (`RunnableParallel`) |

---

## 8. Dependencies

```
streamlit
langchain
langchain-openai
langchain-core
openai
```

---

## 9. Error Handling (Future Scope)

- Handle missing or invalid API key gracefully with a UI message
- Add try/except around `sequential_chain.invoke()` for network errors
- Add loading spinner in Streamlit during API call

---

## 10. Supported Cuisines (v1.0)

- 🇮🇳 Indian
- 🇨🇳 Chinese
- 🇲🇽 Mexican
