from argschema import ArgSchema
from argschema.fields import Float, LogLevel, String

from allensdk.brain_observatory.argschema_utilities import (
    check_read_access,
    check_write_access_overwrite,
    RaisingSchema
)


class InputSchema(ArgSchema):

    # ============== Required fields ==============
    input_file = String(
        required=True,
        validate=check_read_access,
        description=('An h5 file containing ellipses fits for '
                     'eye, pupil, and corneal reflections.')
    )

    output_file = String(
        required=True,
        validate=check_write_access_overwrite,
        description=('Full save path of output h5 file that '
                     'will be created by this module.')
    )

    monitor_position_x_mm = Float(required=True,
                                  description=("Monitor center X position in "
                                               "'global' coordinates "
                                               "(millimeters)."))
    monitor_position_y_mm = Float(required=True,
                                  description=("Monitor center Y position in "
                                               "'global' coordinates "
                                               "(millimeters)."))
    monitor_position_z_mm = Float(required=True,
                                  description=("Monitor center Z position in "
                                               "'global' coordinates "
                                               "(millimeters)."))
    monitor_rotation_x_deg = Float(required=True,
                                   description="Monitor X rotation in degrees")
    monitor_rotation_y_deg = Float(required=True,
                                   description="Monitor Y rotation in degrees")
    monitor_rotation_z_deg = Float(required=True,
                                   description="Monitor Z rotation in degrees")
    camera_position_x_mm = Float(required=True,
                                 description=("Camera center X position in "
                                              "'global' coordinates "
                                              "(millimeters)"))
    camera_position_y_mm = Float(required=True,
                                 description=("Camera center Y position in "
                                              "'global' coordinates "
                                              "(millimeters)"))
    camera_position_z_mm = Float(required=True,
                                 description=("Camera center Z position in "
                                              "'global' coordinates "
                                              "(millimeters)"))
    camera_rotation_x_deg = Float(required=True,
                                  description="Camera X rotation in degrees")
    camera_rotation_y_deg = Float(required=True,
                                  description="Camera Y rotation in degrees")
    camera_rotation_z_deg = Float(required=True,
                                  description="Camera Z rotation in degrees")
    led_position_x_mm = Float(required=True,
                              description=("LED X position in 'global' "
                                           "coordinates (millimeters)"))
    led_position_y_mm = Float(required=True,
                              description=("LED Y position in 'global' "
                                           "coordinates (millimeters)"))
    led_position_z_mm = Float(required=True,
                              description=("LED Z position in 'global' "
                                           "coordinates (millimeters)"))
    equipment = String(required=True,
                       description=('String describing equipment setup used '
                                    'to acquire eye tracking videos.'))
    date_of_acquisition = String(required=True,
                                 description='Acquisition datetime string.')
    eye_video_file = String(required=True, validate=check_read_access,
                            description=('Full path to raw eye video '
                                         'file (*.avi).'))

    # ============== Optional fields ==============
    eye_radius_cm = Float(default=0.1682,
                          description=('Radius of tracked eye(s) in '
                                       'centimeters.'))
    cm_per_pixel = Float(default=(10.2/10000.0),
                         description=('Centimeter per pixel conversion '
                                      'ratio.'))
    log_level = LogLevel(default='INFO',
                         description='Set the logging level of the module.')


class OutputSchema(RaisingSchema):
    screen_mapping_file = String(required=True,
                                 validate=check_write_access_overwrite,
                                 description=('Full save path of output h5 '
                                              'file that will be created by '
                                              'this module.'))