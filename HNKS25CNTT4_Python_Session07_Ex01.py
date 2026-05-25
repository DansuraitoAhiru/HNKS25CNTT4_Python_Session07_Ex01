# code gốc
# student_name = "   nguYEn vAn a   "
# student_code = "   rk-001-python   "
# email = "   Student01@GMAIL.COM   "

# student_name.strip()
# student_name.title()

# student_code.strip()
# student_code.upper()

# email.strip()
# email.lower()

# print("Họ tên:", student_name)
# print("Mã học viên:", student_code)
# print("Email:", email)

# Phân tích lỗi:
# student_name.strip() không làm thay đổi trực tiếp biến student_name do tính bất biến của string, sau khi tạo ko thể thay đổi giá trị đc, trừ khi gán lại biến
# student_name.title() không tạo ra kết quả "Nguyen Van A" trong chương trình hiện tại do tính bất biến của string, sau khi tạo ko thể thay đổi giá trị đc, trừ khi gán lại biến
# student_code.upper() không làm mã học viên chuyển thành chữ hoa do tính bất biến của string, sau khi tạo ko thể thay đổi giá trị đc, trừ khi gán lại biến
# email.lower() không làm email chuyển thành chữ thường do tính bất biến của string, sau khi tạo ko thể thay đổi giá trị đc, trừ khi gán lại biến

student_name = "   nguYEn vAn a   "
student_code = "   rk-001-python   "
email = "   Student01@GMAIL.COM   "

student_name = student_name.strip().title()

student_code = student_code.strip().upper()

email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)
