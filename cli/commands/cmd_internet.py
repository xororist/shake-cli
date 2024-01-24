import click
import psutil
import time
from cli.utils.functions import format_bytes

@click.group()
def cli():
    pass

@cli.command(name="internet")
@click.argument("pid", type=int)
@click.option(
    "-r", "--reset", type=float, help="Time between each refresh", default=0.5
)
def internet(pid, reset):
    try:
        while True:
            proc = psutil.Process(pid)
            io = proc.io_counters()
            bytes_sent, bytes_recv = io.write_bytes, io.read_bytes
            packets_sent, packets_recv = io.write_count, io.read_count
            # clear the screen
            click.clear()
            # print the stats in a nice format
            click.echo(
                f"[-] Pid: {pid} \n"
                f"[-] Name: {proc.name()} \n"
                f"[-] Bytes Sent: {format_bytes(bytes_sent)} \n"
                f"[-] Bytes Received: {format_bytes(bytes_recv)} \n"
                f"[-] Packets Sent: {packets_sent} \n"
                f"[-] Packets Received: {packets_recv} \n",
                nl=False,
            )
            # wait for the reset time
            time.sleep(reset)
    except KeyboardInterrupt:
        click.echo("\nAborted!")
