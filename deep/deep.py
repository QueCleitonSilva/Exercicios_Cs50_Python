## python deep.py

## Pront the user input
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    # Stripping leading and trailing spaces from the input
    answer_stripped = answer.strip()

    # Checking if the stripped input matches 42 or "forty-two" or "forty two" (case-insensitive)
    if answer_stripped.lower() == "42" or "forty-two" in answer_stripped.lower() or "forty two" in answer_stripped.lower():
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
