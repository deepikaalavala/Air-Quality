import streamlit as st

# Set page configuration
st.set_page_config(page_title="Login Page", layout="wide")

# Define initial user credentials
if "USER_CREDENTIALS" not in st.session_state:
    st.session_state["USER_CREDENTIALS"] = {"admin": "password123", "user1": "pass1", "user2": "pass2"}

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# Login function
def login(username, password):
    if username in st.session_state["USER_CREDENTIALS"] and st.session_state["USER_CREDENTIALS"][username] == password:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
    else:
        st.error("Invalid username or password. Please try again.")

# Signup function
def signup(new_username, new_password, confirm_password):
    if new_username in st.session_state["USER_CREDENTIALS"]:
        st.error("Username already exists. Please choose a different username.")
    elif new_password != confirm_password:
        st.error("Passwords do not match. Please try again.")
    else:
        st.session_state["USER_CREDENTIALS"][new_username] = new_password
        st.success("Signup successful! Please log in.")

# Logout function
def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""

# Main Page Logic
if not st.session_state["logged_in"]:
    # Hide sidebar for the login/signup page
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Tabs for Login and Signup
    tab1, tab2 = st.tabs(["Login", "Signup"])

    # Login Tab
    with tab1:
        st.title("Login Page")

        # Use columns to shorten text boxes
        col1, col2, col3 = st.columns([2, 4, 2])
        with col2:
            username = st.text_input("Username", key="login_username", max_chars=20)
            password = st.text_input("Password", type="password", key="login_password", max_chars=20)
            if st.button("Login"):
                login(username, password)

    # Signup Tab
    with tab2:
        st.title("Signup Page")

        # Use columns to shorten text boxes
        col1, col2, col3 = st.columns([2, 4, 2])
        with col2:
            new_username = st.text_input("New Username", key="signup_username", max_chars=20)
            new_password = st.text_input("New Password", type="password", key="signup_password", max_chars=20)
            confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password", max_chars=20)
            if st.button("Signup"):
                signup(new_username, new_password, confirm_password)

else:
    # Sidebar for Logout Button Only
    st.sidebar.button("Logout", on_click=logout)

    # Main content after login
    st.title(f"Welcome, {st.session_state['username']}!")
    st.write("You are successfully logged in.")

    # Embed Power BI report
    st.markdown(
        """
        <iframe title="Power BI Report" width="100%" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiMWE2YWFiYzYtMjM2Ny00YTg1LTg3MmMtZTM4ZGNkMjlhZTQ4IiwidCI6ImY1YjcxNDhiLTNmYzYtNDYwNi04MjgzLWM3MjJmNDQzOGYxMiJ9" frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True,
    )
#https://app.powerbi.com/view?r=eyJrIjoiZGJkYTk1NGQtNWUzMi00MmJhLThmZDMtNTAzOTNjMmRmZWM4IiwidCI6IjkzZTljMTgyLTdhOWMtNGI4YS04YzY1LTM3OTMyNDZlYzgzMyJ9
