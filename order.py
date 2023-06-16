import os
from datetime import datetime, timedelta

# Replace with your directory
dir_path = '.'

# get all md files in the directory
files = [f for f in os.listdir(dir_path) if f.endswith('.md')]

# sort files in ascending order
files.sort()

# result list for new contents
results = []

# Define boundaries
earliest_date = datetime.strptime('2021-01-01', '%Y-%m-%d')
latest_date = datetime.today()

# iterate over files
for i in range(len(files)):
    # get date from file name
    date_str = files[i].split('.')[0]
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    if i == 0: 
        earliest_date = datetime.strptime(files[i].split('.')[0], '%Y-%m-%d')

    # find the next and previous file
    prev_date = date_obj - timedelta(days=1)
    next_date = date_obj + timedelta(days=1)

    # find the closest previous and next files within the boundaries
    while f'{prev_date.strftime("%Y-%m-%d")}.md' not in files:
        if prev_date > earliest_date:
            prev_date -= timedelta(days=1)
        else:
            prev_date = earliest_date
            break
    while f'{next_date.strftime("%Y-%m-%d")}.md' not in files or next_date > latest_date:
        if next_date < latest_date:
            next_date += timedelta(days=1)
        else:
            next_date = latest_date
            break

    # create the new string
    new_str = f'<< [[Daily/{prev_date.strftime("%Y-%m-%d")}|{prev_date.strftime("%a %d %B %Y")}]] | ' \
               f'[[Daily/{next_date.strftime("%Y-%m-%d")}|{next_date.strftime("%a %d %B %Y")}]] >>'

    # append the file name and the new string to the results
    results.append((files[i], new_str))

    # Modify the actual file
    with open(os.path.join(dir_path, files[i]), 'r') as file:
        lines = file.readlines()

    # Check if the line exists
    daily_line_index = None
    for index, line in enumerate(lines):
        if line.startswith('<< [[Daily'):
            daily_line_index = index
            break
        elif line.startswith('*Daily Note*'):
            daily_line_index = index + 1

    if daily_line_index is not None:
        lines[daily_line_index] = new_str + '\n'
    else:
        # Append new_str if the '*Daily Note*' or '<< [[Daily' line doesn't exist
        lines.append(new_str + '\n')

    # Write the modified content back to the file
    with open(os.path.join(dir_path, files[i]), 'w') as file:
        file.writelines(lines)

# output the result to a tsv file
with open('output.tsv', 'w') as f:
    for res in results:
        f.write(f'{res[0]}\t{res[1]}\n')
