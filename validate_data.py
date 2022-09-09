import os
import logging


def validate_path(path):
    while True:
        if os.path.isdir(path):
            break
        else:
            logging.warning("The path is not found")
            path = input("Enter a new path: ")
    return path


def validate_period(period):
    # period should be a number
    while True:
        try:
            period = float(period)
        except ValueError:
            logging.warning("The period is not a number")
            period = input("Enter a new period: ")
        else:
            break
    return period
