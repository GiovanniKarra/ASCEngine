from datetime import datetime


def reset_log():
    log_file = open("log.txt", "w")
    log_file.write("")
    log_file.close()

    error_log_file = open("errorlog.txt", "w")
    error_log_file.write("")
    error_log_file.close()


def log(message):
    log_file = open("log.txt", "a")
    log_file.write(f"[{datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')}] {message}\n")
    log_file.close()


def log_error(message):
    error_log_file = open("errorlog.txt", "a")
    error_log_file.write(f"[{datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')}] {message}\n")
    error_log_file.close()
