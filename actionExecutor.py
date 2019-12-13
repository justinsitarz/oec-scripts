import requests
import json
import argparse
import logging
import sys

from requests.auth import HTTPBasicAuth

# interpret data sent from Opsgenie #
parser = argparse.ArgumentParser()
parser.add_argument('-payload', '--queuePayload', help='Payload from queue', required=True)
parser.add_argument('-apiKey', '--apiKey', help='The apiKey of the integration', required=True)
parser.add_argument('-opsgenieUrl', '--opsgenieUrl', help='The url', required=True)
parser.add_argument('-logLevel', '--logLevel', help='Level of log', required=True)

# args contains everything sent from Opsgenie payload, apiKey, OpsgenieURL, loglevel #
args = vars(parser.parse_args())


api_headers = {'Content-Type': 'application/json'}
url = '<url to post to>'

def main():
   global LOG_PREFIX
   global queue_message
   global timeout

   # queue_message is the variable that contains the alert info (i.e. the queuePayload) # 
   queue_message_string = args['queuePayload']
   queue_message = json.loads(queue_message_string)

   bodytopost = json.dumps(queue_message)
   for x in queue_message:
       logging.debug(x)
   req = requests.post(url, data = bodytopost, headers = api_headers)

if __name__ == '__main__':
    main()
