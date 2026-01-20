from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()
prompt = PromptTemplate(
    template="write a joke on {topic}",
    input_variables=["topic"]
)
model = ChatGroq(
    model_name="openai/gpt-oss-120b",
    temperature=1.8,   
    
)

parser = StrOutputParser()
chain = RunnableSequence(prompt, model, parser)
result = chain.invoke({"topic": "AI"})
print(result)
