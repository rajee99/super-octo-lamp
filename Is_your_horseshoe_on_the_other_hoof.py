colors = list(map(int, input().split()))
unique_colors = set(colors)

color_len = len(colors)
unique_colors_len = len(unique_colors)



print(color_len - unique_colors_len)

