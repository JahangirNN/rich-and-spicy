# build_all_catalogs.py
import json
import os

MANUFACTURER_DEFAULT = {
    "name": "City Gruh Udhyog",
    "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
    "contact": "9898155726"
}

# ==========================================
# 1. BIRYANI PRODUCTS (5 products)
# ==========================================
biryani_catalog = {
    "category": "Biryani",
    "total_products": 5,
    "generated_at": "2026-11-20",
    "brand": "Rich 'n' SP!CY",
    "manufacturer": MANUFACTURER_DEFAULT,
    "products": [
        {
            "id": "biryani-bombay-biryani-40g",
            "name": "Rich 'n' Spicy Bombay Biryani Instant Mix",
            "brand": "Rich 'n' SP!CY",
            "category": "Biryani",
            "product_type": "Instant Mix",
            "tags": ["Biryani", "Rice", "Bombay Biryani", "Chicken", "Mutton", "Instant Mix"],
            "regional_names": {
                "gu": "બોમ્બે બિરયાની"
            },
            "net_weight": {
                "value": 40,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Printed Instant Mix Pouch with Window",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Chicken", "Mutton"]
            },
            "images": {
                "primary": "product images/Biryani/BOMBAY BIRYANI.JPG",
                "filename": "BOMBAY BIRYANI.JPG"
            },
            "recipe": {
                "serves_portion": "500g Chicken/Mutton & 750g Rice",
                "marination_time": "30 minutes",
                "cooking_methods": ["Dum / Slow Cook", "Boil", "Pan Fry"],
                "required_ingredients": [
                    "500g Chicken / Mutton",
                    "750g Basmati Rice",
                    "1 tomato",
                    "4 big onions",
                    "2 tbsp chili, ginger, garlic paste",
                    "½ cup red chili sauce",
                    "½ cup tomato sauce",
                    "2 cups ghee",
                    "Orange red food color",
                    "40g Rich 'n' Spicy Bombay Biryani Instant Mix",
                    "Salt as per taste (for boiling rice)"
                ],
                "instructions": {
                    "en": "Soak Basmati rice in water for 2 hours and half boil it with salt. Wash Chicken/Mutton properly with water. Add chili, ginger, garlic paste, chili sauce, tomato sauce, orange red color to the chicken/mutton and marinate it for 30 minutes. Blend 2 onions and 1 tomato along with Rich'n'Spicy Bombay Biryani instant mix to a fine paste. Add this mixture to the marinated chicken and mix it well. Heat ghee in a pan and add 2 sliced long onions and fry it till light pink in color. Add chicken mixture to it and cook for 10 minutes on a low flame. Spread half boiled rice over the mixture and cook it on a low flame for 30 minutes. Serve hot with onion salad.",
                    "gu": "બાસમતી ચોખાને ૨ કલાક પાણીમાં પલાળી મીઠું નાખી અડધા બાફી લો. ચીકન/મટનને પાણીથી બરાબર ધોઈ લો. તેમાં મરચાં, આદું, લસણની પેસ્ટ, ચીલી સોસ, ટમેટો સોસ અને ઓરેન્જ રેડ કલર ઉમેરી ૩૦ મિનિટ મેરીનેટ કરો. ૨ ડુંગળી અને ૧ ટમેટાને રીચ એન સ્પાઈસી બોમ્બે બિરયાની ઇન્સ્ટન્ટ મિક્સ સાથે બારીક પીસી પેસ્ટ બનાવો. આ પેસ્ટને મેરીનેટ કરેલા મીટમાં ઉમેરી બરાબર મિક્સ કરો. કડાઈમાં ઘી ગરમ કરી ૨ લાંબી સમારેલી ડુંગળી ગુલાબી રંગની થાય ત્યાં સુધી સાંતળો. તેમાં ચીકનનું મિશ્રણ ઉમેરી ૧૦ મિનિટ ધીમી આંચે પકાવો. ઉપર અડધા બાફેલા ચોખા પાથરી ધીમી આંચે ૩૦ મિનિટ દમ આપો. ડુંગળીના સલાડ સાથે ગરમા ગરમ સર્વ કરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "biryani-dum-tikka-biryani-50g",
            "name": "Rich 'n' Spicy Dum Chicken/Mutton Tikka Biryani Instant Mix",
            "brand": "Rich 'n' SP!CY",
            "category": "Biryani",
            "product_type": "Instant Mix",
            "tags": ["Biryani", "Dum Biryani", "Tikka Biryani", "Chicken", "Mutton", "Instant Mix"],
            "regional_names": {
                "gu": "દમ ચિકન/ટીક્કા બિરયાની"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Printed Instant Mix Pouch with Window",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Chicken", "Mutton"]
            },
            "images": {
                "primary": "product images/Biryani/DUM TIKKA BIRYANI.JPG",
                "filename": "DUM TIKKA BIRYANI.JPG"
            },
            "recipe": {
                "serves_portion": "500g Chicken Tikka + 250g Meat & 750g Rice",
                "marination_time": "1 hour",
                "cooking_methods": ["Dum / Slow Cook", "Pan Fry", "Boil"],
                "required_ingredients": [
                    "500g chicken tikka pieces",
                    "250g chicken / mutton pieces",
                    "750g basmati rice",
                    "500g onions",
                    "2 tomatoes",
                    "2-3 tbsp chili, ginger, garlic paste",
                    "2 cups curd",
                    "2 cups ghee",
                    "1 cup oil",
                    "Salt as per taste",
                    "Orange red food color",
                    "Cumin seeds for tempering",
                    "50g Rich 'n' Spicy Dum Tikka Biryani Instant Mix"
                ],
                "instructions": {
                    "en": "Soak Basmati rice in water for 2 hours and half boil it with salt. Wash 500g chicken tikka pieces properly. Add Rich'n'Spicy Dum Chicken Tikka Biryani instant mix (tikka pack), orange red color and curd. Mix well and marinate for 1 hour. Heat oil in a pan, add tikka pieces and cook till tender. Wash 250g meat pieces, add chili ginger garlic paste, tomatoes, salt and keep aside for 30 minutes. In ghee fry chopped potatoes and sliced long onions till golden brown; crush cooled onions. In ghee crackle cumin seeds, add marinated meat and cook till tender. Add crushed onions, potatoes and remaining biryani mix. Layer half-boiled rice and tikka pieces in pot, top with fried jeera tempering, cover and cook on low flame for 30 minutes.",
                    "gu": "બાસમતી ચોખાને ૨ કલાક પલાળી મીઠું નાખી અડધા બાફી લો. ૫૦૦ ગ્રામ ચીકન ટીક્કા ટુકડા ધોઈ રીચ એન સ્પાઈસી દમ ટીક્કા બિરયાની મસાલા, ઓરેન્જ રેડ કલર અને દહીં સાથે મિક્સ કરી ૧ કલાક મેરીનેટ કરો અને તેલમાં ફ્રાય કરી લો. ૨૫૦ ગ્રામ મીટમાં આદું-લસણ-મરચાંની પેસ્ટ, ટમેટાં અને મીઠું ઉમેરી ૩૦ મિનિટ રાખો. ઘીમાં બટાકા અને લાંબી ડુંગળી સોનેરી તળી લો; ઠંડી થયેલી ડુંગળીનો ભૂકો કરો. ઘીમાં જીરું તતડાવી મેરીનેટ કરેલું મીટ પકાવો, તેમાં તળેલી ડુંગળી, બટાકા અને બાકીનો બિરયાની મસાલો ઉમેરો. ચોખા અને તળેલા ટીક્કાના થર ગોઠવી ઉપર જીરાનો વઘાર રેડી ધીમી આંચે ૩૦ મિનિટ દમ આપો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "biryani-hyderabadi-biryani-40g",
            "name": "Rich 'n' Spicy Hyderabadi Biryani Instant Mix",
            "brand": "Rich 'n' SP!CY",
            "category": "Biryani",
            "product_type": "Instant Mix",
            "tags": ["Biryani", "Hyderabadi Biryani", "Rice", "Chicken", "Mutton", "Instant Mix"],
            "regional_names": {
                "gu": "હૈદરાબાદી બિરયાની"
            },
            "net_weight": {
                "value": 40,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Printed Instant Mix Pouch with Window",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Chicken", "Mutton"]
            },
            "images": {
                "primary": "product images/Biryani/HYDERABADI BIRYANI.JPG",
                "filename": "HYDERABADI BIRYANI.JPG"
            },
            "recipe": {
                "serves_portion": "750g Chicken/Mutton & 500g Rice",
                "marination_time": "1 hour",
                "cooking_methods": ["Dum / Slow Cook", "Boil", "Simmer"],
                "required_ingredients": [
                    "750g Chicken / Mutton",
                    "500g Basmati Rice",
                    "2-3 tbsp chili, ginger, garlic paste",
                    "4 onions (sliced long)",
                    "1-1.5 cup curd",
                    "1.5 cup ghee",
                    "Salt for rice",
                    "Fresh mint leaves",
                    "½ tsp green food color",
                    "Cumin seeds for tempering",
                    "40g Rich 'n' Spicy Hyderabadi Biryani Instant Mix"
                ],
                "instructions": {
                    "en": "Soak Biryani rice in water for 2 hours and half boil it with salt. Wash Chicken/Mutton properly with water. Add chili, ginger, garlic paste, curd, green color and marinate it for 1 hour. Heat ghee in a pan and add sliced long onions until light brown in color. Add chicken mixture to it and cook till the chicken is tender. Add Rich'n'Spicy Hyderabadi instant mix along with mint leaves. Cook for 2 minutes. Spread half boiled rice over the Chicken/Mutton mixture. Heat ghee in a small pan, crackle cumin seeds, and sprinkle over the rice. Cook on a low flame for 30 minutes. Serve hot with curd raita or onion salad.",
                    "gu": "બિરયાની ચોખાને ૨ કલાક પલાળી મીઠું નાખી અડધા બાફી લો. ચીકન/મટનને પાણીથી ધોઈ તેમાં આદું-લસણ-મરચાંની પેસ્ટ, દહીં અને લીલો કલર ઉમેરી ૧ કલાક મેરીનેટ કરો. પેનમાં ઘી ગરમ કરી લાંબી સમારેલી ડુંગળી હલકી ગુલાબી તળી લો. તેમાં મેરીનેટ કરેલું મીટ ઉમેરી નરમ થાય ત્યાં સુધી પકાવો. રીચ એન સ્પાઈસી હૈદરાબાદી ઇન્સ્ટન્ટ મિક્સ અને ફુદીનાના પાન ઉમેરી ૨ મિનિટ રાંધો. ઉપર અડધા બાફેલા ચોખા પાથરી દો. નાની કડાઈમાં ઘી ગરમ કરી જીરું તતડાવી ચોખા પર છાંટો. ધીમી આંચે ૩૦ મિનિટ દમ આપો. દહીંના રાયતા કે સલાડ સાથે ગરમા ગરમ સર્વ કરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "biryani-shahi-biryani-40g",
            "name": "Rich 'n' Spicy Shahi Biryani Instant Mix",
            "brand": "Rich 'n' SP!CY",
            "category": "Biryani",
            "product_type": "Instant Mix",
            "tags": ["Biryani", "Shahi Biryani", "Rice", "Chicken", "Mutton", "Instant Mix"],
            "regional_names": {
                "gu": "શાહી બિરયાની મટન-ચિકન"
            },
            "net_weight": {
                "value": 40,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Printed Instant Mix Pouch with Window",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Chicken", "Mutton"]
            },
            "images": {
                "primary": "product images/Biryani/SHAHI BIRYANI.JPG",
                "filename": "SHAHI BIRYANI.JPG"
            },
            "recipe": {
                "serves_portion": "1 kg Chicken/Mutton & 750g Rice",
                "marination_time": "30 minutes",
                "cooking_methods": ["Dum / Slow Cook", "Boil", "Pan Fry"],
                "required_ingredients": [
                    "1 kg Chicken / Mutton",
                    "750g Basmati Rice",
                    "1 cup curd",
                    "4 potatoes",
                    "4-5 tbsp chili, ginger, garlic paste",
                    "1 cup tomato sauce",
                    "2 cups ghee",
                    "Salt for rice",
                    "Lemon yellow food color",
                    "1 tsp cumin seeds",
                    "40g Rich 'n' Spicy Shahi Biryani Instant Mix"
                ],
                "instructions": {
                    "en": "Soak Basmati rice in water for 2 hours and half boil it with salt. Wash Chicken/Mutton properly with water. Add chili, ginger, garlic paste, lemon yellow color and curd; marinate for 30 minutes. Heat oil/ghee in a pan, fry sliced long onions till golden brown and keep aside. In same ghee fry chopped potatoes till golden brown and keep aside. Add 1 tsp cumin seeds and allow it to crackle. Add marinated mixture along with potatoes, tomato sauce and 40g Rich'n'Spicy Shahi Biryani instant mix; cook for a while. Spread half-boiled rice over mixture and cook on a low flame for 30 minutes. Serve hot with salad and buttermilk.",
                    "gu": "બાસમતી ચોખાને ૨ કલાક પલાળી મીઠું નાખી અડધા બાફી લો. ચીકન/મટનને ધોઈ આદું-લસણ-મરચાંની પેસ્ટ, લેમન યલો કલર અને દહીં ઉમેરી ૩૦ મિનિટ મેરીનેટ કરો. ઘીમાં લાંબી ડુંગળી ગોલ્ડન બ્રાઉન તળી અલગ રાખો. એ જ ઘીમાં બટાકાના ટુકડા સોનેરી તળી અલગ રાખો. ઘીમાં ૧ ચમચી જીરું તતડાવી મેરીનેટ કરેલું મીટ, બટાકા, ટમેટો સોસ અને રીચ એન સ્પાઈસી શાહી બિરયાની મસાલો ઉમેરી થોડીવાર પકાવો. ઉપર અડધા બાફેલા ચોખા પાથરી ધીમી આંચે ૩૦ મિનિટ દમ આપો. સલાડ અને છાશ સાથે ગરમા ગરમ સર્વ કરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "biryani-sp-mutton-chicken-biryani-40g",
            "name": "Rich 'n' Spicy Sp. Mutton/Chicken Biryani Instant Mix",
            "brand": "Rich 'n' SP!CY",
            "category": "Biryani",
            "product_type": "Instant Mix",
            "tags": ["Biryani", "Special Biryani", "Rice", "Chicken", "Mutton", "Instant Mix"],
            "regional_names": {
                "gu": "સ્પે. મટન/ચિકન બિરયાની"
            },
            "net_weight": {
                "value": 40,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Printed Instant Mix Pouch with Window",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Chicken", "Mutton"]
            },
            "images": {
                "primary": "product images/Biryani/SP.BIRYANI.JPG",
                "filename": "SP.BIRYANI.JPG"
            },
            "recipe": {
                "serves_portion": "1 kg Chicken/Mutton & 1 kg Rice",
                "marination_time": "1 hour",
                "cooking_methods": ["Dum / Slow Cook", "Boil", "Simmer"],
                "required_ingredients": [
                    "1 kg Chicken / Mutton",
                    "1 kg Basmati rice",
                    "3-4 tbsp chili, ginger, garlic paste",
                    "2-3 tomatoes",
                    "1-1.5 cup curd",
                    "6-8 onions (sliced long)",
                    "250g ghee",
                    "Salt as per taste",
                    "Fresh mint & coriander leaves",
                    "40g Rich 'n' Spicy Sp. Mutton/Chicken Biryani Instant Mix"
                ],
                "instructions": {
                    "en": "Soak Biryani rice in water for 2 hours and half boil it with salt. Wash Chicken/Mutton properly with water. Add chili, ginger, garlic paste, curd, chopped tomatoes and marinate for 1 hour. Heat ghee and fry sliced long onions till golden brown and crispy; remove and keep aside. In the same ghee add marinated mixture to it and cook till chicken/mutton is tender. Add crushed fried onions, salt, Rich'n'Spicy Sp. Mutton/Chicken Biryani instant mix, mint & coriander leaves. Spread half boiled rice over mixture and cook on a low flame for 30 minutes. Serve Biryani hot with salad.",
                    "gu": "બિરયાની ચોખાને ૨ કલાક પલાળી મીઠું નાખી અડધા બાફી લો. ચીકન/મટનને પાણીથી ધોઈ તેમાં આદું-લસણ-મરચાંની પેસ્ટ, દહીં અને સમારેલા ટમેટાં ઉમેરી ૧ કલાક મેરીનેટ કરો. ઘીમાં લાંબી સમારેલી ડુંગળી ક્રિસ્પી ગોલ્ડન તળી બહાર કાઢી લો. એ જ ઘીમાં મેરીનેટ કરેલું મીટ ઉમેરી નરમ થાય ત્યાં સુધી પકાવો. તેમાં તળેલી ડુંગળીનો ભૂકો, મીઠું, રીચ એન સ્પાઈસી સ્પે. બિરયાની ઇન્સ્ટન્ટ મિક્સ, ફુદીનો અને કોથમીર ઉમેરો. ઉપર અડધા બાફેલા ચોખા પાથરી ધીમી આંચે ૩૦ મિનિટ દમ આપો. સલાડ સાથે ગરમા ગરમ પીરસો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        }
    ]
}

with open("biryani_products.json", "w", encoding="utf-8") as f:
    json.dump(biryani_catalog, f, indent=2, ensure_ascii=False)
print("biryani_products.json created successfully!")
