import streamlit as st

# Define a simple function to calculate Predictive LTV
def calculate_predictive_ltv(n_trans, aov, gm, cl, n_cust):
    return (n_trans * aov * gm * cl) / n_cust

# Custom CSS
st.markdown("""
<style>
.big-font {
    font-size:18px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# App title and introduction
st.title('Predictive LTV Calculator')
st.write("This tool allows you to interactively explore how different variables affect the Predictive Lifetime Value (LTV) of customers.")

# Display the formula
st.markdown('<div class="big-font">Predictive LTV Formula:</div>', unsafe_allow_html=True)
st.latex(r'\text{Predictive LTV} = \frac{N_{\text{trans}} \times AOV \times GM \times CL}{N_{\text{cust}}}')

st.text("Where:")
st.text("N_trans = Number of Transactions")
st.text("AOV = Average Order Value")
st.text("GM = Gross Margin (as a fraction)")
st.text("CL = Customer Lifetime (in years)")
st.text("N_cust = Number of Customers")

st.write("---")

# Sliders
n_trans = st.slider('Number of Transactions (N_trans)', 10, 1000, 100)
aov = st.slider('Average Order Value (AOV)', 10.0, 1000.0, 100.0)
gm = st.slider('Gross Margin (GM) [0-1 scale]', 0.1, 1.0, 0.5)
cl = st.slider('Customer Lifetime (CL) [in years]', 0.1, 10.0, 1.0)
n_cust = st.slider('Number of Customers (N_cust)', 10, 10000, 1000)

st.write("---")

# Calculation and display
ltv = calculate_predictive_ltv(n_trans, aov, gm, cl, n_cust)
st.write(f"Predictive LTV: {ltv:.2f}")

