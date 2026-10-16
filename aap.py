import streamlit as st

# Page configuration
st.set_page_config(page_title="Simple Form", page_icon="📝", layout="centered")

st.title("📝 Form Filing Website")
st.write("Apni details fill karein aur submit karein.")

# Form creation
with st.form("user_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    query_type = st.selectbox("Select Query Type", ["General Inquiry", "Technical Support", "Feedback"])
    message = st.text_area("Your Message")
    
    # Submit button
    submitted = st.form_submit_button("Submit Form")

# Form submission logic
if submitted:
    if name and email:
        st.success(f"Thank you, {name}! Aapka form successfully submit ho gaya hai.")
        
        # Submitted data display (Optional)
        st.write("### Submitted Details:")
        st.write(f"- **Name:** {name}")
        st.write(f"- **Email:** {email}")
        st.write(f"- **Phone:** {phone if phone else 'N/A'}")
        st.write(f"- **Category:** {query_type}")
        st.write(f"- **Message:** {message if message else 'N/A'}")
    else:
        st.error("Kripya kam se kam apna Name aur Email zaroor bharein!")
