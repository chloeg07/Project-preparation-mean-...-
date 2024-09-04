#Write program in python using functions to calculate the following:
#1. Mean 2. Median 3. Mode 4. Frequency 5. Top 5 numbers 6. Last 5 numbers
#from a list of up to 20 numbers entered by the user. The user should be able to choose by menu, wwhich option to run. Create a test set of data to input and check the output is as expected.
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    if len(modes) == 1:
        return modes[0]
    else:
        return "No unique mode found."

def calculate_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

def top_5_numbers(numbers):
    return sorted(numbers, reverse=True)[:5]

def last_5_numbers(numbers):
    return sorted(numbers[-5:])

def display_menu():
    print("\nMenu:")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Calculate Mode")
    print("4. Calculate Frequency")
    print("5. Show Top 5 Numbers")
    print("6. Show Last 5 Numbers")
    print("7. Exit")

def main():
    # Get user input for the list of up to 20 numbers
    user_input = input("Enter up to 20 numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    if len(numbers) > 20:
        print("Error: Please enter 20 numbers or fewer.")
        return

    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            print(f"Mean: {calculate_mean(numbers)}")
        elif choice == "2":
            print(f"Median: {calculate_median(numbers)}")
        elif choice == "3":
            print(f"Mode: {calculate_mode(numbers)}")
        elif choice == "4":
            frequency = calculate_frequency(numbers)
            print("Frequency:")
            for num, freq in frequency.items():
                print(f"{num}: {freq} times")
        elif choice == "5":
            print(f"Top 5 Numbers: {top_5_numbers(numbers)}")
        elif choice == "6":
            print(f"Last 5 Numbers (Sorted): {last_5_numbers(numbers)}")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
