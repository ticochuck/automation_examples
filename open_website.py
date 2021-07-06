import webbrowser

pre = "https://"
site = input("Enter site name: ")
suff = ".com"

full = pre + site + suff

print(full)

webbrowser.open_new(full)

webbrowser.open_new_tab(full)
