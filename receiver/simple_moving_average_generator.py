def get_last_five_readings(readings):
    return readings[-5:]


def convert_readings_to_int(readings):
    int_readings = []
    for reading in readings:
        int_readings.append(int(reading))
    return int_readings


def average_of_last_five_values(values):
    readings = get_last_five_readings(values)
    converted_readings = convert_readings_to_int(readings)
    average = sum(converted_readings) / len(converted_readings)
    return average
