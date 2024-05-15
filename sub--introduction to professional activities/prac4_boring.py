def lighten(color: str, percent: int) -> str:
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    r = int(r * (1+(percent/100)))
    g = int(g * (1+(percent/100)))
    b = int(b * (1+(percent/100)))
    if r > 255: r = 255
    if g > 255: g = 255
    if b > 255: b = 255
    darkened_color = "#{:02x}{:02x}{:02x}".format(r, g, b) # Idiot pylint
    return darkened_color

def darken(color: str, percent: int) -> str:
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    r = int(r * (percent/100))
    g = int(g * (percent/100))
    b = int(b * (percent/100))
    darkened_color = "#{:02x}{:02x}{:02x}".format(r, g, b) # Idiot pylint
    return darkened_color


print(darken('#000000', 100))
print(lighten('#99CCFF', 50))
print(darken('#45A1F0', 20))
