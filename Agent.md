# 🤖 Agent Architecture — Restaurant Name Generator

This document describes the LangChain agent/chain design used in this project.

---

## Overview

The project uses **LangChain Expression Language (LCEL)** to build a sequential AI pipeline. It does **not** use a ReAct agent with tools — instead, it uses a two-step **RunnableParallel chain** to generate restaurant names and menu items in sequence.

---

## Chain Design

```
Input: { "cuisine": "Indian" }
         │
         ▼
┌─────────────────────────────────┐
│  RunnableParallel (Step 1)      │
│  restaurant_name = name_chain   │
│    PromptTemplate               │
│      → ChatOpenAI (GPT-4o-mini) │
│      → StrOutputParser          │
└─────────────┬───────────────────┘
              │  { "restaurant_name": "Spice Elysium" }
              ▼
┌─────────────────────────────────────────────────┐
│  RunnableParallel (Step 2)                      │
│  restaurant_name = passthrough lambda           │
│  menu_items = RunnableLambda                    │
│    → PromptTemplate (menu items prompt)         │
│    → ChatOpenAI (GPT-4o-mini)                   │
│    → StrOutputParser                            │
└─────────────────────────────────────────────────┘
              │
              ▼
Output: { "restaurant_name": "...", "menu_items": "..." }
```

---

## Components

### `PromptTemplate` (Name)
```
"I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
```
Takes `cuisine` as input, produces a restaurant name string.

### `PromptTemplate` (Menu Items)
```
"Suggest some menu items for {restaurant_name}. Return it as a comma separated string"
```
Takes `restaurant_name` as input, produces a comma-separated menu items string.

### `ChatOpenAI`
- **Model:** `gpt-4o-mini`
- **Temperature:** `0.7` (creative but consistent)

### `StrOutputParser`
Strips the LangChain message wrapper and returns a plain string.

### `RunnableParallel`
Runs multiple runnables on the same input simultaneously and merges outputs into a dict.

### `RunnableLambda`
Wraps a plain Python lambda as a LangChain-compatible runnable for use in LCEL pipes.

---

## LCEL Pipe Flow

```python
name_chain = prompt_template_name | llm | StrOutputParser()

sequential_chain = (
    RunnableParallel(restaurant_name=name_chain)
    | RunnableParallel(
        restaurant_name=lambda x: x["restaurant_name"],
        menu_items=(
            RunnableLambda(lambda x: {"restaurant_name": x["restaurant_name"]})
            | prompt_template_items | llm | StrOutputParser()
        )
    )
)
```

---

## Extending the Agent

To add more chains (e.g., generate a restaurant description or a tagline), add another `RunnableParallel` step:

```python
| RunnableParallel(
    restaurant_name=lambda x: x["restaurant_name"],
    menu_items=...,
    tagline=RunnableLambda(lambda x: {"restaurant_name": x["restaurant_name"]})
             | tagline_prompt | llm | StrOutputParser()
)
```
