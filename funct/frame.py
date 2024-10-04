def create_frame(lines, width=None, center=False):
    
    

    if width is None:
        width = max(len(line) for line in lines) + 4
    
    # Bordure supérieure et inférieure
    top_bottom_border = "╔" + "═" * (width - 2) + "╗"
    bot_bottom_border = "╚" + "═" * (width - 2) + "╝"
    print(top_bottom_border)
    for line in lines:
        if center is False:
            text_line = f"║ {line.ljust(width - 4)} ║"
        else:
            text_line = f"║ {line.center(width - 4)} ║"
        print(text_line)
    print(bot_bottom_border)