from .vapix import AxisCameraVAPIX
from .onvif import AxisCameraONVIF


def camera(*args, vapix_or_onvif="vapix", **kwargs):
    if vapix_or_onvif == "vapix":
        c = AxisCameraVAPIX
    elif vapix_or_onvif == "onvif":
        c = AxisCameraONVIF
    return c(*args, **kwargs)