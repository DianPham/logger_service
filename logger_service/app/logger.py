from datetime import datetime
import logging.handlers
import logging
import os

class ServiceLogger:
    def __init__(self, service_name, log_level=logging.INFO):
        self.service_name = service_name
        self.log_level = log_level
        self.logger = None
        self.setup_logger()

    def setup_logger(self):
        # Create logs directory if it doesn't exist
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create logger
        self.logger = logging.getLogger(self.service_name)
        self.logger.setLevel(self.log_level)

        # Prevent duplicate handlers
        if self.logger.handlers:
            return

        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s'
        )
        console_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(message)s'
        )

        # File handler (with rotation)
        log_file = os.path.join(log_dir, f'{self.service_name}_{datetime.now().strftime("%Y%m%d")}.log')
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(self.log_level)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(self.log_level)

        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger