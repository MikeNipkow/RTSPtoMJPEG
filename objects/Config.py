import logging
import os.path
from configparser import ConfigParser


class Config:
    config_path: str = None
    config: ConfigParser = ConfigParser()

    def __init__(self, config_path):
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_path):
            logging.warning(f"Failed to load config file: {self.config_path}")
            return False

        self.config.read(self.config_path)

    def camera_stream_link(self):
        return self.config.get("Camera", "Stream-URL")

    def camera_refresh_rate(self):
        return self.config.getfloat("Camera", "Refresh-Rate")


