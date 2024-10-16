# Import modules
import csv
import os

# Load input data
input_file = os.path.join("Resources", "budget_data.csv")

################################## PART #1 ##########################################

# Initialize values
month_count = 0
total_sum = 0
month_of_record = []
MoM_change_list = []

highest_rise = ["", 0] # first element is month, second element is month-over-month change
highest_fall = ["", 9999999999999999999] # first element is month, second element is month-over-month change.  Initially, set a very high value.
        

# Read input data and begin processing
with open(input_file) as input_data:
    reader = csv.reader(input_data)

    # Read the header
    header = next(reader)

    # Deal with first line of data uniquely as it doesn't have a predecessor
    first_line = next(reader)
    month_count += 1
    total_sum += int(first_line[1])
    prev_entry = int(first_line[1])  # since no predecessor, record the first entry as the previous entry

    # Now start looping through the remaining rows to the end
    for row in reader:

        # Continue accumulating months and totals and calculate changes
        month_count += 1
        total_sum += int(row[1])

        # Compute the month-over-month changes
        MoM_change = int(row[1]) - prev_entry
        prev_entry = int(row[1]) # set the current row to prev_entry for the next go-around the loop
        
        # Update the lists
        MoM_change_list += [MoM_change] # add value to the list (and build the list)
        month_of_record += [row[0]] # capture the month value in the list

        # Determine if the current value is higher than the previous highest
        # Determine if the current value is lower than than the previous lowest
        # Keep comparing and record highest rise
        if MoM_change > highest_rise[1]:
            highest_rise[0] = row[0]
            highest_rise[1] = MoM_change

        # Keep comparing and record highest fall
        if MoM_change < highest_fall[1]:
            highest_fall[0] = row[0]
            highest_fall[1] = MoM_change 

################################## PART #2 ##########################################

# Now that monthly changes have been captured along with the highest and lowest changes

# Compute average of changes over the months
MoM_avg = sum(MoM_change_list) / len(MoM_change_list)

# Print Summary
generated_output = (
    f"Budget Analysis Output\n"
    f"----------------------------\n"
    f"Total Count of Months: {month_count}\n"
    f"Total Sum of Changes: ${total_sum}\n"
    f"Average Change: ${MoM_avg:.2f}\n"
    f"Highest Increase: {highest_rise[0]} (${highest_rise[1]})\n"
    f"Highest Fall: {highest_fall[0]} (${highest_fall[1]})\n")


################################## PART #3 ##########################################

# Print to terminal
print(generated_output)

# Set location to output data
output_file = os.path.join("analysis", "budget_data_output.txt")

# Print to file
with open(output_file, "w") as txt_file:
    txt_file.write(generated_output)
