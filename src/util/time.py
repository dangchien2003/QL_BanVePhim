from datetime import datetime


def convertTimeStampToString(timeStamp, format="%H:%M:%S %d-%m-%Y "):
    try:
        date_time = datetime.fromtimestamp(int(timeStamp))
        date_string = date_time.strftime(format)

        return date_string
    except:
        print("Lỗi chuyển đổi thời gian")
        return None
