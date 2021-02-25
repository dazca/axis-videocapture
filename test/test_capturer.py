import pytest
import os
from dotenv import load_dotenv

import axispy

load_dotenv()

ADDRESS = os.environ.get("AXISPY_TEST_ADDRESS")

HTTP_PORT = os.environ.get("AXISPY_TEST_HTTP_PORT")
RTSP_PORT = os.environ.get("AXISPY_TEST_RTSP_PORT")

PASSWORD = os.environ.get("AXISPY_TEST_PASSWORD")
USERNAME = os.environ.get("AXISPY_TEST_USERNAME")


def get_cam():
    return axispy.camera(
        ADDRESS, USERNAME, PASSWORD, http_port=HTTP_PORT, rtsp_port=RTSP_PORT
    )


def get_failing_cam():
    return axispy.camera(
        "fakeaddress",
        "imfoo",
        "no-one-will-use-this-credential-ever-AAA-2Jf",
        http_port="10110",
        rtsp_port="22202",
    )


def test_camera():
    cam = get_cam()


def test_capturer():
    cam = get_cam()
    cap = cam.obtain_streamer()
    ret, img = cap.read()
    assert ret


def test_snapshot():
    cam = get_cam()
    img = cam.snapshot()


def test_error_snapshot():
    cam = get_failing_cam()
    img = cam.snapshot()
