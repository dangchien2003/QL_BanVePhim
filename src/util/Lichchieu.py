class LichchieuUtil:
    def getInfoTableFromArray(self, data):
        return [(item[0], item[1], item[3]) for item in data]

    def getInfoTable(self, data):
        return (data[0], data[1], data[3])
