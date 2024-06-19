# Import necessary libraries
import os
import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Set the page configuration
st.set_page_config(
    page_title="Smart Predictions Hub",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Smart Predictions Hub")

# Create the navigation menu with hierarchical structure
option = st.sidebar.selectbox("Choose a section", ("Home", "Predictions"))

# mentioning the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

if option == "Home":
    # Title and subtitle
    st.title("Smart Predictions Hub")
    st.subheader("Your one-stop solution for predictive analytics across various domains")

    # Introduction section
    st.write("""
    Welcome to the Smart Predictions Hub! This platform leverages the power of machine learning to provide accurate predictions in a variety of fields. Explore the different categories to get insights and predictions tailored to your needs.
    """)

    # Insights about the models
    st.header("About Our Models")
    st.write("""
    Our models are built using state-of-the-art machine learning techniques. Each model is trained on extensive datasets to ensure accuracy and reliability. Here’s a quick overview of what you can expect from each category:
    """)

    # Display categories and their models
    st.subheader("Disease Prediction")
    st.write("""
    - **Heart Disease Prediction:** Assesses risk factors to predict heart disease.
    - **Diabetes Prediction:** Uses patient data to predict the likelihood of diabetes.
    - **Parkinson's Disease Prediction:** Identifies early signs of Parkinson's disease.
    - **Cancer Prediction:** Analyzes medical records to forecast cancer occurrence. - **Currently not available**
    - **Stroke Prediction:** Predicts the probability of a stroke based on health metrics. - **Currently not available**
    - **Kidney Disease Prediction:** Forecasts kidney disease using various health indicators. - **Currently not available**
    - **Liver Disease Prediction:** Uses liver function test results for disease prediction. - **Currently not available**
    - **Alzheimer's Disease Prediction:** Predicts the risk of Alzheimer's based on genetic and health data. - **Currently not available**
    """)

    # Add other categories with similar structure
    # ...

elif option == "Predictions":
     # Display default message
    default_message = st.empty()
    default_message.write(
                "### Welcome to the Prediction Hub!\n\n"
                "#### Choose from a Variety of Predictions\n"
                "Explore our diverse range of prediction categories, each offering unique insights and analysis. Whether you're interested in health, finance, customer behavior, or more, our platform has something for everyone.\n\n"
                "#### How It Works\n"
                "1. **Select a Prediction Category**: Use the sidebar to choose a prediction category that interests you.\n"
                "2. **Provide Input**: Fill in the required information for the selected prediction to receive your personalized result.\n"
                "3. **View Your Prediction**: Receive instant feedback based on your inputs and our predictive models.\n\n"
                "#### Start Exploring\n"
                "Click on a prediction category in the sidebar to begin your journey into the world of predictions. Don't hesitate to try different categories to see the range of insights our platform can provide!\n\n"
                "---\n\n"
    )

    with st.sidebar.expander("Disease Prediction"):
        disease_option = st.selectbox("Choose a disease prediction", ["Select any", "Heart Disease Prediction", "Diabetes Prediction", "Parkinson's Disease Prediction", "Cancer Prediction", "Stroke Prediction", "Kidney Disease Prediction", "Liver Disease Prediction", "Alzheimer's Disease Prediction"])
        if disease_option != "Select any":
            default_message.empty(  )
    # Other categories can be added similarly as expanders
    with st.sidebar.expander("Financial Prediction"):
        financial_option = st.selectbox("Choose a financial prediction", ["Select any", "Stock Price Prediction", "Credit Card Fraud Detection", "Loan Default Prediction", "Bankruptcy Prediction", "Cryptocurrency Price Prediction"])

    with st.sidebar.expander("Customer Behavior Prediction"):
        customer_behavior_option = st.selectbox("Choose a customer behavior prediction", ["Select any", "Customer Churn Prediction", "Customer Lifetime Value Prediction", "Sales Forecasting", "Purchase Intent Prediction"])

    with st.sidebar.expander("NLP"):
        nlp_option = st.selectbox("Choose an NLP prediction", ["Select any", "Sentiment Analysis", "Spam Detection", "Text Classification", "Language Translation"])

    with st.sidebar.expander("Weather Prediction"):
        weather_option = st.selectbox("Choose a weather prediction", ["Select any", "Temperature Prediction", "Rainfall Prediction", "Storm Prediction", "Air Quality Prediction"])

    with st.sidebar.expander("Image Processing"):
        image_processing_option = st.selectbox("Choose an image processing prediction", ["Select any", "Facial Recognition", "Object Detection", "Image Classification", "Medical Image Analysis"])

    with st.sidebar.expander("Recommender Systems"):
        recommender_option = st.selectbox("Choose a recommender system", ["Select any", "Movie Recommendation", "Product Recommendation", "Music Recommendation", "Book Recommendation"])

    with st.sidebar.expander("Transportation"):
        transportation_option = st.selectbox("Choose a transportation prediction", ["Select any", "Traffic Prediction", "Flight Delay Prediction", "Vehicle Maintenance Prediction"])

    with st.sidebar.expander("Agriculture"):
        agriculture_option = st.selectbox("Choose an agriculture prediction", ["Select any", "Crop Yield Prediction", "Soil Health Prediction", "Pest Detection"])

    # Display selected prediction UI
    if disease_option == "Heart Disease Prediction":
        st.title('Heart Disease Prediction')
        st.write("**Please fill in all the details to get the prediction.**")

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        # code for Prediction
        heart_diagnosis = ''

        # creating a button for Prediction
        if st.button('Heart Disease Test Result'):
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            
            # Check if any input is empty
            if any(x == '' for x in user_input):
                st.error('Please enter all the details to predict the Heart Disease..')
            else:
                user_input = [float(x) for x in user_input]
                heart_prediction = heart_disease_model.predict([user_input])

                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person is having heart disease'
                else:
                    heart_diagnosis = 'The person does not have any heart disease'

                st.success(heart_diagnosis)
    elif disease_option == "Diabetes Prediction":
        st.title('Diabetes Prediction')
        st.write("**Please fill in all the details to get the prediction.**")

        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            SkinThickness = st.text_input('Skin Thickness value')

        with col2:
            Insulin = st.text_input('Insulin Level')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        with col2:
            Age = st.text_input('Age of the Person')
        
        diab_diagnosis = ''

        # creating a button for Prediction
        if st.button('Diabetes Test Result'):
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

            # Check if any input is empty
            if any(x == '' for x in user_input):
                st.error('Please enter all the details to predict the Diabetes Disease..')
            else:
                user_input = [float(x) for x in user_input]
                diab_prediction = diabetes_model.predict([user_input])

                if diab_prediction[0] == 1:
                    diab_diagnosis = 'The person is diabetic'
                else:
                    diab_diagnosis = 'The person is not diabetic'

                st.success(diab_diagnosis)
    elif disease_option == "Parkinson's Disease Prediction":
        st.title("Parkinson's Disease Prediction")
        st.write("**Please fill in all the details to get the prediction.**")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')

        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')

        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

        with col1:
            RAP = st.text_input('MDVP:RAP')

        with col2:
            PPQ = st.text_input('MDVP:PPQ')

        with col3:
            DDP = st.text_input('Jitter:DDP')

        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')

        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')

        with col3:
            APQ = st.text_input('MDVP:APQ')

        with col4:
            DDA = st.text_input('Shimmer:DDA')

        with col5:
            NHR = st.text_input('NHR')

        with col1:
            HNR = st.text_input('HNR')

        with col2:
            RPDE = st.text_input('RPDE')

        with col3:
            DFA = st.text_input('DFA')

        with col4:
            spread1 = st.text_input('spread1')

        with col5:
            spread2 = st.text_input('spread2')

        with col1:
            D2 = st.text_input('D2')

        with col2:
            PPE = st.text_input('PPE')

        parkinsons_diagnosis = ''

        if st.button("Parkinson's Test Result"):
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

            if any(x == '' for x in user_input):
                st.error("Please enter all the details to predict Parkinson's Disease..")
            else:
                user_input = [float(x) for x in user_input]
                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person is having Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"

                st.success(parkinsons_diagnosis)
    elif disease_option == "Cancer Prediction":
        st.write(
                "### Cancer Prediction (Coming Soon!)\n\n"
                "#### Explore the Future of Healthcare\n"
                "Our upcoming Cancer Prediction model is designed to revolutionize early detection and intervention strategies. By leveraging cutting-edge machine learning algorithms and the latest research in oncology, our model aims to provide accurate predictions for various types of cancer, empowering individuals and healthcare professionals with crucial information for timely treatment and care.\n\n"
                "#### How It Works\n"
                "1. **Comprehensive Data Analysis**: Our model analyzes a wide range of factors, including genetic markers, lifestyle habits, and medical history, to identify patterns and indicators of cancer.\n"
                "2. **Personalized Risk Assessment**: By inputting your relevant details, our model will generate a personalized risk assessment, highlighting your likelihood of developing cancer.\n"
                "3. **Early Detection**: Early detection is key to successful cancer treatment. Our model can help identify potential risks at an early stage, enabling proactive health management.\n\n"
                "#### Benefits\n"
                "- **Early Intervention**: Receive timely alerts and recommendations for preventive measures based on your personalized risk assessment.\n"
                "- **Improved Outcomes**: Empower yourself with knowledge and take proactive steps to reduce your risk of developing cancer.\n"
                "- **Healthcare Advancement**: Contribute to ongoing research and advancements in cancer detection and treatment by participating in our predictive modeling.\n\n"
                "#### Stay Tuned!\n"
                "The Cancer Prediction model is currently in development, and we're working tirelessly to ensure its accuracy and reliability. Stay tuned for updates and be the first to experience this groundbreaking tool in the fight against cancer."
            )
    elif disease_option == "Stroke Prediction":

        st.write(
                "### Stroke Prediction (Coming Soon!)\n\n"
                "#### Empowering Stroke Prevention\n"
                "Our upcoming Stroke Prediction model is designed to identify individuals at risk of stroke, enabling early intervention and lifestyle modifications. By analyzing a range of health indicators and risk factors, our model aims to provide personalized risk assessments and recommendations for stroke prevention.\n\n"
                "#### How It Works\n"
                "1. **Comprehensive Risk Assessment**: Our model considers various factors such as age, gender, lifestyle habits, and medical history to assess your risk of stroke.\n"
                "2. **Personalized Recommendations**: Based on your risk assessment, our model will provide personalized recommendations to help you reduce your risk of stroke.\n"
                "3. **Health Monitoring**: Stay informed about your health status and receive regular updates and alerts regarding your stroke risk.\n\n"
                "#### Benefits\n"
                "- **Early Warning**: Receive early warnings and take proactive measures to prevent stroke.\n"
                "- **Lifestyle Modifications**: Get personalized recommendations for lifestyle changes that can reduce your risk of stroke.\n"
                "- **Peace of Mind**: Stay informed about your health and take control of your well-being.\n\n"
                "#### Stay Tuned!\n"
                "The Stroke Prediction model is currently in development, and we're working hard to ensure its accuracy and effectiveness. Stay tuned for updates and be the first to benefit from this innovative tool for stroke prevention."
            )
    elif disease_option == "Kidney Disease Prediction":
        st.write(
            "### Kidney Disease Prediction (Coming Soon!)\n\n"
            "#### Enhancing Kidney Health\n"
            "Our upcoming Kidney Disease Prediction model aims to revolutionize the way kidney diseases are diagnosed and managed. By analyzing key health indicators and risk factors, our model will provide early detection and personalized recommendations for maintaining kidney health.\n\n"
            "#### How It Works\n"
            "1. **Comprehensive Health Analysis**: Our model considers a range of factors such as blood pressure, blood sugar levels, and urine tests to assess kidney health.\n"
            "2. **Personalized Recommendations**: Based on your health data, our model will provide personalized recommendations to help you maintain kidney health.\n"
            "3. **Regular Monitoring**: Stay informed about your kidney health status and receive regular updates and alerts.\n\n"
            "#### Benefits\n"
            "- **Early Detection**: Detect potential kidney issues early and take proactive steps to prevent kidney disease.\n"
            "- **Personalized Care**: Receive personalized recommendations for diet and lifestyle changes to improve kidney health.\n"
            "- **Improved Quality of Life**: Maintain optimal kidney function and enjoy a better quality of life.\n\n"
            "#### Stay Tuned!\n"
            "The Kidney Disease Prediction model is currently in development, and we're committed to ensuring its accuracy and reliability. Stay tuned for updates and be the first to benefit from this groundbreaking tool for kidney health."
        )
    elif disease_option == "Liver Disease Prediction":
        st.write(
            "### Liver Disease Prediction (Coming Soon!)\n\n"
            "#### Promoting Liver Health\n"
            "Our upcoming Liver Disease Prediction model is designed to revolutionize the early detection and management of liver diseases. By analyzing key biomarkers and lifestyle factors, our model aims to provide accurate predictions and personalized recommendations for liver health.\n\n"
            "#### How It Works\n"
            "1. **Comprehensive Biomarker Analysis**: Our model analyzes a range of biomarkers, including liver enzymes and bilirubin levels, to assess liver health.\n"
            "2. **Personalized Recommendations**: Based on your health data, our model will provide personalized recommendations to help you maintain liver health.\n"
            "3. **Regular Monitoring**: Stay informed about your liver health status and receive regular updates and alerts.\n\n"
            "#### Benefits\n"
            "- **Early Detection**: Detect liver issues early and take proactive steps to prevent liver disease.\n"
            "- **Personalized Care**: Receive tailored recommendations for diet and lifestyle changes to improve liver health.\n"
            "- **Improved Liver Function**: Maintain optimal liver function and reduce the risk of liver-related complications.\n\n"
            "#### Stay Tuned!\n"
            "The Liver Disease Prediction model is currently in development, and we're dedicated to ensuring its accuracy and reliability. Stay tuned for updates and be the first to benefit from this innovative tool for liver health."
        )
    elif disease_option == "Alzheimer's Disease Prediction":
        st.write(
            "### Alzheimer's Disease Prediction (Coming Soon!)\n\n"
            "#### Pioneering Alzheimer's Research\n"
            "Our upcoming Alzheimer's Disease Prediction model is poised to redefine how we approach the diagnosis and management of Alzheimer's disease. By leveraging advanced machine learning algorithms and biomarker analysis, our model aims to provide early and accurate predictions for Alzheimer's disease, enabling proactive interventions and personalized care.\n\n"
            "#### How It Works\n"
            "1. **Advanced Biomarker Analysis**: Our model analyzes a variety of biomarkers, including genetic markers and cognitive assessments, to assess the risk of Alzheimer's disease.\n"
            "2. **Personalized Risk Assessment**: By inputting relevant data, our model generates a personalized risk assessment, empowering individuals and caregivers with actionable insights.\n"
            "3. **Early Detection and Intervention**: Early detection is crucial for Alzheimer's disease. Our model can identify potential risks early, allowing for timely interventions and improved outcomes.\n\n"
            "#### Benefits\n"
            "- **Early Intervention**: Receive timely alerts and recommendations for lifestyle changes and cognitive exercises to reduce the risk of Alzheimer's disease.\n"
            "- **Improved Quality of Life**: By detecting Alzheimer's disease early, individuals can benefit from early treatments and interventions, leading to a better quality of life.\n"
            "- **Research Advancement**: Contribute to ongoing research and advancements in Alzheimer's disease by participating in our predictive modeling.\n\n"
            "#### Stay Tuned!\n"
            "The Alzheimer's Disease Prediction model is currently under development, and we're committed to ensuring its accuracy and effectiveness. Stay tuned for updates and be the first to experience this groundbreaking tool in the fight against Alzheimer's disease."
        )




        