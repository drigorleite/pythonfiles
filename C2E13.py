row_length = float(input ('Enter length of row in feet: '))
post_length = float(input('Enter length of end post in feet: '))
vine_spacing = float(input('Enter space between vines in feet: '))
vines = (row_length - 2 * post_length) / vine_spacing
print (f'You have enough space for {vines:.2f} vines.')

