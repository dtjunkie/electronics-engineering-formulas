class Diode_approximations:
    
    """returns the values of the bias current, bias voltage, and the 
    voltage across the limit resistor of the diode models in different
    operating conditions or biases"""
    
    def __init__(self, model, v_bias, r_limit, r_dyn=10, i_rev=1e-06):
        self.model = model 
        self.v_bias = v_bias
        self.r_limit = r_limit
        self.r_dyn = r_dyn
        self.i_rev = i_rev
        
    def forward_bias(self):
        if self.model == "ideal":
            i_fwd = self.v_bias / self.r_limit
            v_rlimit = i_fwd * self.r_limit
            print(str(i_fwd) + ", " + str(0) + ", " + str(v_rlimit))
        elif self.model == "practical":
            i_fwd = (self.v_bias - 0.7) / self.r_limit
            v_rlimit = i_fwd * self.r_limit
            print(str(i_fwd) + ", " + str(0.7) + ", " + str(v_rlimit))
        elif self.model == "complete":
            i_fwd = (self.v_bias - 0.7) / (self.r_limit + self.r_dyn)
            v_fwd = 0.7 + (i_fwd * self.r_dyn)
            v_rlimit = i_fwd * self.r_limit
            print(str(i_fwd) + ", " + str(v_fwd) + ", " + str(v_rlimit))
        else:
            return ValueError("Invalid model type.")
        
    def reverse_bias(self):
        if self.model == "ideal":
            print(str(0) + ", " + str(self.v_bias) + ", " + str(0))
        elif self.model == "practical":
            print(str(0) + ", " + str(self.v_bias) + ", " + str(0))
        elif self.model == "complete":
            v_rlimit = self.i_rev * self.r_limit
            v_rev = self.v_bias - v_rlimit
            print(str(self.i_rev) + ", " + str(v_rev) + ", " + str(v_rlimit)) 
        else:
            return ValueError("Invalid model type.")  

"""        
        
where:

model = Diode model ("ideal", "practical", or "complete")
v_bias = Bias voltage, V
r_limit = Limit resistance, ohms
r_dyn = Forward dynamic resistance, ohms
i_rev = Reverse current, V (0 V for ideal and practical models)
i_fwd = Forward current, A
v_rlimit = Voltage across the limiting resistor, V
v_fwd = Forward voltage, V (0 V for ideal model and 0.7 V for practical and complete models)
v_rev = Reverse voltage, V (v_rev = v_bias for ideal and practical models)

"""
