import locale

locale.setlocale(locale.LC_ALL, "vi_VN.UTF-8")
print(locale.format_string("%d", 100000, grouping=True))
