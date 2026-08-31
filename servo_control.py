import math
from controller import Robot

#单条腿的IK解，输入为踝关节的终点坐标（x,z），l1为大腿的长度,l2为小腿的长度
def leg_ik(x,z,l1,l2):
    # 计算横向移动关节角度q1
    y=math.sqrt(l1**2-x**2)
    q1 = math.atan2(y, x)

    # 计算纵向移动关节角度q2
    huai_to_kuan_distance=math.sqrt(((l1+math.sqrt(l2**2-z**2))**2)+z**2)
    cos_q2=(l1**2+l2**2-huai_to_kuan_distance**2)/(2*l1*l2)
    q2=math.acos(cos_q2)

    return q1,q2

#单条腿运行，输入为当前时间t,周期T，上下抬腿高度h，横向移动距离x
def leg_run(t,T,h,x,l1,l2):
    # 计算当前时间t对应的上下抬腿高度h
    h_t=h*math.sin(t/T*math.pi*2)
    sin_q1=h_t/l1
    q1=math.asin(sin_q1)
    q2=-q1

    # 计算当前时间t对应的横向移动距离x
    x_t=x*math.sin(t/T*math.pi*2)
    sin_q0=x_t/2/l2
    q0=math.asin(sin_q0)

    return q0,q1,q2

#单条腿的轨迹，输入为当前相位phase, duty为支撑相的占空比，step_length为步长，step_height为步高，z_ground为地面基准高度z_ground
def leg_trajectory(phase,duty,step_length,step_height,z_ground,l1,l2):
    #判断属于支撑相还是摆动相
    if phase<duty:
        #支撑相
        sin_q1=z_ground/l1
        q1=math.asin(sin_q1)
        q2=-q1
    else:
        #摆动相
        h_t=z_ground+step_height*math.fabs(math.sin(math.pi*phase))
        sin_q1=h_t/l1
        q1=math.asin(sin_q1)
        q2=-q1

    # 计算当前相位phase对应的横向移动距离x
    x_t=step_length*math.sin(phase*math.pi*2)
    sin_q0=x_t/2/l2
    q0=math.asin(sin_q0)

    return q0,q1,q2
