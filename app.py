import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ======================
# TIÊU ĐỀ
# ======================
st.title("Dashboard dự báo dự phòng rủi ro tín dụng (LLP)")

st.write("Ứng dụng mô phỏng tác động của các yếu tố tài chính đến rủi ro tín dụng ngân hàng.")

# ======================
# SIDEBAR INPUT
# ======================
st.sidebar.header("Nhập dữ liệu")

nim = st.sidebar.slider("NIM", 0.0, 0.1, 0.03)
npl = st.sidebar.slider("NPL", 0.0, 0.2, 0.02)
roa = st.sidebar.slider("ROA", 0.0, 0.05, 0.01)
size = st.sidebar.slider("SIZE", 14.0, 22.0, 17.5)

# ======================
# MÔ HÌNH
# ======================
st.subheader("Mô hình")

st.latex(r"LLP = -0.0339 + 0.249NIM + 0.064NPL - 0.281ROA + 0.00212SIZE")

# ======================
# TÍNH LLP
# ======================
llp = -0.0339 + 0.249*nim + 0.064*npl - 0.281*roa + 0.00212*size

st.subheader("Kết quả")
st.metric("LLP dự báo", round(llp, 5))

# ======================
# ĐÁNH GIÁ
# ======================
if llp > 0.02:
    st.write("Mức rủi ro: Cao")
elif llp > 0.01:
    st.write("Mức rủi ro: Trung bình")
else:
    st.write("Mức rủi ro: Thấp")

# ======================
# CHIA CỘT BIỂU ĐỒ
# ======================
col1, col2 = st.columns(2)

# ===== NIM =====
with col1:
    x = np.linspace(0, 0.1, 100)
    y = -0.0339 + 0.249*x + 0.064*npl - 0.281*roa + 0.00212*size

    fig, ax = plt.subplots()
    ax.plot(x, y)

    # điểm hiện tại
    current_llp = -0.0339 + 0.249*nim + 0.064*npl - 0.281*roa + 0.00212*size
    ax.scatter(nim, current_llp)

    ax.set_title("NIM → LLP")
    ax.set_xlabel("NIM")
    ax.set_ylabel("LLP")

    st.pyplot(fig, clear_figure=True)

# ===== NPL =====
with col2:
    x2 = np.linspace(0, 0.2, 100)
    y2 = -0.0339 + 0.249*nim + 0.064*x2 - 0.281*roa + 0.00212*size

    fig2, ax2 = plt.subplots()
    ax2.plot(x2, y2)

    ax2.scatter(npl, current_llp)

    ax2.set_title("NPL → LLP")
    ax2.set_xlabel("NPL")
    ax2.set_ylabel("LLP")

    st.pyplot(fig2, clear_figure=True)

# ===== ROA =====
x3 = np.linspace(0, 0.05, 100)
y3 = -0.0339 + 0.249*nim + 0.064*npl - 0.281*x3 + 0.00212*size

fig3, ax3 = plt.subplots()
ax3.plot(x3, y3)

ax3.scatter(roa, current_llp)

ax3.set_title("ROA → LLP")
ax3.set_xlabel("ROA")
ax3.set_ylabel("LLP")

st.pyplot(fig3, clear_figure=True)

# ======================
# NHẬN XÉT
# ======================
st.subheader("Nhận xét")

st.write("""
- NIM tăng → LLP tăng  
- NPL tăng → LLP tăng mạnh  
- ROA tăng → LLP giảm  

Điểm trên biểu đồ thể hiện giá trị hiện tại theo dữ liệu đã nhập.
""")

# ======================
# KẾT LUẬN
# ======================
st.subheader("Kết luận")

st.write("""
Mô hình cho thấy tỷ lệ nợ xấu (NPL) là yếu tố ảnh hưởng mạnh nhất đến rủi ro tín dụng.
Ứng dụng giúp mô phỏng và hiểu mối quan hệ giữa các biến tài chính và LLP.
""")


""")

