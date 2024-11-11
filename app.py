# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import psycopg2

# from db import get_db_connection
# conn=get_db_connection()

# # Functions for different pages
# st.set_page_config(layout="wide")

# query = """
#     SELECT 
#     s.stud_id, s.name, s.age, s.class, s.birthdate, s.gender, 
#     s.nri, s.address, s.fees, fp.fees_paid
#     FROM 
#     students s
#     LEFT JOIN 
#     fee_paid fp ON s.stud_id = fp.id;
#     """
# data = pd.read_sql(query, conn)
# # df=pd.DataFrame(rows,columns=['ID','Name','Age', 'Class', 'Birth Date', 'Gender', 'Nri', 'Address', 'Fees'])
# data = pd.read_sql(query, conn)
# data.columns = [
#     "ID", "Name", "Age", "Class", "Birthdate", "Gender", 
#     "NRI Status", "Address", "Fees", "Fees Paid"
# ]

# def home_page():
#     st.title("Students Dashboard")
#     cur=conn.cursor()
    
#     # student table fetch with fe paid
#     query = """
#     SELECT 
#     s.stud_id, s.name, s.age, s.class, s.birthdate, s.gender, 
#     s.nri, s.address, s.fees, fp.fees_paid
#     FROM 
#     students s
#     LEFT JOIN 
#     fee_paid fp ON s.stud_id = fp.id;
#     """
#     data = pd.read_sql(query, conn)
#     # df=pd.DataFrame(rows,columns=['ID','Name','Age', 'Class', 'Birth Date', 'Gender', 'Nri', 'Address', 'Fees'])
#     data = pd.read_sql(query, conn)
#     data.columns = [
#     "ID", "Name", "Age", "Class", "Birthdate", "Gender", 
#     "NRI Status", "Address", "Fees", "Fees Paid"
# ]
#     col1, col2  = st.columns([1,1])  # Create two columns
    
    
#     # department table fetch
#     cur.execute("SELECT * From department;")
#     dep=cur.fetchall()
#     dep_df=pd.DataFrame(dep,columns=['Teachers','Department'])
    
#     with col1:
#         st.subheader("Students Table")
#         st.dataframe(data,width=15000, height=700)
    
#     with col2:
#         st.subheader("Department Table")
#         st.dataframe(dep_df,width=15000)
        
       
        

    
#     col5,col6=st.columns([1,1])
    
#     with col5:
#         g=data['Gender'].value_counts()  
#         fig, ax = plt.subplots(dpi=90) # Create a figure and axis
#         explode = [0.01 if i == 0 else 0 for i in range(len(g))]
#         ax.pie(g, labels=g.index, autopct='%1.1f%%', startangle=140, colors=['#605678', '#54473F'],explode=explode,textprops={'fontsize': 5})
#         ax.set_title('Gender Ratio',fontsize=10)   
#         st.pyplot(fig,use_container_width=False) # Display the figure in Streamlit
#         #    GEnder ratio pie
        
#     with col6:
#         st.subheader("NRI Status Count")
#         fig5, ax5 = plt.subplots(dpi=90)
#         n=data['NRI Status'].value_counts()
#         ax5.pie(n, labels=n.index,autopct='%1.1f%%', startangle=140, colors=['#118AB2', '#06D6A0'],explode=explode,textprops={'fontsize': 5})
#         # sns.countplot(x="NRI Status", data=data, palette="viridis", ax=ax)
#         # ax5.set_title("Count of NRI Status")
#         # ax5.set_xlabel("NRI Status")
#         # ax5.set_ylabel("Count")
#         st.pyplot(fig5) 
            
    
#     col3,col4 =st.columns([1,1])
    
#     with col3:
#         fig2, ax1 = plt.subplots(dpi=90)
#         st.subheader("Average Fees by Class and Gender")
#         sns.barplot(x="Class", y="Fees", data=data, estimator=np.mean, hue="Gender", palette="viridis")
#         ax1.set_title("Average Fees by Class and Gender")
#         ax1.set_xlabel("Class")
#         ax1.set_ylabel("Average Fees")
#         st.pyplot(fig2)
    
#     with col4:
#         fees_paid_counts = data['Fees Paid'].value_counts()
#         fig4, ax4 = plt.subplots(dpi=90)
#         fees_paid_counts.plot.pie(autopct='%1.1f%%', startangle=90, ax=ax4, legend=False, colors=['#2ca02c', '#ff7f0e'], labels=['Paid', 'Not Paid'], explode=explode)
#         ax4.set_title("Fees Paid or Not Distribution")

#         st.pyplot(fig4) 
            
    
#     st.subheader("Edit or Add Student Records")   
#     with st.form(key="edit_student_form"):
#         stud_id = st.text_input("Student ID (Leave blank to add a new student)")
#         name = st.text_input("Name")
#         age = st.number_input("Age", min_value=0)
#         class_level = st.number_input("Class", min_value=1)
#         birthdate = st.date_input("Birthdate")
#         gender = st.selectbox("Gender", options=["M", "F"])
#         nri = st.checkbox("NRI Status")
#         address = st.text_area("Address")
#         fees = st.number_input("Fees", min_value=10000, max_value=100000)
#         submit_button = st.form_submit_button(label="Save Student Record")
        
#         if submit_button:
#             cur = conn.cursor()
#             if stud_id:
#                 # Update existing record
#                 cur.execute("""
#                     UPDATE students SET name=%s, age=%s, class=%s, birthdate=%s,
#                     gender=%s, nri=%s, address=%s, fees=%s WHERE stud_id=%s
#                 """, (name, age, class_level, birthdate, gender, nri, address, fees, stud_id))
#                 st.success(f"Student ID {stud_id} updated successfully.")
#             else:
#                 # Insert new record
#                 cur.execute("""
#                     INSERT INTO students (name, age, class, birthdate, gender, nri, address, fees)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#                 """, (name, age, class_level, birthdate, gender, nri, address, fees))
#                 st.success("New student added successfully.")
#             conn.commit()
#             cur.close() 

            
#     st.subheader("Edit or Add Fees Paid Status")
#     with st.form(key="edit_fees_form"):
#         fee_stud_id = st.number_input("Student ID for Fee Status", min_value=1)
#         fees_paid = st.selectbox("Fees Paid", options=[True, False])
#         submit_fee_button = st.form_submit_button(label="Save Fee Status")
        
#         if submit_fee_button:
#             cur = conn.cursor()
#             cur.execute("SELECT id FROM fee_paid WHERE id = %s", (fee_stud_id,))
#             if cur.fetchone():
#                 # Update existing fee status
#                 cur.execute("UPDATE fee_paid SET fees_paid = %s WHERE id = %s", (fees_paid, fee_stud_id))
#                 st.success(f"Fee status for Student ID {fee_stud_id} updated successfully.")
#             else:
#                 # Insert new fee status record
#                 cur.execute("INSERT INTO fee_paid (id, fees_paid) VALUES (%s, %s)", (fee_stud_id, fees_paid))
#                 st.success("Fee status added for new student.")
#             conn.commit()
#             cur.close()                       
        


# if 'page' not in st.session_state:
#     st.session_state.page="Home"





# # # Sidebar with stacked buttons (rows)
# # if st.sidebar.button("Home"):
# #     st.session_state.page = "Home"
# # if st.sidebar.button("Edit Student Details"):
# #     st.session_state.page = "Edit Student Details"
# # if st.sidebar.button("Stats"):
# #     st.session_state.page = "Stats"

# # Render the selected page
# if st.session_state.page == "Home":
#     home_page()
# # elif st.session_state.page == "Edit Student Details":
# #     edit_student_page()
# # elif st.session_state.page == "Stats":
# #     stats_page()


# optimized code for egrest cost-----------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import psycopg2
from db import get_db_connection

# Initialize connection
st.set_page_config(layout="wide")
conn = get_db_connection()

# Cache queries to reduce repeated database calls
@st.cache_data
def fetch_data():
    query = """
        SELECT 
        s.stud_id, s.name, s.age, s.class, s.birthdate, s.gender, 
        s.nri, s.address, s.fees, fp.fees_paid
        FROM 
        students s
        LEFT JOIN 
        fee_paid fp ON s.stud_id = fp.id;
    """
    data = pd.read_sql(query, conn)
    data.columns = [
        "ID", "Name", "Age", "Class", "Birthdate", "Gender", 
        "NRI Status", "Address", "Fees", "Fees Paid"
    ]
    return data

@st.cache_data
def fetch_department_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM department;")
    dep = cur.fetchall()
    cur.close()
    dep_df = pd.DataFrame(dep, columns=['Teachers', 'Department'])
    return dep_df

# Page Function
def home_page():
    st.title("Students Dashboard")
    
    # Fetch cached data
    data = fetch_data()
    dep_df = fetch_department_data()

    col1, col2 = st.columns([1,1])
    
    with col1:
        st.subheader("Students Table")
        st.dataframe(data, width=1500, height=700)
    
    with col2:
        st.subheader("Department Table")
        st.dataframe(dep_df, width=1500)
        
    col3, col4 = st.columns([1,1])
    
    with col3:
        gender_counts = data['Gender'].value_counts()
        fig, ax = plt.subplots(dpi=90)
        explode = [0.01 if i == 0 else 0 for i in range(len(gender_counts))]
        ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, 
               colors=['#605678', '#54473F'], explode=explode, textprops={'fontsize': 5})
        ax.set_title('Gender Ratio', fontsize=10)
        st.pyplot(fig)
    
    with col4:
        nri_counts = data['NRI Status'].value_counts()
        fig2, ax2 = plt.subplots(dpi=90)
        explode = [0.01 if i == 0 else 0 for i in range(len(nri_counts))]
        ax2.pie(nri_counts, labels=nri_counts.index, autopct='%1.1f%%', startangle=140, 
                colors=['#118AB2', '#06D6A0'], explode=explode, textprops={'fontsize': 5})
        ax2.set_title("NRI Status Count")
        st.pyplot(fig2)
    
    col5, col6 = st.columns([1,1])
    
    with col5:
        fig3, ax3 = plt.subplots(dpi=90)
        sns.barplot(x="Class", y="Fees", data=data, estimator=np.mean, hue="Gender", palette="viridis", ax=ax3)
        ax3.set_title("Average Fees by Class and Gender")
        ax3.set_xlabel("Class")
        ax3.set_ylabel("Average Fees")
        st.pyplot(fig3)
    
    with col6:
        fees_paid_counts = data['Fees Paid'].value_counts()
        fig4, ax4 = plt.subplots(dpi=90)
        explode = [0.01 if i == 0 else 0 for i in range(len(fees_paid_counts))]
        ax4.pie(fees_paid_counts, labels=['Paid', 'Not Paid'], autopct='%1.1f%%', startangle=90, 
                colors=['#2ca02c', '#ff7f0e'], explode=explode)
        ax4.set_title("Fees Paid or Not Distribution")
        st.pyplot(fig4)

    st.subheader("Edit or Add Student Records")
    def save_student_record(stud_id, name, age, class_level, birthdate, gender, nri, address, fees):
        try:
            with conn.cursor() as cur:
                if stud_id:
                    # Update existing record
                    cur.execute("""
                        UPDATE students SET  name=%s, age=%s, class=%s, birthdate=%s,
                        gender=%s, nri=%s, address=%s, fees=%s WHERE stud_id=%s
                    """, (name, age, class_level, birthdate, gender, nri, address, fees, stud_id))
                    st.success(f"Student ID {stud_id} updated successfully.")
                else:
                    # Insert new record
                    cur.execute("""
                        INSERT INTO students (stud_id, name, age, class, birthdate, gender, nri, address, fees)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (stud_id, name, age, class_level, birthdate, gender, nri, address, fees))
                    st.success("New student added successfully.")
                conn.commit()
        except Exception as e:
            st.error("Error saving student record.")
            st.write(e)

# Function to save fees status
    def save_fees_status(fee_stud_id, fees_paid):
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM fee_paid WHERE id = %s", (fee_stud_id,))
                if cur.fetchone():
                    # Update existing fee status
                    cur.execute("UPDATE fee_paid SET fees_paid = %s WHERE id = %s", (fees_paid, fee_stud_id))
                    st.success(f"Fee status for Student ID {fee_stud_id} updated successfully.")
                else:
                    # Insert new fee status
                    cur.execute("INSERT INTO fee_paid (id, fees_paid) VALUES (%s, %s)", (fee_stud_id, fees_paid))
                    st.success("Fee status added for new student.")
                conn.commit()
        except Exception as e:
            st.error("Error saving fee status.")
            st.write(e)

    st.header("Student Records Management")

# Form to edit or add student record
    with st.form(key="edit_student_form"):
        stud_id = st.text_input("Student ID (Leave blank to add a new student)")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        class_level = st.number_input("Class", min_value=1)
        birthdate = st.date_input("Birthdate")
        gender = st.selectbox("Gender", options=["M", "F"])
        nri = st.checkbox("NRI Status")
        address = st.text_area("Address")
        fees = st.number_input("Fees", min_value=10000, max_value=100000)
        submit_button = st.form_submit_button(label="Save Student Record")
    
    if submit_button:
        save_student_record(stud_id, name, age, class_level, birthdate, gender, nri, address, fees)

# Form to edit or add fees paid status
    st.subheader("Edit or Add Fees Paid Status")
    with st.form(key="edit_fees_form"):
        fee_stud_id = st.number_input("Student ID for Fee Status", min_value=1)
        fees_paid = st.selectbox("Fees Paid", options=[True, False])
        submit_fee_button = st.form_submit_button(label="Save Fee Status")
        
        if submit_fee_button:
            save_fees_status(fee_stud_id, fees_paid)


if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Render the selected page
if st.session_state.page == "Home":
    home_page()
