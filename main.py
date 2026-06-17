from google import genai
import os 
from dotenv import load_dotenv 

def load_api():
    load_dotenv()
    api_key=os.getenv("GEMINI_API_KEY")

    client=genai.Client(api_key=api_key)

    return client

def get_response(client , question):
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    return response.text

def main():
    client=load_api()
    print("====Ai Study Assistant====")
    print("Type'exit'to quit")

    while True:
        question=input("Ask : ")
        if question.lower()=="exit":
            break
        
        answer=get_response(client,question)

        print("\n AI :")
        print(answer)
        print()

if __name__ == "__main__":
  main()