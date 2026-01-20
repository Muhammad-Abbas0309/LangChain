from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
# we alos use lazy loading for multiple pdf loading 
docs=loader.load()
model= ChatGroq(
    model_name="openai/gpt-oss-120b",
    temperature=.9
)
prompt=PromptTemplate(
    template="write a summary of of text {topic}",
    input_variables=['topic']
)
parser=StrOutputParser()
chain= prompt | model | parser
result=chain.invoke({'topic':docs[0]})
print(result)