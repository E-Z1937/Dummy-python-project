# sum_numbers.py
import os

def read_numbers(file_path):
    try:
        if not os.path.isfile(file_path):  # Check if the file exists
            print("File does not exist.")
            return None
        
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
        return sum(numbers)
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    file_path = input("Enter the file path of the text file with numbers: ")
    if not file_path.endswith(".txt"):
        print("Please provide a .txt file.")
    else:
        result = read_numbers(file_path)
        if result is not None:
            print("The sum of numbers is:", result)
