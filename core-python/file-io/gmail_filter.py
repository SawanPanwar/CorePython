import re
import os


def readLine():
    base_dir = os.path.dirname(__file__)  # Get current script directory
    input_path = os.path.join(base_dir, "..", "files", "gmail.txt")
    output_path = os.path.join(base_dir, "..", "files", "correct_gmail.txt")

    input_file = open(input_path, 'r')
    output_file = open(output_path, "w")

    for line in input_file:
        if (re.search("@gmail.com", line)):
            output_file.write(line)
    input_file.close()
    output_file.close()


readLine()
