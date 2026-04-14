import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ======================
# 1. TIÊU ĐỀ
# ======================
st.title("Dự báo dự phòng rủi ro tín dụng (LLP)")


# ======================
# 2. MÔ HÌNH
# ======================
st.subheader("Mô hình hồi quy")

st.latex(r"LLP = -0.0339 + 0.249NIM + 0.064NPL - 0.281ROA + 0.00212SIZE")

st.write("""
Giải thích:
- NIM: Thu nhập lãi cận biên → tăng thì LLP tăng
- NPL: Tỷ lệ nợ xấu → tăng thì LLP tăng mạnh
- ROA: Lợi nhuận trên tài sản → tăng thì LLP giảm
- SIZE: Quy mô ngân hàng → tăng thì LLP tăng
""")

# ======================
# 3. INPUT
# ======================
st.subheader("Nhập dữ liệu")

nim = st.slider("NIM", 0.0, 0.1, 0.03)
npl = st.slider("NPL", 0.0, 0.2, 0.02)
roa = st.slider("ROA", 0.0, 0.05, 0.01)
size = st.slider("SIZE", 14.0, 22.0, 17.5)

st.write("""
Chú thích:
- Giá trị mặc định được lấy gần với trung bình trong bài nghiên cứu
- Người dùng có thể thay đổi để xem tác động
""")

# ======================
# 4. TÍNH LLP
# ======================
llp = -0.0339 + 0.249*nim + 0.064*npl - 0.281*roa + 0.00212*size

st.subheader("Kết quả dự báo")
st.write("LLP =", round(llp, 5))

# ======================
# 5. ĐÁNH GIÁ
# ======================
st.subheader("Đánh giá mức độ rủi ro")

if llp > 0.02:
    st.write("Rủi ro cao: Ngân hàng có khả năng phải trích lập dự phòng lớn.")
elif llp > 0.01:
    st.write("Rủi ro trung bình: Cần theo dõi thêm các chỉ số tài chính.")
else:
    st.write("Rủi ro thấp: Tình hình tín dụng tương đối ổn định.")

# ======================
# 6. BIỂU ĐỒ NIM
# ======================
st.subheader("Phân tích ảnh hưởng của NIM")

x = np.linspace(0, 0.1, 50)
y = -0.0339 + 0.249*x + 0.064*npl - 0.281*roa + 0.00212*size

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("NIM")
ax.set_ylabel("LLP")

st.pyplot(fig)

st.write("""
Nhận xét:
- Khi NIM tăng thì LLP tăng
- Điều này cho thấy hoạt động cho vay nhiều hơn sẽ làm rủi ro tín dụng tăng
""")

# ======================
# 7. BIỂU ĐỒ NPL
# ======================
st.subheader("Phân tích ảnh hưởng của NPL")

x2 = np.linspace(0, 0.2, 50)
y2 = -0.0339 + 0.249*nim + 0.064*x2 - 0.281*roa + 0.00212*size

fig2, ax2 = plt.subplots()
ax2.plot(x2, y2)
ax2.set_xlabel("NPL")
ax2.set_ylabel("LLP")

st.pyplot(fig2)

st.write("""
Nhận xét:
- NPL tăng làm LLP tăng mạnh
- Đây là yếu tố quan trọng nhất ảnh hưởng đến rủi ro tín dụng
""")

# ======================
# 8. BIỂU ĐỒ ROA
# ======================
st.subheader("Phân tích ảnh hưởng của ROA")

x3 = np.linspace(0, 0.05, 50)
y3 = -0.0339 + 0.249*nim + 0.064*npl - 0.281*x3 + 0.00212*size

fig3, ax3 = plt.subplots()
ax3.plot(x3, y3)
ax3.set_xlabel("ROA")
ax3.set_ylabel("LLP")

st.pyplot(fig3)

st.write("""
Nhận xét:
- ROA tăng làm LLP giảm
- Ngân hàng hoạt động hiệu quả sẽ giảm rủi ro tín dụng
""")

# ======================
# 9. KẾT LUẬN
# ======================
st.subheader("Kết luận")

st.write("""
- LLP tăng khi NIM và NPL tăng
- LLP giảm khi ROA tăng
- NPL là yếu tố ảnh hưởng mạnh nhất


""")

