import streamlit as st
import urllib.parse
import re

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="EDC Payment Machine | Chennai Merchants",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# SETTINGS
# =========================================================

WHATSAPP_NUMBER = "917448326548"
CALL_NUMBER = "+91 74483 26548"

# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    """
<style>

/* =====================================================
   APP BACKGROUND
===================================================== */

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(99,102,241,.08),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(16,185,129,.07),
            transparent 25%
        ),
        #f7f8fc;
}

[data-testid="stHeader"] {
    background: rgba(247,248,252,.90);
}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 5.5rem;
}

/* =====================================================
   TYPOGRAPHY
===================================================== */

html,
body,
[class*="css"] {
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
}

h1,
h2,
h3,
h4 {
    color: #111827 !important;
}

p,
li,
span,
label {
    color: #374151;
}


/* =====================================================
   TOP BAR
===================================================== */

.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 0 8px;
}

.brand {
    font-weight: 800;
    font-size: 20px;
    color: #111827 !important;
}

.brand span {
    color: #4f46e5 !important;
}

.badge {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 999px;
    background: #eef2ff;
    color: #4338ca !important;
    font-size: 12px;
    font-weight: 700;
}


/* =====================================================
   HERO
===================================================== */

.hero {
    margin-top: 18px;
    padding: 54px 30px 46px;
    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            #ffffff 0%,
            #f5f7ff 100%
        );

    border: 1px solid #e5e7eb;

    box-shadow:
        0 16px 45px rgba(17,24,39,.08);

    text-align: center;
}

.hero-eyebrow {
    display: inline-block;

    padding: 8px 14px;

    border-radius: 999px;

    background: #ecfdf5;

    color: #047857 !important;

    font-size: 13px;

    font-weight: 800;

    margin-bottom: 15px;
}

.hero h1 {
    font-size: clamp(34px, 5vw, 58px);

    line-height: 1.05;

    letter-spacing: -1.8px;

    font-weight: 850;

    margin: 0 auto 16px;

    max-width: 900px;
}

.hero h1 .accent {
    color: #4f46e5 !important;
}

.hero p {
    max-width: 760px;

    margin: 0 auto;

    font-size: 18px;

    line-height: 1.65;

    color: #4b5563 !important;
}

.hero-note {
    margin-top: 16px;

    font-size: 12px;

    color: #6b7280 !important;
}


/* =====================================================
   BUTTONS
===================================================== */

div.stButton > button {
    border-radius: 12px;

    min-height: 48px;

    font-weight: 800;

    border: 0;
}

div.stButton > button[kind="primary"] {
    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #4338ca
        );
}

div.stButton > button:hover {
    transform: translateY(-1px);

    box-shadow:
        0 8px 20px rgba(79,70,229,.18);
}


/* =====================================================
   SECTION
===================================================== */

.section {
    padding: 12px 0 4px;
}

.section-kicker {
    color: #4f46e5 !important;

    font-size: 12px;

    font-weight: 850;

    text-transform: uppercase;

    letter-spacing: 1.2px;
}

.section-title {
    font-size: 32px;

    font-weight: 850;

    margin: 5px 0 7px;
}

.section-subtitle {
    color: #6b7280 !important;

    margin: 0 0 20px;
}


/* =====================================================
   FEATURE CARDS
===================================================== */

.feature-card {
    height: 100%;

    padding: 24px 20px;

    border-radius: 18px;

    background: #ffffff;

    border: 1px solid #e5e7eb;

    box-shadow:
        0 8px 24px rgba(17,24,39,.05);
}

.feature-icon {
    font-size: 30px;

    margin-bottom: 10px;
}

.feature-card h3 {
    font-size: 17px;

    margin: 0 0 7px;
}

.feature-card p {
    font-size: 14px;

    line-height: 1.55;

    color: #6b7280 !important;

    margin: 0;
}


/* =====================================================
   PLAN CARDS
===================================================== */

.plan-card {
    position: relative;

    height: 100%;

    padding: 30px;

    border-radius: 22px;

    background: #ffffff !important;

    border: 1px solid #e5e7eb;

    box-shadow:
        0 12px 32px rgba(17,24,39,.07);

    color: #111827 !important;
}

.plan-card.featured {
    border: 2px solid #4f46e5;

    box-shadow:
        0 16px 38px rgba(79,70,229,.15);
}

.plan-ribbon {
    position: absolute;

    top: 18px;

    right: 18px;

    padding: 6px 10px;

    border-radius: 999px;

    background: #eef2ff;

    color: #4338ca !important;

    font-size: 11px;

    font-weight: 850;
}

.plan-name {
    font-size: 22px;

    font-weight: 850;

    color: #111827 !important;

    margin-bottom: 8px;
}

.plan-price {
    font-size: 43px;

    line-height: 1;

    font-weight: 900;

    color: #111827 !important;
}

.plan-gst {
    margin-top: 8px;

    font-size: 13px;

    color: #6b7280 !important;
}

.plan-divider {
    border-top: 1px solid #e5e7eb;

    margin: 22px 0;
}

.plan-feature {
    margin: 13px 0;

    font-size: 15px;

    color: #374151 !important;

    line-height: 1.45;
}

.plan-feature strong {
    color: #047857 !important;
}

.plan-footnote {
    margin-top: 18px;

    font-size: 11px;

    color: #6b7280 !important;

    line-height: 1.5;
}


/* =====================================================
   COMPARISON TABLE
===================================================== */

.compare-wrap {
    overflow-x: auto;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    background: #ffffff;

    box-shadow:
        0 8px 24px rgba(17,24,39,.05);
}

.compare-table {
    width: 100%;

    border-collapse: collapse;

    min-width: 650px;
}

.compare-table th,
.compare-table td {
    padding: 15px 18px;

    border-bottom: 1px solid #eef0f4;

    text-align: left;

    color: #374151 !important;

    font-size: 14px;
}

.compare-table th {
    background: #f8fafc;

    color: #111827 !important;

    font-weight: 850;
}

.compare-table tr:last-child td {
    border-bottom: 0;
}


/* =====================================================
   CALCULATOR
===================================================== */

.calc-card {
    padding: 28px;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            #ffffff,
            #f8faff
        );

    border: 1px solid #e5e7eb;

    box-shadow:
        0 12px 30px rgba(17,24,39,.06);
}

.result-good {
    padding: 18px;

    border-radius: 14px;

    background: #ecfdf5;

    border: 1px solid #a7f3d0;

    color: #065f46 !important;

    font-weight: 750;
}

.result-rental {
    padding: 18px;

    border-radius: 14px;

    background: #fff7ed;

    border: 1px solid #fed7aa;

    color: #9a3412 !important;

    font-weight: 750;
}


/* =====================================================
   AREA PILLS
===================================================== */

.area-pill {
    display: inline-block;

    margin: 5px 4px 5px 0;

    padding: 9px 13px;

    border-radius: 999px;

    background: #ffffff;

    border: 1px solid #e5e7eb;

    color: #374151 !important;

    font-size: 13px;

    font-weight: 650;
}


/* =====================================================
   LEAD BOX
===================================================== */

.lead-box {
    padding: 32px;

    border-radius: 24px;

    background: #111827;

    box-shadow:
        0 18px 45px rgba(17,24,39,.16);
}

.lead-box h2,
.lead-box p {
    color: #ffffff !important;
}

.lead-box .muted {
    color: #cbd5e1 !important;
}


/* =====================================================
   FAQ
===================================================== */

.faq {
    border-radius: 15px;

    background: #ffffff;

    border: 1px solid #e5e7eb;

    padding: 18px 20px;

    margin-bottom: 10px;
}

.faq-q {
    font-weight: 800;

    color: #111827 !important;

    margin-bottom: 6px;
}

.faq-a {
    color: #6b7280 !important;

    font-size: 14px;

    line-height: 1.55;
}


/* =====================================================
   MOBILE CTA
===================================================== */

.mobile-cta {
    position: fixed;

    left: 12px;
    right: 12px;
    bottom: 12px;

    z-index: 9999;

    display: flex;

    gap: 8px;

    padding: 8px;

    background: rgba(255,255,255,.96);

    border: 1px solid #e5e7eb;

    border-radius: 16px;

    box-shadow:
        0 12px 35px rgba(0,0,0,.14);

    backdrop-filter: blur(10px);
}

.mobile-cta a {
    flex: 1;

    text-align: center;

    text-decoration: none;

    padding: 12px 8px;

    border-radius: 10px;

    font-weight: 850;

    font-size: 14px;
}

.mobile-cta .wa {
    background: #16a34a;

    color: white !important;
}

.mobile-cta .call {
    background: #4f46e5;

    color: white !important;
}


/* =====================================================
   FOOTER
===================================================== */

.footer {
    text-align: center;

    padding: 28px 0 10px;

    color: #6b7280 !important;

    font-size: 11px;

    line-height: 1.6;
}


/* =====================================================
   MOBILE
===================================================== */

@media (max-width: 700px) {

    .block-container {
        padding-left: 14px;
        padding-right: 14px;
        padding-bottom: 6rem;
    }

    .hero {
        padding: 38px 18px 32px;

        border-radius: 22px;
    }

    .hero p {
        font-size: 16px;
    }

    .plan-card {
        padding: 23px;

        margin-bottom: 4px;
    }

    .plan-price {
        font-size: 37px;
    }

    .section-title {
        font-size: 27px;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# TOP BAR
# =========================================================

st.markdown(
    """
<div class="topbar">

    <div class="brand">
        EDC <span>Merchant Assistance</span>
    </div>

    <div class="badge">
        Chennai • Merchant Enquiries
    </div>

</div>
""",
    unsafe_allow_html=True,
)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
<div class="hero">

    <div class="hero-eyebrow">
        💳 PAYMENT SOLUTION FOR BUSINESSES
    </div>

    <h1>
        Get an
        <span class="accent">
            EDC Payment Machine
        </span>
        for Your Business
    </h1>

    <p>
        Explore annual and monthly EDC plan options
        and request a callback for merchant assistance
        across Chennai.
    </p>

    <div class="hero-note">
        Pricing and benefits are subject to applicable
        eligibility and merchant terms.
    </div>

</div>
""",
    unsafe_allow_html=True,
)


# =========================================================
# QUICK PRICE SUMMARY
# =========================================================

hero_col1, hero_col2, hero_col3 = st.columns(3)

with hero_col1:

    st.metric(
        "Annual plan",
        "₹4,128*",
        "Including GST"
    )

with hero_col2:

    st.metric(
        "Monthly plan",
        "₹1,528*",
        "Including GST"
    )

with hero_col3:

    st.metric(
        "Monthly rental condition",
        "₹2L*",
        "Transaction threshold"
    )


st.divider()


# =========================================================
# HERO CTA
# =========================================================

cta1, cta2 = st.columns(2)


with cta1:

    if st.button(
        "🚀 Get EDC Machine",
        type="primary",
        use_container_width=True
    ):

        st.session_state["focus_lead"] = True


with cta2:

    quick_message = (
        "Hi, I am interested in getting an EDC machine "
        "for my business in Chennai. Please share the details."
    )

    quick_wa = (
        f"https://wa.me/{WHATSAPP_NUMBER}"
        f"?text={urllib.parse.quote(quick_message)}"
    )

    st.link_button(
        "💬 WhatsApp Enquiry",
        quick_wa,
        use_container_width=True
    )


# =========================================================
# FEATURES
# =========================================================

st.markdown(
    """
<div class="section">

    <div class="section-kicker">
        Why EDC?
    </div>

    <div class="section-title">
        Built around everyday merchant needs
    </div>

    <div class="section-subtitle">
        Simple information, transparent plan comparison
        and a quick enquiry process.
    </div>

</div>
""",
    unsafe_allow_html=True,
)


f1, f2, f3, f4 = st.columns(4)


features = [

    (
        "💳",
        "Accept Card Payments",
        "Give customers another convenient way to pay."
    ),

    (
        "⚡",
        "Smooth Checkout",
        "Make the payment experience simple for your customers."
    ),

    (
        "🧾",
        "Paper Roll Benefit",
        "Lifetime paper roll benefit as per applicable terms."
    ),

    (
        "📊",
        "Plan Choice",
        "Compare annual and monthly options before choosing."
    ),
]


for col, (icon, title, desc) in zip(
    [f1, f2, f3, f4],
    features
):

    with col:

        st.markdown(
            f"""
            <div class="feature-card">

                <div class="feature-icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {desc}
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )


st.divider()


# =========================================================
# PLANS
# =========================================================

st.markdown(
    """
<div class="section">

    <div class="section-kicker">
        Plans
    </div>

    <div class="section-title">
        Choose the plan that fits your business
    </div>

    <div class="section-subtitle">
        Compare the key commercial details below.
    </div>

</div>
""",
    unsafe_allow_html=True,
)


p1, p2 = st.columns(2)


# =========================================================
# ANNUAL PLAN
# =========================================================

with p1:

    st.markdown(
        """
        <div class="plan-card">

            <div class="plan-ribbon">
                NO RENTAL
            </div>

            <div class="plan-name">
                ⭐ Annual Plan
            </div>

            <div class="plan-price">
                ₹4,128
            </div>

            <div class="plan-gst">
                ₹3,499 + GST • Total including GST
            </div>

            <div class="plan-divider"></div>

            <div class="plan-feature">
                ✔ <strong>No rental</strong>
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
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# MONTHLY PLAN
# =========================================================

with p2:

    st.markdown(
        """
        <div class="plan-card featured">

            <div class="plan-ribbon">
                LOWER UPFRONT
            </div>

            <div class="plan-name">
                📅 Monthly Plan
            </div>

            <div class="plan-price">
                ₹1,528
            </div>

            <div class="plan-gst">
                ₹1,300 + GST • Total including GST
            </div>

            <div class="plan-divider"></div>

            <div class="plan-feature">
                ✔ ₹470 rental may apply*
            </div>

            <div class="plan-feature">
                ✔ <strong>₹2 lakh monthly transaction target</strong>
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
                *Rental waiver and all commercial terms
                are subject to applicable eligibility
                and merchant agreement.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# =========================================================
# PLAN COMPARISON
# =========================================================

st.markdown(
    """
<div class="section">

    <div class="section-kicker">
        Quick comparison
    </div>

    <div class="section-title">
        Annual vs Monthly
    </div>

</div>

<div class="compare-wrap">

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
        <td>Rental-waiver condition</td>
        <td>Not applicable</td>
        <td>₹2 lakh monthly transaction target*</td>
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
""",
    unsafe_allow_html=True,
)


st.divider()


# =========================================================
# RENTAL CALCULATOR
# =========================================================

st.markdown(
    """
<div class="section">

    <div class="section-kicker">
        Interactive tool
    </div>

    <div class="section-title">
        Monthly Plan Rental Calculator
    </div>

    <div class="section-subtitle">
        Enter your estimated monthly transaction volume.
    </div>

</div>
""",
    unsafe_allow_html=True,
)


c1, c2 = st.columns([1, 1])


with c1:

    transaction = st.number_input(
        "Estimated monthly transaction volume (₹)",

        min_value=0,

        max_value=10000000,

        value=200000,

        step=10000,

        format="%d",
    )


with c2:

    st.markdown(
        '<div class="calc-card">',
        unsafe_allow_html=True
    )

    if transaction >= 200000:

        st.markdown(
            """
            <div class="result-good">

                ✅ ₹2 lakh threshold reached

                <br><br>

                The stated rental-waiver condition
                may apply, subject to applicable
                terms and eligibility.

            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            """
            <div class="result-rental">

                ⚠️ Below ₹2 lakh

                <br><br>

                ₹470 rental may apply under
                the monthly plan.

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )


st.caption(
    "This calculator is only an indicative guide and does not "
    "determine final billing or eligibility."
)


st.divider()


# =========================================================
# BUSINESS TYPES
# =========================================================

st.markdown(
    """
<div class="section">

    <div class="section-kicker">
        Business categories
    </div>

    <div class="section-title">
        Useful for different types of merchants
    </div>

</div>
""",
    unsafe_allow_html=True,
)


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


biz_cols = st.columns(4)


for i, business in enumerate(businesses):

    with biz_cols[i % 4]:

        st.info(business)


st.divider()


# =========================================================
# CHENNAI AREAS
# =========================================================

st.markdown(
    """
<div class="section">

    <div class="section-kicker">
        Local assistance
    </div>

    <div class="section-title">
        Merchant assistance across Chennai
    </div>

    <div class="section-subtitle">
        Enquiries can be raised from merchants
        in and around these areas.
    </div>

</div>
""",
    unsafe_allow_html=True,
)


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
    "Tambaram"

]


area_html = "".join(

    f'<span class="area-pill">{area}</span>'

    for area in areas

)


st.markdown(
    f'<div>{area_html}</div>',
    unsafe_allow_html=True
)


st.divider()


# =========================================================
# LEAD FORM
# =========================================================

st.markdown(
    """
<div id="get-edc" class="section">

    <div class="section-kicker">
        Get started
    </div>

    <div class="section-title">
        Request EDC assistance
    </div>

    <div class="section-subtitle">
        Share your business details and continue
        through WhatsApp for faster assistance.
    </div>

</div>
""",
    unsafe_allow_html=True,
)


lead_left, lead_right = st.columns([1, 1.15])


# =========================================================
# LEAD INFORMATION
# =========================================================

with lead_left:

    st.markdown(
        """
        <div class="lead-box">

            <h2>
                Let's discuss your business
            </h2>

            <p class="muted">
                Tell us a little about your business
                so the right plan can be discussed
                with you.
            </p>

            <br>

            <p class="muted">
                ✓ Chennai merchant assistance
            </p>

            <p class="muted">
                ✓ Annual & monthly plan information
            </p>

            <p class="muted">
                ✓ Quick WhatsApp enquiry
            </p>

            <p class="muted">
                ✓ No obligation to proceed
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# FORM
# =========================================================

with lead_right:

    with st.form(
        "lead_form",
        clear_on_submit=False
    ):

        name = st.text_input(
            "Your Name *"
        )

        business_name = st.text_input(
            "Business Name *"
        )

        mobile = st.text_input(
            "Mobile Number *",
            placeholder="10-digit mobile number"
        )

        area = st.selectbox(
            "Business Area *",

            [
                "Select Area"
            ]
            + areas
            + [
                "Other Chennai Area"
            ],
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

                "Other",

            ],

        )

        monthly_transaction = st.selectbox(

            "Approx. Monthly Transaction",

            [

                "Below ₹50,000",

                "₹50,000 – ₹1,00,000",

                "₹1,00,000 – ₹2,00,000",

                "₹2,00,000 – ₹5,00,000",

                "Above ₹5,00,000",

                "Not sure",

            ],

        )

        preferred_plan = st.radio(

            "Preferred Plan",

            [

                "Annual",

                "Monthly",

                "Need guidance"

            ],

            horizontal=True,

        )


        submitted = st.form_submit_button(

            "🚀 Request EDC Assistance",

            use_container_width=True,

            type="primary",

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


    # -----------------------------------------
    # VALIDATION
    # -----------------------------------------

    if (

        not name.strip()

        or not business_name.strip()

        or not clean_mobile

    ):

        st.error(
            "Please enter your name, business name "
            "and mobile number."
        )


    elif len(clean_mobile) != 10:

        st.error(
            "Please enter a valid 10-digit Indian "
            "mobile number."
        )


    elif area == "Select Area":

        st.error(
            "Please select your business area."
        )


    else:

        # -----------------------------------------
        # WHATSAPP MESSAGE
        # -----------------------------------------

        lead_message = f"""

Hi, I am interested in an EDC machine.

Name: {name}

Business: {business_name}

Mobile: {mobile}

Area: {area}

Business Type: {business_type}

Approx. Monthly Transaction:
{monthly_transaction}

Preferred Plan:
{preferred_plan}

Please share the details.

""".strip()


        whatsapp_url = (

            f"https://wa.me/{WHATSAPP_NUMBER}"

            f"?text={urllib.parse.quote(lead_message)}"

        )


        st.success(
            "✅ Your enquiry is ready. "
            "Click WhatsApp below to send the details."
        )


        st.link_button(

            "💬 Send Enquiry on WhatsApp",

            whatsapp_url,

            use_container_width=True,

        )


# =========================================================
# FAQ
# =========================================================

st.divider()


st.markdown(
    """
<div class="section">

    <div class="section-kicker">
        FAQ
    </div>

    <div class="section-title">
        Frequently asked questions
    </div>

</div>
""",
    unsafe_allow_html=True,
)


faqs = [

    (

        "What is an EDC machine?",

        "An EDC/payment terminal is a device used by "
        "businesses to accept eligible electronic/card payments."

    ),

    (

        "Which plan should I choose?",

        "The annual plan is suitable if you prefer "
        "the stated no-rental structure. The monthly "
        "plan has a lower upfront fee but its rental-waiver "
        "condition is linked to the stated monthly "
        "transaction threshold."

    ),

    (

        "Is the ₹2 lakh target applicable to the annual plan?",

        "No. Based on the commercial details provided "
        "for this page, the ₹2 lakh transaction condition "
        "is associated with the monthly plan's "
        "rental-waiver condition."

    ),

    (

        "Do paper rolls have a charge?",

        "The stated benefit is lifetime paper roll free, "
        "subject to the applicable merchant terms."

    ),

    (

        "Are the MDR rates the same for every business?",

        "The rates shown here are the supplied grocery "
        "and non-grocery rates. Final applicable pricing "
        "should be confirmed during merchant onboarding."

    ),

]


for question, answer in faqs:

    st.markdown(

        f"""
        <div class="faq">

            <div class="faq-q">
                {question}
            </div>

            <div class="faq-a">
                {answer}
            </div>

        </div>
        """,

        unsafe_allow_html=True,

    )


# =========================================================
# FINAL CTA
# =========================================================

st.divider()


final_message = (
    "Hi, I want to know more about the EDC machine "
    "plans for my business in Chennai."
)


final_wa = (

    f"https://wa.me/{WHATSAPP_NUMBER}"

    f"?text={urllib.parse.quote(final_message)}"

)


st.markdown(

    """
    <div class="hero" style="padding:35px 20px;">

        <div class="hero-eyebrow">
            READY TO ENQUIRE?
        </div>

        <h2 style="font-size:32px;">
            Get EDC assistance for your business
        </h2>

        <p>
            Send your requirement through WhatsApp
            or call for assistance.
        </p>

    </div>
    """,

    unsafe_allow_html=True,

)


final_c1, final_c2 = st.columns(2)


with final_c1:

    st.link_button(

        "💬 WhatsApp Now",

        final_wa,

        use_container_width=True

    )


with final_c2:

    st.link_button(

        "📞 Call Now",

        f"tel:{CALL_NUMBER}",

        use_container_width=True

    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(

    """
    <div class="footer">

        EDC merchant assistance page for Chennai enquiries.

        <br>

        Pricing, MDR, rental, paper-roll benefits,
        eligibility and other commercial terms are
        subject to applicable terms, eligibility
        and merchant agreement.

        <br>

        Please verify final commercial terms
        before activation.

    </div>
    """,

    unsafe_allow_html=True,

)


# =========================================================
# STICKY MOBILE CTA
# =========================================================

sticky_message = (

    "Hi, I am interested in an EDC machine "
    "for my business in Chennai. Please share the details."

)


sticky_wa = (

    f"https://wa.me/{WHATSAPP_NUMBER}"

    f"?text={urllib.parse.quote(sticky_message)}"

)


st.markdown(

    f"""
    <div class="mobile-cta">

        <a
            class="wa"
            href="{sticky_wa}"
            target="_blank"
        >
            💬 WhatsApp
        </a>

        <a
            class="call"
            href="tel:{CALL_NUMBER}"
        >
            📞 Call
        </a>

    </div>
    """,

    unsafe_allow_html=True,

)
