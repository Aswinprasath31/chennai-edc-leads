import streamlit as st
import urllib.parse
import re


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="EDC Payment Machine Chennai | Merchant Assistance",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# SETTINGS
# =========================================================

WHATSAPP_NUMBER = "917448326548"
CALL_NUMBER = "917448326548"


# =========================================================
# HEADER
# =========================================================

header_left, header_right = st.columns([2.5, 1])

with header_left:
    st.title("💳 EDC Merchant Assistance")

with header_right:
    st.write("")
    st.info("📍 Chennai Merchant Enquiries")


st.divider()


# =========================================================
# HERO
# =========================================================

st.markdown(
    "# Get an EDC Payment Machine for Your Business"
)

st.markdown(
    """
    Explore EDC plan options for your business and
    request assistance from a merchant representative
    across Chennai.
    """
)

st.caption(
    "Transparent plan information • Quick enquiry • Chennai assistance"
)


hero1, hero2 = st.columns(2)


with hero1:

    if st.button(
        "🚀 GET EDC MACHINE",
        type="primary",
        use_container_width=True
    ):

        st.session_state["show_lead"] = True


with hero2:

    quick_message = (
        "Hi, I am interested in getting an EDC machine "
        "for my business in Chennai. Please share the details."
    )

    quick_whatsapp_url = (
        f"https://wa.me/{WHATSAPP_NUMBER}"
        f"?text={urllib.parse.quote(quick_message)}"
    )

    st.link_button(
        "💬 WHATSAPP ENQUIRY",
        quick_whatsapp_url,
        use_container_width=True
    )


st.divider()


# =========================================================
# QUICK PRICE SUMMARY
# =========================================================

st.subheader("Quick Plan Overview")


price1, price2, price3 = st.columns(3)


with price1:

    st.metric(
        label="Annual Plan",
        value="₹4,128",
        delta="Including GST"
    )


with price2:

    st.metric(
        label="Monthly Plan",
        value="₹1,528",
        delta="Including GST"
    )


with price3:

    st.metric(
        label="Monthly Transaction Condition",
        value="₹2 Lakh",
        delta="For stated rental waiver"
    )


st.divider()


# =========================================================
# WHY EDC
# =========================================================

st.header("Why Businesses Choose an EDC Machine")

st.write(
    "A simple payment solution for everyday merchant needs."
)


feature1, feature2, feature3, feature4 = st.columns(4)


with feature1:

    with st.container(border=True):

        st.markdown("## 💳")

        st.subheader("Accept Card Payments")

        st.write(
            "Give your customers another convenient way to pay."
        )


with feature2:

    with st.container(border=True):

        st.markdown("## ⚡")

        st.subheader("Easy Checkout")

        st.write(
            "Make the payment experience simple and convenient."
        )


with feature3:

    with st.container(border=True):

        st.markdown("## 🧾")

        st.subheader("Paper Roll Benefit")

        st.write(
            "Lifetime paper roll benefit as per applicable terms."
        )


with feature4:

    with st.container(border=True):

        st.markdown("## 📊")

        st.subheader("Flexible Plans")

        st.write(
            "Compare annual and monthly options before choosing."
        )


st.divider()


# =========================================================
# PLANS
# =========================================================

st.header("Choose Your Plan")

st.write(
    "Compare the two available EDC plan structures."
)


annual_col, monthly_col = st.columns(2)


# =========================================================
# ANNUAL PLAN
# =========================================================

with annual_col:

    with st.container(border=True):

        st.markdown("## ⭐ Annual Plan")

        st.markdown("# ₹4,128")

        st.caption(
            "₹3,499 + GST • Total including GST"
        )

        st.divider()

        st.success("🟢 No Rental")

        st.write(
            "✔ No transaction target for rental"
        )

        st.write(
            "✔ Lifetime paper roll benefit*"
        )

        st.write(
            "✔ Grocery MDR: 1.3%*"
        )

        st.write(
            "✔ Non-grocery MDR: 1.64%*"
        )

        st.divider()

        st.caption(
            "*Subject to applicable eligibility, "
            "commercial terms and merchant agreement."
        )


# =========================================================
# MONTHLY PLAN
# =========================================================

with monthly_col:

    with st.container(border=True):

        st.markdown("## 🔥 Monthly Plan")

        st.markdown("# ₹1,528")

        st.caption(
            "₹1,300 + GST • Total including GST"
        )

        st.divider()

        st.info(
            "💡 Lower upfront cost"
        )

        st.write(
            "✔ ₹470 rental may apply*"
        )

        st.write(
            "✔ ₹2 lakh monthly transaction target "
            "for the stated rental-waiver condition*"
        )

        st.write(
            "✔ Lifetime paper roll benefit*"
        )

        st.write(
            "✔ Grocery MDR: 1.3%*"
        )

        st.write(
            "✔ Non-grocery MDR: 1.64%*"
        )

        st.divider()

        st.caption(
            "*Rental waiver and commercial terms are subject "
            "to applicable eligibility and merchant agreement."
        )


st.divider()


# =========================================================
# PLAN COMPARISON
# =========================================================

st.header("Annual vs Monthly")

st.write(
    "Quick comparison of the key plan details."
)


comparison_data = {

    "Feature": [

        "Setup Fee",

        "Total Including GST",

        "Rental",

        "Rental Waiver Condition",

        "Paper Roll",

        "Grocery MDR",

        "Non-Grocery MDR"

    ],

    "Annual Plan": [

        "₹3,499 + GST",

        "₹4,128",

        "No Rental",

        "Not Applicable",

        "Lifetime Benefit*",

        "1.3%*",

        "1.64%*"

    ],

    "Monthly Plan": [

        "₹1,300 + GST",

        "₹1,528",

        "₹470 may apply*",

        "₹2 lakh monthly transaction*",

        "Lifetime Benefit*",

        "1.3%*",

        "1.64%*"

    ]

}


st.dataframe(
    comparison_data,
    use_container_width=True,
    hide_index=True
)


st.caption(
    "*Final commercial terms are subject to applicable "
    "eligibility and merchant agreement."
)


st.divider()


# =========================================================
# RENTAL CALCULATOR
# =========================================================

st.header("💰 Monthly Plan Rental Calculator")

st.write(
    "Check whether your estimated monthly transaction "
    "volume reaches the stated ₹2 lakh threshold."
)


calculator_left, calculator_right = st.columns(2)


with calculator_left:

    transaction = st.number_input(

        "Estimated Monthly Transaction Volume (₹)",

        min_value=0,

        max_value=10000000,

        value=200000,

        step=10000,

        format="%d"

    )


with calculator_right:

    if transaction >= 200000:

        st.success(
            """
            ✅ ₹2 lakh threshold reached.

            The stated rental-waiver condition may apply,
            subject to applicable eligibility and terms.
            """
        )

    else:

        st.warning(
            """
            ⚠️ Below ₹2 lakh.

            ₹470 rental may apply under the monthly plan.
            """
        )


st.caption(
    "Indicative calculator only. Final billing and eligibility "
    "are determined by applicable merchant terms."
)


st.divider()


# =========================================================
# BUSINESS TYPES
# =========================================================

st.header("🏪 Suitable for Different Businesses")

st.write(
    "EDC enquiries from different merchant categories are welcome."
)


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


business_columns = st.columns(4)


for i, business in enumerate(businesses):

    with business_columns[i % 4]:

        st.info(business)


st.divider()


# =========================================================
# CHENNAI AREAS
# =========================================================

st.header("📍 Merchant Assistance Across Chennai")

st.write(
    "Enquiries can be raised from merchants in and around these areas."
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


area_columns = st.columns(4)


for i, area in enumerate(areas):

    with area_columns[i % 4]:

        st.write(f"📍 **{area}**")


st.divider()


# =========================================================
# LEAD SECTION
# =========================================================

st.header("📲 Request EDC Assistance")

st.write(
    "Share your business details and continue through WhatsApp."
)


lead_left, lead_right = st.columns([0.8, 1.2])


# =========================================================
# LEFT INFORMATION
# =========================================================

with lead_left:

    with st.container(border=True):

        st.subheader("Let's Discuss Your Business")

        st.write(
            """
            Share a few details about your business so
            the appropriate plan information can be discussed.
            """
        )

        st.success(
            "✓ Chennai merchant assistance"
        )

        st.success(
            "✓ Annual & Monthly plans"
        )

        st.success(
            "✓ Quick WhatsApp enquiry"
        )

        st.success(
            "✓ No obligation to proceed"
        )


# =========================================================
# LEAD FORM
# =========================================================

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

            [
                "Select Area"
            ]
            + areas
            + [
                "Other Chennai Area"
            ]

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

                "Need Guidance"

            ],

            horizontal=True

        )


        submitted = st.form_submit_button(

            "🚀 REQUEST EDC ASSISTANCE",

            type="primary",

            use_container_width=True

        )


# =========================================================
# PROCESS LEAD
# =========================================================

if submitted:

    clean_mobile = re.sub(
        r"\D",
        "",
        mobile
    )


    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

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

        # -------------------------------------------------
        # WHATSAPP MESSAGE
        # -------------------------------------------------

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
            "✅ Your enquiry has been prepared successfully."
        )


        st.link_button(

            "💬 SEND DETAILS ON WHATSAPP",

            whatsapp_url,

            use_container_width=True

        )


st.divider()


# =========================================================
# FAQ
# =========================================================

st.header("Frequently Asked Questions")


with st.expander(
    "What is an EDC machine?"
):

    st.write(
        """
        An EDC/payment terminal is a device used by businesses
        to accept eligible electronic/card payments.
        """
    )


with st.expander(
    "Which plan should I choose?"
):

    st.write(
        """
        The annual plan has the stated no-rental structure.
        The monthly plan has a lower upfront fee, with the
        stated rental-waiver condition linked to the monthly
        transaction threshold.
        """
    )


with st.expander(
    "Is the ₹2 lakh condition applicable to the annual plan?"
):

    st.write(
        """
        Based on the commercial details supplied for this page,
        the ₹2 lakh transaction condition is associated with
        the monthly plan's rental-waiver condition.
        """
    )


with st.expander(
    "Are paper rolls free?"
):

    st.write(
        """
        The stated benefit is lifetime paper roll free,
        subject to applicable merchant terms.
        """
    )


with st.expander(
    "Are the MDR rates final?"
):

    st.write(
        """
        The rates displayed are the supplied grocery and
        non-grocery rates. Final applicable pricing should
        be confirmed during merchant onboarding.
        """
    )


st.divider()


# =========================================================
# FINAL CALL TO ACTION
# =========================================================

st.header("🚀 Ready to Enquire?")

st.write(
    "Get EDC assistance for your business in Chennai."
)


final_message = (
    "Hi, I want to know more about the EDC machine "
    "plans for my business in Chennai."
)


final_whatsapp_url = (

    f"https://wa.me/{WHATSAPP_NUMBER}"

    f"?text={urllib.parse.quote(final_message)}"

)


final1, final2 = st.columns(2)


with final1:

    st.link_button(

        "💬 WHATSAPP NOW",

        final_whatsapp_url,

        use_container_width=True

    )


with final2:

    st.link_button(

        "📞 CALL NOW",

        f"tel:+{CALL_NUMBER}",

        use_container_width=True

    )


st.divider()


# =========================================================
# FOOTER
# =========================================================

st.caption(
    """
    EDC merchant assistance page for Chennai enquiries.

    Pricing, MDR, rental, paper-roll benefits, eligibility
    and other commercial terms are subject to applicable
    terms, eligibility and merchant agreement.

    Please verify final commercial terms before activation.
    """
)
