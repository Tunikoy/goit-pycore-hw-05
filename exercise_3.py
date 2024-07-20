import sys
import re
from typing import List, Dict, Callable

def parse_log_line(line: str) -> Dict[str, str]:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level.ljust(16)} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"No logs found for level: {level.upper()}")

if __name__ == "__main__":
    main()
    
# Виведення конкретного рівна логування python3 exercise_3.py /Users/a1234/Projects/vscode-basics/goit-pycore-hw-05/logs/logfile.log ERROR
