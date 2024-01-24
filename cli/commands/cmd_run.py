import click
import time
import psutil
from cli.utils.functions import format_memory, format_bytes

@click.group()
def cli():
    pass

@cli.command()
@click.argument("pid", type=int)
@click.option(
    "-r", "--reset", type=float, help="Time between each refresh", default=0.5
)
def run(pid, reset):
    try:
        while True:
            processes = psutil.process_iter(
                attrs=["pid", "name", "cpu_percent", "memory_info", "memory_percent"]
            )
            display_process_info(pid, processes)
            display_internet_info(pid)
            time.sleep(reset)
    except KeyboardInterrupt:
        click.echo("\nAborted!")

def display_process_info(target_pid, processes):
    for proc in processes:
        if proc.info["pid"] == target_pid:
            formatted_memory_usage = format_memory(proc.info["memory_info"].rss)
            formatted_cpu = f"{proc.info['cpu_percent']:.2f}%"
            click.clear()
            click.echo(
                f"[-] Name: {proc.info['name'].capitalize()} \n"
                f"[-] Memory Usage: {formatted_memory_usage} \n"
                f"[-] CPU Usage: {formatted_cpu} \n",
                nl=False,
            )

def display_internet_info(pid):
    try:
        proc = psutil.Process(pid)
        io = proc.io_counters()
        bytes_sent, bytes_recv = io.write_bytes, io.read_bytes
        packets_sent, packets_recv = io.write_count, io.read_count
        click.echo(
            f"\n[Network Usage] \n"
            f"[-] Bytes Sent: {format_bytes(bytes_sent)} \n"
            f"[-] Bytes Received: {format_bytes(bytes_recv)} \n"
            f"[-] Packets Sent: {packets_sent} \n"
            f"[-] Packets Received: {packets_recv} \n",
            nl=False,
        )
    except psutil.NoSuchProcess:
        click.echo(f"Process with PID {pid} not found.")
