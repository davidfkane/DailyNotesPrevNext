# Daily Note Link Update Script

This Python script is designed to process a set of markdown files, each named with a date in the format 'YYYY-MM-DD.md'. The script updates a specific line in each markdown file to reflect the correct chronological linking to the previous and next markdown files, based on their names.

## What does the script do?

The script does the following:

1. It collects all the markdown (.md) files from a specified directory.
2. It determines the date from the filename of each .md file.
3. It finds the chronologically next and previous file for each .md file.
4. In each .md file, it locates a line starting with '<< [[Daily'. If such a line is found, it replaces the line with a new string reflecting the correct previous and next files. If the line doesn't exist but a line starting with '*Daily Note*' is found, it adds the new line below this line. If neither line exists, it appends the new line to the end of the file.
5. It writes the new content back into each .md file.
6. It logs all the changes made into a tab-separated file 'output.tsv'.

## How to Use

1. Ensure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Navigate to the script's directory via your terminal.
4. Replace `'.'` in the script with your target directory path if the script and the .md files are not in the same directory.
5. Run the script using the command `python filename.py` (replace 'filename.py' with the actual script filename).

Please note that this script was designed to work on a specific type of markdown file structure, as described above. You might need to adjust the script to match your specific markdown file structure.

## License

This project is licensed under the terms of the MIT license.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer

Please ensure you have backups of your files before running the script. The script directly modifies the content of your files. Although it's been tested and found to work as expected, it's always a good idea to keep backups when running a new script on your files.

## Contact

If you have any questions, issues, or suggestions, please open an issue in this repository.
