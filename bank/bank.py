def main():
    greeting = input("Greeting: ")
    greeting_function(greeting)

def greeting_function(greeting):

    greeting_striped = greeting.strip()

    if greeting_striped.lower().startswith("hello"):
        print("$0")
    elif greeting_striped.lower().startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
