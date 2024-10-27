# sum_numbers.py
import os

def read_numbers(file_path):
    """
    Read numbers from a text file and return their sum.

    Parameters:
        file_path (str): The path to the text file containing numbers.

    Returns:
        int: The sum of the numbers in the file, or None if an error occurs.
    """
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            print("File does not exist.")
            return None

        # Open the file and read each line
        with open(file_path, 'r') as file:
            # Convert valid integer lines to a list of numbers
            numbers = []
            for line in file:
                stripped_line = line.strip()
                if stripped_line.isdigit():
                    numbers.append(int(stripped_line))
                else:
                    print(f"Skipping invalid line: '{stripped_line}'")

        # Return the sum of all valid numbers
        return sum(numbers)

    except Exception as e:
        # Print any error encountered during processing
        print("Error:", e)
        return None

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
