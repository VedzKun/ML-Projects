from agent.gemini_client import GeminiDebugAgent

def main():
    print("Welcome to my debugger")
    error=input("Paste error code:")
    print("\nPaste your CODE here: (enter twice when finished)")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "" and (not lines or lines[-1].strip() == ""):
                break
            lines.append(line)
        except EOFError:
            break
    code = "\n".join(lines).strip()
    
    if not error or not code:
        print("Error or code cannot be empty...")
        return
    agent = GeminiDebugAgent()
    print("\n" + "="*40)
    print("Agent is thinking")

    result = agent.debug(error, code)
    print("--Debugging Solution--")
    print(result)

if __name__ == "__main__":
    main()    