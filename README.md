# University Analytics Pandas Project Dataset

Use these files for the University Student Performance & Analytics System.

Files:
- data/students.csv
- data/courses.csv
- data/marks.csv
- data/attendance.csv
- data/fees.csv
- data/activities.csv
- university_source_data.xlsx

The dataset intentionally contains some data-quality problems:
- duplicate student record
- missing values
- inconsistent text formatting
- an invalid attendance record
- mixed realistic values

Suggested workflow:
1. Load all files with Pandas.
2. Inspect shape, columns, dtypes and missing values.
3. Clean and validate the datasets.
4. Merge the datasets.
5. Calculate marks, grades, attendance percentage and fee dues.
6. Perform department/course/semester analysis.
7. Create rankings and academic-risk detection.
8. Export a multi-sheet Excel report.

Do not manually fix the deliberately introduced issues before starting; use Pandas to detect and fix them.
