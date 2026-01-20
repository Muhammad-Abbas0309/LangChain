from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    temperature=0.9,
    model="llama-3.1-8b-instant"
)

# ✅ Correct message list
chathistory = [
    SystemMessage(content="You are a helpful assistant."),
]
while True:
    user_input=input("you:")
    # convert it into human message
    chathistory.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result=llm.invoke(chathistory)
    # now convet response into the ai message through following code 
    chathistory.append(AIMessage(content=result.content))
    print("Ai:",result.content)
print(chathistory)

