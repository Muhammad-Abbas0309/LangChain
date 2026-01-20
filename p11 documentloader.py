from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
loader=TextLoader(r"F:\ssd\ai project\langchain\file.txt",encoding='utf-8')
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