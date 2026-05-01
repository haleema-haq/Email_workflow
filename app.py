import os

def main():
    print("1. Ingest Emails")
    print("2. Query Emails")

    choice = input("Choose option: ")

    if choice == "1":
        os.system("python ingest.py")

    elif choice == "2":
        os.system("python query.py")

if __name__ == "__main__":
    main()