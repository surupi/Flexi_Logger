import streamlit as st
import re
import hashlib
import base64
import time

st.set_page_config(
    page_title="FlexiLogger Playground 🪵",
    page_icon="🪵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for crisp, modern light mode aesthetics
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        color: #0f172a;
    }
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }
    .metric-card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        color: #0f172a;
    }
    .log-box {
        background-color: #f1f5f9;
        color: #0369a1;
        font-family: 'Courier New', Courier, monospace;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #0284c7;
        font-size: 16px;
        white-space: pre-wrap;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
    }
    .highlight-positive {
        color: #15803d;
        font-weight: bold;
    }
    .highlight-negative {
        color: #b91c1c;
        font-weight: bold;
    }
    div[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Helper Functions for Transformations
def mask_pii(text):
    masked = re.sub(r'(?i)\b([a-z0-9._%+-]+)@([a-z0-9.-]+\.[a-z]{2,})\b', r'\1***@***.\2', text)
    masked = re.sub(r'\b(?:\d[ -]*?){13,16}\b', '****-****-****-****', masked)
    masked = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '***-***-****', masked)
    return masked

def sha256_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def to_nato(text):
    nato_dict = {
        'a': "Alpha", 'b': "Bravo", 'c': "Charlie", 'd': "Delta", 'e': "Echo",
        'f': "Foxtrot", 'g': "Golf", 'h': "Hotel", 'i': "India", 'j': "Juliett",
        'k': "Kilo", 'l': "Lima", 'm': "Mike", 'n': "November", 'o': "Oscar",
        'p': "Papa", 'q': "Quebec", 'r': "Romeo", 's': "Sierra", 't': "Tango",
        'u': "Uniform", 'v': "Victor", 'w': "Whiskey", 'x': "Xray", 'y': "Yankee", 'z': "Zulu"
    }
    return " ".join([nato_dict.get(c.lower(), c) for c in text])

def rot13(text):
    res = []
    for c in text:
        if 'a' <= c <= 'z':
            res.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            res.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
        else:
            res.append(c)
    return "".join(res)

def pig_latin(text):
    def convert_word(word):
        if not word.isalpha():
            return word
        vowels = "aeiouAEIOU"
        if word[0] in vowels:
            return word + "way"
        for i, char in enumerate(word):
            if char in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"
    
    words = re.split(r'(\s+)', text)
    return "".join([convert_word(w) for w in words])

def to_hex(text):
    return " ".join([hex(ord(c))[2:] for c in text])

def to_binary(text):
    return " ".join([format(ord(c), '08b') for c in text])

# Sidebar Navigation
st.sidebar.title("🪵 FlexiLogger")
st.sidebar.markdown("---")
category = st.sidebar.radio(
    "Select Transformation Category:",
    ["🛡️ Security & Privacy", "🔠 Ciphers & Phonetic", "🔢 Encodings", "🎨 Formatting & Sentiment", "📊 Animated Progress"]
)

st.title("🪵 FlexiLogger Interactive Playground")
st.caption("Real-time visual demonstration of custom Java FlexiLogger transformations")

# Main Container
if category == "🛡️ Security & Privacy":
    st.subheader("🛡️ Security & PII Redaction")
    input_msg = st.text_area(
        "Enter raw log message:",
        "User john.doe@example.com logged in from 123-456-7890 using credit card 4111-2222-3333-4444",
        height=100
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔒 Masked PII Output")
        masked = mask_pii(input_msg)
        st.markdown(f'<div class="log-box">{masked}</div>', unsafe_allow_html=True)
        st.code('logger.logWithMaskedPii(message);', language='java')

    with col2:
        st.markdown("### 🔑 SHA-256 Digest")
        hashed = sha256_hash(input_msg)
        st.markdown(f'<div class="log-box">[SHA-256] {hashed}</div>', unsafe_allow_html=True)
        st.code('logger.logSha256Hash(message);', language='java')

elif category == "🔠 Ciphers & Phonetic":
    st.subheader("🔠 Ciphers & Text Transformations")
    input_msg = st.text_input("Enter message to transform:", "Attack at dawn with FlexiLogger")
    
    tab1, tab2, tab3, tab4 = st.tabs(["NATO Phonetic", "ROT13 Cipher", "Pig Latin", "Leetspeak"])
    
    with tab1:
        st.markdown("### NATO Phonetic Alphabet")
        output = to_nato(input_msg)
        st.markdown(f'<div class="log-box">{output}</div>', unsafe_allow_html=True)
        st.code('logger.logInNatoPhonetic(message);', language='java')
        
    with tab2:
        st.markdown("### ROT13 Cipher")
        output = rot13(input_msg)
        st.markdown(f'<div class="log-box">{output}</div>', unsafe_allow_html=True)
        st.code('logger.logWithRot13(message);', language='java')
        
    with tab3:
        st.markdown("### Pig Latin")
        output = pig_latin(input_msg)
        st.markdown(f'<div class="log-box">{output}</div>', unsafe_allow_html=True)
        st.code('logger.logInPigLatin(message);', language='java')

    with tab4:
        st.markdown("### Leetspeak")
        output = input_msg.replace('e', '3').replace('o', '0').replace('s', '5').replace('a', '@')
        st.markdown(f'<div class="log-box">{output}</div>', unsafe_allow_html=True)
        st.code('logger.logInLeetSpeak(message);', language='java')

elif category == "🔢 Encodings":
    st.subheader("🔢 Binary, Hex & Base64 Encodings")
    input_msg = st.text_input("Enter text to encode:", "FlexiLogger")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Base64")
        b64 = base64.b64encode(input_msg.encode('utf-8')).decode('utf-8')
        st.markdown(f'<div class="log-box">{b64}</div>', unsafe_allow_html=True)
        st.code('logger.logBase64Encoded(msg);', language='java')

    with col2:
        st.markdown("### Hexadecimal")
        hex_out = to_hex(input_msg)
        st.markdown(f'<div class="log-box">{hex_out}</div>', unsafe_allow_html=True)
        st.code('logger.logInHex(msg);', language='java')

    with col3:
        st.markdown("### 8-Bit Binary")
        bin_out = to_binary(input_msg)
        st.markdown(f'<div class="log-box" style="font-size:12px;">{bin_out}</div>', unsafe_allow_html=True)
        st.code('logger.logInBinary(msg);', language='java')

elif category == "🎨 Formatting & Sentiment":
    st.subheader("🎨 Formatting & Sentiment Highlights")
    input_msg = st.text_input("Enter log statement:", "This is a fantastic feature, but that was a terrible bug!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Sentiment Highlight Log")
        positives = ["good", "great", "happy", "fantastic"]
        negatives = ["bad", "sad", "hate", "terrible", "bug"]
        
        lower = input_msg.lower()
        if any(p in lower for p in positives):
            st.markdown(f'<div class="log-box highlight-positive">🟢 {input_msg}</div>', unsafe_allow_html=True)
        elif any(n in lower for n in negatives):
            st.markdown(f'<div class="log-box highlight-negative">🔴 {input_msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="log-box">⚪ {input_msg}</div>', unsafe_allow_html=True)
        st.code('logger.logWithSentimentHighlight(message);', language='java')

    with col2:
        st.markdown("### HTML / CSS Styled Output")
        color = st.color_picker("Choose span color:", "#38bdf8")
        st.markdown(f'<div class="log-box"><span style="color:{color}; font-weight:bold;">{input_msg}</span></div>', unsafe_allow_html=True)
        st.code(f'logger.logWithHtmlStyle(message, "color: {color}; font-weight: bold");', language='java')

elif category == "📊 Animated Progress":
    st.subheader("📊 Log Progress Bar Simulator")
    task_name = st.text_input("Task Name:", "Downloading database backup...")
    steps = st.slider("Total Steps:", 5, 20, 10)
    
    if st.button("▶️ Simulate Progress Logging"):
        progress_placeholder = st.empty()
        for i in range(steps + 1):
            percent = int((i / steps) * 100)
            units = int((i / steps) * 10)
            bar = "[" + "#" * units + "-" * (10 - units) + "]"
            progress_placeholder.markdown(
                f'<div class="log-box">{task_name} {bar} {percent}%</div>',
                unsafe_allow_html=True
            )
            time.sleep(0.3)
        st.success("Task execution complete!")
        st.code('logger.logWithProgressBar(taskName, step, totalSteps);', language='java')

st.markdown("---")
st.caption("FlexiLogger Java Library Playground | Powered by Streamlit")
