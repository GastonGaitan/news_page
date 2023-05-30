import datetime
import os

def new_day_call_api():
    """
    The new_day_call_api function checks if the date in the file is different from today's date.
    If it is, then it updates the file with today's date and returns True. If not, then it returns False.
    
    :return: True if the file content is different from today's date
    :doc-author: Trelent
    """
    today = datetime.date.today().strftime("%Y-%m-%d")
    if not os.path.exists('date.txt'):
        with open("date.txt", "w") as date_file:
            date_file.write(today)
    with open('date.txt', 'r') as date_file:
        file_content = date_file.read()
        if file_content != today:
            with open("date.txt", "w") as date_file:
                date_file.write(today)
            return True
        else:
            return False