import math

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