def capacitor_input_filter(n, v_rms,r_load, c, f=120):
    
    """returns the values of the peak-to-peak ripple voltage, DC output voltage, 
    and the ripple factor"""
    
    vp_pri = 1.414 * v_rms
    vp_sec = n * vp_pri
    vp_rect = vp_sec - 1.4
    vr_pp = (1 / (f * r_load * c)) * vp_rect
    v_dc = (1-(1/(2 * f * r_load * c))) * vp_rect
    rip_f = (vr_pp / v_dc) * 100
    print(str(vr_pp) + ", " + str(v_dc) + ", " + str(rip_f))
    
"""

where:

- n = turns ratio
- v_rms = RMS secondary voltage, V
- r_load = Load resistance, ohms
- c = capacitance of the capacitor, farads
- f = frequency, hz (default: 120 hz for the frequency of a full-wave rectified voltage)
- vp_pri = Voltage in the primary circuit, V
- vp_sec = Voltage in the secondary circuit, V
- vp_rect = Unfiltered peak full-wave rectified voltage, V
- vr_pp = Peak-to-peak ripple voltage, V
- v_dc = DC output voltage, V
- rip_f = ripple factor, %

"""
