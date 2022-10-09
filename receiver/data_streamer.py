from receiver.min_and_max_generator import get_max_and_min_values
from receiver.data_reader import ReceiverDataHandler
from receiver.simple_moving_average_generator import average_of_last_five_values

receiver_obj = ReceiverDataHandler.parameters_with_corresponding_readings()
param_and_readings = receiver_obj.params_and_readings_dict


def stream_min_and_max_readings():
    for param, readings in param_and_readings.items():
        _min, _max = get_max_and_min_values(readings)
        print("{} minimum: {} maximum: {}".format(param, _min, _max))


def stream_sma_of_last_five_readings():
    for param, readings in param_and_readings.items():
        average = average_of_last_five_values(readings)
        print("Simple Moving Average of {} is {}".format(param, average))
