  
import streamlit as st  
import joblib  
import pandas as pd  

# Load trained model  
model = joblib.load("RandomForest_Airdrop_Model.pkl")  

# Streamlit UI  
st.title("Crypto Airdrop Success Predictor")  
st.write("Enter details about the airdrop project to predict its success score.")  

# User Inputs  
funding = st.number_input("Funding Amount ($M)", min_value=0.0, step=0.1)  
tasks_required = st.selectbox("Tasks Required", ["None", "Social Engagement", "Referral", "Staking", "Multiple"])  
free_to_join = st.selectbox("Free to Join?", ["Yes", "No"])  
vc_backing = st.selectbox("VC Backing?", ["Yes", "No"])  
airdrops_longevity = st.number_input("Airdrop Longevity (Days)", min_value=0, step=1)  
token_utility = st.selectbox("Token Utility", ["Governance", "Payment", "Staking", "Other"])  
team_size = st.number_input("Team Size", min_value=1, step=1)  
github_activity = st.selectbox("GitHub Activity", ["Low", "Medium", "High"])  
twitter_followers = st.number_input("Twitter Followers", min_value=0, step=100)  
community_size = st.number_input("Community Size", min_value=0, step=100)  
market_condition = st.selectbox("Market Condition", ["Bull", "Bear", "Neutral"])  
blockchain = st.selectbox("Blockchain", ["Ethereum", "Solana", "Polygon", "BNB Chain", "Other"])  
sector = st.text_input("Sector (e.g., DeFi, NFT, Gaming)")
initial_value = st.number_input("Initial Value ($)", min_value=0.0, step=0.01)  
peak_value = st.number_input("Peak Value ($)", min_value=0.0, step=0.01)  
average_value = st.number_input("Average Value ($)", min_value=0.0, step=0.01)  

# Convert categorical inputs to numerical  
tasks_required_mapping = {"None": 0, "Social Engagement": 1, "Referral": 2, "Staking": 3, "Multiple": 4}  
free_to_join_mapping = {"Yes": 1, "No": 0}  
vc_backing_mapping = {"Yes": 1, "No": 0}  
token_utility_mapping = {"Governance": 0, "Payment": 1, "Staking": 2, "Other": 3}  
github_mapping = {"Low": 0, "Medium": 1, "High": 2}  
market_mapping = {"Bull": 1, "Bear": -1, "Neutral": 0}  
blockchain_mapping = {"Ethereum": 0, "Solana": 1, "Polygon": 2, "BNB Chain": 3, "Other": 4}  

# Encode categorical values  
tasks_required_encoded = tasks_required_mapping[tasks_required]  
free_to_join_encoded = free_to_join_mapping[free_to_join]  
vc_backing_encoded = vc_backing_mapping[vc_backing]  
token_utility_encoded = token_utility_mapping[token_utility]  
github_encoded = github_mapping[github_activity]  
market_encoded = market_mapping[market_condition]  
blockchain_encoded = blockchain_mapping[blockchain]  

sector_mapping = {"DeFi": 0, "NFT": 1, "Gaming": 2, "Infrastructure": 3, "Other": 4}
sector_encoded = sector_mapping.get(sector, 4)  # Default to "Other" if not found

# Predict button  
if st.button("Predict Airdrop Success"):  
    input_data = pd.DataFrame([[funding, tasks_required_encoded, free_to_join_encoded, vc_backing_encoded,  
                            airdrops_longevity, token_utility_encoded, team_size, github_encoded,  
                            twitter_followers, community_size, market_encoded, blockchain_encoded, sector_encoded,
                            initial_value, peak_value, average_value]],  
                          columns=["Funding ($M)", "Tasks Required", "Free to Join(Yes=1, No=0)", "VC Backing(Yes=1, No=0)",  
                                   "Airdrop Longevity (Days)", "Token Utility", "Team Size", "GitHub Activity(Low=0, Medium=1, High=2)",  
                                   "Twitter Followers", "Community Size", "Market Condition(Bull=1, Bear= -1, Neutral=0)",  
                                   "Blockchain",  "Sector", "Initial Value ($)", "Peak Value ($)", "Average value($)"])  
    prediction = model.predict(input_data)  
    st.success(f"Predicted Success Score: {prediction[0]:.2f}")  
