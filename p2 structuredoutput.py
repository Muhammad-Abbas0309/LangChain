# from langchain_groq import ChatGroq
# from typing import TypedDict
# from dotenv import load_dotenv

# load_dotenv()

# # ----------------------
# # LLM
# # ----------------------
# model = ChatGroq(
#     temperature=.6,
#     model="llama-3.1-8b-instant"
# )

# # ----------------------
# # Define structured output
# # ----------------------
# class Review(TypedDict):
#     summary: str
#     sentiment: str

# # ----------------------
# # Wrap model with structured output
# # ----------------------
# structure_model = model.with_structured_output(Review,strict=True)

# # ----------------------
# # Input review text
# # ----------------------
# review_text = (
#     "I recently bought this mobile and I’m really impressed! "
#     "The display is bright and clear, the battery lasts all day even with heavy use, "
#     "and the camera takes sharp, vibrant photos. Performance is smooth, "
#     "and switching between apps is fast. The only minor downside is that it heats up slightly "
#     "during gaming, but overall it’s an excellent device for the price. Highly recommended!"
# )

# # ----------------------
# # Get structured result
# # ----------------------
# result = structure_model.invoke(review_text)

# # ----------------------
# # Print result
# # ----------------------
# print(result.content)
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

# LLM
model = ChatGroq(
    temperature=0.9,
    model="llama-3.1-8b-instant"
)

# TypedDict
class Review(TypedDict):
    summary: str
    sentiment: str

# Structured output with strict enforcement
structure_model = model.with_structured_output(Review, strict=True)

# System + human messages
messages = [
    SystemMessage(content="You are a JSON generator. "
                          "Always return exactly a JSON object with keys 'summary' and 'sentiment'."),
    HumanMessage(content="I recently bought this mobile and I’m really impressed! "
                         "The display is bright and clear, the battery lasts all day even with heavy use, "
                         "and the camera takes sharp, vibrant photos. Performance is smooth, "
                         "and switching between apps is fast. The only minor downside is that it heats up slightly "
                         "during gaming, but overall it’s an excellent device for the price. Highly recommended!")
]

# Invoke
result = structure_model.invoke(messages)

# Print
print(result)
print(result['summary'])
print(result['sentiment'])
