import hashlib
import time
import streamlit as st

# Define a block
class Block:
    def __init__(self, student_name, grade, previous_hash):
        self.student_name = student_name
        self.grade = grade
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Create a hash for the block
    def calculate_hash(self):
        data = self.student_name + self.grade + str(self.timestamp) + self.previous_hash
        return hashlib.sha256(data.encode()).hexdigest()

# Define the blockchain
class ReportCardBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # First block (genesis block)
    def create_genesis_block(self):
        genesis = Block("Genesis", "None", "0")
        self.chain.append(genesis)

    # Add new block (report card)
    def add_report_card(self, student_name, grade):
        last_block = self.chain[-1]
        new_block = Block(student_name, grade, last_block.hash)
        self.chain.append(new_block)

    # Display all report cards
    def display_chain(self):
        st.write("### Report Card Blockchain")
        for block in self.chain:
            st.write(f"#### Student: {block.student_name}")
            st.write(f"Grade: {block.grade}")
            st.write(f"Timestamp: {time.ctime(block.timestamp)}")
            st.write(f"Hash: {block.hash}")
            st.write(f"Previous Hash: {block.previous_hash}")
            st.write("---")

# Streamlit UI
st.title("School Report Card Blockchain")

school_chain = ReportCardBlockchain()

# Input form to add a report card
with st.form("Add Report Card"):
    student_name = st.text_input("Student Name")
    grade = st.text_input("Grade (e.g., Math: A)")
    submit_button = st.form_submit_button("Add Report Card")
    
    if submit_button and student_name and grade:
        school_chain.add_report_card(student_name, grade)
        st.success(f"Report card for {student_name} added successfully!")

# Display the blockchain
school_chain.display_chain()
