from receiver.min_and_max_generator import get_max_and_min_values
from receiver.data_reader import ReceiverDataHandler
from receiver.simple_moving_average_generator import average_of_last_five_values


class Streamer(ReceiverDataHandler):
    def __init__(self):
        super().__init__()
        self.parameters_with_corresponding_readings()

    def stream_min_and_max_readings(self):
        for param, readings in self.params_and_readings_dict.items():
            _min, _max = get_max_and_min_values(readings)
            print("{}_minimum: {}".format(param, _min))
            print("{}_maximum: {}".format(param, _max))

    def stream_sma_of_last_five_readings(self):
        for param, readings in self.params_and_readings_dict.items():
            average = average_of_last_five_values(readings)
            print("{}_SMA: {}".format(param, average))
