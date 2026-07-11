import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda
from secret_key import openapi_key

os.environ["OPENAI_API_KEY"] = openapi_key

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

def generate_restaurant_name_and_items(cuisine: str) -> dict:
    prompt_template_name = PromptTemplate.from_template(
        "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    prompt_template_items = PromptTemplate.from_template(
        "Suggest some menu items for {restaurant_name}. Return it as a comma separated string"
    )

    name_chain = prompt_template_name | llm | StrOutputParser()

    # Generate restaurant name first, then use it to generate menu items
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

    response = sequential_chain.invoke({"cuisine": cuisine})
    return response

if __name__ == "__main__":
    result = generate_restaurant_name_and_items("Italian")
    print(result)