from jokes import get_joke

print("Welcome to the Funny Bot. Type 'exit' to quit.\n")

while True:
    user = input("You: ").strip()

    if user.lower() == "exit":
        print("FunnyBot: Goodbye. This was emotionally unnecessary.")
        break

    response = get_joke(user)
    print("FunnyBot:", response)
