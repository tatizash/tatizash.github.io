conversion = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

def to_hex(n):
    hex = ''
    while 0 < n <= 255:
        r = n % 16
        hex = conversion[r] + hex
        n = n // 16
  
    return hex
  
n = 10
print(to_hex(n))

def hex_color(red, green, blue):
    if ((0 <= red <= 255) and
            (0 <= green <= 255) and
            (0 <= blue <= 255)):

        hex_red=to_hex(red)
        hex_green=to_hex(green)
        hex_blue=to_hex(blue)

        if len(hex_red)==1:
            hex_red="0" + hex_red 
        
        if len(hex_green)==1:
            hex_green="0"+hex_green

        if len(hex_blue)==1:
            hex_blue="0"+hex_blue

        hex_code = "#" + hex_red + hex_green + hex_blue
        return hex_code


    else:
        return "-1"

red = 10
green = 32
blue = 255
print(hex_color(red, green, blue))