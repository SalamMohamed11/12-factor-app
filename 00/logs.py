import logging

Logger = logging.getLogger(__name__)
Logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()

# FIXED: Added the missing hyphen before %(levelname)s
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)
Logger.addHandler(console_handler)