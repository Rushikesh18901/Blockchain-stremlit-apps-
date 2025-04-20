import streamlit as st
import time
import hashlib

# Title
st.title("🧬 Simple Medical Blockchain")

# Initialize session state for blockchain
if 'blockchain' not in st.session_state:
    # Genesis block
    def create_block(index, data, previous_hash):
        return {
            "index": index,
            "data": data,
            "timestamp": time.time(),
            "previous_hash": previous_hash
        }

    def generate_hash(block):
        block_string = f"{block['index']}{block['data']}{block['timestamp']}{block['previous_hash']}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Create the genesis block
    genesis_block = create_block(1, "Genesis Block", "0")
    st.session_state.blockchain = [genesis_block]

# Functions for creating and adding blocks
def create_block(index, data, previous_hash):
    return {
        "index": index,
        "data": data,
        "timestamp": time.time(),
        "previous_hash": previous_hash
    }

def generate_hash(block):
    block_string = f"{block['index']}{block['data']}{block['timestamp']}{block['previous_hash']}"
    return hashlib.sha256(block_string.encode()).hexdigest()

def add_block(data):
    previous_block = st.session_state.blockchain[-1]
    new_index = previous_block["index"] + 1
    new_hash = generate_hash(previous_block)
    new_block = create_block(new_index, data, new_hash)
    st.session_state.blockchain.append(new_block)

# Input form to add new block
st.subheader("➕ Add New Medical Record")
with st.form("new_block_form"):
    record_data = st.text_input("Enter Patient Medical Record:")
    submitted = st.form_submit_button("Add Record")
    if submitted and record_data:
        add_block(record_data)
        st.success("✅ New block added to the blockchain!")

# Display the blockchain
st.subheader("🔗 Current Blockchain")
for block in st.session_state.blockchain:
    st.markdown(f"""
    **Block #{block['index']}**
    - 📝 **Data:** {block['data']}
    - 🕒 **Timestamp:** {block['timestamp']}
    - 🔐 **Previous Hash:** `{block['previous_hash']}`
    ---
    """)
