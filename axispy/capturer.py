from urllib.parse import urlparse, uses_fragment
from .url_to_image import urlauth_to_image
import warnings

cv2_imported = False
try:
    import cv2

    cv2_imported = True
except:
    warnings.warn("Could not import OpenCV", ImportWarning)


RTSP_PATH = "/axis-media/media.amp"
HTTP_PATH = "/mjpg/1/video.mjpg?"

DEFAULT_PROTOCOL_HTTP = 80
DEFAULT_PROTOCOL_RTSP = 513

URL_CREDENTIALS = "{username}:{password}@"
URL_CAPTURE = "{protocol}://{credentials}{netdir}:{port}{urlargs}"

AVAILABLE_STERAM = ["rtsp", "http"]


class AxisCamera(object):
    def __init__(
        self,
        address,
        username=None,
        password=None,
        http_port=DEFAULT_PROTOCOL_HTTP,
        rtsp_port=DEFAULT_PROTOCOL_RTSP,
        # vapix_or_onvif="vapix",
    ):

        p = urlparse(address)
        self.username = p.username if p.username else username
        self.password = p.password if p.password else password
        self.netdir = p.hostname

        self.http_port = http_port
        self.rtsp_port = rtsp_port
        # cv2.VideoCapture.__init__(self, self.capture_url)

    def _obtain_url_capture(self, protocol, add_credentials=True, add_urlargs=True):
        if not protocol in AVAILABLE_STERAM:
            raise (
                ValueError(
                    "Protocol '{protocol}' unrecognized. Available:", AVAILABLE_STERAM
                )
            )
        credentials = ""
        if credentials:
            credentials = URL_CREDENTIALS.format(
                username=self.username, password=self.password
            )
        urlargs = ""
        if add_urlargs:
            if protocol == "rtsp":
                urlargs = RTSP_PATH
            elif protocol == "http":
                urlargs = HTTP_PATH
        url_res = URL_CAPTURE.format(
            protocol=protocol,
            credentials=credentials,
            netdir=self.netdir,
            port=self.http_port if protocol == "http" else self.rtsp_port,
            urlargs=urlargs,
        )
        return url_res

    def obtain_streamer(self):
        if not cv2_imported:
            raise (ImportError("OpenCV could not be imported. Streamer not available"))
        return cv2.VideoCapture(self._obtain_url_capture("rtsp"))

    def snapshot(self):
        ret = False
        image = None
        url = self._obtain_url_capture("http", add_credentials=False)
        try:
            image = urlauth_to_image(url, self.username, self.password)
        except ConnectionError as e:
            print(f"Retrieving image got ConnectionError with {url}:", e)
        except Exception as e:
            print(f"Retrieving image got Unknown error with url {url}", e)

        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        if image is not None:
            ret = True
        return ret, image
