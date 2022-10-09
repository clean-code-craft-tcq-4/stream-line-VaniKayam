import click

from receiver import data_streamer

cli = click.Group()


@cli.command()
def min_max():
    """
    Prints Minimum and Maximum readings from Sensors
    """
    data_streamer.stream_min_and_max_readings()


@cli.command()
def sma():
    """
    Prints SMA of the Sensors readings
    """
    data_streamer.stream_sma_of_last_five_readings()


@cli.command()
@click.pass_context
def min_max_and_sma(ctx):
    """
    Prints both Minimum and Maximum readings and SMA from Sensors
    """
    ctx.invoke(min_max)
    ctx.invoke(sma)


if __name__ == '__main__':
    cli()
