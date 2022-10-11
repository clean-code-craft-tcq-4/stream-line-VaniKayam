
class ReceiverDataHandler:
    def __init__(self):
        self.params_and_readings_dict = {}

    def parameters_with_corresponding_readings(self):
        console_data = self.read_data_from_console()
        params = self.get_parameters_list(console_data)
        readings = self.get_readings_list(console_data)
        for i in range(len(params)):
            self.params_and_readings_dict.update({params[i]: readings[i]})

    @staticmethod
    def read_data_from_console():
        data = []
        for line in range(0, 51):
            console_output = input()
            data.append(console_output)
        return data

    @staticmethod
    def get_parameters_list(data):
        params = data[0].split(',')
        return params

    @staticmethod
    def get_readings_list(data):
        param_1_readings = []
        param_2_readings = []
        for datum in data[1:]:
            readings = datum.split(',')
            param_1_readings.append(readings[0])
            param_2_readings.append(readings[1])
        return [param_1_readings, param_2_readings]
