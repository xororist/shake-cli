import click
from cli.utils.functions import get_all_processes_default


@click.group()
def cli():
    pass


@cli.command(name="find")
@click.argument("name", nargs=-1, type=str)
@click.option("-s", "--sort", is_flag=True, help="Sort PIDs before displaying")
@click.option("-c", "--count", is_flag=True, help="Count total of PIDs")
def find(sort, count, name):
    processes = get_all_processes_default()

    if not name:
        display_processes(processes)
        return

    if name:
        for n in name:
            get_process_by_name(processes, n)

    if count:
        count_total_pids(processes)

    if sort:
        list_all_processes_sorted(processes)


def list_all_processes_sorted(processes):
    return sorted(processes, key=lambda x: x.name().lower())


def get_process_by_name(processes, name):
    found_processes = [
        process for process in processes if name.lower() in process.name().lower()
    ]
    if found_processes:
        for process in found_processes:
            click.echo(
                f"[-] Pid: {process.pid} \n"
                f"[-] Name: {process.name()} \n"
                f"[-] Is running: {process.is_running()} \n"
            )
    else:
        print(f"[x] No processes found with name: {name}")


def count_total_pids(processes):
    print(f"Current number of processes running: {len(processes)}")


def display_processes(processes):
    max_pid_length = max(len(str(process.pid)) for process in processes)
    for process in processes:
        print(f"[-] Pid: {process.pid:>{max_pid_length}} | Name: {process.name()}")
