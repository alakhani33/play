import csv
import os

input_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("analysis", "budget_data_output.txt")

month_count = 0
total_sum = 0
months = []
monthly_changes = []

highest_rise = {"month": "", "change": 0}
# highest_rise = {"month": "", "change": -float('inf')}
highest_fall = {"month": "", "change": float("inf")}

with open(input_file) as input_data:
    reader = csv.reader(input_data)
    header = next(reader)

    first_row = next(reader)
    month_count += 1
    total_sum += int(first_row[1])
    previous_value = int(first_row[1])

    for row in reader:
        month_count += 1
        current_value = int(row[1])
        total_sum += current_value

        monthly_change = current_value - previous_value
        previous_value = current_value

        months.append(row[0])
        monthly_changes.append(monthly_change)

        if monthly_change > highest_rise["change"]:
            highest_rise["month"] = row[0]
            highest_rise["change"] = monthly_change

        if monthly_change < highest_fall["change"]:
            highest_fall["month"] = row[0]
            highest_fall["change"] = monthly_change

average_change = sum(monthly_changes) / len(monthly_changes)

output = (
    f"Budget Analysis Output\n"
    f"----------------------------\n"
    f"Total Count of Months: {month_count}\n"
    f"Total Sum of Changes: ${total_sum}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Highest Increase in Profits: {highest_rise['month']} (${highest_rise['change']})\n"
    f"Greatest Decrease in Profits: {highest_fall['month']} (${highest_fall['change']})\n"
)

print(output)

with open(output_file, "w") as txt_file:
    txt_file.write(output)
