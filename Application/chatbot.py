import streamlit as st

# Title of the chatbot application
st.title("Plant Information Chatbot 🌱")

# Introduction
st.write(
    """
    Welcome to the Plant Information Chatbot! 🤖 
    Ask me about plant care, diseases, or preventive measures for crops like rice and wheat.
    """
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
        }
    },
    "wheat": {
        "rust": {
            "description": "A fungal disease caused by Puccinia species, including leaf rust, stem rust, and stripe rust, affecting photosynthesis and plant health.",
            "pathogen": "Puccinia species.",
            "symptoms": [
                "Orange-red pustules on leaves and stems.",
                "Premature drying and withering of leaves.",
                "Reduction in photosynthetic ability leading to stunted growth."
            ],
            "transmission": [
                "Spores spread through wind over long distances.",
                "Infection occurs under warm, moist conditions."
            ],
            "conditions_favoring_disease": [
                "Mild temperatures with high humidity.",
                "Presence of alternate hosts like barberry for certain rust species.",
                "Prolonged leaf wetness from rain or dew."
            ],
            "preventive_measures": [
                "Plant resistant wheat varieties.",
                "Practice crop rotation to break the disease cycle.",
                "Apply fungicides as a preventive or early control measure.",
                "Remove volunteer wheat plants that may harbor rust pathogens.",
                "Monitor fields regularly to detect early signs of rust."
            ]
        }
    }
}

# Function to Fetch Disease Information
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
            f"**Description:** {description}\n\n"
            f"**Pathogen:** {info['pathogen']}\n\n"
            f"**Symptoms:**\n{symptoms}\n\n"
            f"**Transmission:**\n{transmission}\n\n"
            f"**Conditions Favoring the Disease:**\n{conditions}\n\n"
            f"**Preventive Measures:**\n{measures}"
        )
    else:
        return "I'm sorry, I don't have information on that disease. Try asking about specific diseases in rice or wheat."
    
    # Input for user queries
st.write("### Ask about plant diseases!")
crop = st.text_input("Enter the crop name (e.g., rice, wheat):")
disease = st.text_input("Enter the disease name (e.g., rust, brown spot):")

# Display the response
if crop and disease:
    response = get_disease_info(crop, disease)
    st.markdown(response)
