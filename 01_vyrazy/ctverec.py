from math import pi

def obvod_ctverce(strana): 
    """Program vypočítá obvod čtverce zadané strany."""
    return strana * 4

def obsah_ctverce(strana): 
    """Program vypočítá obsah čtverce zadané strany."""
    return strana ** 2

def obvod_a_obsah_kruhu(polomer): 
    """Program vypočítá obvod a obsah kruhu. """
    obvod = 2 * pi * polomer
    obsah = pi * polomer ** 2
    return obvod, obsah


# strana = 356
strana = 0
while True: 
    if strana > 0: 
        break
    else: 
        try: 
            strana = int(input('Zadej délku strany/poloměru: '))
            if strana <=0: 
                print('Zadej kladné číslo. ')
        except ValueError: 
            print('Zadej kladné číslo. ')        
    

print('\nObvod čtverce se stranou', strana, 'cm je', obvod_ctverce(strana), 'cm. ') 
print('Obsah čtverce se stranou', strana, 'cm je', obsah_ctverce(strana), 'cm2. ')
obvod, obsah = obvod_a_obsah_kruhu(strana)
print('Obvod kruhu s poloměrem', strana, 'cm je', obvod, 'cm a jeho obsah je', obsah, 'cm2.\n')



