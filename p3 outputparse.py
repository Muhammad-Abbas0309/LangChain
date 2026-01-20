from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model =ChatGroq(
    temperature=0.9,
    model="llama-3.1-8b-instant"
)
# first prompt detai
template1=PromptTemplate(
    template='write a detail note on {topic}',
    input_variables=['topic']
)
# second
template2=PromptTemplate(
    template='write a 5 line summary on following text: {text}',
    input_variables=['text']
) 
prompt1=template1.invoke({'topic':'black hole'})
result1=model.invoke(prompt1)
prompt2=template2.invoke({'text': result1.content})
result2=model.invoke(prompt2)
print(result1.content)
print(result2.content)
