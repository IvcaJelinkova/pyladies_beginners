def obvod_ctverce(strana): 
    """Program vypočítá obvod čtverce zadané strany."""
    return strana * 4

def obsah_ctverce(strana): 
    """Program vypočítá obsah čtverce zadané strany."""
    return strana ** 2

strana = 356
print('Obvod čtverce se stranou', strana, 'cm je', obvod_ctverce(strana), 'cm. ') 
print('Obsah čtverce se stranou', strana, 'cm je', obsah_ctverce(strana), 'cm2. ')

