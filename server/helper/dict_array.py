
def check_last_time(array_of_arrays, time, session_id):
    for element in array_of_arrays:
        if session_id == element[0]:
            if time.minute == element[1].minute:
                return False
    return True
