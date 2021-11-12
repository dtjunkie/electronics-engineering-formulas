class bipolar_junction_transistor:
    
    def __init__(self,volt_bb, volt_cc, r_base, r_coll, beta_dc, volt_be=0.7):
        self.volt_bb = volt_bb
        self.volt_cc = volt_cc
        self.r_base = r_base
        self.r_coll = r_coll
        self.beta_dc = beta_dc
        self.volt_be = volt_be
    
    def circuit_analysis(self):
        
        """returns the values of the current and voltage measurements in the BJT circuit"""
        
        i_base = (self.volt_bb - self.volt_be) / self.r_base
        i_coll = self.beta_dc * i_base
        i_emit = i_coll + i_base
        volt_ce = self.volt_cc - (i_coll * self.r_coll)
        volt_cb = volt_ce - self.volt_be
        print(str(i_base) + ", " + str(i_coll) + ", " + str(i_emit) + ", " + str(volt_ce)+ ", " + str(volt_cb))
        
    def voltage_gain(self, r_acemit):
        
        """returns the value of the approximate ac voltage gain in BJT circuit"""
        
        v_gain = self.r_base / r_acemit
        print(int(v_gain))
        
    def cutoff(self):
        
        """returns the value of collector-emitter voltage in the BJT during cut-off"""
        
        vce_cutoff = self.volt_cc
        print(str(vce_cutoff))
        
        
    def saturation(self, vce_sat=0):
        
        """returns the values of the voltage and current measurments in the BJT during saturation"""
        
        ic_sat = (self.volt_cc - vce_sat) / self.r_coll
        ib_min = ic_sat / self.beta_dc
        print(str(ic_sat) + ", " + str(ib_min))
        
"""

where:

- volt_bb = Base-bias voltage, V
- volt_cc = Collector-bias voltage, V
- r_base = Base resistance, ohms
- r_coll = Collector resistance, ohms
- beta_dc = DC current gain of a transistor, unitless
- volt_be = Base-emitter voltage, V (default is 0.7 V)
- i_base = Base current, A
- i_coll = Collector current, A
- i_emit = Emitter current, A
- volt_ce = Collector-emitter voltage, V
- volt_cb = Collector-base voltage, V

- r_acemit = AC emitter resistance, ohms
- v_gain = Approximate AC voltage gain, unitless

- vce_cutoff = Collector-emitter cut-off voltage, V
- vce_sat = Collector-emitter saturation voltage, V
- ic_sat = Collector saturation current, A
- ib_min = Minimum base current needed to produce saturation, A

"""
