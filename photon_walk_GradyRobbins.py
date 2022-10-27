#code worked on by Grady Robbins
import numpy as np
print("working...")
path_photon = 4e-3 #mean free path of photon in meters
R_sun = .7 #simulated radius of sun in meters
def r(x,y):
    return (x**2 + y**2)**(.5)
def theta(x,y):
    return np.arctan(y/x)*180/np.pi #functions to convert to polar coordinates (in degrees)
counter = 0
for n in range(100): #averaging values
    new_positionx,new_positiony,photon_position = 0,0,0
    while  photon_position < R_sun:
        rand_direction = np.random.randint(0,360) #choosing random direction
        new_positionx,new_positiony = path_photon*np.cos(rand_direction) + new_positionx, path_photon*np.sin(rand_direction) + new_positiony #setting coordinates and adding old ones
        counter +=1 #this is how many steps the photon took 
        photon_position = r(new_positionx,new_positiony) #testing parameter
time_per_step = 4e-3 / 3e8
photon_total_time = counter * time_per_step/100 #calculating total time travelled
print("in this random simulation, this photon's distance from the star's center is",photon_position,"which is near the star's radius.")
print("this photon took",counter/10,"steps to escape the star. Given the speed of light as 3e8 m/s and that the photon travelled 4e-3 m each step, the photon took",photon_total_time,"seconds to escape.")
#repeating for greater radius
print("working...")
counter1 = 0
R_sun = 7
for n in range(10):
    new_positionx,new_positiony,photon_position = 0,0,0
    while  photon_position < R_sun:
        rand_direction = np.random.randint(0,360) #choosing random direction                                                                                                 
        new_positionx,new_positiony = path_photon*np.cos(rand_direction) + new_positionx, path_photon*np.sin(rand_direction) + new_positiony #setting coordinates and adding old ones       
        counter1 +=1 #this is how many steps the photon took                                                                                                                                
        photon_position = r(new_positionx,new_positiony) #testing parameter                                                                                                                  

time_per_step = 4e-3 / 3e8
photon_total_time1 = (counter1 / 10) * time_per_step #calculating total time travelled                                                 
ratio_time = photon_total_time1/photon_total_time
total_time_big = ( (ratio_time)**15) * photon_total_time1 /(60*60*24*365) #time of star with r = 7e8 in years
print("in this random simulation, this photon's distance from the star's center is",photon_position,"which is near the star's radius.")
print("this photon took",counter1,"steps to escape the star. Given the speed of light as 3e8 m/s and that the photon travelled 4e-3 m each step, the photon took",photon_total_time1,"seconds to escape.")
print()
print("the scenario is very difficult to simulate because the walk is completely random, which means there are large errors in finding a result, sometimes in two orders of magnitude which you may see here.")
if total_time_big >= 100000 or total_time_big <10000:
    print("given the ratio of time from the radius increasing by a factor of 10 being",ratio_time," a star of radius 7e8 m may have a photon walk time of", total_time_big,"years, which is not near the range of 10,000's of years")
    print("like here, the error is very large, so please run the code again to try to get a value closer to the result.")
else:
    print("given the ratio of time from the radius increasing by a factor of 10 being",ratio_time," a star of radius 7e8 m may have a photon walk time of", total_time_big,"years, which should be near the range of 10,000's of years")
