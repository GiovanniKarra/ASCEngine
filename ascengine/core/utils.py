from datetime import datetime


LOG_FILE = "log.log"
ERROR_LOG_FILE = "error.log"

def reset_log():
	log_file = open(LOG_FILE, "w")
	log_file.write("")
	log_file.close()

	error_log_file = open(ERROR_LOG_FILE, "w")
	error_log_file.write("")
	error_log_file.close()


def log(message):
	with open(LOG_FILE, "a") as log_file:
		log_file.write(f"[{datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')}] {message}\n")


def log_error(message):
	with open(ERROR_LOG_FILE, "a") as error_log_file:
		error_log_file.write(f"[{datetime.now().strftime(r'%d/%m/%Y %H:%M:%S')}] {message}\n")
