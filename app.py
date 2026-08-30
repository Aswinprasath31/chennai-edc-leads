
import streamlit as st
import urllib.parse
import re
import textwrap

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="EDC Payment Machine Chennai | Merchant Assistance",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# SETTINGS
# =========================================================

WHATSAPP_NUMBER = "917448326548"
CALL_NUMBER = "+917448326548"

# =========================================================
# SAFE HTML RENDERER
# =========================================================
# IMPORTANT:
# Streamlit treats indented HTML inside st.markdown() as code.
# dedent() removes the indentation before rendering.

def render_html(content):
    st.markdown(
        textwrap.dedent(content).strip(),
        unsafe_allow_html=True,
    )


# =========================================================
# CSS
# =========================================================

render_html("""
<style>
.stApp {
    background: #F5F7FB !important;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1180px;
    padding-top: 20px;
    padding-bottom: 80px;
}

h1, h2, h3, h4 {
    color: #111827 !important;
}

p, label {
    color: #374151;
}

/* NAV */
.navbar {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 14px;
    padding: 15px 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 5px 18px rgba(0,0,0,.05);
    margin-bottom: 24px;
}

.logo {
    color: #111827 !important;
    font-size: 20px;
    font-weight: 850;
}

.logo-accent {
    color: #4F46E5 !important;
}

.nav-badge {
    background: #EEF2FF;
    color: #4338CA !important;
    padding: 7px 12px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 750;
}

/* HERO */
.hero {
    background: linear-gradient(135deg, #111827 0%, #312E81 100%);
    border-radius: 28px;
    padding: 58px 30px;
    text-align: center;
    box-shadow: 0 20px 45px rgba(17,24,39,.18);
    margin-bottom: 22px;
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,.12);
    color: #FFFFFF !important;
    padding: 8px 14px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 16px;
}

.hero-title {
    color: #FFFFFF !important;
    font-size: clamp(34px, 5vw, 58px);
    line-height: 1.06;
    font-weight: 900;
    letter-spacing: -1.5px;
    margin: 0 0 17px;
}

.hero-title span {
    color: #A5B4FC !important;
}

.hero-text {
    color: #D1D5DB !important;
    font-size: 18px;
    line-height: 1.6;
    max-width: 760px;
    margin: auto;
}

.hero-note {
    color: #9CA3AF !important;
    font-size: 12px;
    margin-top: 17px;
}

/* PRICE SUMMARY */
.price-box {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 18px;
    padding: 20px 15px;
    text-align: center;
    box-shadow: 0 7px 22px rgba(0,0,0,.05);
}

.price-label {
    color: #6B7280 !important;
    font-size: 12px;
    font-weight: 750;
    letter-spacing: .5px;
}

.price-value {
    color: #111827 !important;
    font-size: 29px;
    font-weight: 900;
    margin: 5px 0;
}

.price-note {
    color: #4F46E5 !important;
    font-size: 12px;
    font-weight: 750;
}

/* SECTION */
.section-title {
    color: #111827 !important;
    font-size: 31px;
    font-weight: 900;
    margin: 15px 0 5px;
}

.section-subtitle {
    color: #6B7280 !important;
    font-size: 15px;
    margin-bottom: 20px;
}

/* FEATURE */
.feature-card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 18px;
    padding: 23px;
    min-height: 175px;
    box-shadow: 0 7px 22px rgba(0,0,0,.045);
}

.feature-icon {
    font-size: 30px;
    margin-bottom: 10px;
}

.feature-title {
    color: #111827 !important;
    font-size: 17px;
    font-weight: 850;
    margin-bottom: 7px;
}

.feature-text {
    color: #6B7280 !important;
    font-size: 14px;
    line-height: 1.55;
}

/* PLANS */
.plan-card {
    background: #FFFFFF !important;
    border: 1px solid #D1D5DB;
    border-radius: 22px;
    padding: 30px;
    min-height: 445px;
    box-shadow: 0 10px 30px rgba(0,0,0,.065);
}

.plan-card.featured {
    border: 2px solid #4F46E5;
    box-shadow: 0 15px 35px rgba(79,70,229,.14);
}

.plan-tag {
    display: inline-block;
    background: #EEF2FF;
    color: #4338CA !important;
    padding: 6px 11px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 850;
    margin-bottom: 14px;
}

.plan-title {
    color: #111827 !important;
    font-size: 25px;
    font-weight: 900;
    margin-bottom: 8px;
}

.plan-price {
    color: #111827 !important;
    font-size: 44px;
    font-weight: 950;
    line-height: 1;
}

.plan-note {
    color: #6B7280 !important;
    font-size: 13px;
    margin-top: 8px;
}

.plan-line {
    border-top: 1px solid #E5E7EB;
    margin: 22px 0;
}

.plan-feature {
    color: #374151 !important;
    font-size: 15px;
    margin: 13px 0;
    line-height: 1.5;
}

.green {
    color: #047857 !important;
    font-weight: 850;
}

.plan-footnote {
    color: #6B7280 !important;
    font-size: 11px;
    line-height: 1.5;
    margin-top: 18px;
}

/* COMPARISON */
.compare-card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 20px;
    overflow-x: auto;
    box-shadow: 0 8px 25px rgba(0,0,0,.05);
}

.compare-table {
    width: 100%;
    min-width: 650px;
    border-collapse: collapse;
}

.compare-table th {
    background: #111827;
    color: #FFFFFF !important;
    padding: 16px;
    text-align: left;
    font-size: 14px;
}

.compare-table td {
    color: #374151 !important;
    padding: 15px 16px;
    border-bottom: 1px solid #E5E7EB;
    font-size: 14px;
}

.compare-table tr:last-child td {
    border-bottom: none;
}

/* CALCULATOR */
.calculator {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,.06);
}

.result-green {
    background: #ECFDF5;
    border: 1px solid #A7F3D0;
    border-radius: 14px;
    padding: 19px;
    color: #065F46 !important;
    font-weight: 750;
    line-height: 1.5;
}

.result-orange {
    background: #FFF7ED;
    border: 1px solid #FED7AA;
    border-radius: 14px;
    padding: 19px;
    color: #9A3412 !important;
    font-weight: 750;
    line-height: 1.5;
}

/* AREAS */
.area-container {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 20px;
    padding: 23px;
    text-align: center;
    box-shadow: 0 7px 22px rgba(0,0,0,.045);
}

.area-pill {
    display: inline-block;
    background: #F3F4F6;
    border: 1px solid #E5E7EB;
    color: #374151 !important;
    padding: 8px 13px;
    border-radius: 30px;
    margin: 4px;
    font-size: 13px;
    font-weight: 650;
}

/* LEAD */
.lead-info {
    background: linear-gradient(135deg, #111827 0%, #312E81 100%);
    border-radius: 22px;
    padding: 32px;
    min-height: 100%;
    box-shadow: 0 15px 35px rgba(17,24,39,.15);
}

.lead-info h2 {
    color: #FFFFFF !important;
    font-size: 29px;
}

.lead-info p {
    color: #D1D5DB !important;
    line-height: 1.6;
}

.lead-point {
    color: #FFFFFF !important;
    font-size: 14px;
    margin: 15px 0;
}

/* FAQ */
.faq {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 15px;
    padding: 18px 20px;
    margin-bottom: 10px;
}

.faq-question {
    color: #111827 !important;
    font-weight: 850;
    font-size: 15px;
    margin-bottom: 7px;
}

.faq-answer {
    color: #6B7280 !important;
    font-size: 14px;
    line-height: 1.55;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #6B7280 !important;
    font-size: 11px;
    line-height: 1.6;
    padding: 28px 10px 12px;
}

/* MOBILE */
@media (max-width: 700px) {
    .block-container {
        padding-left: 12px;
        padding-right: 12px;
        padding-bottom: 80px;
    }

    .navbar {
        padding: 13px 15px;
    }

    .nav-badge {
        display: none;
    }

    .hero {
        padding: 42px 18px;
        border-radius: 22px;
    }

    .hero-title {
        font-size: 36px;
    }

    .hero-text {
        font-size: 16px;
    }

    .section-title {
        font-size: 27px;
    }

    .plan-card {
        min-height: auto;
        padding: 24px;
        margin-bottom: 15px;
    }

    .plan-price {
        font-size: 38px;
    }
}
</style>
""")


# =========================================================
# TOP NAV
# =========================================================

render_html("""
<div class="navbar">
    <div class="logo">
        EDC <span class="logo-accent">Merchant Assistance</span>
    </div>
    <div class="nav-badge">
        Chennai Merchant Enquiries
    </div>
</div>
""")


# =========================================================
# HERO
# =========================================================

render_html("""
<div class="hero">
    <div class="hero-badge">
        💳 PAYMENT SOLUTION FOR BUSINESSES
    </div>

    <div class="hero-title">
        Get an <span>EDC Payment Machine</span><br>
        for Your Business
    </div>

    <div class="hero-text">
        Explore annual and monthly EDC plan options
        and request assistance for your business
        across Chennai.
    </div>

    <div class="hero-note">
        Pricing and benefits are subject to applicable
        eligibility and merchant terms.
    </div>
</div>
""")


# =========================================================
# PRICE SUMMARY
# =========================================================

c1, c2, c3 = st.columns(3)

with c1:
    render_html("""
    <div class="price-box">
        <div class="price-label">ANNUAL PLAN</div>
        <div class="price-value">₹4,128</div>
        <div class="price-note">Including GST</div>
    </div>
    """)

with c2:
    render_html("""
    <div class="price-box">
        <div class="price-label">MONTHLY PLAN</div>
        <div class="price-value">₹1,528</div>
        <div class="price-note">Including GST</div>
    </div>
    """)

with c3:
    render_html("""
    <div class="price-box">
        <div class="price-label">MONTHLY RENTAL CONDITION</div>
        <div class="price-value">₹2 LAKH*</div>
        <div class="price-note">Monthly transaction threshold</div>
    </div>
    """)


st.write("")


# =========================================================
# HERO CTA
# =========================================================

b1, b2 = st.columns(2)

with b1:
    if st.button(
        "🚀 GET EDC MACHINE",
        type="primary",
        use_container_width=True
    ):
        st.session_state["show_lead"] = True

with b2:
    quick_message = (
        "Hi, I am interested in getting an EDC machine "
        "for my business in Chennai. Please share the details."
    )

    quick_url = (
        f"https://wa.me/{WHATSAPP_NUMBER}"
        f"?text={urllib.parse.quote(quick_message)}"
    )

    st.link_button(
        "💬 WHATSAPP ENQUIRY",
        quick_url,
        use_container_width=True
    )


st.divider()


# =========================================================
# FEATURES
# =========================================================

render_html("""
<div class="section-title">
    Why businesses choose an EDC machine
</div>

<div class="section-subtitle">
    A simple payment solution for everyday merchant needs.
</div>
""")


feature_data = [
    ("💳", "Accept Card Payments", "Give your customers another convenient way to pay."),
    ("⚡", "Easy Checkout", "Make the payment experience simple and convenient."),
    ("🧾", "Paper Roll Benefit", "Lifetime paper roll benefit as per applicable terms."),
    ("📊", "Flexible Plans", "Compare annual and monthly options for your business."),
]

fc1, fc2, fc3, fc4 = st.columns(4)

for col, data in zip(
    [fc1, fc2, fc3, fc4],
    feature_data
):
    icon, title, description = data

    with col:
        render_html(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-text">{description}</div>
        </div>
        """)


st.divider()


# =========================================================
# PLANS
# =========================================================

render_html("""
<div class="section-title">
    Choose your plan
</div>

<div class="section-subtitle">
    Compare the two available plan structures.
</div>
""")


annual, monthly = st.columns(2)


with annual:
    render_html("""
    <div class="plan-card">

        <div class="plan-tag">
            ⭐ NO RENTAL
        </div>

        <div class="plan-title">
            Annual Plan
        </div>

        <div class="plan-price">
            ₹4,128
        </div>

        <div class="plan-note">
            ₹3,499 + GST • Total including GST
        </div>

        <div class="plan-line"></div>

        <div class="plan-feature">
            ✔ <span class="green">No rental</span>
        </div>

        <div class="plan-feature">
            ✔ No transaction target for rental
        </div>

        <div class="plan-feature">
            ✔ Lifetime paper roll benefit*
        </div>

        <div class="plan-feature">
            ✔ Grocery MDR: 1.3%*
        </div>

        <div class="plan-feature">
            ✔ Non-grocery MDR: 1.64%*
        </div>

        <div class="plan-footnote">
            *Subject to applicable eligibility,
            commercial terms and merchant agreement.
        </div>

    </div>
    """)


with monthly:
    render_html("""
    <div class="plan-card featured">

        <div class="plan-tag">
            🔥 LOWER UPFRONT COST
        </div>

        <div class="plan-title">
            Monthly Plan
        </div>

        <div class="plan-price">
            ₹1,528
        </div>

        <div class="plan-note">
            ₹1,300 + GST • Total including GST
        </div>

        <div class="plan-line"></div>

        <div class="plan-feature">
            ✔ ₹470 rental may apply*
        </div>

        <div class="plan-feature">
            ✔ <span class="green">₹2 lakh monthly transaction target</span>
            for the stated rental-waiver condition*
        </div>

        <div class="plan-feature">
            ✔ Lifetime paper roll benefit*
        </div>

        <div class="plan-feature">
            ✔ Grocery MDR: 1.3%*
        </div>

        <div class="plan-feature">
            ✔ Non-grocery MDR: 1.64%*
        </div>

        <div class="plan-footnote">
            *Rental waiver and commercial terms are subject
            to applicable eligibility and merchant agreement.
        </div>

    </div>
    """)


st.divider()


# =========================================================
# COMPARISON
# =========================================================

render_html("""
<div class="section-title">
    Annual vs Monthly
</div>

<div class="section-subtitle">
    Quick comparison of the key plan details.
</div>

<div class="compare-card">
<table class="compare-table">
<tr>
    <th>Feature</th>
    <th>Annual Plan</th>
    <th>Monthly Plan</th>
</tr>
<tr>
    <td>Setup fee</td>
    <td>₹3,499 + GST</td>
    <td>₹1,300 + GST</td>
</tr>
<tr>
    <td>Total including GST</td>
    <td><strong>₹4,128</strong></td>
    <td><strong>₹1,528</strong></td>
</tr>
<tr>
    <td>Rental</td>
    <td>No rental</td>
    <td>₹470 may apply*</td>
</tr>
<tr>
    <td>Rental waiver condition</td>
    <td>Not applicable</td>
    <td>₹2 lakh monthly transaction*</td>
</tr>
<tr>
    <td>Paper roll</td>
    <td>Lifetime benefit*</td>
    <td>Lifetime benefit*</td>
</tr>
<tr>
    <td>Grocery MDR</td>
    <td>1.3%*</td>
    <td>1.3%*</td>
</tr>
<tr>
    <td>Non-grocery MDR</td>
    <td>1.64%*</td>
    <td>1.64%*</td>
</tr>
</table>
</div>
""")


st.divider()


# =========================================================
# CALCULATOR
# =========================================================

render_html("""
<div class="section-title">
    💰 Monthly Plan Rental Calculator
</div>

<div class="section-subtitle">
    Check the stated ₹2 lakh monthly transaction condition.
</div>
""")


calc1, calc2 = st.columns(2)

with calc1:
    transaction = st.number_input(
        "Estimated monthly transaction volume (₹)",
        min_value=0,
        max_value=10000000,
        value=200000,
        step=10000,
        format="%d"
    )

with calc2:

    if transaction >= 200000:
        render_html("""
        <div class="calculator">
            <div class="result-green">
                ✅ ₹2 lakh threshold reached
                <br><br>
                The stated rental-waiver condition may apply,
                subject to applicable eligibility and terms.
            </div>
        </div>
        """)
    else:
        render_html("""
        <div class="calculator">
            <div class="result-orange">
                ⚠️ Below ₹2 lakh
                <br><br>
                ₹470 rental may apply under the monthly plan.
            </div>
        </div>
        """)


st.caption(
    "Indicative calculator only. Final billing and eligibility "
    "are determined by applicable merchant terms."
)


st.divider()


# =========================================================
# BUSINESS TYPES
# =========================================================

render_html("""
<div class="section-title">
    🏪 Suitable for different businesses
</div>

<div class="section-subtitle">
    EDC enquiries from different merchant categories are welcome.
</div>
""")


businesses = [
    "🛒 Grocery Stores",
    "🍴 Restaurants",
    "👕 Clothing Stores",
    "💊 Pharmacies",
    "💇 Salons",
    "📱 Mobile Stores",
    "🔧 Service Businesses",
    "🏪 Retail Shops",
]

business_cols = st.columns(4)

for i, business in enumerate(businesses):
    with business_cols[i % 4]:
        st.info(business)


st.divider()


# =========================================================
# CHENNAI AREAS
# =========================================================

render_html("""
<div class="section-title">
    📍 Merchant assistance across Chennai
</div>

<div class="section-subtitle">
    Enquiries can be raised from merchants in and around these areas.
</div>
""")


areas = [
    "Ashok Nagar",
    "KK Nagar",
    "T. Nagar",
    "CIT Nagar",
    "Nandanam",
    "Kotturpuram",
    "Saidapet",
    "Guindy",
    "Adyar",
    "Mylapore",
    "Velachery",
    "Vadapalani",
    "Anna Nagar",
    "Tambaram",
]

area_html = ""

for area in areas:
    area_html += f'<span class="area-pill">{area}</span>'

render_html(f"""
<div class="area-container">
    {area_html}
</div>
""")


st.divider()


# =========================================================
# LEAD FORM
# =========================================================

render_html("""
<div class="section-title">
    📲 Request EDC assistance
</div>

<div class="section-subtitle">
    Share your business details and continue through WhatsApp.
</div>
""")


lead_left, lead_right = st.columns([0.9, 1.1])


with lead_left:
    render_html("""
    <div class="lead-info">

        <h2>
            Let's discuss your business
        </h2>

        <p>
            Share a few details about your business
            so the appropriate plan information
            can be discussed with you.
        </p>

        <div class="lead-point">
            ✓ Chennai merchant assistance
        </div>

        <div class="lead-point">
            ✓ Annual & Monthly plans
        </div>

        <div class="lead-point">
            ✓ Quick WhatsApp enquiry
        </div>

        <div class="lead-point">
            ✓ No obligation to proceed
        </div>

    </div>
    """)


with lead_right:

    with st.form("merchant_lead_form"):

        name = st.text_input(
            "Your Name *"
        )

        business_name = st.text_input(
            "Business Name *"
        )

        mobile = st.text_input(
            "Mobile Number *",
            placeholder="Enter 10-digit mobile number"
        )

        area = st.selectbox(
            "Business Area *",
            ["Select Area"] + areas + ["Other Chennai Area"]
        )

        business_type = st.selectbox(
            "Business Type",
            [
                "Grocery",
                "Restaurant",
                "Retail",
                "Pharmacy",
                "Salon",
                "Mobile Store",
                "Clothing Store",
                "Service Business",
                "Other"
            ]
        )

        monthly_transaction = st.selectbox(
            "Approx. Monthly Transaction",
            [
                "Below ₹50,000",
                "₹50,000 – ₹1,00,000",
                "₹1,00,000 – ₹2,00,000",
                "₹2,00,000 – ₹5,00,000",
                "Above ₹5,00,000",
                "Not sure"
            ]
        )

        preferred_plan = st.radio(
            "Preferred Plan",
            [
                "Annual",
                "Monthly",
                "Need guidance"
            ],
            horizontal=True
        )

        submitted = st.form_submit_button(
            "🚀 REQUEST EDC ASSISTANCE",
            type="primary",
            use_container_width=True
        )


# =========================================================
# FORM PROCESSING
# =========================================================

if submitted:

    clean_mobile = re.sub(
        r"\D",
        "",
        mobile
    )

    if not name.strip():

        st.error(
            "Please enter your name."
        )

    elif not business_name.strip():

        st.error(
            "Please enter your business name."
        )

    elif len(clean_mobile) != 10:

        st.error(
            "Please enter a valid 10-digit Indian mobile number."
        )

    elif area == "Select Area":

        st.error(
            "Please select your business area."
        )

    else:

        lead_message = f"""
Hi, I am interested in an EDC machine.

Name: {name}
Business: {business_name}
Mobile: {mobile}
Area: {area}
Business Type: {business_type}
Approx. Monthly Transaction: {monthly_transaction}
Preferred Plan: {preferred_plan}

Please share the details.
""".strip()

        lead_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}"
            f"?text={urllib.parse.quote(lead_message)}"
        )

        st.success(
            "✅ Enquiry prepared successfully!"
        )

        st.link_button(
            "💬 SEND DETAILS ON WHATSAPP",
            lead_url,
            use_container_width=True
        )


# =========================================================
# FAQ
# =========================================================

st.divider()


render_html("""
<div class="section-title">
    Frequently asked questions
</div>
""")


faqs = [
    (
        "What is an EDC machine?",
        "An EDC/payment terminal is a device used by businesses "
        "to accept eligible electronic/card payments."
    ),
    (
        "Which plan should I choose?",
        "The annual plan has the stated no-rental structure. "
        "The monthly plan has a lower upfront fee, with the "
        "stated rental-waiver condition linked to the monthly "
        "transaction threshold."
    ),
    (
        "Is the ₹2 lakh condition for the annual plan?",
        "Based on the commercial details supplied for this page, "
        "the ₹2 lakh transaction condition is associated with "
        "the monthly plan's rental-waiver condition."
    ),
    (
        "Are paper rolls free?",
        "The stated benefit is lifetime paper roll free, "
        "subject to applicable merchant terms."
    ),
    (
        "Are the MDR rates final?",
        "The rates displayed are the supplied grocery and "
        "non-grocery rates. Final applicable pricing should "
        "be confirmed during merchant onboarding."
    ),
]


for question, answer in faqs:

    render_html(f"""
    <div class="faq">
        <div class="faq-question">
            {question}
        </div>

        <div class="faq-answer">
            {answer}
        </div>
    </div>
    """)


# =========================================================
# FINAL CTA
# =========================================================

st.divider()


final_message = (
    "Hi, I want to know more about the EDC machine "
    "plans for my business in Chennai."
)

final_url = (
    f"https://wa.me/{WHATSAPP_NUMBER}"
    f"?text={urllib.parse.quote(final_message)}"
)


render_html("""
<div class="hero">
    <div class="hero-badge">
        READY TO ENQUIRE?
    </div>

    <div class="hero-title" style="font-size:38px;">
        Get EDC assistance for your business
    </div>

    <div class="hero-text">
        Contact us through WhatsApp or call for assistance.
    </div>
</div>
""")


end1, end2 = st.columns(2)

with end1:
    st.link_button(
        "💬 WHATSAPP NOW",
        final_url,
        use_container_width=True
    )

with end2:
    st.link_button(
        "📞 CALL NOW",
        f"tel:{CALL_NUMBER}",
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

render_html("""
<div class="footer">
    EDC merchant assistance page for Chennai enquiries.
    <br><br>
    Pricing, MDR, rental, paper-roll benefits, eligibility
    and other commercial terms are subject to applicable
    terms, eligibility and merchant agreement.
    <br>
    Please verify final commercial terms before activation.
</div>
""")


# =========================================================
# MOBILE BOTTOM BAR
# =========================================================

mobile_message = (
    "Hi, I am interested in an EDC machine "
    "for my business in Chennai. Please share the details."
)

mobile_url = (
    f"https://wa.me/{WHATSAPP_NUMBER}"
    f"?text={urllib.parse.quote(mobile_message)}"
)

render_html(f"""
<style>
.mobile-bottom-bar {{
    position: fixed;
    left: 10px;
    right: 10px;
    bottom: 10px;
    z-index: 99999;
    display: flex;
    gap: 8px;
    padding: 8px;
    background: rgba(255,255,255,.97);
    border: 1px solid #E5E7EB;
    border-radius: 15px;
    box-shadow: 0 10px 35px rgba(0,0,0,.15);
}}

.mobile-bottom-bar a {{
    flex: 1;
    text-align: center;
    text-decoration: none;
    padding: 12px;
    border-radius: 10px;
    font-weight: 800;
    font-size: 14px;
}}

.mobile-wa {{
    background: #16A34A;
    color: #FFFFFF !important;
}}

.mobile-call {{
    background: #4F46E5;
    color: #FFFFFF !important;
}}
</style>

<div class="mobile-bottom-bar">
    <a class="mobile-wa" href="{mobile_url}" target="_blank">
        💬 WhatsApp
    </a>

    <a class="mobile-call" href="tel:{CALL_NUMBER}">
        📞 Call
    </a>
</div>
""")
