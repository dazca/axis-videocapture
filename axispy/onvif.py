from sensecam_control.onvif_config import (
    CameraConfiguration as CameraConfigurationONVIF,
)
from sensecam_control.onvif_control import CameraControl as CameraControlONVIF
from .capturer import AxisCamera


class AxisCameraONVIF(AxisCamera, CameraControlONVIF, CameraConfigurationONVIF):
    def __init__(self, *args, **kwargs):
        AxisCamera.__init__(self, *args, **kwargs)
        control_url = self._obtain_url_capture("http", add_urlargs=False)
        CameraControlONVIF.__init__(self, control_url, self.username, self.password)
        CameraConfigurationONVIF.__init__(
            self, control_url, self.username, self.password
        )