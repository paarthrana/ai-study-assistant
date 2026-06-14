from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client =genai.Client(api_key=api_key)

try:
 print("=====AI STUDY ASSISTANT====={type \"exit\" to leave}")
 while True:
  
  question = input("ASK:\t")
  if question.strip()=="":
     print("Please enter a question") 
     continue
  elif question.lower()=="exit":
   break
  response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)
  print("\nAI: ")
  print(response.text)
  print()
  

except Exception as e:
 print("Error found",e)

