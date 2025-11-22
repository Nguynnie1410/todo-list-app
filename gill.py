# Chương trình tính tổng các số nguyên do người dùng nhập

def tinh_tong():
    try:
        # Nhập danh sách số, cách nhau bởi dấu cách
        chuoi_so = input("Nhập các số nguyên, cách nhau bởi dấu cách: ").strip()
        
        # Kiểm tra chuỗi rỗng
        if not chuoi_so:
            print("Bạn chưa nhập số nào.")
            return
        
        # Chuyển đổi sang danh sách số nguyên
        danh_sach_so = list(map(int, chuoi_so.split()))
        
        # Tính tổng
        tong = sum(danh_sach_so)
        
        print(f"Tổng các số bạn nhập là: {tong}")
    
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên hợp lệ.")

if __name__ == "__main__":
    tinh_tong()
