import os
import jsonpickle
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('## Event received via API Gateway:T\r' + jsonpickle.encode(event))
    logger.info('## Lambda context:\r' + jsonpickle.encode(context))
    return 'Lambda Invoked: OK'