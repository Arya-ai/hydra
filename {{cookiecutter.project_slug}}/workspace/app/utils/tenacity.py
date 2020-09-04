"""
Custom Tencity Methods to handle Loguru loggers
"""
from tenacity import _utils


def custom_before_log(resource_name, logger, log_level):
    """Before call strategy that logs to some logger the attempt."""

    def log_it(retry_state):
        log_message = f"Starting call to `{resource_name}`, this is " \
                      f"the {_utils.to_ordinal(retry_state.attempt_number)} time calling it "
        logger.log(log_level.name, log_message)

    return log_it


def custom_after_log(resource_name, logger, log_level):
    """After call strategy that logs to some logger the finished attempt."""

    def log_it(retry_state):
        log_message = f"Finished call to `{resource_name}` after " \
                      f"{retry_state.seconds_since_start:0.3f}(s), this was " \
                      f"the {_utils.to_ordinal(retry_state.attempt_number)} time calling it"
        logger.log(log_level.name, log_message)

    return log_it
