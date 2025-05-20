import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

def main():
    while True:
        print("1. Get total issues of one type")
        print("2. Get total solutions of one type")
        print("3. Exit")

        try:
            option = int(input("> "))
        except ValueError:
            print("Input must be an integer ")
            continue

        if option == 1:
            issue_type = convert_issue()
            get_issue(issue_type)
        elif option == 2:
            pass
        elif option == 3:
            break
        else:
            print("Invalid input. Please try again")
            continue

def convert_issue():
    while True:
        print("Select an issue:")
        print("1. Collection Issue")
        print("2. Delivery Issue")
        print("3. Customer Issue")
        print("4. Service Issue")

        try:
            option = int(input("> "))
        except ValueError:
            print("Input must be an integer")
            continue

        if option == 1:
            return "collection_issue"
        elif option == 2:
            return "delivery_issue"
        elif option == 3:
            return "customer_issue"
        elif option == 4:
            return "service_issue"
        else:
            print("Invalid input, please try again")
            continue

def get_issue(issue_type):
    filtered_df = df[df["issue_type"] == issue_type]
    print(filtered_df)

if __name__ == "__main__":
    main()