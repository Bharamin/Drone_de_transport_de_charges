from rplidar import RPLidar, RPLidarException
import sys

lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

#d[0] : Qualite de la mesure
#d[1] : Valeur de l'angle en degree
#d[2] : Valeur de la distance avec l'obstacle en mm
try:
    for i, scan in enumerate(lidar.iter_scans()):
        scan_data = []
        for d in scan:
            #Valeur de 90 degree devant le LIDAR
            if 0< d[1] <45 or 335< d[1] <380 :
                #Verifie si un obstacle est a moins de 40cm du drone
                if 0< d[2]< 400:
                    print("Trop proche devant")
            #Recupere l'angle a la droite du Drone
            if 45< d[1] < 90:
                #Verifie si un obstacle est a moins de 15cm sur le coté droit du drone
                if 0< d[2]< 150:
                    print("Trop proche coté droit")
            #Recupere l'angle a la droite du Drone
            if 290<d[1] < 335:
                #Verifie si un obstacle est a moins de 15cm sur le coté gauche du drone
                if 0<d[2]<150:
                    print("trop proche coté gauche")


        if False:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
            break
except KeyboardInterrupt as err:
    print('key board interupt')
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()

except RPLidarException as err:
    print(err)
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
except AttributeError:
    print('hi attribute error')
