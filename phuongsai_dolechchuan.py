#phương sai
def tinh_phuong_sai(danh_sach_so):
    # Tính giá trung bình của các số
    trung_binh = sum(danh_sach_so) / len(danh_sach_so)
    
    # Tính phương sai
    phuong_sai = sum((x - trung_binh) ** 2 for x in danh_sach_so) / len(danh_sach_so)
    
    return phuong_sai

# Nhập danh sách các số
danh_sach_so = [1, 2, 3, 4, 5]

# Gọi hàm để tính phương sai
phuong_sai = tinh_phuong_sai(danh_sach_so)

# In kết quả
print(f'Phương sai của danh sách là: {phuong_sai}')
#độ lệch chuẩn
import math

def tinh_do_lech_chuan(danh_sach_so):
    # Tính giá trung bình của các số
    trung_binh = sum(danh_sach_so) / len(danh_sach_so)
    
    # Tính tổng bình phương khoảng cách từ mỗi số đến giá trung bình
    tong_binh_phuong = sum((x - trung_binh) ** 2 for x in danh_sach_so)
    
    # Tính độ lệch chuẩn bằng cách lấy căn bậc hai của tổng bình phương chia cho số lượng số
    do_lech_chuan = math.sqrt(tong_binh_phuong / len(danh_sach_so))
    
    return do_lech_chuan

# Nhập danh sách các số
danh_sach_so = [1, 2, 3, 4, 5]

# Gọi hàm để tính độ lệch chuẩn
do_lech_chuan = tinh_do_lech_chuan(danh_sach_so)

# In kết quả
print(f'Độ lệch chuẩn của danh sách là: {do_lech_chuan}')