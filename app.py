import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Dashboard du bao LLP")

# =======================
# TẠO DỮ LIỆU
# =======================
llp = np.random.normal(0.04, 0.01, 50)
npl_data = np.random.uniform(0.01, 0.1, 50)

# =======================
# BIỂU ĐỒ 1: HISTOGRAM
# =======================
fig1, ax1 = plt.subplots()
ax1.hist(llp, bins=10)
ax1.set_title("Phan phoi LLP")

st.pyplot(fig1)

# CHÚ THÍCH
st.write("Biểu đồ này thể hiện phân phối của LLP.")
st.write("Giá trị LLP tập trung quanh mức trung bình.")

# =======================
# BIỂU ĐỒ 2: SCATTER
# =======================
fig2, ax2 = plt.subplots()
ax2.scatter(npl_data, llp)
ax2.set_title("Quan he NPL va LLP")

st.pyplot(fig2)

# CHÚ THÍCH
st.write("Biểu đồ này thể hiện mối quan hệ giữa NPL và LLP.")
st.write("Khi NPL tăng, LLP có xu hướng tăng.")

# =======================
# INPUT
# =======================
st.subheader("Nhap gia tri du bao")

npl = st.slider("NPL", 0.0, 0.2, 0.05, key="npl")
roa = st.slider("ROA", 0.0, 0.05, 0.01, key="roa")
size = st.slider("SIZE", 14.0, 22.0, 18.0, key="size")

# =======================
# DỰ BÁO
# =======================
llp_pred = -0.0339 \
           + 0.249139 * nim \
           + 0.064820 * npl \
           - 0.281107 * roa \
           + 0.00212 * size

st.write("LLP dự báo:", round(llp_pred, 4))

# CHÚ THÍCH
st.write("Nguoi dung co the thay doi cac bien de xem ket qua du bao.")
