class Diode_approximations:
    
    def ideal_model_fwd(v_bias, r_limit):
        i_fwd = v_bias / r_limit
        v_rlimit = i_fwd * r_limit
        print(str(i_fwd) + ", " + str(0) + ", " + str(v_rlimit))
        #returns the values of the forward current, forward voltage, and the voltage across the limit resistor of the ideal diode
        
    def practical_model_fwd(v_bias, r_limit):
        i_fwd = (v_bias - 0.7) / r_limit
        v_rlimit = i_fwd * r_limit
        print(str(i_fwd) + ", " + str(0.7) + ", " + str(v_rlimit))
        #returns the values of the forward current, forward voltage, and the voltage across the limit resistor of the practical diode
        
    def complete_model_fwd(v_bias, r_limit, r_dyn=10):
        i_fwd = (v_bias - 0.7) / (r_limit + r_dyn)
        v_fwd = 0.7 + (i_fwd * r_dyn)
        v_rlimit = i_fwd * r_limit
        print(str(i_fwd) + ", " + str(v_fwd) + ", " + str(v_rlimit))
        #returns the values of the forward current, forward voltage, and the voltage across the limit resistor of the complete diode
        
    def ideal_model_rev(v_bias, r_limit):
        print(str(0) + ", " + str(v_bias) + ", " + str(0))
        #returns the values of the reverse current, reverse voltage, and the voltage across the limit resistor of the ideal diode
        
    def practical_model_rev(v_bias, r_limit):
        print(str(0) + ", " + str(v_rev) + ", " + str(0))
        #returns the values of the reverse current, reverse voltage, and the voltage across the limit resistor of the practical diode
        
    def complete_model_rev(v_bias, r_limit, i_rev=1e-06):
        v_rlimit = i_rev * r_limit
        v_rev = v_bias - v_rlimit
        print(str(i_rev) + ", " + str(v_rev) + ", " + str(v_rlimit)) 
        #returns the values of the reverse current, reverse voltage, and the voltage across the limit resistor of the complete diode

"""        
        
where:

i_fwd = Forward current, A
v_bias = Bias voltage, V
r_limit = Limit resistance, ohms
v_rlimit = Voltage across the limiting resistor, V
v_fwd = Forward voltage, V (0 V for ideal model and 0.7 V for practical and complete models)
r_dyn = Forward dynamic resistance, ohms
v_rev = Reverse voltage, V (v_rev = v_bias for ideal and practical models)
i_rev = Reverse current, V (0 V for ideal and practical models)

"""