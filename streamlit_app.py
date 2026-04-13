import streamlit as st
import requests
from requests.exceptions import JSONDecodeError, RequestException
import os
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Credit Card Validator",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .valid-card {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        color: #155724;
    }
    .invalid-card {
        background-color: #f8d7da;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        color: #721c24;
    }
    .card-info-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

def check_card(card_num):
    """Validate card and fetch card info"""
    api_key = os.getenv("HANDY_API_KEY")
    if not api_key:
        st.error("❌ API Key not found. Please configure HANDY_API_KEY in your .env file")
        return False, None
    
    card_info = None
    clean_card_num = card_num.replace(" ", "").replace("-", "")
    
    try:
        response = requests.get(
            f"https://data.handyapi.com/bin/{clean_card_num}",
            headers={"x-api-key": api_key},
            timeout=5
        )
        response.raise_for_status()  
        card_info = response.json()
        
    except (JSONDecodeError, RequestException, Exception) as e:
        st.warning(f"⚠️ Could not fetch card info from API: {e}")
        card_info = None
    
    # Validate card using Luhn algorithm
    num_lst = [int(i) for i in clean_card_num[::-1]]

    for i in range(1, len(num_lst), 2):
        num_lst[i] *= 2
        if num_lst[i] > 9:
            num_lst[i] -= 9
    
    is_valid = sum(num_lst) % 10 == 0
    return is_valid, card_info

# Title and description
st.title("💳 Credit Card Validator")
st.write("Validate credit card numbers and get card details")
st.divider()

# Input field
card_number = st.text_input(
    "Enter Card Number",
    placeholder="e.g., 4242 4242 4242 4242",
    max_chars=25
)

# Validate button
if st.button("✓ Validate Card", use_container_width=True, type="primary"):
    if not card_number:
        st.error("Please enter a card number")
    else:
        # Show spinner while processing
        with st.spinner("Validating card..."):
            is_valid, card_info = check_card(card_number)
        
        # Display validation result
        if is_valid:
            st.markdown('<div class="valid-card"><h3>✅ Card is Valid</h3>The card passed the Luhn algorithm check</div>', 
                       unsafe_allow_html=True)
        else:
            st.markdown('<div class="invalid-card"><h3>❌ Card is Invalid</h3>The card failed the Luhn algorithm check</div>', 
                       unsafe_allow_html=True)
        
        st.divider()
        
        # Display card information if available
        if card_info and card_info.get("Status") == "SUCCESS":
            st.subheader("📋 Card Information")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Scheme", card_info.get("Scheme", "N/A"))
                st.metric("Card Type", card_info.get("Type", "N/A"))
            
            with col2:
                st.metric("Card Tier", card_info.get("CardTier", "N/A"))
                country_name = card_info.get("Country", {}).get("Name", "N/A")
                st.metric("Country", country_name)
            
            # Issuer information
            st.markdown('<div class="card-info-box">', unsafe_allow_html=True)
            st.write(f"**Issuer:** {card_info.get('Issuer', 'N/A')}")
            st.markdown('</div>', unsafe_allow_html=True)
        elif card_info:
            st.info("📌 Card passed Luhn check but API didn't return full details")
            st.json(card_info)
        else:
            st.info("📌 Card validation complete but API info unavailable")

st.divider()

# Footer with test cards
with st.expander("Test Card Numbers"):
    st.write("""
    **Valid Test Cards:**
    - `4242 4242 4242 4242` - Visa (Stripe)
    - `5555 5555 5555 4444` - Mastercard
    - `6011 1111 1111 1117` - Discover
    - `3782 822463 10005` - American Express
    """)
