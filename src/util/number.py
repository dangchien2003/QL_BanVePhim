import locale

locale.setlocale(locale.LC_ALL, "vi_VN.UTF-8")


def convertPrice(price):
    return locale.format_string("%d", price, grouping=True)
