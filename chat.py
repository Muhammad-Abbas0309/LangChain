from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

import os 
load_dotenv()
llm=ChatGroq(
    temperature=0.9,
    # grog_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"

)
result=llm.invoke(" who is most famous scientist in electromagnet give me just name")
print(result.content)

