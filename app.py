import streamlit as st
import urllib.parse

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="EDC Machine for Chennai Merchants",
    page_icon="💳",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background-color: #f8f9fb;
}

.hero {
    padding: 50px 20px;
    text-align: center;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    color: #555;
}

.plan {
    padding: 25px;
    border-radius: 15px;
    background: white;
    border: 1px solid #e5e5e5;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
}

.price {
    font-size: 38px;
    font-weight: 800;
}

.feature {
    margin: 10px 0;
}

.cta {
    text-align: center;
    padding: 40px 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------

st.markdown("""
<div class="hero">

<h1>Get an EDC Payment Machine for Your Business</h1>

<p>
Accept card and digital payments easily with a payment machine
for your business.
</p>

</div>
""", unsafe_allow_html=True)

if st.button("🚀 Get EDC Machine", use_container_width=True):

    st.session_state["show_form"] = True

st.divider()

# -----------------------------
# BENEFITS
# -----------------------------

st.subheader("Why Get an EDC Machine?")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 💳")
    st.write("Accept Card Payments")

with col2:
    st.markdown("### ⚡")
    st.write("Fast Payment Experience")

with col3:
    st.markdown("### 🧾")
    st.write("Lifetime Paper Roll Benefit*")

with col4:
    st.markdown("### 💰")
    st.write("Flexible Plans")

st.divider()

# -----------------------------
# PLANS
# -----------------------------

st.subheader("Choose Your Plan")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="plan">

    <h2>⭐ Annual Plan</h2>

    <div class="price">₹4,128</div>

    <p>Including GST</p>

    <hr>

    <div class="feature">✔ Setup fee: ₹3,499 + GST</div>
    <div class="feature">✔ No rental</div>
    <div class="feature">✔ No transaction target for rental</div>
    <div class="feature">✔ Lifetime paper roll benefit*</div>
    <div class="feature">✔ Grocery MDR: 1.3%</div>
    <div class="feature">✔ Non-grocery MDR: 1.64%</div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="plan">

    <h2>📅 Monthly Plan</h2>

    <div class="price">₹1,528</div>

    <p>Including GST</p>

    <hr>

    <div class="feature">✔ Setup fee: ₹1,300 + GST</div>
    <div class="feature">✔ ₹470 rental subject to applicable conditions</div>
    <div class="feature">✔ ₹2 lakh monthly transaction target for rental waiver*</div>
    <div class="feature">✔ Lifetime paper roll benefit*</div>
    <div class="feature">✔ Grocery MDR: 1.3%</div>
    <div class="feature">✔ Non-grocery MDR: 1.64%</div>

    </div>
    """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# CALCULATOR
# -----------------------------

st.subheader("💰 Monthly Plan Rental Calculator")

transaction = st.number_input(
    "Enter estimated monthly transaction volume",
    min_value=0,
    max_value=10000000,
    value=200000,
    step=10000
)

if transaction >= 200000:

    st.success(
        "Your transaction volume meets the ₹2 lakh threshold for the stated rental-waiver condition."
    )

else:

    st.warning(
        "Below ₹2 lakh monthly transaction volume, ₹470 rental may apply."
    )

st.divider()

# -----------------------------
# BUSINESS TYPES
# -----------------------------

st.subheader("Suitable for Different Businesses")

businesses = [
    "🛒 Grocery Stores",
    "🍴 Restaurants",
    "👕 Clothing Stores",
    "💊 Pharmacies",
    "💇 Salons",
    "📱 Mobile Stores",
    "🔧 Service Businesses",
    "🏪 Retail Shops"
]

cols = st.columns(4)

for i, business in enumerate(businesses):

    with cols[i % 4]:
        st.info(business)

st.divider()

# -----------------------------
# CHENNAI AREAS
# -----------------------------

st.subheader("Merchant Assistance Across Chennai")

st.write(
    "Ashok Nagar • KK Nagar • T. Nagar • CIT Nagar • "
    "Nandanam • Kotturpuram • Saidapet • Guindy • "
    "Adyar • Mylapore • Velachery"
)

st.divider()

# -----------------------------
# LEAD FORM
# -----------------------------

st.subheader("📲 Get a Callback")

with st.form("lead_form"):

    name = st.text_input("Your Name")

    business_name = st.text_input("Business Name")

    mobile = st.text_input("Mobile Number")

    area = st.text_input("Business Area")

    business_type = st.selectbox(
        "Business Type",
        [
            "Grocery",
            "Restaurant",
            "Retail",
            "Pharmacy",
            "Salon",
            "Mobile Store",
            "Service Business",
            "Other"
        ]
    )

    submitted = st.form_submit_button(
        "🚀 Request EDC Assistance",
        use_container_width=True
    )

    if submitted:

        if name and business_name and mobile and area:

            message = f"""
Hi, I am interested in an EDC machine.

Name: {name}
Business: {business_name}
Mobile: {mobile}
Area: {area}
Business Type: {business_type}
"""

            whatsapp_url = (
                "https://wa.me/7448326548"
                + urllib.parse.quote(message)
            )

            st.success(
                "Thank you! Your enquiry has been received."
            )

            st.markdown(
                f"[💬 Continue on WhatsApp]({whatsapp_url})"
            )

        else:

            st.error(
                "Please fill in all required fields."
            )

# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption(
    "Pricing and benefits are subject to applicable terms, eligibility "
    "and merchant agreement. Please verify final commercial terms before activation."
)
