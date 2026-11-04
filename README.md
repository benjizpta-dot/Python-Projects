# Python Fundamentals

A collection of Python learning exercises covering algorithms, strings, file
handling, dates, and object-oriented programming. These are small practice
programs, with runnable demonstrations of each topic.

## Explore the exercises

| Topic | Example | What it demonstrates |
| --- | --- | --- |
| Algorithms | [Check order](algorithms/check_order.py) | Detect ascending, descending, or unordered sequences |
| Strings | [Count first-character repeats](strings/count_first_character_repeats.py) | Case-insensitive counting after the first character |
| Dates | [Age calculator](dates/age_calculator.py) | Calendar-aware age calculation and input validation |
| File handling | [Sort countries](file_handling/sort_countries.py) | Read, normalize, sort, and write text data |
| File handling | [Write presidents](file_handling/write_presidents.py), [read presidents](file_handling/read_presidents.py) | Write and read a shared text file |
| File handling | [Write odd numbers](file_handling/write_odd_numbers.py) | Generate numbers and save text output |
| Objects | [Shape attributes](object_oriented/shape_attributes/geometric_shape.py) | Inheritance, encapsulation, and string representations |
| Objects | [Shape measurements](object_oriented/shape_measurements/geometric_shape.py) | Circle and rectangle area/perimeter methods |
| Objects | [People and students](object_oriented/people/person.py) | Inheritance and comparison by student ID |

The two shape examples are separate exercises with different constructors and
methods. Each has its own demo and should be run separately.

## Setup

Use Python 3.10 or newer. From the repository folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

On macOS/Linux, use `python3 -m venv .venv` and `.venv/bin/python` instead.
Only the age calculator needs the external `python-dateutil` package; the other
exercises use Python's standard library.

## Run examples

From the repository folder on Windows:

```powershell
.\.venv\Scripts\python.exe algorithms/check_order.py
.\.venv\Scripts\python.exe strings/count_first_character_repeats.py
.\.venv\Scripts\python.exe dates/age_calculator.py
.\.venv\Scripts\python.exe file_handling/read_presidents.py
.\.venv\Scripts\python.exe file_handling/write_presidents.py
.\.venv\Scripts\python.exe file_handling/write_odd_numbers.py
.\.venv\Scripts\python.exe file_handling/sort_countries.py
.\.venv\Scripts\python.exe object_oriented/shape_attributes/demo.py
.\.venv\Scripts\python.exe object_oriented/shape_measurements/demo.py
.\.venv\Scripts\python.exe object_oriented/people/demo.py
```

`check_order` returns `1` for ascending, `-1` for descending, and `0` for
unordered sequences. Equal-valued, empty, and single-item sequences return `1`.
The string exercise prints `0` for `Benji` and `4` for `DDDDD`: the first
character itself is excluded from the count.

File paths are resolved beside each file-handling script, so those scripts also
work when launched from another folder. `sort_countries.py` overwrites the
tracked sample `countries.txt` with sorted, one-per-line names and accepts commas
or line breaks as input. `write_presidents.py` overwrites the tracked sample
`data.txt`. `write_odd_numbers.py` creates an ignored `odds.txt` containing odd
numbers from 1 through 99.
