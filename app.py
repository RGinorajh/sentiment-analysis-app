import streamlit as st
from transformers import pipeline

# Load the sentiment analysis model
model_name = "GinorajhR/GBert"
classifier = pipeline("sentiment-analysis", model=model_name)

# Add padding to the bottom of the content for the footer
st.markdown("""
<style>
.stApp {
    padding-bottom: 200px !important;  /* Increased padding to account for footer */
    min-height: 100vh;
}

/* Main content container */
.block-container {
    padding-bottom: 200px !important;
}
</style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("😊 Sentiment Analysis App")
st.write("Analyze the sentiment of your text in seconds!")

# Sidebar with instructions
with st.sidebar:
    st.header("Instructions")
    st.write("1. Enter your text in the box below.")
    st.write("2. Click 'Analyze Sentiment' to see the results.")
    st.write("3. View the sentiment and confidence score.")

# Text input
user_input = st.text_area("Enter your text here:",height=150)

# Analyze button with Instagram-like gradient
st.markdown("""
<style>
div.stButton > button:first-child {
    background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 25px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    margin-bottom: 20px;
}
div.stButton > button:first-child:hover {
    transform: scale(1.05);
    box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.2);
}
</style>
""", unsafe_allow_html=True)

if st.button("Analyze Sentiment"):
    if user_input:
        # Handle specific phrases
        if "hate" in user_input.lower():
            sentiment = "Negative 😠"
            score = 1.0
        else:
            # Get sentiment prediction from the model
            result = classifier(user_input)[0]
            label = result['label']
            score = result['score']
            sentiment = "Positive 😊" if label == "LABEL_1" else "Negative 😠"

        # Display sentiment with emoji
        st.subheader("Sentiment:")
        if sentiment == "Positive 😊":
            st.success(f"{sentiment}")
        else:
            st.error(f"{sentiment}")

        # Display confidence score with a progress bar
        st.subheader("Confidence:")
        st.progress(score)
        st.write(f"Confidence: {score * 100:.2f}%")
        
        # Add some spacing after the results
        st.markdown("<div style='margin-bottom: 50px;'></div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter some text.")

# Back/Refresh Button in Corner
st.markdown("""
<style>
.back-button {
    position: fixed;
    top: 20px;
    left: 20px;
    font-size: 24px;
    color: #405DE6;
    cursor: pointer;
    z-index: 9999;  /* Highest z-index to ensure visibility */
    background: white;
    border-radius: 50%;
    padding: 8px;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}
.back-button:hover {
    color: #833AB4;
    transform: scale(1.1);
}
</style>
<div class="back-button" onclick="window.location.reload()">🔄</div>
""", unsafe_allow_html=True)

# Gradient Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
    color: white;
    text-align: center;
    padding: 15px 0;
    font-family: Arial, sans-serif;
    z-index: 100;  /* Lower than back button */
    height: auto;
    min-height: 100px;
}
.footer p {
    margin: 5px 0;
}
.footer a {
    color: white;
    margin: 0 15px;
    text-decoration: none;
    font-size: 18px;
    display: inline-flex;
    align-items: center;
}
.footer a:hover {
    color: #FFD700;
}
.footer i {
    margin-right: 5px;
}
</style>
<div class="footer">
    <p>Built with ❤️ by <strong>GinorajhR</strong></p>
    <div>
        <a href="https://github.com/yourusername" target="_blank">
            <i class="fab fa-github"></i> GitHub
        </a>
        <a href="https://linkedin.com/in/yourusername" target="_blank">
            <i class="fab fa-linkedin"></i> LinkedIn
        </a>
        <a href="https://twitter.com/yourusername" target="_blank">
            <i class="fab fa-twitter"></i> Twitter
        </a>
    </div>
</div>
""", unsafe_allow_html=True)