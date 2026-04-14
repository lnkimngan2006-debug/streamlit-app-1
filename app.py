import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ======================
# TIÊU ĐỀ
# ======================
st.title("Dashboard dự báo LLP")

st.write("Ứng dụng dự báo rủi ro tín dụng dựa trên mô hình hồi quy.")

# ======================
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

st.subheader("Kết quả dự báo")
st.metric("LLP", round(llp, 5))

# ======================
# ======================
col1, col2 = st.columns(2)

# ======================
# BIỂU ĐỒ NIM
# ======================
with col1:
    x = np.linspace(0, 0.1, 50)
    y = -0.0339 + 0.249*x + 0.064*npl - 0.281*roa + 0.00212*size

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='LLP'))

    fig.update_layout(
        title="Ảnh hưởng NIM → LLP",
        xaxis_title="NIM",
        yaxis_title="LLP"
    )

    st.plotly_chart(fig, use_container_width=True)

# ======================
# BIỂU ĐỒ NPL
# ======================
with col2:
    x2 = np.linspace(0, 0.2, 50)
    y2 = -0.0339 + 0.249*nim + 0.064*x2 - 0.281*roa + 0.00212*size

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='LLP'))

    fig2.update_layout(
        title="Ảnh hưởng NPL → LLP",
        xaxis_title="NPL",
        yaxis_title="LLP"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ======================
# BIỂU ĐỒ ROA (full width)
# ======================
x3 = np.linspace(0, 0.05, 50)
y3 = -0.0339 + 0.249*nim + 0.064*npl - 0.281*x3 + 0.00212*size

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x3, y=y3, mode='lines', name='LLP'))

fig3.update_layout(
    title="Ảnh hưởng ROA → LLP",
    xaxis_title="ROA",
    yaxis_title="LLP"
)

st.plotly_chart(fig3, use_container_width=True)

# ======================
# NHẬN XÉT
# ======================
st.subheader("Nhận xét")

st.write("""
- NIM tăng → LLP tăng  
- NPL tăng → LLP tăng mạnh  
- ROA tăng → LLP giảm  

NPL là yếu tố ảnh hưởng lớn nhất đến rủi ro tín dụng.
""")
