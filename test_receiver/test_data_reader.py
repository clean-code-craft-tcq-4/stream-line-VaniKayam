from unittest import TestCase
from unittest.mock import patch
from receiver.data_reader import ReceiverDataHandler


class TestDataReader(TestCase):
    def setUp(self):
        self.console_out = ['Temp,soc', '20,40', '40,20']

    def test_parameters_with_corresponding_readings(self):
        with patch('receiver.data_reader.ReceiverDataHandler.'
                   'read_data_from_console',
                   return_value=self.console_out):
            obj = ReceiverDataHandler()
            obj.parameters_with_corresponding_readings()
        self.assertEqual(obj.params_and_readings_dict, {'Temp': ['20', '40'],
                                                        'soc': ['40', '20']})

    def test_get_parameters_list(self):
        receiver_obj = ReceiverDataHandler()
        params_list = receiver_obj.get_parameters_list(self.console_out)
        self.assertEqual(['Temp', 'soc'], params_list)

    def test_get_readings_list(self):
        receiver_obj = ReceiverDataHandler()
        readings_list = receiver_obj.get_readings_list(self.console_out)
        self.assertEqual([['20', '40'], ['40', '20']], readings_list)
