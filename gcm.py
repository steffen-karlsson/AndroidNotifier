#
# Created by steffenkarlsson on 8/18/16.
#

from argparse import ArgumentParser
from io import BytesIO
from json import loads, dumps
from pprint import pprint
from pycurl import Curl
from os import environ

API_ACCESS_KEY = None
REGISTRATION_IDS = []


def send_notification(title, message, should_vibrate, use_sound):
    curl_msg = {
        'title': title,
        'message': message,
        'vibrate': int(should_vibrate),
        'sound': int(use_sound)
    }

    fields = {
        'registration_ids': REGISTRATION_IDS,
        'data': curl_msg
    }

    headers = [
        'Authorization: key=%s' % API_ACCESS_KEY,
        'Content-Type: application/json'
    ]

    b = BytesIO()
    c = Curl()
    c.setopt(c.URL, 'https://android.googleapis.com/gcm/send')
    c.setopt(c.WRITEFUNCTION, b.write)
    c.setopt(c.SSL_VERIFYPEER, False)
    c.setopt(c.HTTPHEADER, headers)
    c.setopt(c.POST, 1)
    c.setopt(c.POSTFIELDS, dumps(fields))
    c.setopt(c.SSL_VERIFYPEER, False)
    c.perform()
    c.close()
    result = b.getvalue().decode('UTF-8')
    pprint(loads(result))


if __name__ == '__main__':
    parser = ArgumentParser(description='Sends a notification to an Android device')
    parser.add_argument('-t', type=str, help='Title')
    parser.add_argument('-m', type=str, help='Message')
    parser.add_argument('--vibrate', type=str, help='Should vibrate')
    parser.add_argument('--sound', type=str, help='Use sound')
    
    if not "GCM_KEY" in environ:
        parser.add_argument('K', type=str, help='API Access Key')
    else:
	API_ACCESS_KEY = environ['GCM_KEY']
    
    parser.add_argument('R', metavar='R', type=str, nargs='+', help='Registration ids')
    args = parser.parse_args()

    if not API_ACCESS_KEY:
    	API_ACCESS_KEY = args.K
    
    REGISTRATION_IDS = args.R

    send_notification(args.t, args.m, args.vibrate is not None, args.sound is not None)
