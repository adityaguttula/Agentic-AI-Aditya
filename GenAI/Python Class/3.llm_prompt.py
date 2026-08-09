import os
import json
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
load_dotenv()
llm = ChatVertexAI(cd
    model_name="gemini-2.5-pro",
    project=os.getenv("GCP_PROJECT_ID"),
    location='us-central1',
    temperature=0
)
MESSAGE = (
    """Hi, I am facing an issue with my account. I am unable to login and
      I keep getting an error message. Can you please help me resolve 
      this issue?""")
messages = [
    {"role": "system", "content": "You are a customer support assistant . Always respond in a polite and helpful manner."},
    {"role": "user", "content": MESSAGE}]

####Zero_Shot Prompting######
prompt = ('Read the customer message and return two things  "a catrgory(e.g. shipping, billing, product issue) and a sentiment(positive, negative, or frustrated) in a JSON format. The JSON should have two keys: "category" and "sentiment".')

##### One_Shot Prompting####
prompt= """Read the customer message and answer in below format : "Category: <one word> | Sentiment: <one word>" 
Example:
Message: "My invoice charged me twice this month, please fix it."
Answer: Category: Billing | Sentiment: Negative
Message: """+ MESSAGE + """
Answer:"""


response = llm.invoke(prompt)
print(response.content)

