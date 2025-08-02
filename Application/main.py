import numpy as np 
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import os   
import base64

# Streamlit config
st.set_page_config(
    page_title="SmartAgri Detection",
    page_icon="🌱",
    layout="centered"
)


def set_background(image_file):
    if os.path.exists(image_file):
        with open(image_file, 'rb') as f:
            image_url = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
        st.markdown(
        f"""
        <style>
        .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    else:
        st.error(f"Background image file '{image_file}' not found. Please check the file path.")



disease_info = {
    "Rice_BacterialLeafBlight": {
        "symptoms": "A bacterial disease caused by Xanthomonas oryzae that leads to wilting and yellowing of rice leaves.",
        "preventive_measures": [
            "Use resistant rice varieties.",
            "Avoid excessive nitrogen fertilizers.",
            "Ensure proper water drainage and maintain field hygiene.",
            "Apply copper-based bactericides or antibiotics as needed."
        ]
    },
    "Rice_BrownSpot": {
        "symptoms": "A fungal disease caused by Bipolaris oryzae characterized by small brown spots on leaves and grain.",
        "preventive_measures": [
            "Use disease-free seeds and resistant varieties.",
            "Apply balanced fertilizers, particularly potassium.",
            "Remove infected plant debris from the field.",
            "Use fungicides like carbendazim or mancozeb if required."
        ]
    },
    "Rice_Healthy":{
        "symptoms":"Indicates rice plants without any visible diseases or damage.",
        "preventive_measures":[
            "Maintain optimal growing conditions with adequate irrigation, nutrients, and pest control.",
            "Monitor fields regularly to prevent diseases."
        ]
    },
    "Rice_LeafBlast":{
        "symptoms":"A fungal infection caused by Magnaporthe oryzae leading to oval lesions with gray centers on leaves.",
        "preventive_measures":[
            "Plant resistant varieties and avoid planting in humid conditions.",
            "Practice crop rotation and field sanitation.",
            "Avoid excessive nitrogen application.",
            "Use fungicides such as tricyclazole during early stages."
        ]
    },
    "Rice_LeafScald":{
        "symptoms":"A disease caused by Rhynchosporium oryzae producing streaked or burnt leaf tips.",
        "preventive_measures":[
            "Grow tolerant rice varieties.",
            "Ensure proper water management and avoid waterlogging.",
            "Remove and destroy infected plant debris."
        ]
    },
    "Rice_NarrowBrownSpot":{
        "symptoms":"A fungal disease caused by Cercospora oryzae resulting in narrow brown streaks on leaves.",
        "preventive_measures":[
            "Use disease-free seeds and resistant varieties.",
            "Practice balanced fertilization, especially with potassium.",
            "Remove and destroy crop residues.",
            "Apply appropriate fungicides when symptoms appear."
        ]
    },
    "Wheat_BrownRust":{
        "symptoms":"A fungal disease caused by Puccinia triticina, forming reddish-brown pustules on wheat leaves.",
        "preventive_measures":[
            "Grow resistant wheat varieties.",
            "Avoid excessive irrigation and overcrowding of plants.",
            "Apply fungicides like propiconazole at early infection stages.",
            "Remove alternative hosts of rust from nearby fields."
        ]
    },
    "Wheat_Healthy":{
        "symptoms":"Indicates wheat plants without any visible signs of diseases or stress.",
        "preventive_measures":[
            "Use certified seeds and maintain proper crop management practices.",
            "Regularly inspect fields for early signs of disease or pests.",
            "Practice crop rotation and balanced fertilization."
        ]
    },
    "Wheat_Septoria":{
        "symptoms":"A fungal disease caused by Zymoseptoria tritici, showing chlorotic lesions with dark specks.",
        "preventive_measures":[
            "Plant resistant varieties and avoid sowing in highly humid areas.",
            "Ensure good air circulation by spacing plants properly.",
            "Apply fungicides like tebuconazole or chlorothalonil as needed.",
            "Rotate crops and remove infected debris from fields."
        ]
    },
    "Wheat_YellowSmut":{
        "symptoms":"A fungal disease caused by Ustilago tritici leading to yellowish smut-like structures on spikes.",
        "preventive_measures":[
            "Use smut-free seeds treated with fungicides like carboxin or thiram.",
            "Avoid waterlogging and ensure proper drainage in the field.",
            "Remove infected plants and debris immediately."
        ]
    }
}


def model_prediction(test_image):
    model = tf.keras.models.load_model('leafs/trained_model.keras')
    image=tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr=tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

#sidebar
st.sidebar.title("MENU")
app_mode = st.sidebar.selectbox("Select page",["Home","About","Disease Recognition","Chat With Us"])
path=r"C:\Users\ganas\Downloads\pg1.JPG"
#Main Page
if(app_mode=="Home"):
    st.markdown("<h1 style='text-align:center;color:white;'>SMART AGRI DETECTION </h1>",unsafe_allow_html=True)
    set_background(path)
    st.markdown("<h1 style='text-align:center;color:white;'>Welcome to the SmartAgri Detection! 🌿</h1>",unsafe_allow_html=True)
    st.markdown(
            """
            <div style="color:white;">
                <h4>Overview</h4>
                <p>
                This application leverages advanced AI and Deep Learning technologies to help farmers, gardeners, and agricultural experts identify diseases affecting plant leaves. Simply upload an image of the affected leaf, and our system will provide instant predictions along with actionable information to help protect and nurture your plants.
                </p>
            </div>
            """,unsafe_allow_html=True)
    st.markdown(
            """
            <div style="color:white;">            
                <h4>How It Works</h4>
                <ol>
                    <li>Take a clear photo of the affected leaf and upload it to the app.</li>
                    <li>Let our AI-powered model analyze the image to detect the disease.</li>
                    <li>Receive instant results with detailed information on the disease and how to manage it.</li>
                    <li>Act swiftly to prevent further damage to your crops or plants.</li>
                </ol>
            </div>
            """,unsafe_allow_html=True)
    st.markdown(
            """
            <div style="color:white;">
                <h4>Supported Diseases</h4>
                <p>Our system currently supports:</p>
                <ul>
                    <li><b>Rice Diseases:</b> Bacterial Leaf Blight, Brown Spot, Leaf Blast, and more.</li>
                    <li><b>Wheat Diseases:</b> Brown Rust, Septoria, Yellow Smut.</li>
                </ul>
            </div>
            """,unsafe_allow_html=True)
    st.markdown(
            """
            <div style="color:white;">
                <h4 style='color:white'>About the Technology</h4>
                <p>
                Powered by a state-of-the-art convolutional neural network (CNN), our model is trained on a large dataset of leaf images to ensure high accuracy and reliability. This technology bridges the gap between traditional farming methods and modern AI innovations.
            """,unsafe_allow_html=True)
    

#About Project
elif(app_mode=="About"):
    path=r"C:\Users\ganas\Downloads\about.JPG"
    set_background(path)
    st.markdown("<h1 style='text-align:center;color:#ECEBDE;'>About Us 🌟</h1>",unsafe_allow_html=True)
    st.markdown("""
                #### Our Mission
                To enhance agricultural productivity and sustainability by leveraging Artificial Intelligence for the timely detection and management of leaf diseases, ensuring better yields, reduced losses, and a healthier environment.

                #### Our Vision
                To become a global leader in AI-driven agricultural solutions, ensuring food security and sustainable farming practices for future generations.
                
                #### Why We Built This Platform
                Leaf diseases can significantly impact crop health, yield, and quality. Unfortunately, early disease detection is often challenging and requires expert knowledge.
                We built this platform to:

                - Make disease detection accessible to everyone, regardless of expertise.
                - Reduce the dependency on manual inspections and consultations.
                - Encourage sustainable and eco-friendly farming practices by minimizing overuse of chemicals.
            
                #### Our Technology
                The backbone of this system is a robust machine learning model trained on thousands of leaf images to ensure:

                1. High accuracy in detecting diseases.
                2. Fast and reliable predictions.
                3. Coverage of a two variety of crops and diseases.
                4. The model uses Convolutional Neural Networks (CNNs) to analyze image patterns, identifying even subtle signs of disease. We continue to refine and expand our system with regular updates and new features.


            """)
    
 
#prediction page
elif(app_mode == "Disease Recognition"):
    path=r"C:\Users\ganas\Downloads\pg3.3.JPG"
    set_background(path)
    st.markdown("<h1 style='text-align:center;color:black;'>DISEASE RECOGNITION</h1>",unsafe_allow_html=True)
    test_image= st.file_uploader("choose an image:")
    if(st.button("Show Image")):
        col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns
        with col2:  # Center column
            st.image(test_image, width=300)  # Display the image in the center column

     #predict Button
    if(st.button("Predict")):
        with st.spinner("please wait.."):
            st.markdown("<h2 style='text-align:center;color:black;'>Our Prediction</h1>",unsafe_allow_html=True)
            result_index = model_prediction(test_image)
            #define class
            class_name = class_name=[ 'Rice_BacterialLeafBlight',
                    'Rice_BrownSpot',
                    'Rice_Healthy',
                    'Rice_LeafBlast',
                    'Rice_LeafScald',
                    'Rice_NarrowBrownSpot',
                    'Wheat_BrownRust',
                    'Wheat_Healthy',
                    'Wheat_Septoria',
                    'Wheat_YellowSmut']
            predicted_class = class_name[result_index]
            st.markdown(
                f"<div style='background-color: #d4edda; color: black; padding: 10px; border-radius: 5px;'>"
                f"Model is predicting as <b>{predicted_class}</b>"
                f"</div>",
                unsafe_allow_html=True
            )

            st.markdown(f"<h3 style='text-align:center;color:#1B1833;'> {predicted_class} </h1>",unsafe_allow_html=True)
            # Display detailed information
            if predicted_class in disease_info:
                st.markdown(f"<h4 style='color:#000000;'> Symptoms </h4>",unsafe_allow_html=True)
                st.markdown(f"<p style='color:black;'>{disease_info[predicted_class]['symptoms']}</p>", unsafe_allow_html=True)

                st.markdown(f"<h4 style='color:#000000;'>Preventive Measures</h4>",unsafe_allow_html=True)
                st.markdown(
                "<ul>" +
                "".join(f"<li style='color:black;'>{measure}</li>" for measure in disease_info[predicted_class]["preventive_measures"]) +
                "</ul>",
                unsafe_allow_html=True
            )

            else:
                    st.warning("No additional information available for this prediction.")

                # Show the image again
            col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns
            with col2:  # Center column
                st.image(test_image, width=300)  # Display the image in the center column

    else:
            st.warning("Please upload an image to predict!")
    st.markdown("<h3 style='color:black;'>For more information, navigate to the Chat With Us page.</h3>",unsafe_allow_html=True)



#chatbot page
else:
    path=r"C:\Users\ganas\Downloads\pg4.1.JPG"
    set_background(path)
     #Title of the chatbot application
    st.markdown("<h1 style='color: black;'>AgriBot 🌱</h1>", unsafe_allow_html=True)

    # Introduction
    st.markdown(
        """
        <p style='color: black;'>
        Welcome to the AgriBot! 🤖 <br>
        Ask me about plant care, diseases, or preventive measures for crops like rice and wheat.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Disease information for rice and wheat
    disease_info = {
        "rice": {
            "bacterial leaf blight": {
                "description": "A severe bacterial disease caused by Xanthomonas oryzae pv. oryzae (Xoo), leading to yield losses.",
                "pathogen": "Xanthomonas oryzae pv. oryzae (Xoo).",
                "symptoms": [
                    "Water-soaked lesions: Appear along the leaf edges or tips.",
                    "Yellowing and browning: Infected areas turn yellow and then brown as the disease progresses.",
                    "Wilting: Severe infections cause wilting, especially in young plants.",
                    "Kresek: A systemic infection resulting in the wilting of seedlings or younger leaves, common in the early stages of the crop."
                ],
                "transmission": [
                    "The bacteria spread through rain splashes, irrigation water, and infected seeds.",
                    "Wounds or natural openings, like stomata, are entry points."
                ],
                "conditions_favoring_disease": [
                    "Warm temperatures (25–34°C).",
                    "High humidity.",
                    "Rainy or wet conditions.",
                    "Dense planting, leading to poor air circulation."
                ],
                "preventive_measures": [
                    "Plant resistant varieties: Use rice varieties that are genetically resistant to Xoo.",
                    "Seed selection: Use certified, disease-free seeds.",
                    "Crop rotation: Avoid successive planting of rice to reduce pathogen build-up.",
                    "Field hygiene: Remove and destroy infected plants and crop residues.",
                    "Water management: Prevent water stagnation to reduce bacterial spread."
                ]
            },
            "brown_spot":{
                "description":"Brown Spot is a fungal disease of rice caused by Bipolaris oryzae (formerly Helminthosporium oryzae). It affects seedlings, leaves, and grains, resulting in yield losses, particularly in nutrient-deficient soils or under stress conditions.",
                "pathogen":"Bipolaris oryzae (Helminthosporium oryzae).",
                "symptoms":[
                    "Small, circular to oval brown lesions with gray or whitish centers and dark brown margins.",
                    "Lesions may merge to form large blighted areas, causing leaf drying and death."
                ],
                "transmission":[
                    "Infected seeds are the main source of transmission",
                    "Airborne spores disperse the pathogen over short distances.",
                    "Rain splash can spread the spores to neighboring plants.",
                ],
                "conditions_favoring_disease":[
                    "Warm and humid climates (optimum temperature: 25–30°C).",
                    "Poor soil fertility, especially nitrogen and potassium deficiency.",
                    "Water stress (drought conditions).",
                    "Overcrowded plants with poor air circulation.",
                    "High relative humidity and frequent dew formation on leaves."
                ],
                "preventive_measures":[
                    "Use Resistant Varieties: Plant rice varieties resistant to Bipolaris oryzae.",
                    "Seed Treatment: Treat seeds with fungicides like carbendazim or thiram to eliminate seed-borne pathogens.",
                    "Balanced Fertilization: Ensure proper nitrogen, phosphorus, and potassium application to reduce plant stress.",
                    "Field Hygiene: Remove infected crop residues and weeds from fields to minimize the source of inoculum.",
                    "Water Management: Avoid water stress by ensuring consistent irrigation during critical growth stages.",
                    "Fungicide Application: Apply fungicides like mancozeb, propiconazole, or tricyclazole at the first appearance of symptoms to control the spread."
                ]
            },
            "healthy": {
                "description": "A general term referring to the condition of rice plants being free from diseases, pests, and physiological disorders, ensuring optimal growth and yield.",
                "pathogen": "N/A (No pathogen involved in healthy rice plants).",
                "symptoms": [
                    "Healthy, green, and upright leaves.",
                    "Uniform plant height and vigor.",
                    "No visible signs of lesions, wilting, or discoloration.",
                    "Optimal grain development and absence of empty grains."
                ],
                "transmission": [
                    "N/A (Healthy plants are not infected)."
                ],
                "conditions_favoring_disease": [
                    "Balanced fertilization.",
                    "Adequate water supply and management.",
                    "Use of certified seeds and resistant varieties.",
                    "Regular field monitoring and timely pest and disease management."
                ],
                "preventive_measures": [
                    "Adopt integrated pest and disease management (IPDM).",
                    "Use disease-free seeds and follow recommended planting practices.",
                    "Ensure proper water and nutrient management.",
                    "Remove weeds and crop residues to minimize pest habitats."
                ]
            },
            "leaf_scald": {
                "description": "A fungal disease caused by Microdochium oryzae, affecting leaves and reducing photosynthetic capacity.",
                "pathogen": "Microdochium oryzae.",
                "symptoms": [
                    "Irregular, water-soaked lesions that turn grayish-white with brown borders.",
                    "Lesions coalesce, forming large blighted areas on leaves.",
                    "Severe infections cause premature drying and death of leaves."
                ],
                "transmission": [
                    "Spread through infected seeds.",
                    "Wind and rain splashes carry fungal spores."
                ],
                "conditions_favoring_disease": [
                    "High humidity and frequent rain.",
                    "Warm temperatures (25–30°C).",
                    "Dense planting with poor air circulation."
                ],
                "preventive_measures": [
                    "Use resistant rice varieties.",
                    "Treat seeds with fungicides to prevent seed-borne infections.",
                    "Avoid over-irrigation and improve field drainage.",
                    "Apply foliar fungicides like mancozeb or propiconazole when symptoms appear."
                ]
            },
            "leaf_blast": {
                "description": "A fungal disease caused by Magnaporthe oryzae, leading to significant yield losses by affecting leaves, stems, and panicles.",
                "pathogen": "Magnaporthe oryzae.",
                "symptoms": [
                    "Diamond-shaped lesions with gray centers and brown or reddish margins on leaves.",
                    "Lesions can expand, causing leaf death.",
                    "In severe cases, neck blast affects the panicle, leading to sterility."
                ],
                "transmission": [
                    "Spread through airborne conidia.",
                    "Rain splashes and infected seeds serve as sources of infection."
                ],
                "conditions_favoring_disease": [
                    "High humidity and temperatures between 20–28°C.",
                    "Frequent dew or rainfall.",
                    "Nitrogen over-fertilization."
                ],
                "preventive_measures": [
                    "Plant resistant varieties.",
                    "Avoid excessive nitrogen fertilization.",
                    "Maintain proper field drainage to reduce humidity.",
                    "Apply systemic fungicides like tricyclazole or azoxystrobin."
                ]
            },
            "narrow_brown_spot": {
                "description": "A fungal disease caused by Cercospora janseana, commonly affecting leaves and reducing photosynthetic efficiency.",
                "pathogen": "Cercospora janseana.",
                "symptoms": [
                    "Narrow, elongated brown lesions on leaves, usually parallel to the veins.",
                    "Lesions may turn gray in the center as they age.",
                    "Severe infections cause leaf blight and premature drying."
                ],
                "transmission": [
                    "Spread through infected seeds and crop residues.",
                    "Wind and rain splashes disperse fungal spores."
                ],
                "conditions_favoring_disease": [
                    "Warm and humid weather conditions.",
                    "Prolonged leaf wetness from rain or dew.",
                    "Nutrient-deficient soils."
                ],
                "preventive_measures": [
                    "Plant resistant rice varieties.",
                    "Use certified, disease-free seeds.",
                    "Treat seeds with fungicides to eliminate seed-borne infections.",
                    "Apply foliar fungicides when symptoms appear.",
                    "Ensure balanced fertilization to minimize stress on plants."
                ]
            }
        },
        "wheat": {
            "brown_rust": {
                "description": "A fungal disease caused by Puccinia triticina, affecting wheat leaves and reducing photosynthesis and yield.",
                "pathogen": "Puccinia triticina.",
                "symptoms": [
                    "Small, circular, orange-brown pustules appear on the upper leaf surface.",
                    "As the disease progresses, pustules coalesce, causing leaf tissue damage.",
                    "Severe infections lead to premature leaf drying and reduced grain filling."
                ],
                "transmission": [
                    "Airborne urediniospores spread the disease across fields.",
                    "Infection occurs under warm, moist conditions."
                ],
                "conditions_favoring_disease": [
                    "Mild temperatures (15–22°C).",
                    "High humidity and prolonged leaf wetness.",
                    "Presence of susceptible wheat varieties."
                ],
                "preventive_measures": [
                    "Plant rust-resistant wheat varieties.",
                    "Apply foliar fungicides like propiconazole or tebuconazole when rust symptoms appear.",
                    "Monitor fields regularly for early signs of rust.",
                    "Avoid over-fertilization with nitrogen, which can promote disease development."
                ]
            },
            "healthy": {
                "description": "A condition where wheat plants are free from diseases, pests, and physiological stress, ensuring optimal growth and yield.",
                "pathogen": "N/A (No pathogen involved in healthy wheat plants).",
                "symptoms": [
                    "Green, upright leaves with no visible lesions or discoloration.",
                    "Uniform plant height and vigor.",
                    "Healthy root system with no signs of decay.",
                    "Full grain development with no empty grains."
                ],
                "transmission": [
                    "N/A (Healthy plants are not infected)."
                ],
                "conditions_favoring_disease": [
                    "Balanced fertilization with nitrogen, phosphorus, and potassium.",
                    "Adequate water supply and irrigation management.",
                    "Use of certified, disease-free seeds.",
                    "Regular monitoring to prevent disease or pest outbreaks."
                ],
                "preventive_measures": [
                    "Adopt integrated pest and disease management (IPDM).",
                    "Ensure timely sowing and optimal planting density.",
                    "Remove weeds and crop residues from the field.",
                    "Monitor and manage field moisture to avoid water stress or stagnation."
                ]
            },
            "septoria": {
                "description": "A fungal disease caused by Zymoseptoria tritici, commonly affecting wheat leaves and reducing photosynthetic activity and yield.",
                "pathogen": "Zymoseptoria tritici.",
                "symptoms": [
                    "Small, yellow to brown lesions appear on lower leaves.",
                    "Lesions expand, forming large, irregular blotches with black fruiting bodies (pycnidia) in the center.",
                    "Severe infections result in premature leaf death."
                ],
                "transmission": [
                    "Spread through rain splashes carrying fungal spores.",
                    "Infected crop residues and airborne spores are primary sources of infection."
                ],
                "conditions_favoring_disease": [
                    "Cool, wet weather conditions (15–20°C).",
                    "Prolonged leaf wetness from rain or dew.",
                    "Dense planting with poor air circulation."
                ],
                "preventive_measures": [
                    "Plant wheat varieties with resistance to Septoria.",
                    "Practice crop rotation to reduce inoculum levels.",
                    "Remove and destroy infected crop residues after harvest.",
                    "Apply fungicides like azoxystrobin or epoxiconazole during early infection stages."
                ]
            },
            "yellow_smut": {
                "description": "A fungal disease caused by Ustilago tritici, affecting wheat ears and leading to grain losses.",
                "pathogen": "Ustilago tritici.",
                "symptoms": [
                    "Infected plants produce spiked heads with a yellow or golden appearance.",
                    "Smut spores replace the grains in infected ears.",
                    "Spores are easily dislodged, leaving a barren, skeleton-like spike."
                ],
                "transmission": [
                    "Seed-borne spores infect seedlings during germination.",
                    "Spores spread to healthy plants through wind or rain splashes."
                ],
                "conditions_favoring_disease": [
                    "Cool and humid weather during seedling emergence.",
                    "Use of untreated, infected seeds.",
                    "Prolonged leaf wetness and favorable conditions for spore germination."
                ],
                "preventive_measures": [
                    "Use certified, smut-free seeds.",
                    "Treat seeds with fungicides like carboxin or thiram before sowing.",
                    "Avoid planting wheat in fields with a history of smut infection.",
                    "Monitor and destroy infected plants early to prevent spore dispersal."
                ]
            }
        }
    }

    # Function to retrieve disease information
    def get_disease_info(crop, disease):
        crop = crop.lower()
        disease = disease.lower()
        if crop in disease_info and disease in disease_info[crop]:
            info = disease_info[crop][disease]
            description = info["description"]
            symptoms = "\n".join(f"- {symptom}" for symptom in info["symptoms"])
            transmission = "\n".join(f"- {method}" for method in info["transmission"])
            conditions = "\n".join(f"- {condition}" for condition in info["conditions_favoring_disease"])
            measures = "\n".join(f"- {measure}" for measure in info["preventive_measures"])
            return (
                f"<div style='color: black;'>"
                f"\n\n"
                f"**Description:** {description}\n\n"
                f"**Pathogen:** {info['pathogen']}\n\n"
                f"**Symptoms:**\n{symptoms}\n\n"
                f"**Transmission:**\n{transmission}\n\n"
                f"**Conditions Favoring the Disease:**\n{conditions}\n\n"
                f"**Preventive Measures:**\n{measures}"
                f"</div>"
            )
        else:
            return "I'm sorry, I don't have information on that disease. Try asking about specific diseases in rice or wheat."

    # Input for user queries
    st.markdown("<h3 style='color: black;'>Ask about plant diseases!</h3>", unsafe_allow_html=True)

    # Dropdown for selecting crop
    st.markdown("<p style='color: black;'>Select a crop:</p>", unsafe_allow_html=True)
    crop = st.selectbox("", options=list(disease_info.keys()))

    # Dropdown for selecting disease based on the chosen crop
    st.markdown("<p style='color: black;'>Select a disease:</p>", unsafe_allow_html=True)
    disease = st.selectbox("", options=list(disease_info[crop].keys()))


    # Display the response
    if crop and disease:
        response = get_disease_info(crop, disease)
        st.markdown(response, unsafe_allow_html=True)