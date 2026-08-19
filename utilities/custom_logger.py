import logging

class log_maker:
    @staticmethod
    def log():
        logging.basicConfig(filename=".\\logs\\Automation.log", format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger