import time

import streamlit as st

from pages.oct_model import main


def add_custom_css():
    st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .main-title {
        font-size: 2.5rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 2rem;
        color: #2980b9;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .pricing-card {
        border: 2px solid #e6e6e6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        height: 420px;
        background-color: #f9f9f9;
    }
    .pricing-card h2 {
        font-size: 1.5rem;
        color: #3498db;
    }
    .pricing-card p {
        font-size: 1.2rem;
        color: #2c3e50;
    }
    .pricing-card ul {
        margin-left:-10px;
        list-style-type: none;
        padding: 0;
    }
    .pricing-card ul li {
        font-size: 1rem;
        color: #7f8c8d;
    }
    .testimonial {
        font-style: italic;
        color: #34495e;
        margin: 1rem 0;
    }
    .testimonial-author {
        font-weight: bold;
        color: #2c3e50;
    }
    .cta {
        background-color: #2980b9;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .cta a {
        color: white;
        font-weight: bold;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)


def landing_page():
    add_custom_css()

    def pricing_section():
        st.markdown('<div class="section-title">Pricing Plans</div>', unsafe_allow_html=True)
        left_co, cent_co, last_co = st.columns(3)
        with cent_co:
            st.image("tag.png", width=200)
        plans = [
            {
                "name": "Basic Plan",
                "price": 14.99,
                "features": [
                    "Up to 120 predictions",
                    "Basic support",
                    "Access to community forums"
                ]
            },
            {
                "name": "Pro Plan",
                "price": 99,
                "features": [
                    "Up to 1,500 predictions",
                    "Priority support",
                    "Access to private forums",
                    "Data Discovery Dialogues: Unlock Insights Monthly"
                ]
            },
            {
                "name": "Enterprise Plan",
                "price": 299,
                "features": [
                    "Unlimited predictions",
                    "24/7 dedicated support",
                    "Customized solutions",
                    "Quarterly business reviews",
                    "Dedicated account manager"
                ]
            }
        ]

        col1, col2, col3 = st.columns(3)

        def generate_plan_html(name, price, features):
            features_html = ''.join([f"<li>{feature}</li>" for feature in features])
            return f"""
            <div class="pricing-card">
                <h2>{name}</h2>
                <p><strong>Price:</strong> ${price}/month</p>
                <h3>Features</h3>
                <ul>{features_html}</ul>
            </div>
            """

        for col, plan in zip([col1, col2, col3], plans):
            col.markdown(generate_plan_html(plan['name'], plan['price'], plan['features']), unsafe_allow_html=True)

        st.markdown("For more information, please contact our [sales team](mailto:sales@example.com).")

    def features_section():
        st.markdown('<div class="section-title">Key Features</div>', unsafe_allow_html=True)
        left_co, cent_co, last_co = st.columns(3)
        with cent_co:
            st.image("features.png", width=200)
        st.markdown("""
        - **AI-Powered Diagnoses**: Leverage the power of advanced AI algorithms for accurate eye health assessments.
        - **User-Friendly Interface**: Easily navigate and utilize our platform with an intuitive design.
        - **Secure and Compliant**: Ensure patient data privacy with our secure and compliant infrastructure.
        - **Scalable Solutions**: Flexible plans that grow with your needs, from individual practitioners to large enterprises.
        """)

    def testimonials_section():
        st.markdown('<div class="section-title">What Our Users Say</div>', unsafe_allow_html=True)
        left_co, cent_co, last_co = st.columns(3)
        with cent_co:
            st.image("rating.png", width=200)
        testimonials = [
            {
                "name": "Dr. Smith",
                "quote": "EleVision AI has revolutionized the way we diagnose and treat eye conditions. The accuracy and speed are unmatched."
            },
            {
                "name": "Dr. Johnson",
                "quote": "The AI predictions have significantly improved our workflow, allowing us to focus more on patient care."
            },
            {
                "name": "Dr. Lee",
                "quote": "As an enterprise user, the dedicated support and customized solutions have been invaluable to our practice."
            }
        ]

        for testimonial in testimonials:
            st.markdown(f"""
            <div class="testimonial">
                "{testimonial['quote']}"
                <div class="testimonial-author">- {testimonial['name']}</div>
            </div>
            """, unsafe_allow_html=True)

    def cta_section():
        st.markdown('<div class="section-title">Get Started Today</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="cta">
            Ready to revolutionize your eye care practice with AI? Choose a plan that fits your needs and get started today!<br>
            <a href="#">Sign Up Now</a><br>
            For more information, contact our <a href="mailto:sales@example.com">sales team</a>.
        </div>
        """, unsafe_allow_html=True)

    # Display the logo
    st.image("logo.png", width=200)

    st.markdown('<div class="main-title">EleVision AI - AI Eye Diagnoses Solutions</div>', unsafe_allow_html=True)

    st.markdown("""
        Welcome to EleVision AI, your premier AI-driven platform for eye diagnoses. Our state-of-the-art AI models 
        provide accurate and efficient eye health assessments to help medical professionals and patients alike. 
        Explore our flexible pricing plans tailored to meet the needs of individuals, small practices, and large enterprises.
    """)

    plans = [
        {
            "name": "Basic Plan",
            "price": 14.99,
            "features": [
                "Up to 120 predictions",
                "Basic support",
                "Access to community forums"
            ]
        },
        {
            "name": "Pro Plan",
            "price": 99,
            "features": [
                "Up to 1,500 predictions",
                "Priority support",
                "Access to private forums",
                "Data Discovery Dialogues: Unlock Insights Monthly"
            ]
        },
        {
            "name": "Enterprise Plan",
            "price": 299,
            "features": [
                "Unlimited predictions",
                "24/7 dedicated support",
                "Customized solutions",
                "Quarterly business reviews",
                "Dedicated account manager"
            ]
        }
    ]

    if page == "Home":
        features_section()
        testimonials_section()
        pricing_section()
        cta_section()
    elif page == "Login":
        login_page()
    elif page == "Signup":
        signup_page()
    elif page == "Subscribe":
        subscribe_page(plans)

def login_page():
    st.markdown('<div class="main-title">Login</div>', unsafe_allow_html=True)
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        submit_button = st.form_submit_button(label='Login')
        if submit_button:
            st.success(f"Welcome {username}!")


def signup_page():
    st.markdown('<div class="main-title">Signup</div>', unsafe_allow_html=True)
    with st.form(key='signup_form'):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')

        # Additional fields for doctors and hospitals
        full_name = st.text_input("Full Name")
        hospital_name = st.text_input("Hospital/Clinic Name")
        specialization = st.text_input("Specialization")
        location = st.text_input("Location")
        contact_number = st.text_input("Contact Number")

        submit_button = st.form_submit_button(label='Signup')

        if submit_button:
            st.success(f"Account created for {username}!")


def subscribe_page(plans):
    st.markdown('<div class="main-title">Subscribe</div>', unsafe_allow_html=True)

    plan_names = [plan["name"] for plan in plans]
    selected_plan_index = st.selectbox("Select a plan", range(len(plan_names)), format_func=lambda i: plan_names[i])

    if selected_plan_index is not None:
        selected_plan = plans[selected_plan_index]
        st.info(f"You selected the {selected_plan['name']}.")
        st.write(f"**Price:** ${selected_plan['price']:.2f}/month")
        st.write("**Features:**")
        for feature in selected_plan["features"]:
            st.write(f"- {feature}")

    payment_method = st.radio("Payment Method", ["Credit Card", "PayPal", "BaridiMob", "CCP"])

    if payment_method:
        st.info(f"Selected payment method: {payment_method}")

    if selected_plan_index is not None and st.button("Proceed to Payment"):
        with st.spinner('Payment Loading...'):
            # Simulate payment processing
            import time
            time.sleep(3)
            st.success("Payment Successful!")
            st.info(f"Thank you for subscribing to the {plans[selected_plan_index]['name']}.")

if __name__ == "__main__":
    st.set_page_config(layout="centered")
    page = st.sidebar.radio("Go to", ["Home", "Login", "Signup", "Subscribe"])
    landing_page()

