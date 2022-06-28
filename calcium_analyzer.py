class calcium_analyzer:
    def __init__(self, dt=0.05, tau0=0.6, tau1=0.8, tau2=60, theta=0.1):
        self.N = 0
        self.T = 0
        self.dt = dt
        self.tau0 = int(tau0/dt)
        self.tau1 = int(tau1/dt)
        self.tau2 = int(tau2/dt/2)
        self.theta = theta/dt
        self.Mean = np.zeros((0, 0))
        self.Smoothed = np.zeros((0, 0))
        self.F_0 = np.zeros((0, 0))
        self.sm_RFU = np.zeros((0, 0))
        self.RFU = np.zeros((0, 0))
        self.diff = np.zeros((0, 0))
        self.raster = np.zeros((0, 0))
    def extract_raw_data(self, filename):
        data = np.loadtxt(filename, delimiter="\t", dtype="str")
        row, col = data.shape
        self.N = (col - 1)//4; self.T = row - 1
        self.Mean = data[1:self.T+1, 2::4].T.astype(np.float32)
    def smooth_filter(self):
        W = np.ones(self.tau1)
        W = np.matrix(W)
        self.Smoothed = signal.convolve2d(self.Mean, W, mode="valid")/self.tau1
    def calc_baseline(self):
        self.F_0 = np.zeros((self.N, self.T))
        self.F_0[:, 0] = np.min(self.Smoothed[:, 0:self.tau2], axis=1)
        for t in range(1, self.T):
            self.F_0[:, t] = np.min(self.Smoothed[:, max(0,t-self.tau2):min(self.T, t+self.tau2)], axis=1)
    def calc_RFU(self):       
        self.RFU = (self.Mean - self.F_0) / self.F_0
    def exponential_filter(self):
        tau = np.arange(101)
        W = 1/tau0*np.exp(-tau/tau0)
        W = np.matrix(W)
        self.sm_RFU = signal.convolve2d(self.RFU, W, mode="full")[:, :-100]
    def signal2raster(self):
        W = [1,0,-1]
        W = np.matrix(W)
        self.diff = signal.convolve2d(self.RFU, W, mode="same")/(2*self.dt)
        self.raster = np.where(self.diff > self.theta, 1, 0)
    def run(self, filename):
        self.extract_raw_data(filename)
        self.smooth_filter()
        self.calc_baseline()
        self.calc_RFU()
        #self.exponential_filter()
        self.signal2raster()