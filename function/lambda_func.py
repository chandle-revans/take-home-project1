import os
import json
import logging
import socket
import ssl
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Expired(Exception):
    pass

def lambda_handler(event, context):
    host = event["host"]
    days = event["days"]
    
    logger.info('SSL Check host: %s with %s days cushion',  host, days)
    
    try:
        is_expiring = is_ssl_cert_expiring(host, days)
        if is_expiring:
            return { 'status': 200, 'certExpStatus': 'expiring' }
        else:
            return { 'status': 200, 'certExpStatus': 'valid' }
    except Expired as ex:
        logger.error('Certificate for host: %s is expired', host)
        return { 'status': 200, 'certExpStatus': 'expired' }
    except Exception as ex:
        logger.error('An error has occurred. Unable to retrieve certificate expiration info for host: %s', host)
        return { 'status': 500, 'certExpStatus': 'unknown' }

def get_ssl_expire_time(host):
    context = ssl.create_default_context()
    with socket.create_connection((host, 443)) as sock:
        with context.wrap_socket(sock, server_hostname = host) as ssock:
            ssl_info = ssock.getpeercert()
    
    expire_time = ssl_info['notAfter']
    ssl_date_format = r'%b %d %H:%M:%S %Y %Z'
    return datetime.datetime.strptime(expire_time, ssl_date_format)

def get_ssl_remaining_time(host):
    expires = get_ssl_expire_time(host)
    logger.debug('SSL cert for %s expires at %s', host, expires.isoformat())
    return expires - datetime.datetime.utcnow()
    
def is_ssl_cert_expiring(host, days):
    remaining = get_ssl_remaining_time(host)

    if remaining < datetime.timedelta(days=0):
        raise Expired("SSL Cert for host %s expired %s days ago" % (host, remaining.days))
    elif remaining < datetime.timedelta(days=days):
        logger.warning('SSL Cert for host %s expires in %s days', host, remaining.days)
        return True
    else:
        return False
