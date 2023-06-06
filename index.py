from chatgpt_wrapper import ChatGPTWrapper
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chatgpt = ChatGPTWrapper(EMAIL, PASSWORD)
response = chatgpt.ask("How are you?")
print(response)