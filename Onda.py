import numpy as np

class Onda:
    
    def __init__ (self, L,T,N,M,V):
        """
        Costruttore:
        L = lunghezza intervallo spaziale
        T = lunghezza intervallo temporale
        N = step spaziali
        M = step temporali
        
        Return:
        traj = matrice di N*(M+1)
        """
        self.L = L
        self.T = T
        self.N = N
        self.M = M+1
        self.V = V
        self.norma = np.zeros(self.M)
        
        self.k = np.fft.fftfreq(self.N)
        self.k = self.k*((2.*np.pi)*N/self.L)
        self.x = np.linspace(0.,L,N,endpoint=False)
        self.dx = self.x[1]
        self.dt = T/M
        
        self.traj = np.zeros((self.N,self.M),dtype = "complex_")
        
    def evoluzione(self,num_step):
        #definizione vettori da usare
        y_re_1 = np.zeros(self.N, dtype = "complex_")
        y_compl = np.zeros(self.N, dtype = "complex_")
        y_re_2 = np.zeros(self.N, dtype = "complex_")
        #applicazione di G1
        y_re_1 = np.exp(-1j*self.dt/2*self.V)*self.traj[:,num_step-1]
        #applicazione di G2
        y_compl = np.fft.fft(y_re_1)
        y_compl = np.exp(-1j*self.dt/2*(self.k[:]**2))*y_compl
        #applicazione di G3
        y_re_2 = np.fft.ifft(y_compl)
        y_re_2 = np.exp(-1j*self.dt/2*self.V)*y_re_2
        
        self.traj[:,num_step] = y_re_2
        self.norma[num_step] = np.sum(np.abs(self.traj[:,num_step])**2)