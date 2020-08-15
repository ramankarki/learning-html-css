def copy_font(old_filename, new_filename):
    font = open(old_filename, "br")
    data = font.readlines()
    new_font = open(new_filename, "bw")

    for row in data:
        new_font.write(row)

    font.close()
    new_font.close()

copy_font("Roboto-Black.ttf", "font/dekho mera naya font.ttf")
