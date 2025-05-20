import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

def main():
    while True:
        print("1. Get issue distribution for one issue type")
        print("2. Get total parcels for one issue type")
        print("3. Exit")

        try:
            option = int(input("> "))
        except ValueError:
            print("Input must be an integer ")
            continue

        if option == 1:
            issue_type = convert_issue()
            get_issue_data(issue_type)
        elif option == 2:
            issue_type = convert_issue()
            get_total_parcels(issue_type)
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

def get_issue_data(issue_type):
    issue_type_df = df[df["issue_type"] == issue_type]
    filtered_df = df[df["issue_type"] != issue_type]

    data = [len(issue_type_df),len(filtered_df)]

    formatted_label = issue_type.replace("_"," ").title()
    labels = [f"Contains {formatted_label}",f"Does not contain {formatted_label}"]

    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.title("Distribution of Issue Types")
    plt.show()

    print("\n",issue_type_df)

def get_total_parcels(issue_type):
    filtered_df = df[df["issue_type"] == issue_type]
    grouped = filtered_df.groupby("solution_type")["number_of_parcels"].sum()

    formatted_label = issue_type.replace("_"," ").title()

    plt.bar(grouped.index,grouped.values)
    plt.title(f"Total Parcel Distribution for {formatted_label}")
    plt.xlabel("Solution Types")
    plt.ylabel("Parcels")
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    main()