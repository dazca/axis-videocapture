__license__ = "GNU"
__email__ = "dani.azemar@ctrl4enviro.com"
__author__ = "CTRL 4 Enviro"
__version__ = "0.0.0"

import faulthandler
import urllib.error
import urllib.parse
import urllib.request

import cv2
import numpy as np
import requests
from requests.auth import HTTPDigestAuth
from requests.exceptions import ConnectionError
from requests.packages.urllib3.exceptions import InsecureRequestWarning

urlAuths = {}


def urlauth_to_image(url, user, password):
    global urlAuths

    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    if not faulthandler.is_enabled():
        faulthandler.enable()
    if url not in urlAuths:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        httpsDAuth = HTTPDigestAuth(user, password)
        urlAuths[url] = httpsDAuth
    else:
        httpsDAuth = urlAuths[url]
    r = requests.get(url, auth=httpsDAuth, verify=False)
    subimg = np.asarray(bytearray(r.content), dtype="uint8")
    image = cv2.imdecode(subimg, cv2.IMREAD_COLOR)
    # return the image
    return image