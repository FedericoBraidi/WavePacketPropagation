import numpy as np

class Animazione:
    
    def __init__(self,ax,wave):
        self.x = wave.x
        self.y = wave.traj
        self.line, = ax.plot([],[])             #ax.plot ritorna una lista, a noi serve solo l'elemento,
        self.ax = ax 
                                                #quindi mettiamo la virgola. vedi "unpacking di liste in python"   
        self.ax.set_xlim(0, wave.L)
        self.ax.set_ylim(0, 2.5)
        
    def new_frame(self,num_frame):
        self.line.set_data(self.x,np.abs(self.y[:,num_frame]))
        return self.line,