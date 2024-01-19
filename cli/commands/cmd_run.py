import click
import time
import psutil
from cli.utils.functions import format_memory


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
