def zener_impedance(delv_z, deli_z):
    
    """returns the value of the zener impedance(resistance)"""
    
    r_zener = delv_z/deli_z
    print(str(r_zener))

"""    
    
where:

r_zener = Zener impedance, ohms
delv_z = Change in the zener breakdown voltage, V
deli_z = Change in the zener current, A

"""
