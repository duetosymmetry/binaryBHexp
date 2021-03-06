import os
import numpy as np

prec_cmd = "./binaryBHexp --q 2 --chiA 0.3 0.7 -0.1 --chiB 0.3 0.6 0.1 --omega_ref 1.8e-2 --save_file animations/precessing.mp4"

prec_rot_cmd = "./binaryBHexp --q 2 --chiA 0.3 0.7 -0.1 --chiB 0.3 0.6 0.1 --omega_ref 1.8e-2 --auto_rotate_camera --save_file animations/precessing_auto_rotate.mp4"

super_kick_cmd = "./binaryBHexp --q 1.34 --chiA 0.62 -0.27 0.34 --chiB -0.62 0.27 0.34 --save_file animations/super_kick.mp4"

aligned_cmd = "./binaryBHexp --q 2 --chiA 0 0 -0.6 --chiB 0 0 0.8 --omega_ref 1.8e-2 --save_file animations/aligned.mp4"

os.system(prec_cmd)
for still_time in [-3650, -2000, -1000, -100, -10, 0, 15, 45, 75, 2280]:
    os.system('%s --still_time %f --no_surrogate_label'%(prec_cmd, still_time))

os.system(prec_rot_cmd)
for still_time in [-3800, -3450, -3100]:
    os.system('%s --still_time %f --no_surrogate_label'%(prec_rot_cmd, \
        still_time))

os.system(super_kick_cmd)
for still_time in [-2600, -100, 8.35, 1366]:
    os.system('%s --still_time %f --no_surrogate_label'%(super_kick_cmd, \
        still_time))

os.system(aligned_cmd)
