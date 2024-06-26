from datetime import datetime


def convertTimeStampToString(timeStamp, format="%H:%M:%S %d-%m-%Y "):
    try:
        date_time = datetime.fromtimestamp(int(timeStamp))
        date_string = date_time.strftime(format)

        return date_string
    except:
        print("Lỗi chuyển đổi thời gian")
        return None


def convertTimeToTimestamp(date, formatDate):
    try:
        time_object = datetime.strptime(date, formatDate)
        timestamp = time_object.timestamp()
        return timestamp
    except Exception as e:
        print(e)
        print("Lỗi chuyển timestamp")
        return None
