class Half_wave_rectifier:
"""returns a value of the peak_output, average_output, and peak inverse voltages of the
    half-wave rectifier"""
    
    def __init__(self, vp_in, n):
        self.vp_in = vp_in
        self.n = n
        
    def peak_output_voltage(self):
        vp_pri = self.vp_in
        vp_sec = self.n * vp_pri
        vp_out = vp_sec - 0.7
        print(str(vp_out)) 
    
    def average_output_voltage(self):
        v_ave = ((self.n * self.vp_in) - 0.7) / pi
        print(str(v_ave)) 
        
    def peak_inverse_voltage(self):
        piv = self.n * self.vp_in
        print(str(piv)) 

"""
        
where:

vp_in = Input peak voltage, V
n = turns ratio
vp_pri = Voltage in the primary circuit, V
vp_sec = Voltage in the secondary circuit, V
vp_out = Output peak voltage, V
v_ave = Average output voltage, V
piv = Peak inverse voltage, V

"""
