from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

version = "llama3.2" ## version downloaded from ollama website

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model=version) ##

## step 1 - execute once
# result = model.invoke(input="hello world")
# print(result)

## step 2 - inloop with the use of prompt
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to AI chatbot. Type 'exit' to quit.")
    while True: ## run a loop
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break ## break the loop

        result = chain.invoke(
            {
                "context": context,
                "question": user_input
            }
        )
        print("BOT Response:", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()

## Note:
# Each time you interact with the bot, it's a new conversation and it doesn't retain any information from previous conversations.
