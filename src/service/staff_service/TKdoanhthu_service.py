import sys
import os
import calendar
import time
from datetime import date, datetime
from src.util import time
from src.util.response import Res
from src.repository.TKdoanhthu_reponsitory import TKdoanhthuRepository
from src.model.dulieudoanhthu import DuLieuDoanhThu
class GetTKdoanhthu_Service():

   

    def __init__(self):
        self.Repository = TKdoanhthuRepository()
        return
    def fillter(self, style, day, month, year):
        start_timestamp = 0
        end_timestamp = 0
       
        print(style)
       
        if style == 1:
            
            start_timestamp = time.convertTimeToTimestamp(f"{day}-{month}-{year}", "%d-%m-%Y")
            end_timestamp = start_timestamp + 86400 
        elif style ==2:
            start_timestamp = time.convertTimeToTimestamp(f"{month}-{year}", "%m-%Y")
            days = calendar.monthrange(year, month)[1]
            end_timestamp = start_timestamp + 86400 * days
        elif style ==3:
            start_timestamp = time.convertTimeToTimestamp(f"{year}", "%Y")
            days = 366 if calendar.isleap(year) else 365 
            end_timestamp = start_timestamp + 86400 * days 
        else:
            return Res(False, "Không hỗ trợ, vui lòng nhập lại")
    
    
        result = self.Repository.getInfo(start_timestamp,end_timestamp)
        ketQuaThongKe = self.thongKeNgay(result)
        return Res(True, data=ketQuaThongKe)
        
    def thongKeNgay(self, data):
        if not data:  # Kiểm tra nếu danh sách data rỗng
            raise ValueError("Không có dữ liệu cho ngày được chọn")
        
        doanhthuve = doanhthunuoc = doanhthubong = 0
        array = []
        for item in data:
            doanhthuve += item[1]
            doanhthunuoc += item[2]
            doanhthubong += item[3]

        sum = doanhthuve + doanhthunuoc + doanhthubong
        date = time.convertTimeStampToString(data[0][0], "%d-%m-%Y")
        
        array.append(DuLieuDoanhThu(date, doanhthuve, doanhthunuoc, doanhthubong, sum))
        return array
    
    def thongKeThang(self, data, timestamp):
        daily_data = time.convertTimeStampToString(data[0][0], "%d-%m-%Y")
        
        # Tính toán doanh thu cho từng ngày
        for item in data:
            day = time.convertTimeToTimestamp(item[0])
            daily_data[day][0] += item[1]  # doanhthuve
            daily_data[day][1] += item[2]  # doanhthunuoc
            daily_data[day][2] += item[3]  # doanhthubong
        result = []
        for day, values in daily_data.items():
            doanhthuve, doanhthunuoc, doanhthubong = values
            sum = doanhthuve + doanhthunuoc + doanhthubong
            result.append(DuLieuDoanhThu(day, doanhthuve, doanhthunuoc, doanhthubong, sum))

        return result
    def checkdate(self,style, day, month, year):
        result = self.Repository(style, day, month, year)  # Giả sử đây là phương thức lấy dữ liệu
        if not result:
            return Res(success=False, message="Không có dữ liệu cho ngày được chọn")
        try:
            ketQuaThongKe = self.thongKeNgay(result)
            return Res(success=True, data=ketQuaThongKe)
        except Exception as e:
            return Res(success=False, message=str(e))



       