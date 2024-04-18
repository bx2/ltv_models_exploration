import streamlit as st

# Define a simple function to calculate Flexible LTV
def calculate_flexible_ltv(lgm, r, disc_rate):
    # Ensure that the denominator does not go to zero
    if 1 + disc_rate - r == 0:
        return "Undefined (division by zero)"
    return lgm * (r / (1 + disc_rate - r))

# Add custom CSS for styling
st.markdown("""
<style>
.big-font {
    font-size:18px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title('Flexible LTV Calculator')
st.write("This interactive tool helps you explore the impact of various parameters on the Flexible Lifetime Value (LTV) of customers.")

# Display the Flexible LTV formula
st.markdown('<div class="big-font">Flexible LTV Formula:</div>', unsafe_allow_html=True)
st.latex(r'\text{Flexible LTV} = LGM \times \left(\frac{R}{1 + r - R}\right)')

# Explanation of parameters
st.markdown("""
### Where:
- **Lifetime Gross Margin (LGM):** The total profit generated from an average customer over their lifetime, considering the gross margin.
- **Retention Rate (R):** The percentage of customers from the start of the period who remain at the end of the period.
- **Discount Rate (r):** The interest rate used to discount future cash flows back to their present value.
""")

st.write("---")

# Setting up sliders
lgm = st.slider('Lifetime Gross Margin (LGM)', min_value=0.1, max_value=1.0, value=0.5, step=0.01)
r = st.slider('Retention Rate (R) [0-1 scale]', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
disc_rate = st.slider('Discount Rate (r) [0-1 scale]', min_value=0.01, max_value=1.0, value=0.05, step=0.01)

st.write("---")

# Calculate LTV
flexible_ltv = calculate_flexible_ltv(lgm, r, disc_rate)

# Display LTV
st.write(f"Flexible LTV: {flexible_ltv}")


