import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===== TIÊU ĐỀ =====
st.title("Dự báo rủi ro tín dụng (LLP)")

# ===== INPUT =====
st.sidebar.header("Nhập dữ liệu")

nim = st.sidebar.slider("NIM", 0.0, 0.1, 0.03)
npl = st.sidebar.slider("NPL", 0.0, 0.2, 0.02)
roa = st.sidebar.slider("ROA", 0.0, 0.05, 0.01)
size = st.sidebar.slider("SIZE", 14.0, 22.0, 17.5)

# ===== TÍNH LLP =====
llp = -0.0339 + 0.249*nim + 0.064*npl - 0.281*roa + 0.00212*size

st.subheader("Kết quả")
st.write("LLP:", round(llp, 5))

# ======================
# BIỂU ĐỒ NIM
# ======================
st.subheader("Ảnh hưởng của NIM")

x = np.linspace(0, 0.1, 50)
y = -0.0339 + 0.249*x + 0.064*npl - 0.281*roa + 0.00212*size

fig, ax = plt.subplots()
ax.plot(x, y)

# điểm hiện tại
current_llp = llp
ax.scatter(nim, current_llp)

ax.set_xlabel("NIM")
ax.set_ylabel("LLP")

st.pyplot(fig)

st.write("Nhận xét: Khi NIM tăng thì LLP tăng → ngân hàng cho vay nhiều hơn dẫn đến rủi ro tăng.")

# ======================
# BIỂU ĐỒ NPL
# ======================
st.subheader("Ảnh hưởng của NPL")

x2 = np.linspace(0, 0.2, 50)
y2 = -0.0339 + 0.249*nim + 0.064*x2 - 0.281*roa + 0.00212*size

fig2, ax2 = plt.subplots()
ax2.plot(x2, y2)
ax2.scatter(npl, current_llp)

ax2.set_xlabel("NPL")
ax2.set_ylabel("LLP")

st.pyplot(fig2)

st.write("Nhận xét: NPL tăng làm LLP tăng mạnh → nợ xấu là yếu tố ảnh hưởng lớn nhất.")

# ======================
# BIỂU ĐỒ ROA
# ======================
st.subheader("Ảnh hưởng của ROA")

x3 = np.linspace(0, 0.05, 50)
y3 = -0.0339 + 0.249*nim + 0.064*npl - 0.281*x3 + 0.00212*size

fig3, ax3 = plt.subplots()
ax3.plot(x3, y3)
ax3.scatter(roa, current_llp)

ax3.set_xlabel("ROA")
ax3.set_ylabel("LLP")

st.pyplot(fig3)

st.write("Nhận xét: ROA tăng làm LLP giảm → ngân hàng hoạt động hiệu quả thì rủi ro giảm.")



