# input
# mã bệnh nhân str, nhiệt độ float, nhịp tim int
"""
 ép kiểu 1
nhiet_do = input("Nhập nhiệt độ: ")
nhiet_do = float(nhiet_do)
"""
"""
ép kiểu 2 
nhiet_do = float(input("Nhập nhiệt độ: "))
"""
# Giải pháp 1: Nhập dữ liệu trước rồi mới ép kiểu giúp học dễ hiểu và dễ dò lỗi, nhưng code dài hơn và sử dụng nhiều biến hơn.
# Giải pháp 2: Ép kiểu ngay khi nhập giúp code ngắn gọn, ít biến hơn và xử lý nhanh hơn, tốc độ và độ chính xác cao.

print("--- HỆ THỐNG CHUẨN HÓA SINH HIỆU ---")
ma_bn = input("Nhập mã bệnh nhân: ")
nhiet_do = float(input("Nhập nhiệt độ cơ thể: "))
nhip_tim = int(input("Nhập nhịp tim: "))
print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print("Mã bệnh nhân:", ma_bn)
print("Nhiệt độ cơ thể:", nhiet_do, "độ C")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(nhiet_do))
print("Nhịp tim:", nhip_tim, "nhịp/phút")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(nhip_tim))
print("---------------------------------")
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")