import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ======================
# 1. TIÊU ĐỀ
# ======================
st.title("Dự báo dự phòng rủi ro tín dụng (Loan Loss Provision - LLP)")

st.write("""
Ứng dụng mô phỏng mức độ rủi ro tín dụng của ngân hàng dựa trên mô hình hồi quy.
Các biến đầu vào được sử dụng để đánh giá tác động đến mức trích lập dự phòng (LLP).
""")

# ======================
# 2. MÔ HÌNH
# ======================
st.subheader("Mô hình hồi quy")

st.latex(r"LLP = -0.0339 + 0.249NIM + 0.064NPL - 0.281ROA + 0.00212SIZE")

st.write("""
Trong đó:
- LLP (Loan Loss Provision): Dự phòng rủi ro tín dụng  
- NIM (Net Interest Margin): Thu nhập lãi cận biên  
- NPL (Non-Performing Loans): Tỷ lệ nợ xấu  
- ROA (Return on Assets): Tỷ suất sinh lời trên tài sản  
- SIZE: Quy mô ngân hàng (log tổng tài sản)  
""")

st.write("""
Ý nghĩa hệ số:
- NIM (+): Khi NIM tăng → LLP tăng  
- NPL (+): Khi nợ xấu tăng → LLP tăng mạnh  
- ROA (-): Khi hiệu quả hoạt động tăng → LLP giảm  
- SIZE (+): Ngân hàng lớn → mức dự phòng cao hơn  
""")

# ======================
# 3. INPUT
# ======================
st.subheader("Nhập dữ liệu")

nim = st.slider("NIM (Net Interest Margin)", 0.0, 0.1, 0.03)
npl = st.slider("NPL (Non-Performing Loans)", 0.0, 0.2, 0.02)
roa = st.slider("ROA (Return on Assets)", 0.0, 0.05, 0.01)
size = st.slider("SIZE (Quy mô ngân hàng)", 14.0, 22.0, 17.5)

st.write("""
Chú thích:
Các giá trị mặc định được lựa chọn gần với giá trị trung bình trong nghiên cứu.
Người dùng có thể thay đổi để quan sát tác động đến LLP.
""")

# ======================
# 4. TÍNH LLP
# ======================
llp = -0.0339 + 0.249*nim + 0.064*npl - 0.281*roa + 0.00212*size

st.subheader("Kết quả dự báo")
st.write("Giá trị LLP:", round(llp, 5))

# ======================
# 5. BIỂU ĐỒ 1
# ======================
st.subheader("Biểu đồ 1: Mối quan hệ giữa NIM và LLP")

x = np.linspace(0, 0.1, 50)
y = -0.0339 + 0.249*x + 0.064*npl - 0.281*roa + 0.00212*size

fig, ax = plt.subplots()
ax.plot(x, y)
ax.scatter(nim, llp)

ax.set_xlabel("NIM (Net Interest Margin)")
ax.set_ylabel("LLP")

st.pyplot(fig)

st.caption("""
Chú thích: Biểu đồ thể hiện mối quan hệ cùng chiều giữa NIM và LLP.
Khi NIM tăng, ngân hàng mở rộng hoạt động tín dụng, làm gia tăng rủi ro và mức trích lập dự phòng.
""")

# ======================
# 6. BIỂU ĐỒ 2
# ======================
st.subheader("Biểu đồ 2: Mối quan hệ giữa NPL và LLP")

x2 = np.linspace(0, 0.2, 50)
y2 = -0.0339 + 0.249*nim + 0.064*x2 - 0.281*roa + 0.00212*size

fig2, ax2 = plt.subplots()
ax2.plot(x2, y2)
ax2.scatter(npl, llp)

ax2.set_xlabel("NPL (Non-Performing Loans)")
ax2.set_ylabel("LLP")

st.pyplot(fig2)

st.caption("""
Chú thích: Biểu đồ cho thấy mối quan hệ cùng chiều mạnh giữa NPL và LLP.
Khi tỷ lệ nợ xấu tăng, ngân hàng phải tăng trích lập dự phòng để bù đắp rủi ro tín dụng.
""")

# ======================
# 7. BIỂU ĐỒ 3
# ======================
st.subheader("Biểu đồ 3: Mối quan hệ giữa ROA và LLP")

x3 = np.linspace(0, 0.05, 50)
y3 = -0.0339 + 0.249*nim + 0.064*npl - 0.281*x3 + 0.00212*size

fig3, ax3 = plt.subplots()
ax3.plot(x3, y3)
ax3.scatter(roa, llp)

ax3.set_xlabel("ROA (Return on Assets)")
ax3.set_ylabel("LLP")

st.pyplot(fig3)

st.caption("""
Chú thích: Biểu đồ thể hiện mối quan hệ ngược chiều giữa ROA và LLP.
Khi ngân hàng hoạt động hiệu quả hơn, rủi ro tín dụng giảm, do đó mức dự phòng cũng giảm.
""")

# ======================
# 8. KẾT LUẬN
# ======================
st.subheader("Kết luận")

st.write("""
- NIM và NPL có tác động cùng chiều đến LLP  
- ROA có tác động ngược chiều đến LLP  
- NPL là yếu tố ảnh hưởng mạnh nhất đến rủi ro tín dụng  

Ứng dụng giúp minh họa trực quan mối quan hệ giữa các biến tài chính và dự phòng rủi ro tín dụng.
""")


