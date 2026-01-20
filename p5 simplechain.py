
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
prompt=PromptTemplate(
    template='generate 5 interesting fact about {topic}',
    input_variables=['topic']
)
model=ChatGroq(
    temperature=0.9,
    model="openai/gpt-oss-120b"
)
parser=StrOutputParser()
chain=prompt | model | parser
result= chain.invoke("cricket")
print(result)