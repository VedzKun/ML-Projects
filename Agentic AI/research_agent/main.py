# main.py
from agent.research_agent import research
from dotenv import load_dotenv

load_dotenv()

def main():
   
    print("After research, you can request changes and get a revised Word document.\n")

    while True:
        query = input("\nWhat do you want to research? (or type 'exit' to quit)\n> ").strip()
        
        if query.lower() in ['exit', 'quit', 'q']:
            print(" Goodbye!")
            break
            
        if query:
            research(query)

if __name__ == "__main__":
    main()