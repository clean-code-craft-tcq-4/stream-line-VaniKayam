import io
import sys
from unittest import TestCase
from unittest.mock import patch


class TestStreamer(TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
        with patch('receiver.data_reader.ReceiverDataHandler'):
            import receiver.data_streamer as streamer
            streamer.param_and_readings = {
                'Temp': ['20', '40'],
                'soc': ['40', '20']
            }
            self.streamer = streamer

    def test_stream_min_and_max_readings(self):
        self.streamer.stream_min_and_max_readings()
        console_output = self.capturedOutput.getvalue()
        self.assertIn("Temp minimum: 20 maximum: 40", console_output)
        self.assertIn("soc minimum: 20 maximum: 40", console_output)

    def test_stream_sma_of_last_five_readings(self):
        self.streamer.stream_sma_of_last_five_readings()
        console_output = self.capturedOutput.getvalue()
        self.assertIn("Simple Moving Average of Temp is 30.0", console_output)
        self.assertIn("Simple Moving Average of soc is 30.0", console_output)
