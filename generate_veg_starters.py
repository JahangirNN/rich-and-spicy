# generate_veg_starters.py
import json
import os

MANUFACTURER_DEFAULT = {
    "name": "City Gruh Udhyog",
    "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
    "contact": "9898155726"
}

vegstarters_catalog = {
    "category": "Veg Starters",
    "total_products": 7,
    "generated_at": "2026-11-21",
    "brand": "Rich 'n' SP!CY",
    "manufacturer": MANUFACTURER_DEFAULT,
    "products": [
        {
            "id": "vegstarter-chaat-masala-50g",
            "name": "Rich 'n' Spicy Chaat Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Veg Starters",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Veg Starters", "Chaat", "Street Food", "Dry Marinade", "Seasoning"],
            "regional_names": {
                "gu": "ચાટ"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Transparent Pouch with Full-Label Sticker",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Potatoes", "Sprouts", "Fruits", "Paneer"]
            },
            "images": {
                "primary": "product images/veg starters/chaat.JPG",
                "filename": "chaat.JPG"
            },
            "recipe": {
                "serves_portion": "500g Potatoes / Fruit Chaat",
                "marination_time": "Instant",
                "cooking_methods": ["Toss", "Sprinkle"],
                "required_ingredients": [
                    "500g boiled diced potatoes",
                    "2 tbsp fresh mint chutney",
                    "1 tbsp fresh lemon juice",
                    "½ tbsp grated ginger",
                    "1 chopped green chilli",
                    "Salt to taste",
                    "Rich 'n' Spicy Chaat Masala to taste",
                    "Chopped fresh coriander leaves"
                ],
                "instructions": {
                    "en": "Boil 500g potatoes, cut into bite-sized cubes, and lightly fry until crisp. In a mixing bowl, toss with 2 tbsp mint chutney, 1 tbsp lemon juice, grated ginger, chopped green chilli, salt, and Rich 'n' Spicy Chaat Masala to taste. Garnish with fresh coriander. A versatile tangy seasoning also ideal for Fruit Chaat, Aloo Chaat, Sprouted Beans, Finger Chips, Sandwiches, and Tandoori platters.",
                    "gu": "૫૦૦ ગ્રામ બટાકા બાફી ટુકડા કરી આછા તળી લો. તેમાં ૨ ચમચી ફુદીનાની ચટણી, ૧ ચમચી લીંબુનો રસ, આદું, લીલું મરચું, મીઠું અને સ્વાદ મુજબ રીચ એન સ્પાઈસી ચાટ મસાલો નાખી હલાવો. ફ્રુટ ચાટ, આલુ ચાટ, કઠોળ, ફિંગર ચીપ્સ અને સેન્ડવીચ માટે ઉત્તમ."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "vegstarter-dahi-wada-50g",
            "name": "Rich 'n' Spicy Dahi Wada Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Veg Starters",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Veg Starters", "Dahi Vada", "Street Food", "Dry Marinade", "Festive"],
            "regional_names": {
                "gu": "દહીં વડા"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Transparent Pouch with Full-Label Sticker",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Urad Dal", "Sweet Curd"]
            },
            "images": {
                "primary": "product images/veg starters/dahi wada.JPG",
                "filename": "dahi wada.JPG"
            },
            "recipe": {
                "serves_portion": "500g Urad Dal (Yields 20-25 Vadas)",
                "marination_time": "Soak Dal 6 hours",
                "cooking_methods": ["Deep Fry", "Soak in Buttermilk", "Chilled Assemble"],
                "required_ingredients": [
                    "500g urad dal (soaked 6 hours)",
                    "Whisked sweetened curd",
                    "Buttermilk for soaking",
                    "Sweet tamarind-date (imli khajoor) chutney",
                    "Green mint chutney",
                    "50g Rich 'n' Spicy Dahi Wada Masala",
                    "Oil for frying",
                    "Chopped coriander and green chillies"
                ],
                "instructions": {
                    "en": "Soak 500g urad dal for 6 hours, drain, and grind into a fluffy batter adding salt to taste. Shape into small dumplings and deep fry until golden. Soak fried wadas in buttermilk for 30 minutes, then gently squeeze out excess liquid. Arrange wadas on a platter, cover generously with whisked chilled sweet curd, drizzle date-tamarind chutney, and sprinkle Rich 'n' Spicy Dahi Wada Masala with fresh coriander.",
                    "gu": "૫૦૦ ગ્રામ અડદની દાળ ૬ કલાક પલાળી વાટી લો. નાના વડા બનાવી તેલમાં તળો. તળેલા વડાને અડધો કલાક છાસમાં પલાળી હળવેથી નિતારી લો. ઉપર મીઠું ફેંટેલું દહીં, ખજૂર આમલીની ચટણી અને રીચ એન સ્પાઈસી દહીં વડા મસાલો છાંટી કોથમીરથી સજાવી સર્વ કરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "vegstarter-frankie-masala-30g",
            "name": "Rich 'n' Spicy Frankie Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Veg Starters",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Veg Starters", "Frankie", "Rolls", "Street Food", "Dry Marinade"],
            "regional_names": {
                "gu": "ફ્રેન્કી"
            },
            "net_weight": {
                "value": 30,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Transparent Pouch with Full-Label Sticker",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Potatoes", "Paneer", "Noodles"]
            },
            "images": {
                "primary": "product images/veg starters/frankie.JPG",
                "filename": "frankie.JPG"
            },
            "recipe": {
                "serves_portion": "6-8 Frankies",
                "marination_time": "None",
                "cooking_methods": ["Tawa Toast", "Roll"],
                "required_ingredients": [
                    "Maida or wheat rotis/tortillas",
                    "Spiced mashed potato cutlets or paneer cubes",
                    "Finely sliced onions soaked in vinegar",
                    "Shredded cabbage and capsicum",
                    "Green chili vinegar sauce",
                    "30g Rich 'n' Spicy Frankie Masala",
                    "Butter for toasting"
                ],
                "instructions": {
                    "en": "Warm roti on tawa with a dab of butter. Place hot spiced potato roll or sauteed paneer in the center. Add shredded cabbage, sliced vinegar onions, and green chili sauce. Generously dust with Rich 'n' Spicy Frankie Masala. Roll up tightly in parchment paper and serve piping hot.",
                    "gu": "તવા પર માખણ લગાવી રોટલી ગરમ કરો. વચ્ચે મસાલેદાર આલુ રોલ અથવા પનીર મૂકો. છીણેલી કોબી, વિનેગાર વાળી ડુંગળી અને ગ્રીન ચીલી સોસ નાખો. ઉપરથી રીચ એન સ્પાઈસી ફ્રેન્કી મસાલો છાંટી રોલ વાળી ગરમા ગરમ પીરસો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "vegstarter-idli-vada-dosa-sambhar-50g",
            "name": "Rich 'n' Spicy Idli / Vada / Dosa Sambhar Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Veg Starters",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Veg Starters", "Sambhar", "South Indian", "Idli", "Dosa", "Dry Marinade"],
            "regional_names": {
                "gu": "સંભાર ઈડલી/વડા/ઢોસા સંભાર"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Transparent Pouch with Full-Label Sticker",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Toor Dal", "Vegetables"]
            },
            "images": {
                "primary": "product images/veg starters/idli sambhar.JPG",
                "filename": "idli sambhar.JPG"
            },
            "recipe": {
                "serves_portion": "100g Toor Dal (Serves 4-5)",
                "marination_time": "Soak Dal 30 mins",
                "cooking_methods": ["Boil", "Tadka / Tempering"],
                "required_ingredients": [
                    "100g toor dal (soaked 30 mins)",
                    "Drumsticks (sargavo), chopped onions, brinjal, bottle gourd (doodhi)",
                    "2 tbsp tamarind pulp",
                    "2-3 tbsp Rich 'n' Spicy Sambhar Masala",
                    "Salt to taste",
                    "Tempering: 3 tsp oil, 2 dry red chilies, ¼ tsp fenugreek seeds, ½ tsp mustard seeds, curry leaves, pinch of hing"
                ],
                "instructions": {
                    "en": "Soak 100g toor dal for 30 minutes. In a pot, boil dal along with drumsticks, onions, brinjal, bottle gourd, 2 tbsp tamarind pulp, salt, and 2-3 tbsp Rich 'n' Spicy Sambhar Masala. In a separate pan, prepare tempering: heat 3 tsp oil, crackle mustard seeds, fenugreek seeds, dried red chillies, curry leaves, and hing. Pour tempering over the boiling dal and simmer for 2 minutes. Serve steaming hot with Idli, Vada, or Dosa.",
                    "gu": "૧૦૦ ગ્રામ તુવેર દાળ ૩૦ મિનિટ પલાળી સરગવાની સીંગ, કાંદા, રીંગણ, દૂધી, ૨ ચમચી આમલીનો રસો, મીઠું અને ૨-૩ ચમચી સંભાર મસાલો નાખી ઉકાળો. તેલમાં રાય, મેથી, સૂકાં લાલ મરચાં, કઢીપત્તા અને હીંગનો વઘાર કરી દાળમાં ઉમેરી ૨ મિનિટ ઉકાળો. ઈડલી, વડા કે ઢોસા સાથે ગરમ પીરસો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "vegstarter-maggi-noodles-masala-50g",
            "name": "Rich 'n' Spicy Maggi Noodles Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Veg Starters",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Veg Starters", "Noodles", "Maggi Masala", "Kids Favorite", "Dry Marinade"],
            "regional_names": {
                "gu": "મેગી નુડલ્સ"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Transparent Pouch with Full-Label Sticker",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Noodles", "Vegetables"]
            },
            "images": {
                "primary": "product images/veg starters/maggi masala.JPG",
                "filename": "maggi masala.JPG"
            },
            "recipe": {
                "serves_portion": "2-4 Noodle Cakes",
                "marination_time": "None",
                "cooking_methods": ["Boil", "Stir Fry & Simmer"],
                "required_ingredients": [
                    "2 packets noodles",
                    "1 large onion sliced",
                    "1 large tomato chopped",
                    "Assorted vegetables (carrots, cabbage, capsicum, green peas)",
                    "2-3 tbsp oil",
                    "½ glass water",
                    "1-2 tbsp soya sauce",
                    "Rich 'n' Spicy Maggi Noodles Masala"
                ],
                "instructions": {
                    "en": "Boil noodles in water with ½ tsp oil and salt until tender; drain well. In a non-stick pan, heat 2-3 tbsp oil and fry sliced onions for 2-3 minutes. Add chopped tomatoes and fry for 1-2 minutes. Add assorted veggies (carrots, cabbage, capsicum, peas) and fry, then add ½ glass water and cook until tender. Add boiled noodles, desired quantity of Rich 'n' Spicy Maggi Noodles Masala, and 1-2 tbsp soya sauce. Toss gently on low heat and serve steaming hot.",
                    "gu": "નુડલ્સને તેલ અને મીઠું નાખી બાફી ચારણીમાં નિતારી લો. પેનમાં તેલ ગરમ કરી કાંદા, ટામેટાં અને મનપસંદ શાકભાજી (ગાજર, કોબી, કેપ્સીકમ, વટાણા) સાંતળો. અડધો ગ્લાસ પાણી નાખી શાક ચડવા દો. બાફેલા નુડલ્સ, રીચ એન સ્પાઈસી મેગી મસાલો અને સોયા સોસ ઉમેરી ધીમી આંચે ટોસ કરો. ગરમા ગરમ બાઉલમાં સર્વ કરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "vegstarter-pani-puri-masala-50g",
            "name": "Rich 'n' Spicy Pani Puri Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Veg Starters",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Veg Starters", "Pani Puri", "Gol Gappa", "Street Food", "Dry Marinade"],
            "regional_names": {
                "gu": "પાણી પુરી"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Transparent Pouch with Full-Label Sticker",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Chickpeas", "Potatoes", "Moong"]
            },
            "images": {
                "primary": "product images/veg starters/pani puri.JPG",
                "filename": "pani puri.JPG"
            },
            "recipe": {
                "serves_portion": "50-100 Puris (1-2 Litres Flavored Water)",
                "marination_time": "None",
                "cooking_methods": ["Blend", "Chilled Assemble"],
                "required_ingredients": [
                    "50g fresh coriander leaves",
                    "50g fresh mint leaves",
                    "8-10 green chillies",
                    "1 small piece ginger",
                    "Tamarind water & jaggery paste",
                    "Rich 'n' Spicy Pani Puri Masala",
                    "Chilled water & ice cubes",
                    "Crispy puris, boiled black chana, mashed potatoes"
                ],
                "instructions": {
                    "en": "Blend 50g fresh coriander, 50g mint leaves, green chillies, and ginger into a smooth green paste. Mix paste into tamarind water, add salt and Rich 'n' Spicy Pani Puri Masala to taste, and dilute with 2 glasses of chilled water. For sweet chutney water, soak equal quantities of dates and jaggery in warm water and blend. Crack open crispy puris, fill with boiled chickpeas and potatoes, dip into spicy and sweet waters, and enjoy fresh.",
                    "gu": "કોથમીર, ફુદીનો, લીલાં મરચાં અને આદુને મિક્સરમાં બારીક પીસી લો. આ પેસ્ટને આમલીના પાણીમાં ઉમેરી મીઠું, રીચ એન સ્પાઈસી પાણીપુરી મસાલો અને ૨ ગ્લાસ ઠંડુ પાણી ઉમેરી તીખું પાણી તૈયાર કરો. મીઠા પાણી માટે ખજૂર-ગોળ વાટીને બનાવો. પૂરીમાં બાફેલા ચણા-બટાકા ભરી પાણીપુરીની મજા માણો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "vegstarter-sandwich-masala-50g",
            "name": "Rich 'n' Spicy Sandwich Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Veg Starters",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Veg Starters", "Sandwich", "Bombay Sandwich", "Street Food", "Dry Marinade"],
            "regional_names": {
                "gu": "સેન્ડવીચ"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Transparent Pouch with Full-Label Sticker",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Cheese", "Potatoes", "Vegetables"]
            },
            "images": {
                "primary": "product images/veg starters/sandwich.JPG",
                "filename": "sandwich.JPG"
            },
            "recipe": {
                "serves_portion": "8-10 Sandwiches",
                "marination_time": "None",
                "cooking_methods": ["Assemble", "Toast / Grill (Optional)"],
                "required_ingredients": [
                    "White or brown bread slices & salted butter",
                    "Green chutney: 100g coriander, 50g mint, 25-30 green chillies, 50g roasted dalia, 1-2 tsp sugar, 1 lemon juice",
                    "Sliced boiled potatoes, cucumber, tomatoes, onions, boiled beetroot",
                    "Rich 'n' Spicy Sandwich Masala",
                    "Grated processed cheese (for cheese sandwich)"
                ],
                "instructions": {
                    "en": "Prepare green chutney by blending coriander, mint, green chillies, dalia, sugar, salt, and lemon juice. Spread butter and green chutney evenly over bread slices. Layer with sliced boiled potatoes, crunchy cucumber, tomatoes, onions, and boiled beetroot. Dust generously with Rich 'n' Spicy Sandwich Masala. For cheese sandwiches, top with a lavish mound of grated cheese. Serve cold or toasted crisp.",
                    "gu": "કોથમીર, ફુદીનો, મરચાં, દાળિયા, ખાંડ અને લીંબુથી લીલી ચટણી બનાવો. બ્રેડ પર માખણ અને ચટણી લગાવી બાફેલા બટાકા, કાકડી, ટામેટાં, કાંદા અને બીટના સ્લાઈસ ગોઠવો. ઉપર સ્વાદ મુજબ રીચ એન સ્પાઈસી સેન્ડવીચ મસાલો છાંટો. ચીઝ છીણીને સેન્ડવીચ ગ્રીલ કે ટોસ્ટ કરી ગરમ પીરસો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        }
    ]
}

with open("veg_starters_products.json", "w", encoding="utf-8") as f:
    json.dump(vegstarters_catalog, f, indent=2, ensure_ascii=False)

print(f"Generated veg_starters_products.json with {len(vegstarters_catalog['products'])} products.")
