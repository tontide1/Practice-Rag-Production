from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI


model = ChatGoogleGenerativeAI(model="gemma-4-31b-it")
response = model.invoke("Hello, done setup !")
print(response)