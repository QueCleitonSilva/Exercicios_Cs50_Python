def main():
    amount_due = 50
    total_inserted = 0

    while total_inserted < amount_due:
        coin=int(input("Insert a coin of 50, 25, 10, or 5 cents: "))

        if coin in [5, 10, 25, 50]:
            total_inserted += coin
            if total_inserted < amount_due:
                print("Amount Due:", amount_due - total_inserted)

        else:
            print("Amount Due:", amount_due)

    if total_inserted == amount_due:
        print("Change Owed:", 0)

    if total_inserted > amount_due:
        change = total_inserted - amount_due
        print("Change Owed:", change)

if __name__ == "__main__":
    main()
