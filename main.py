#!/usr/bin/env python
'''Main'''
import sys
import yaml
import logging
import logging.config
from pprint import pprint
import server

CONFIG = None
LOGGER = None

def main():
    '''main'''
    config = _init_config()
    logger = _init_logger(config)
    _init_server(config, logger)

def _init_config():
    '''inits config'''
    config = None
    with open("config.yaml", "r") as config_file_stream:
        config = yaml.load(config_file_stream)
    return config

def _init_logger(config):
    '''inits logger'''
    log_settings = config["logging"]
    logging.config.dictConfig(log_settings)
    return logging.getLogger()

def _init_server(config, logger):
    '''inits server'''
    logger.info("Starting Chevir v0.1")
    logger.info("ffmpeg settings: " + str(config["ffmpeg"]))
    logger.info("rabbitmq_server: " + config["rabbitmq_server"])
    chevir_server = server.Server(logger, config)
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            if len(sys.argv) >= 3:
                chevir_server.publish_test_message(sys.argv[2])
            else:
                print("Please specify a test video file to encode.") 
        elif sys.argv[1] == "start":
            chevir_server.start_listening()
    else:
        print("Please specify a command (start or test).")

if __name__ == "__main__":
    main()
