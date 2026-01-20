from langchain_groq import ChatGroq
from langchain_core.prompts  import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
prompt1=PromptTemplate(
    template="write a tweet on {topic}",
    input_variables=['topic']

)   
prompt2=PromptTemplate(
    template="write linkenin post note on {topic}",
    input_variables=['topic']
)
model=ChatGroq(
    model_name="openai/gpt-oss-120b",
    temperature=.9
)
parser=StrOutputParser()
chain=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1,model,parser),
        'facebook':RunnableSequence(prompt2,model,parser)
    }
)
result=chain.invoke({'topic': "ai"})
print(result['tweet'])
print("*****************************************")
print(result['facebook'])