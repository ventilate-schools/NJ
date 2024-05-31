import os
import re
import statistics
from collections import defaultdict

def extract_grades(file_path):
    """Extract numeric grades from markdown files based on a specific pattern."""
    pattern = r"\*\*School's overall airborne virus protection grade \(0-5\)\*\*: (\d)"
    grades = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                grade = int(match.group(1))
                grades.append(grade)
    return grades

def write_html(file_path, frequencies, where):
    """Write frequency of grades to an HTML file."""
    with open(file_path, 'w') as file:
        file.write('<!-- This file is generated by a Python Script - do not edit it to update numbers please -->\n')
        file.write('<p><b>Ventilation grade breakdown for schools in ' + where + ':</b></p>\n<ul>\n')
        for grade, freq in sorted(frequencies.items()):
            file.write(f'<li>Grade {grade}: {freq}</li>\n')
        file.write('</ul>\n')

def analyze_directory(base_path):
    """Analyze all markdown files in the directory tree starting from base_path."""
    grade_map = defaultdict(list)
    total_grades = []

    # Walk through all files and directories within the base_path
    for root, dirs, files in os.walk(base_path):
        local_grades = []
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                grades = extract_grades(file_path)
                local_grades.extend(grades)
                grade_map[root].extend(grades)
                total_grades.extend(grades)

        if local_grades:
            freq = {grade: local_grades.count(grade) for grade in set(local_grades)}
            write_html(os.path.join(root, 'grade.html'), freq, 'the county/district')

    # Aggregate statistics for the entire directory tree
    if total_grades:
        total_freq = {grade: total_grades.count(grade) for grade in set(total_grades)}
        write_html(os.path.join(base_path, 'grade.html'), total_freq, 'NJ')

# Run the analysis starting from the current directory
analyze_directory(os.getcwd())
