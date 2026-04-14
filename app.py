import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===== TIÊU ĐỀ =====
st.title("Dự báo dự phòng rủi ro tín dụng (Loan Loss Provision - LLP)")

st.write("Ứng dụng mô phỏng tác động của các yếu tố tài chính đến rủi ro tín dụng ngân hàng.")

st.write("""
- NIM: Thu nhập lãi cận biên (+)
- NPL: Tỷ lệ nợ xấu (+)
- ROA: Lợi nhuận trên tài sản (-)
- SIZE: Quy mô ngân hàng (+)
""")

# ===== INPUT =====
st.sidebar.header("Nhập dữ liệu")

nim = st.sidebar.slider("NIM (Net Interest Margin)", 0.0, 0.1, 0.03)
npl = st.sidebar.slider("NPL (Non-Performing Loans)", 0.0, 0.2, 0.02)
roa = st.sidebar.slider("ROA (Return on Assets)", 0.0, 0.05, 0.01)
size = st.sidebar.slider("SIZE (Quy mô ngân hàng)", 14.0, 22.0, 17.5)

# ===== TÍNH LLP =====
llp = -0.0339 + 0.249*nim + 0.064*npl - 0.281*roa + 0.00212*size

st.subheader("Kết quả dự báo")
st.write("Giá trị LLP:", round(llp, 5))

# ======================
# BIỂU ĐỒ NIM
# ======================
st.subheader("Biểu đồ 1: Mối quan hệ giữa NIM và LLP")

x = np.linspace(0, 0.1, 50)
y = -0.0339 + 0.249*x + 0.064*npl - 0.281*roa + 0.00212*size

fig, ax = plt.subplots()
ax.plot(x, y)

current_llp = llp
ax.scatter(nim, current_llp)

ax.set_xlabel("NIM (Net Interest Margin)")
ax.set_ylabel("LLP")

st.pyplot(fig)

st.caption("""
Chú thích: Biểu đồ thể hiện mối quan hệ cùng chiều giữa NIM và LLP.
Khi NIM tăng, ngân hàng mở rộng hoạt động cho vay, từ đó làm gia tăng rủi ro tín dụng và mức trích lập dự phòng.
""")

# ======================
# BIỂU ĐỒ NPL
# ======================
st.subheader("Biểu đồ 2: Mối quan hệ giữa NPL và LLP")

x2 = np.linspace(0, 0.2, 50)
y2 = -0.0339 + 0.249*nim + 0.064*x2 - 0.281*roa + 0.00212*size

fig2, ax2 = plt.subplots()
ax2.plot(x2, y2)
ax2.scatter(npl, current_llp)

ax2.set_xlabel("NPL (Non-Performing Loans)")
ax2.set_ylabel("LLP")

st.pyplot(fig2)

st.caption("""
Chú thích: Biểu đồ cho thấy mối quan hệ cùng chiều mạnh giữa NPL và LLP.
Khi tỷ lệ nợ xấu tăng, ngân hàng phải tăng trích lập dự phòng để bù đắp rủi ro tín dụng.
""")

# ======================
# BIỂU ĐỒ ROA
# ======================
st.subheader("Biểu đồ 3: Mối quan hệ giữa ROA và LLP")

x3 = np.linspace(0, 0.05, 50)
y3 = -0.0339 + 0.249*nim + 0.064*npl - 0.281*x3 + 0.00212*size

fig3, ax3 = plt.subplots()
ax3.plot(x3, y3)
ax3.scatter(roa, current_llp)

ax3.set_xlabel("ROA (Return on Assets)")
ax3.set_ylabel("LLP")

st.pyplot(fig3)

st.caption("""
Chú thích: Biểu đồ thể hiện mối quan hệ ngược chiều giữa ROA và LLP.
Khi hiệu quả hoạt động của ngân hàng tăng, rủi ro tín dụng giảm, dẫn đến mức dự phòng thấp hơn.
""")

# ===== KẾT LUẬN =====
st.subheader("Kết luận")

st.write("""
- NIM và NPL có tác động cùng chiều đến LLP  
- ROA có tác động ngược chiều đến LLP  
- NPL là yếu tố ảnh hưởng mạnh nhất đến rủi ro tín dụng  

Các biểu đồ giúp minh họa trực quan mối quan hệ giữa các biến tài chính và mức dự phòng rủi ro.
""")



