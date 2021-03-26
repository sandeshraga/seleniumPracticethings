import logging

logging.basicConfig(filename="D:\Study material\MS\selenium testing codes\logfile.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt= '%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")


