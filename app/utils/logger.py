import logging
from logging.handlers import RotatingFileHandler
import os

def set_up_logging(app):
    log_file_path = os.path.abspath(app.config['log_file'])
    if not os.path.exists(log_file_path):
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    handler = RotatingFileHandler(app.config['log_file'], maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)