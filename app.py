import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from scipy.stats import norm

def sample_size(N, margin_error=0.05, confidence_level=0.95, p=0.5):
    Z = norm.ppf(1 - (1 - confidence_level) / 2)
    n0 = (Z**2 * p * (1 - p)) / margin_error**2
    n = n0 / (1 + (n0 - 1) / N)
    return round(n)

# Streamlit UI
st.set_page_config(page_title="Sample Size Calculator")  # Unique browser tab title
st.title("Sample Size Calculator")
st.write("Calculate the required sample size for a survey and visualize how input parameters affect it.")

# Inputs
col1, col2 = st.columns(2)
with col1:
    N = st.number_input("Population Size (N)", min_value=1, value=1300000, step=1)
with col2:
    margin_error = st.number_input("Margin of Error", min_value=0.01, max_value=0.5, value=0.05, step=0.01)

col3, col4 = st.columns(2)
with col3:
    confidence_level = st.number_input("Confidence Level", min_value=0.8, max_value=0.999, value=0.95, step=0.01)
with col4:
    p = st.number_input("Proportion (p)", min_value=0.01, max_value=0.99, value=0.5, step=0.01)

# Calculate and display
if st.button("Calculate Sample Size"):
    result = sample_size(N, margin_error, confidence_level, p)
    st.success(f"The required sample size is: **{result}**")

# Plots
st.markdown("---")
st.subheader("Graphs: Sample Size vs. Input Parameters")

# 1. Sample Size vs. Margin of Error
margin_errors = np.linspace(0.01, 0.2, 100)
sample_sizes_me = [sample_size(N, me, confidence_level, p) for me in margin_errors]
fig1, ax1 = plt.subplots()
ax1.plot(margin_errors, sample_sizes_me)
ax1.set_xlabel("Margin of Error")
ax1.set_ylabel("Sample Size")
ax1.set_title("Sample Size vs. Margin of Error")
st.pyplot(fig1)

# 2. Sample Size vs. Confidence Level
confidence_levels = np.linspace(0.8, 0.999, 100)
sample_sizes_cl = [sample_size(N, margin_error, cl, p) for cl in confidence_levels]
fig2, ax2 = plt.subplots()
ax2.plot(confidence_levels, sample_sizes_cl)
ax2.set_xlabel("Confidence Level")
ax2.set_ylabel("Sample Size")
ax2.set_title("Sample Size vs. Confidence Level")
st.pyplot(fig2)

# 3. Sample Size vs. Proportion (p)
ps = np.linspace(0.01, 0.99, 100)
sample_sizes_p = [sample_size(N, margin_error, confidence_level, p_val) for p_val in ps]
fig3, ax3 = plt.subplots()
ax3.plot(ps, sample_sizes_p)
ax3.set_xlabel("Proportion (p)")
ax3.set_ylabel("Sample Size")
ax3.set_title("Sample Size vs. Proportion (p)")
st.pyplot(fig3)

# Example
st.markdown("---")
st.subheader("Example")
st.write(f"For a population of 1.3 million, 1% margin of error, 99% confidence level, and p=0.5:")
st.write(f"Sample size = **{sample_size(1.3e6, 0.01, 0.99, 0.5)}**")
