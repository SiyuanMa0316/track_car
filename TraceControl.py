pic_wid = 640
pic_len = 400#NOT needed
initial_vel = 40
delta_wid = 80
delta_vel = 20
delta_radius = 50
    
def velcontrol(position_wid0,radius0):
    position_wid = position_wid0 - pic_wid * 0.5
    radius = radius0
    velosity_left = initial_vel
    velosity_right = initial_vel
    if  position_wid  > 0 :
        while ( position_wid  > delta_wid ) :
            velosity_left = velosity_left + delta_vel
            #velosity_right = velosity_right - delta_vel
            position_wid = position_wid - delta_wid
    elif  position_wid  < 0 :
        while ( position_wid  < - delta_wid ) :
            #velosity_left = velosity_left - delta_vel
            velosity_right = velosity_right + delta_vel
            position_wid = position_wid + delta_wid
    while ( radius > 0 ) :
        velosity_left = velosity_left - delta_vel
        velosity_right = velosity_right - delta_vel
        radius = radius - delta_radius
    return [velosity_left,velosity_right]

def driven(vel):
    vel4 = [0,0,0,0]
    if  vel[0] > 0 :
        vel4[0] = vel[0]
    elif  vel[0] < 0 :
        vel4[1] = - vel[0]
    if  vel[1] > 0 :
        vel4[2] = vel[1]
    elif  vel[1] < 0 :
        vel4[3] = - vel[1]
    return vel4
