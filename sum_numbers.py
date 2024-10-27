# sum_numbers.py
import os

# Function to read numbers from a text file and return their sum
def read_numbers(file_path):
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            print("File does not exist.")
            return None

        # Open the file and read each line
        with open(file_path, 'r') as file:
            # Convert valid integer lines to a list of numbers
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
        # Return the sum of all numbers
        return sum(numbers)
    except Exception as e:
        # Print any error encountered during processing
        print("Error:", e)
        return None

# Main execution block
if __name__ == "__main__":
    # Ask user for the path of the file containing numbers
    file_path = input("Enter the file path of the text file with numbers: ")
    
    # Check if the provided file is a .txt file
    if not file_path.endswith(".txt"):
        print("Please provide a .txt file.")
    else:
        # Call the function to calculate the sum and display the result
        result = read_numbers(file_path)
        if result is not None:
            print("The sum of numbers is:", result)
