"""A solver for the 1D diffusion equation."""
import numpy as np

np.set_printoptions(formatter={"float": "{: 6.1f}".format}) #when you print a numpy array, if their values are a float, they will take up
                                                            #6 spaces, with one decimal point.


def solve1d(concentration, grid_spacing, time_step, diffusivity):
    flux = -diffusivity * np.diff(concentration) / grid_spacing
    concentration[1:-1] -= time_step * np.diff(flux) / grid_spacing #we don't start at 0, and leave out the end because we only want the
                                                                    #the model to evaluate the inside, not the edges.
    return concentration #you don't need "return" in this specific case because we use numpy arrays. In any other case, you need this line.
    #print("hi") #this was for unit tests


def _example():
    #these settings will reach stability after 50 time steps (1,51)
    D = 100
    Lx = 10
    dx = 0.5
    C1 = 500
    C2 = 0
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / D / 2.1
    print(C)
    
    for _ in range(1,4): #underscore is placeholder for a loop counter, but you could not not use it. This will iterate 4 times (1,2,3,4)
        C = solve1d(C, dx, dt, D)
        print(C)
    
    
if __name__  == "__main__": #two underscores here!
    _example()