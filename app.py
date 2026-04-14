import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ======================
# 1. TIÊU ĐỀ
# ======================
st.title("Dự báo dự phòng rủi ro tín dụng (LLP)")

st.write("Nhập các chỉ số tài chính để dự báo mức độ rủi ro tín dụng của ngân hàng.")

# ======================
# 2. MÔ HÌNH
# ======================
st.subheader("Mô hình sử dụng")

st.latex(r"LLP = -0.0339 + 0.249NIM + 0.064NPL - 0.281ROA + 0.00212SIZE")

# ======================
# 3. NHẬP DỮ LIỆU
# ======================
st.subheader("Nhập dữ liệu")

nim = st.slider("NIM", 0.0, 0.1, 0.03)
npl = st.slider("NPL", 0.0, 0.2, 0.02)
roa = st.slider("ROA", 0.0, 0.05, 0.01)
size = st.slider("SIZE", 14.0, 22.0, 17.5)

# ======================
# 4. TÍNH LLP
# ======================
llp = -0.0339 + 0.249*nim + 0.064*npl - 0.281*roa + 0.00212*size

st.subheader("Kết quả")
st.write("LLP dự báo:", round(llp, 5))

# ======================
# 5. ĐÁNH GIÁ
# ======================
if llp > 0.02:
    st.write("Rủi ro cao")
elif llp > 0.01:
    st.write("Rủi ro trung bình")
else:
    st.write("Rủi ro thấp")

# ======================
# 6. BIỂU ĐỒ NIM
# ======================
st.subheader("Ảnh hưởng của NIM")

x = np.linspace(0, 0.1, 50)
y = -0.0339 + 0.249*x + 0.064*npl - 0.281*roa + 0.00212*size

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("NIM")
ax.set_ylabel("LLP")

st.pyplot(fig)

st.write("Khi NIM tăng thì LLP tăng.")

# ======================
# 7. BIỂU ĐỒ NPL
# ======================
st.subheader("Ảnh hưởng của NPL")

x2 = np.linspace(0, 0.2, 50)
y2 = -0.0339 + 0.249*nim + 0.064*x2 - 0.281*roa + 0.00212*size

fig2, ax2 = plt.subplots()
ax2.plot(x2, y2)
ax2.set_xlabel("NPL")
ax2.set_ylabel("LLP")

st.pyplot(fig2)

st.write("Nợ xấu tăng làm LLP tăng.")

# ======================
# 8. BIỂU ĐỒ ROA
# ======================
st.subheader("Ảnh hưởng của ROA")

x3 = np.linspace(0, 0.05, 50)
y3 = -0.0339 + 0.249*nim + 0.064*npl - 0.281*x3 + 0.00212*size

fig3, ax3 = plt.subplots()
ax3.plot(x3, y3)
ax3.set_xlabel("ROA")
ax3.set_ylabel("LLP")

st.pyplot(fig3)

st.write("ROA tăng làm LLP giảm.")

# ======================
# 9. KẾT LUẬN
# ======================
st.subheader("Kết luận")

st.write("""
LLP tăng khi NIM, NPL tăng.  
LLP giảm khi ROA tăng.  
""")
