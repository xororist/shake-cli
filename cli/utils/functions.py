import psutil


def get_all_processes_default():
    return list(psutil.process_iter())


def format_memory(memory_usage):
    return f"{memory_usage / (1024 * 1024):.3f} MB"


def format_bytes(byte_value):
    # Convert bytes to appropriate unit (KB, MB, GB, etc.)
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if byte_value < 1024.0:
            break
        byte_value /= 1024.0
    return f"{byte_value:.2f} {unit}"
