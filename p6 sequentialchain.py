from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed note on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Give a short summary of the following text:\n{text}",
    input_variables=["text"]
)

model = ChatGroq(
    temperature=0.8,
    model="openai/gpt-oss-120b"
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

# ✅ Correct input format
result = chain.invoke({"topic": "cricket"})

print(result)
