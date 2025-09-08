def print_file_content(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Файл не найден")

def non_closed_files(files):
    return list(filter(lambda x: not x.closed, files))

def log_for(logfile: str, date_str: str):
    with (
        open(logfile, 'r', encoding="utf8") as in_file,
        open(f'log_for_{date_str}.txt', 'w', encoding='utf8') as out_file
    ):
        for line in in_file:
            if line.startswith(date_str):
                out_file.write(line.split(f"{date_str} ")[1])