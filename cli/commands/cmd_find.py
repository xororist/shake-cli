import click
import psutil


def cli():
    pass


@click.command(name="find")
@click.option("-n", "--name", help="Get a PID by name")
@click.option("-s", "--sort", is_flag=True, help="Sort PIDs before displaying")
@click.option("-c", "--count", is_flag=True, help="Count total of PIDs")
def find(sort, count, name):
    processes = list_all_processes_default()

    if name:
        return get_process_by_name(processes, name)

    if count:
        return count_total_pids(processes)

    if sort:
        processes = list_all_processes_sorted(processes)

    display_processes(processes)


def list_all_processes_default():
    return list(psutil.process_iter())


def list_all_processes_sorted(processes):
    return sorted(processes, key=lambda x: x.name().lower())


def get_process_by_name(processes, name):
    found_processes = [process for process in processes if process.name() == name]
    if found_processes:
        max_pid_length = max(len(str(process.pid)) for process in found_processes)
        for process in found_processes:
            print(f"[-] pid = {process.pid:>{max_pid_length}} - name = {process.name()}")
    else:
        print(f"[x] No processes found with name: {name}")


def count_total_pids(processes):
    print(f"Current numbers of processes running: {len(processes)}")


def display_processes(processes):
    max_pid_length = max(len(str(process.pid)) for process in processes)
    for process in processes:
        print(f"[-] pid: {process.pid:>{max_pid_length}} | name: {process.name()}")
