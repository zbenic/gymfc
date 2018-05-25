from gym.envs.registration import register
import math
import numpy as np


continuous_kwargs = {
     "memory_size": 1,
     "world": "attitude-iris.world", 
     "omega_bounds": [-math.pi*2,math.pi*2],
     "command_time_off":[0.1, 1.0],
     "command_time_on":[0.1, 1.0],
     "max_sim_time": 60,
     "model":"quadcopter",
     }
id = 'AttFC_Err-MotorVel_M4_Con-v0'
register(
    id=id,
    entry_point='gymfc.envs:GyroErrorESCVelocityFeedbackContinuousEnv',
    kwargs=continuous_kwargs)

for m in range(1,11):
    for noise in np.arange(0.0, 1.0, 0.1): # noise
        episodic_kwargs = {
            "memory_size": m,
            "world": "attitude-iris.world", 
            "omega_bounds": [-math.pi*2,math.pi*2],
            "max_sim_time": 1.,
            "motor_count":4,
            "model":"quadcopter_model",
            "noise_stddev":noise,
            }
        if noise == 0: 
            id = 'AttFC_GyroErr{}_M4_Ep-v0'.format(m)
        else:
            id = 'AttFC_GyroErr{}-Noise{}_M4_Ep-v0'.format(m,noise)

        register(
            id=id,
            entry_point='gymfc.envs:GyroErrorFeedbackEnv',
            kwargs=episodic_kwargs)


episodic_kwargs = {
    "memory_size": 1,
    "world": "attitude-iris.world", 
    "omega_bounds": [-math.pi*2,math.pi*2],
    "max_sim_time": 1.,
    "motor_count":4,
    }
id = 'AttFC_Err-MotorVel_M4_Ep-v0'
register(
    id=id,
    entry_point='gymfc.envs:GyroErrorESCVelocityFeedbackEnv',
    kwargs=episodic_kwargs)


for i in np.arange(0.0, 0.1, 1):
    id = 'AttFC_GyroErr-MotorVel-Noisy{}_M4_Ep-v0'.format(i)
    register(
        id=id,
        entry_point='gymfc.envs:GyroErrorESCVelocityFeedbackEnv',
        kwargs=episodic_kwargs)
