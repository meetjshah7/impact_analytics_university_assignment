import sys
from university import University

if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
    except IndexError:
        print("Please pass 'no. of days' argument in command line. Hint: `python3 main.py`")
    except ValueError:
        print("Could not pass the argument for to integer. Please ensure the argument 'no. of days' is a number")
    else:
        university = University(days)
        print(university.number_of_ways_to_attend_classes)
        print(f"{university.number_of_ways_to_miss_graduation_ceremony}/{university.number_of_ways_to_attend_classes}")
