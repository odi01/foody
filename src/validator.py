from config import USER_PROFILE_NAME, USER_AGE, USER_BALANCE
import structlog


log = structlog.get_logger()

# todo: check when the zero balance isn't working


def is_valid_user(api_input_data: dict) -> bool:
    is_valid = []
    if api_input_data.get(USER_PROFILE_NAME, []):
        if api_input_data[USER_PROFILE_NAME] is not None and type(api_input_data[USER_PROFILE_NAME]) is str:
            is_valid.append(True)

    if api_input_data.get(USER_AGE, []):
        if api_input_data[USER_AGE] is not None and type(api_input_data[USER_AGE]) is int:
            is_valid.append(True)

    if api_input_data.get(USER_BALANCE):
        balance = api_input_data[USER_BALANCE]
        if (balance is not None) and (type(balance) in [float, int]) and (balance >= 0):
            is_valid.append(True)

    if len(is_valid) != 3:
        log.warning("invalid user")
        return False

    log.info("Valid user")
    return True
