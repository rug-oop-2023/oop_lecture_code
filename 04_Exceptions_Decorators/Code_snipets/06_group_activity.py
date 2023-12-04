def calculate_average(scores):
    try:
        total = sum(scores)
        count = len(scores)
        average = total / count
        print(f"The average score is: {average}")
    except ZeroDivisionError:
        print("You can not provide an empty list")
    except TypeError:
        print('The list should only contain numbers')

# Example data
scores_data = [95, 85, 75, '90', None, 80]
calculate_average(scores_data)

scores_data = []
calculate_average(scores_data)
