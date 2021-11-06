class Full_wave_rectifier:
    """returns a value of the peak_output, average_output, and peak inverse voltages of the
    full-wave rectifier"""
    
    def __init__(self, vp_in, n, v_rms=0):
        self.vp_in = vp_in
        self.n = n
        self.v_rms = v_rms
        
    def center_tapped_fwr(self):
        vp_pri = self.vp_in
        vp_sec = self.n * vp_pri
        vp_out = (vp_sec / 2) - 0.7
        v_ave = (2 * vp_out) / pi
        piv = (2 * vp_out) + 0.7
        print(str(vp_out) + ", " + str(v_ave) + ", " + str(piv))
        
    def bridge_type_fwr(self):
        vp_sec = 1.414 * self.v_rms
        vp_out = vp_sec - 1.4
        v_ave = (2 * vp_out) / pi
        piv = vp_out + 0.7
        print(str(vp_out) + ", " + str(v_ave) + ", " + str(piv))

"""
        
where:

vp_in = Input peak voltage, V
n = turns ratio
v_rms = RMS secondary voltage, V
vp_sec = Voltage in the secondary circuit, V
vp_out = Output peak voltage, V
v_ave = Average output voltage, V
piv = Peak inverse voltage, V

NOTE: When using the bridge_type_fwr function, set vp_in and n to 0 to avoid errors

"""
