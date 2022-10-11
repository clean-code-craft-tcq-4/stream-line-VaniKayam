import io
import sys
from unittest import TestCase
from unittest.mock import patch

from receiver.data_streamer import Streamer


class TestStreamer(TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
        with patch('receiver.data_reader.ReceiverDataHandler.'
                   'parameters_with_corresponding_readings'):
            self.streamer = Streamer()
            self.streamer.params_and_readings_dict = {
                    'Temp': ['20', '40'],
                    'soc': ['40', '20']
            }

    def test_stream_min_and_max_readings(self):
        self.streamer.stream_min_and_max_readings()
        console_output = self.capturedOutput.getvalue()
        self.assertIn("Temp_minimum: 20", console_output)
        self.assertIn("Temp_maximum: 40", console_output)
        self.assertIn("soc_minimum: 20", console_output)
        self.assertIn("soc_maximum: 40", console_output)

    def test_stream_sma_of_last_five_readings(self):
        self.streamer.stream_sma_of_last_five_readings()
        console_output = self.capturedOutput.getvalue()
        self.assertIn("Temp_SMA: 30.0", console_output)
        self.assertIn("soc_SMA: 30.0", console_output)
