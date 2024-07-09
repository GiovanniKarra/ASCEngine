from datetime import datetime


LOG_FILE = "log.log"
ERROR_LOG_FILE = "error.log"


def reset_file(filename):
	with open(filename, "w") as file:
		file.write("")


def reset_log():
	reset_file(LOG_FILE)
	reset_file(ERROR_LOG_FILE)


def log_to_file(message, filename):
	with open(filename, "a") as log_file:
		log_file.write(f"[{datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')}] {message}\n")


def log(message):
	log_to_file(message, LOG_FILE)


def log_error(message):
	log_to_file(message, ERROR_LOG_FILE)