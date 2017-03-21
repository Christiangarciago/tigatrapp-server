import ssl
import json
import socket
import struct
import binascii
import urllib2
import json
from tigaserver_project import settings_local

def send_message_ios(token,alert_message,link_url):
    cert = '/home/webuser/webapps/tigaserver/CertificatMosquito.pem'
    TOKEN = token
    PAYLOAD = {
        'aps': {
            'alert': alert_message,
            'sound': 'default',
            'link_url': link_url
        }
    }

    # APNS development server
    apns_address = ('gateway.sandbox.push.apple.com', 2195)

    # Use a socket to connect to APNS over SSL
    s = socket.socket()
    sock = ssl.wrap_socket(s, certfile=cert)
    sock.connect(apns_address)

    # Generate a notification packet
    TOKEN = binascii.unhexlify(TOKEN)
    PAYLOAD = json.dumps(PAYLOAD)
    fmt = '!cH32sH{0:d}s'.format(len(PAYLOAD))
    cmd = '\x00'
    message = struct.pack(fmt, cmd, len(TOKEN), TOKEN, len(PAYLOAD), PAYLOAD)

    response = sock.write(message)
    #print response
    sock.close()
    return response

def send_message_android(token,title, message):
    try:
        #token = 'eqFkux_dIuo:APA91bGmmOxn16z8VhHE3O0tB7VmDsPX5p0xBfzJpSPi8O8gNaCbyJlJDwTdOAm4cOADCZ4KK5JRgV1NvAH_1YriYZob00Y5QCBw9FefMrpbs2pCD5TAKrkWy3vUNbwZQZGkySOqLH79'
        app_id = settings_local.ANDROID_GCM_API_KEY
        # List of device tokens to send the message to. Can be 1 item
        private_keys = [token]
        #private_keys.append(token)

        url = "https://android.googleapis.com/gcm/send"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "key=" + app_id
        }

        values = {
            "registration_ids": private_keys,
            "data": {
                "message": message,
                "title": title
            }
        }

        values = json.dumps(values)
        req = urllib2.Request(url, values, headers)
        resp = urllib2.urlopen(req)
        resp_txt = resp.read()
        return resp_txt

    except AttributeError:
        return "No app id available in config"