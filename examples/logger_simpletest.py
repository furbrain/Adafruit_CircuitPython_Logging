#pylint:disable=undefined-variable,wildcard-import,no-name-in-module
#pylint:disable=no-member

import logging

logger = logging.getLogger('test')

logger.setLevel(logging.ERROR)
logger.info('Info message')
logger.error('Error message')
