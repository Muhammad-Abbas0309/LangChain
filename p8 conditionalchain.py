from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()  # Make sure GROQ_API_KEY is set

# -----------------------------
# Step 1: Initialize Groq model
# -----------------------------
model = ChatGroq(
    model="openai/gpt-oss-120b",  # use a currently supported Groq model
    temperature=0.7
)

# -----------------------------
# Step 2: Output parsers
# -----------------------------
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative:\n{feedback}\n{format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback:\n{feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback:\n{feedback}',
    input_variables=['feedback']
)
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not determine sentiment")
)
chain = classifier_chain | branch_chain
feedback_text = "This is a beautiful phone"
result = chain.invoke({'feedback': feedback_text})

print("Response:")
print(result)

# Optional: visualize chain graph
chain.get_graph().print_ascii()
