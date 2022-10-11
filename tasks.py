import os

import click

from StreamLine_Sender import ReadSensorReadings
from receiver.data_streamer import Streamer

cli = click.Group()


@cli.command()
def min_max_and_sma():
    """
    Prints Min and Max and SMA of received sensor readings
    """
    streamer = Streamer()
    streamer.stream_min_and_max_readings()
    streamer.stream_sma_of_last_five_readings()


@cli.command()
def sensor_readings():
    """
    Prints the readings from sensors
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readings_file_path = os.path.join(script_dir, 'SensorParameterReadings.csv')
    ReadSensorReadings(readings_file_path)


if __name__ == '__main__':
    cli()
