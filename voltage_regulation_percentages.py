class Voltage_regulation_percentages:
    
    def __init__(self, dv_out, dv_in, volt_nl=0, volt_fl=0):
        self.dv_out = dv_out
        self.dv_in = dv_in 
        self.volt_nl= volt_nl
        self.volt_fl = volt_fl
        
    def load_regulation(self):
        
        """returns a percentage value of the load regulation"""
        
        load_reg = (self.dv_out/self.dv_in) * 100
        print(str(load_reg))
        
    def line_regulation(self):
        
        """returns a percentage value of the line regulation"""
        
        line_reg = ((self.volt_nl - self.volt_fl)/self.volt_fl) * 100
        print(str(line_reg))
"""

where:

dv_out = Change in the output voltage, V
dv_in = Change in the input voltage, V
volt_nl = Output no-load voltage, V
volt_fl = Output full-load voltage, V
load_reg = Load regulation, %
line_reg = Line Regulation, %

NOTE: For line regulation, set dv_out and dv_in to 0 to avoid errors.

"""
