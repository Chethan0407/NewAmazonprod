import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a logs directory if it doesn't exist
log_dir = "/Users/chethangopal/Desktop/AmazonAutomation/Logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = os.path.join(log_dir, 'Automation.log')

fh = logging.FileHandler(log_file_path, mode='a')  # Append mode ('a') to append logs
fh.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt="%y-%d-%m %H:%M:%S %p")

fh.setFormatter(formatter)

# console handler
# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Add file handler to the logger
logger.addHandler(fh)
ch.setFormatter(formatter)
logger.addHandler(ch)


def take_screenshots_on_failure(driver, failure_screenshots):
    screenshot_dir = os.path.join(log_dir, 'FailedTest_PageScreenshots')
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_path = os.path.join(screenshot_dir, f'{failure_screenshots}_{timestamp}.png')

    try:
        driver.save_screenshot(screenshot_path)
        logger.info(f'screenshot_saved: {screenshot_path}')
    except Exception as e:
        logger.error(f'failed to take screenshot as :{e}')

    return screenshot_path


def configure_logger():
    return logger
