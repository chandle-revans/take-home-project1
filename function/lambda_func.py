import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    host = event["host"]
    days = event["days"]
    
    logger.info('SSL Check host: %s with %s days cushion',  host, days)
    return 'Ok'