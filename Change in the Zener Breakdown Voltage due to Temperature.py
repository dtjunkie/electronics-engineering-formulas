class Delta_zener_breakdown_voltage:
    
    """returns the value of the change in the zener breakdown voltage due to temperature"""
    
    def __init__(self, tc, t_initial, t_final, volt_z=0):
        self.tc = tc
        self.d_temp = t_final - t_initial
        self.volt_z = volt_z
        
    def delta_zbv1(self):
        delta_zbv = self.volt_z * self.tc * self.d_temp
        print(str(delta_zbv))
        
    def delta_zbv2(self):
        delta_zbv = self.tc * self.d_temp
        print(str(delta_zbv))

"""        
        
where:

tc = Temperature coefficient, %/deg. C or mV/ deg. C
t_initial = Initial temperature, deg. C
t_final = Final temperature, deg. C
volt_z = Zener voltage, V
d_temp = Change in the temperature(t_final-t_initial), deg. C
delta_zbv = Change in the zener breakdown voltage, V

NOTE: Use delta_zbv1 if the coefficient unit is in %/ deg. C. Otherwise, use delta_zbv2.

"""
