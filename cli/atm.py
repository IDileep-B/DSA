# ATM Simulation Program with Exception Handling

accounts = {
    "101": {"name": "Alice", "balance": 5000},
    "102": {"name": "Bob", "balance": 3000}
}

transactions = [1000, -500, 2000]

while True:
    print("\n--- ATM Simulation Menu ---")
    print("1. Check Average Transaction (ZeroDivisionError)")
    print("2. Withdraw with Invalid Input (ValueError)")
    print("3. Deposit with Invalid Data Type (TypeError)")
    print("4. Access Invalid Transaction History (IndexError)")
    print("5. Access Non-Existent Account (KeyError)")
    print("6. Read Missing Transaction Log File (FileNotFoundError)")
    print("7. Exit")

    choice = input("Select an option (1-7): ")

    try:
        if choice == "1":
            # ZeroDivisionError
            total = sum(transactions)
            count = int(input("Enter number of transactions to divide by: "))
            avg = total / count
            print("Average Transaction:", avg)

        elif choice == "2":
            # ValueError
            amount = int(input("Enter withdrawal amount: "))
            if amount < 0:
                print("Invalid withdrawal amount!")
            else:
                print("Withdrawal successful!")

        elif choice == "3":
            # TypeError
            deposit = input("Enter deposit amount: ")
            result = deposit + 1000   # Intentionally causes TypeError
            print("Updated balance:", result)

        elif choice == "4":
            # IndexError
            index = int(input("Enter transaction index: "))
            print("Transaction:", transactions[index])

        elif choice == "5":
            # KeyError
            acc_no = input("Enter account number: ")
            print("Account Holder:", accounts[acc_no]["name"])

        elif choice == "6":
            # FileNotFoundError
            with open("transaction_log.txt", "r") as file:
                print(file.read())

        elif choice == "7":
            print("Exiting ATM Simulation...")
            break

        else:
            print("Invalid option selected!")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except ValueError:
        print("Error: Invalid input! Please enter numeric values only.")

    except TypeError:
        print("Error: Invalid data type used in operation!")

    except IndexError:
        print("Error: Transaction index out of range!")

    except KeyError:
        print("Error: Account number does not exist!")

    except FileNotFoundError:
        print("Error: Transaction log file not found!")

    except Exception as e:
        print("Unexpected Error:", e)