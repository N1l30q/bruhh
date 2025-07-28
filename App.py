
import streamlit as st

# --- Sign Up Page ---
if 'signed_up' not in st.session_state:
    st.session_state['signed_up'] = False

if not st.session_state['signed_up']:
    st.title("Sign Up to Join the Study Group Platform")
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    if st.button("Sign Up"):
        if name.strip() and email.strip():
            st.session_state['signed_up'] = True
            st.success(f"Welcome, {name}! You have signed up successfully.")
            st.rerun()
        else:
            st.error("Please enter both your name and email to sign up.")
    st.stop()

st.set_page_config(page_title="Website", page_icon=":tada:", layout="wide")

with st.container():
    st.title("Hello! Welcome to Our Study Group Platform :wave:")
    st.write("Welcome to our study group platform! Here, you can find study partners, share resources, and collaborate on projects.")

st.markdown("<br><br>", unsafe_allow_html=True)  # Add bigger space
st.markdown("---")  # Divider

with st.container():
    st.subheader("How to Use This Website")
    st.markdown("""
    1. **Post Your Subject:** Enter the subject you are currently studying to let others know what you're working on.
    2. **Find Study Partners:** Browse the list of subjects to find other students studying the same topic.
    3. **Message Others:** Connect and chat with students who share your interests to form study groups or ask questions.
    4. **Share Resources:** Upload and share helpful materials with your study group.
    5. **Collaborate:** Work together on assignments, projects, or exam preparation.
    """)

st.markdown("<br><br>", unsafe_allow_html=True)  # Add bigger space
st.markdown("---")  # Divider

# User options: Create a post or look for posts
st.subheader("What would you like to do?")
option = st.selectbox(
    "Choose an action:",
    ("Create a Post", "Look for Posts")
)

if option == "Create a Post":
    st.markdown("#### Create a New Study Post")
    st.info("""
    **Tips for a Great Post Description:**
    - Mention the specific topic or course you are studying.
    - Share where you prefer to study (e.g., library, online, coffee shop).
    - Suggest your preferred study times or availability.
    - Add any goals or resources you want to share.
    """)
    subject = st.text_input("What subject are you studying?")
    description = st.text_area("Add more details (optional):")
    if st.button("Post"): 
        st.session_state['my_post'] = {'subject': subject, 'description': description}
        st.success(f"Your post about '{subject}' has been created!")
elif option == "Look for Posts":
    st.markdown("#### Browse Study Posts")
    if 'my_post' in st.session_state:
        st.markdown("**Your Post:**")
        st.markdown(f"- **Subject:** {st.session_state['my_post']['subject']}")
        st.markdown(f"- **Description:** {st.session_state['my_post']['description']}")
        st.markdown("---")

    # Simulated posts from other users
    other_posts = [
        {"name": "Alice", "subject": "Calculus", "description": "Looking for a study buddy for morning sessions at the library."},
        {"name": "Bob", "subject": "Biology", "description": "Prefers online study groups, evenings."},
        {"name": "Charlie", "subject": "History", "description": "Wants to meet at the coffee shop on weekends."}
    ]

    st.markdown("**Other Students' Posts:**")
    for post in other_posts:
        col1, col2 = st.columns([2, 6])
        with col1:
            if st.button(post["name"], key=f"user_{post['name']}"):
                st.session_state["chat_with"] = post["name"]
        with col2:
            st.markdown(f"- **Subject:** {post['subject']}  ")
            st.markdown(f"- **Description:** {post['description']}")
        st.markdown("---")

    # Chat interface
    if "chat_with" in st.session_state:
        chat_user = st.session_state["chat_with"]
        st.markdown(f"### Chat with {chat_user}")
        if f"chat_history_{chat_user}" not in st.session_state:
            st.session_state[f"chat_history_{chat_user}"] = []
        chat_history = st.session_state[f"chat_history_{chat_user}"]
        for msg in chat_history:
            st.markdown(msg)
        chat_input = st.text_input(f"Message {chat_user}", key=f"chat_input_{chat_user}")
        if st.button("Send", key=f"send_{chat_user}"):
            if chat_input.strip():
                chat_history.append(f"You: {chat_input}")
                st.session_state[f"chat_history_{chat_user}"] = chat_history
                st.experimental_rerun()


