import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ======================
# TIÊU ĐỀ
# ======================
st.title("Dashboard dự báo LLP")

# ======================
# SIDEBAR (giống app xịn)
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
# KẾT QUẢ (hiển thị đẹp hơn)
# ======================
llp = -0.0339 + 0.249*nim + 0.064*npl - 0.281*roa + 0.00212*size

st.subheader("Kết quả")
st.metric("LLP", round(llp, 5))

# ======================
# CHIA 2 CỘT
# ======================
col1, col2 = st.columns(2)

# ===== BIỂU ĐỒ NIM =====
with col1:
    x = np.linspace(0, 0.1, 50)
    y = -0.0339 + 0.249*x + 0.064*npl - 0.281*roa + 0.00212*size

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("NIM → LLP")
    ax.set_xlabel("NIM")
    ax.set_ylabel("LLP")

    st.pyplot(fig)

# ===== BIỂU ĐỒ NPL =====
with col2:
    x2 = np.linspace(0, 0.2, 50)
    y2 = -0.0339 + 0.249*nim + 0.064*x2 - 0.281*roa + 0.00212*size

    fig2, ax2 = plt.subplots()
    ax2.plot(x2, y2)
    ax2.set_title("NPL → LLP")
    ax2.set_xlabel("NPL")
    ax2.set_ylabel("LLP")

    st.pyplot(fig2)

# ======================
# BIỂU ĐỒ ROA (FULL)
# ======================
x3 = np.linspace(0, 0.05, 50)
y3 = -0.0339 + 0.249*nim + 0.064*npl - 0.281*x3 + 0.00212*size

fig3, ax3 = plt.subplots()
ax3.plot(x3, y3)
ax3.set_title("ROA → LLP")
ax3.set_xlabel("ROA")
ax3.set_ylabel("LLP")

st.pyplot(fig3)

# ======================
# NHẬN XÉT
# ======================
st.subheader("Nhận xét")

st.write("""
- NIM tăng → LLP tăng  
- NPL tăng → LLP tăng mạnh  
- ROA tăng → LLP giảm  
""")
