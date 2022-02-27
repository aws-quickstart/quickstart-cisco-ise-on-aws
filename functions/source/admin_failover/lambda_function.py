import os
import requests
import boto3
import botocore
import logging
import json
import sys
import threading

from botocore.exceptions import ClientError

logging.basicConfig(stream = sys.stdout)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main(event, context):
    # This lambda function applies the configuration of the Primary PSN to the Secondary PSN when the LB detects a healthcheck failure

    try:
        logger.info('Lambda Execution: Executed on event {0}'.format(event))
        # write your code logic here
        print("Hello World")
    except Exception as e:
        logging.error('Exception: %s' % e, exc_info=True)

if __name__ == "__main__":   
    main('', '')
