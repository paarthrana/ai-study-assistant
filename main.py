from google import genai
import os 
from dotenv import load_dotenv 
import json

def load_api():
    load_dotenv()
    api_key=os.getenv("GEMINI_API_KEY")

    client=genai.Client(api_key=api_key)

    return client

def save_history(mode, topic , answer):
    try:
        entry={
        "mode":mode,
        "topic":topic,
        "answer":answer
        }
    
        with open("history.json","r") as file:
            data=json.load(file)
            data.append(entry)
        with open("history.json","w") as file:
            json.dump(data,file,indent=4)

    except Exception as e:
        data=[]
        data.append(entry)
        with open("history.json","w") as file:
            json.dump(data, file, indent=4)

def veiw_history():
    try :
      with open ("history.txt","r")as file:
       history =file.read()
       print("\n===== Chat History =====\n")
       print(history)
    except Exception as e:
       print("History not found")
       print(type(e).__name__)


def get_response(client , question):
    prompt =f'''You are a Helpful AI study assistant.

    Rules:
    - Explain concepts clearly.
    - Give examples whenever possible.
    - Keep answers beginner-friendly.
    - Focus on learning and education.

    Question:
    {question}'''
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text



def main():
    try :

     client=load_api()
     while True:
        print("====Ai Study Assistant====")
        print("1. Ask a question")
        print("2. Explain like i'm 5")
        print("3. Quiz me")
        print("4. Summarise Topic")
        print("5. Veiw history")
        print("6. Exit")
        choice = input("Enter a choice : ")
        if choice =="6":
            break
        elif choice=="1":
           question=input("\nASK:")
           answer = get_response(client,question)
           print(answer)
           save_history("Ask",question,answer)

        elif choice=="2":
           topic =input("Enter a topic:")
           prompt=f''' Explain the following topic to a 5-year-old child 
           using simple words and examples:
           {topic}
           '''
           answer=get_response(client,prompt)
           print(answer)
           save_history("ELI5",topic ,answer)

        elif choice=="3":
           topic =input("Enter a topic:")
           prompt=f''' Create 7 multiple choice questions on :
           {topic}
           provide
           -questions
           -4 options 
           -correct answer and explanation why it is correct in 20 words
           '''
           answer=get_response(client ,prompt)
           print(answer)
           save_history("Quiz", topic ,answer)

        elif choice=="4":
           topic =input("Enter a topic:")
           prompt=f''' Summarise this topic using 10 solid bullet points:
           {topic}
        
           '''
           answer=get_response(client ,prompt)
           print(answer)
           save_history("Summarise", topic ,answer)

        elif choice=="5":
           veiw_history()



 
    except Exception as e:
        print("ERROR:")
        print(type(e).__name__)
        print(e)

if __name__ == "__main__":
  main()