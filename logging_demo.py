import logging

# Configure logging
logging.basicConfig(
    filename="app.log",  # Log file path
    level=logging.DEBUG,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)


# Example usage of logging
def main():
    logging.info("Application started")
    try:
        # Your application logic here
        logging.debug("Running application logic")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Application finished")


if __name__ == "__main__":
    main()
