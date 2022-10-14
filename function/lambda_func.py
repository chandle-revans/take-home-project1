import os
import json
import logging
import socket
import ssl
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    host = event["host"]
    days = event["days"]
    
    logger.info('SSL Check host: %s with %s days cushion',  host, days)
    exp_time = get_ssl_expire_time(host)
    return { 'status': 200, 'expires': json.dumps(exp_time) }

def get_ssl_expire_time(host):
    context = ssl.create_default_context()
    with socket.create_connection((host, 443)) as sock:
        with context.wrap_socket(sock, server_hostname = host) as ssock:
            ssl_info = ssock.getpeercert()
    
    expireTime = ssl_info['notAfter']
    ssl_date_format = r'%b %d %H:%M:%S %Y %Z'
    return datetime.datetime.strptime(expireTime, ssl_date_format)