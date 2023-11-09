import logging
import configparser

def configure_logging_from_file():
    try:
        # Read the logger configuration from file
        config = configparser.ConfigParser()
        config.read('/app/data/logger.conf')

        print("Logger configuration file successfully read.")

        # Create a logger using the configuration
        logger = logging.getLogger('myLogger')

        # Set the level for the logger
        logger.setLevel(logging.getLevelName(config.get('logger_myLogger', 'level')))

        # Create a file handler instead of SysLogHandler
        log_file_path = config.get('handler_fileHandler', 'args')
        file_handler = logging.FileHandler(log_file_path)
        
        # Set the level for the file handler
        file_handler.setLevel(logging.getLevelName(config.get('handler_fileHandler', 'level')))

        # Create a formatter
        formatter = logging.Formatter(
            config.get('formatter_simpleFormatter', 'format'),
            datefmt=config.get('formatter_simpleFormatter', 'datefmt')
        )

        # Set the formatter for the file handler
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        return logger

    except (configparser.Error, FileNotFoundError) as e:
        # If the configuration file cannot be read, configure basic logging
        logging.basicConfig(level=logging.DEBUG)
        logging.warning(f"Failed to read logger configuration file: {str(e)}")
        logging.warning("Configuring basic logging.")
        return logging.getLogger()
