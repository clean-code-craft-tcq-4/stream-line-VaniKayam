def read_data_from_console():
    data = []
    for line in range(0, 51):
        console_output = input()
        data.append(console_output)
    return data


class ReceiverDataHandler:
    def __init__(self):
        self.console_data = read_data_from_console()
        self.params_and_readings_dict = {}

    @classmethod
    def parameters_with_corresponding_readings(cls):
        cls_obj = ReceiverDataHandler()
        params = cls.get_parameters_list(cls_obj)
        readings = cls.get_readings_list(cls_obj)
        for i in range(len(params)):
            cls_obj.params_and_readings_dict.update({params[i]: readings[i]})
        return cls_obj

    def get_parameters_list(self):
        params = self.console_data[0].split(',')
        return params

    def get_readings_list(self):
        param_1_readings = []
        param_2_readings = []
        for readings in self.console_data[1:]:
            readings = readings.split(',')
            param_1_readings.append(readings[0])
            param_2_readings.append(readings[1])
        return [param_1_readings, param_2_readings]
