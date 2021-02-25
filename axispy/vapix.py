from sensecam_control.vapix_config import (
    CameraConfiguration as CameraConfigurationVAPIX,
)
from sensecam_control.vapix_control import CameraControl as CameraControlVAPIX
from .capturer import AxisCamera


class AxisCameraVAPIX(AxisCamera, CameraControlVAPIX, CameraConfigurationVAPIX):
    def __init__(self, *args, **kwargs):
        AxisCamera.__init__(self, *args, **kwargs)
        control_url = self._obtain_url_capture("http", add_urlargs=False)
        CameraControlVAPIX.__init__(self, control_url, self.username, self.password)
        CameraConfigurationVAPIX.__init__(
            self, control_url, self.username, self.password
        )
