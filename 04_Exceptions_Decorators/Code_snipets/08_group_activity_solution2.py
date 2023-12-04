class Unsummable:
    def __iter__(self):
        raise RuntimeError("This object cannot be iterated")

def calculate_average(scores):
    try:
        total = sum(scores)
        count = len(scores)
        average = total / count
        print(f"The average score is: {average}")
    except TypeError:
        print("Error: Non-numeric values found in the scores list.")
    except ZeroDivisionError:
        print("Error: Cannot calculate average - no scores provided.")

# Example data
scores_data = [95, 85, 75, '90', None, 80]
# scores_data = []
scores_data = Unsummable()

try:
    calculate_average(scores_data)
except Exception as e:
    print(f"An error occurred: {e}")