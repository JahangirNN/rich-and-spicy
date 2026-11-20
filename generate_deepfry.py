# generate_deepfry.py
import json

raw_json = """{
  "category": "Deep Fry",
  "total_products": 8,
  "generated_at": "2026-11-20",
  "brand": "Rich 'n' SP!CY",
  "manufacturer": {
    "name": "City Gruh Udhyog",
    "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
    "contact": "9898155726"
  },
  "products": [
    {
      "id": "deepfry-chicken-65-50g",
      "name": "Rich 'n' Spicy Chicken 65 Instant Mix",
      "brand": "Rich 'n' SP!CY",
      "category": "Deep Fry",
      "product_type": "Instant Mix",
      "tags": [
        "Deep Fry",
        "Chicken 65",
        "Chicken",
        "Starter",
        "Instant Mix"
      ],
      "regional_names": {
        "gu": "ચિકન 65"
      },
      "net_weight": {
        "value": 50,
        "unit": "g"
      },
      "pricing": {
        "mrp": null,
        "currency": "INR"
      },
      "packaging_type": "Printed Instant Mix Pouch with Window",
      "dietary": {
        "is_vegetarian_mix": true,
        "suggested_protein": [
          "Chicken"
        ]
      },
      "images": {
        "primary": "product images/deep fry/65.JPG",
        "filename": "65.JPG"
      },
      "recipe": {
        "serves_portion": "500g Chicken Tikka Pieces",
        "marination_time": "3 hours",
        "cooking_methods": [
          "Deep Fry"
        ],
        "required_ingredients": [
          "500g Chicken Tikka Pieces",
          "1 raw egg",
          "Oil for frying",
          "Curry leaves and slit green chilies (optional)",
          "Orange red food color",
          "Rich'n'Spicy Schezwan sauce (for serving)",
          "50g Rich'n'Spicy Chicken 65 Instant Mix"
        ],
        "instructions": {
          "en": "Wash 500g Chicken tikka pieces with water thoroughly and drain out excess water. Add Rich'n'Spicy Chicken 65 Instant mix, orange red color to the chicken tikka pieces. Mix well and allow it to marinate for 3 hours. Before frying break open the eggshell of 1 raw egg and add it to the marinated chicken. Mix well so that it blends properly. Heat oil in a pan and deep fry the chicken pieces until golden brown. Then add pinch of curry leaves and chilies to it and fry. Drain them on a kitchen tissue. Serve hot with Rich'n'Spicy Schezwan sauce.",
          "gu": "૫૦૦ ગ્રામ ચીકન ટીક્કાના ટુકડાને પાણીથી સારી રીતે ધોઈ વધારાનું પાણી નિતારી લો. તેમાં રીચ એન સ્પાઈસી ચીકન ૬૫ ઇન્સ્ટન્ટ મિક્સ અને ઓરેન્જ રેડ કલર ઉમેરી બરાબર મિક્સ કરો અને ૩ કલાક મેરીનેટ થવા દો. તળતા પહેલા ૧ કાચું ઈંડું ઉમેરી સારી રીતે એકરસ કરો. કડાઈમાં તેલ ગરમ કરી ચીકનના ટુકડા સુવર્ણ રંગના થાય ત્યાં સુધી ડીપ ફ્રાય કરો. તેમાં લીમડો અને ચીરેલાં લીલાં મરચાં ઉમેરી તળી લો. કિચન ટીશ્યુ પર નિતારી રીચ એન સ્પાઈસી શેઝવાન સોસ સાથે ગરમા ગરમ સર્વ કરો."
        }
      },
      "manufacturer": {
        "name": "City Gruh Udhyog",
        "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
        "contact": "9898155726"
      }
    },
    {
      "id": "deepfry-chicken-chilli-paneer-chilli-50g",
      "name": "Rich 'n' Spicy Chicken Chilly / Paneer Chilly Mix",
      "brand": "Rich 'n' SP!CY",
      "category": "Deep Fry",
      "product_type": "Instant Mix",
      "tags": [
        "Deep Fry",
        "Indo-Chinese",
        "Chicken Chilli",
        "Paneer Chilli",
        "Starter",
        "Instant Mix"
      ],
      "regional_names": {
        "gu": "ચિકન ચીલી/પનીર ચીલી મિક્સ"
      },
      "net_weight": {
        "value": 50,
        "unit": "g"
      },
      "pricing": {
        "mrp": null,
        "currency": "INR"
      },
      "packaging_type": "Specialty Shield-Cutout Packaging with Window",
      "dietary": {
        "is_vegetarian_mix": true,
        "suggested_protein": [
          "Chicken",
          "Paneer"
        ]
      },
      "images": {
        "primary": "product images/deep fry/chicken chilli paneer chilli.JPG",
        "filename": "chicken chilli paneer chilli.JPG"
      },
      "recipe": {
        "serves_portion": "500g Chicken Tikka Pieces / Paneer",
        "marination_time": "2-3 hours",
        "cooking_methods": [
          "Pan Fry",
          "Stir Fry"
        ],
        "required_ingredients": [
          "500g Chicken Tikka Pieces / Paneer",
          "2 tbsp soya sauce",
          "2 tbsp chili sauce",
          "10 green chilies (slit)",
          "Water (splash)",
          "Oil for frying",
          "50g Rich'n'Spicy Chicken Chilli / Paneer Chilli Instant Mix"
        ],
        "instructions": {
          "en": "Wash 500g Chicken tikka pieces with water thoroughly and drain out excess water. Marinate the tikka pieces with chili sauce, soya sauce, and 50g Rich'n'Spicy Chicken chilli / paneer chilli instant mix for 2-3 hours. Heat oil in a pan and fry slit green chilies for 2-3 minutes. Add the marinated chicken mixture to it and fry. Add splash of water and allow the chicken to cook on a low flame till the water dries up. Keep stirring the mixture. Serve Hot!",
          "gu": "૫૦૦ ગ્રામ ચીકન ટીક્કા (અથવા પનીર) ને ધોઈ પાણી નિતારી લો. તેમાં ચીલી સોસ, સોયા સોસ અને ૫૦ ગ્રામ રીચ એન સ્પાઈસી ચીકન ચીલી / પનીર ચીલી ઇન્સ્ટન્ટ મિક્સ ઉમેરી ૨-૩ કલાક મેરીનેટ કરો. કડાઈમાં તેલ ગરમ કરી ચીરેલાં લીલાં મરચાં ૨-૩ મિનિટ સાંતળો. મેરીનેટ કરેલું ચીકન ઉમેરી સાંતળો. થોડું પાણી છાંટી ધીમી આંચે પાણી સુકાઈ જાય ત્યાં સુધી પકાવો. હલાવતા રહી ગરમા ગરમ સર્વ કરો."
        }
      },
      "manufacturer": {
        "name": "City Gruh Udhyog",
        "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
        "contact": "9898155726"
      }
    },
    {
      "id": "deepfry-chicken-dana-100g",
      "name": "Rich 'n' Spicy Chicken Dana Instant Mix",
      "brand": "Rich 'n' SP!CY",
      "category": "Deep Fry",
      "product_type": "Instant Mix",
      "tags": [
        "Deep Fry",
        "Chicken Dana",
        "Chicken",
        "Bite Size",
        "Starter",
        "Instant Mix"
      ],
      "regional_names": {
        "gu": "ચીકન દાના"
      },
      "net_weight": {
        "value": 100,
        "unit": "g"
      },
      "pricing": {
        "mrp": null,
        "currency": "INR"
      },
      "packaging_type": "Printed Instant Mix Pouch with Window",
      "dietary": {
        "is_vegetarian_mix": true,
        "suggested_protein": [
          "Chicken"
        ]
      },
      "images": {
        "primary": "product images/deep fry/chicken dana.JPG",
        "filename": "chicken dana.JPG"
      },
      "recipe": {
        "serves_portion": "500g Chicken Tikka Pieces",
        "marination_time": "2 hours",
        "cooking_methods": [
          "Deep Fry"
        ],
        "required_ingredients": [
          "500g Chicken Tikka pieces",
          "1 large potato (cut into chips)",
          "1 cup curd",
          "1-2 tbsp chili, ginger, garlic paste",
          "100g Rich'n'Spicy Chicken Dana Instant Mix",
          "Oil for frying",
          "Curry leaves & slit green chilies",
          "Rich'n'Spicy Schezwan sauce (for serving)"
        ],
        "instructions": {
          "en": "Wash 500g Chicken tikka pieces and potato chips with water thoroughly and drain out excess water. Add chili, ginger, garlic paste, curd, and Rich'n'Spicy chicken dana instant mix to the chicken. Mix well and marinate it for 2 hours. Heat oil and deep fry the marinated chicken tikka pieces and potato chips along with curry leaves and slit green chilies until crispy and golden. Serve hot with Rich'n'Spicy Schezwan sauce.",
          "gu": "૫૦૦ ગ્રામ ચીકન ટીક્કા અને બટાકાની ચિપ્સ ધોઈ પાણી નિતારી લો. તેમાં આદું-લસણ-મરચાંની પેસ્ટ, દહીં અને ૧૦૦ ગ્રામ રીચ એન સ્પાઈસી ચીકન દાના ઇન્સ્ટન્ટ મિક્સ ઉમેરી ૨ કલાક મેરીનેટ કરો. તેલ ગરમ કરી મેરીનેટ કરેલા ચીકન અને બટાકાની ચિપ્સને મીઠા લીમડા અને લીલાં મરચાં સાથે ક્રિસ્પી થાય ત્યાં સુધી ડીપ ફ્રાય કરો. રીચ એન સ્પાઈસી શેઝવાન સોસ સાથે ગરમા ગરમ સર્વ કરો."
        }
      },
      "manufacturer": {
        "name": "City Gruh Udhyog",
        "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
        "contact": "9898155726"
      }
    },
    {
      "id": "deepfry-chicken-lollipop-50g",
      "name": "Rich 'n' Spicy Chicken Lollipop Instant Mix",
      "brand": "Rich 'n' SP!CY",
      "category": "Deep Fry",
      "product_type": "Instant Mix",
      "tags": [
        "Deep Fry",
        "Chicken Lollipop",
        "Chicken Wings",
        "Starter",
        "Appetizer",
        "Instant Mix"
      ],
      "regional_names": {
        "gu": "ચિકન લોલીપોપ"
      },
      "net_weight": {
        "value": 50,
        "unit": "g"
      },
      "pricing": {
        "mrp": null,
        "currency": "INR"
      },
      "packaging_type": "Printed Instant Mix Pouch with Window",
      "dietary": {
        "is_vegetarian_mix": true,
        "suggested_protein": [
          "Chicken"
        ]
      },
      "images": {
        "primary": "product images/deep fry/chicken lollipop.JPG",
        "filename": "chicken lollipop.JPG"
      },
      "recipe": {
        "serves_portion": "500g Chicken Lollipop",
        "marination_time": "30 minutes",
        "cooking_methods": [
          "Deep Fry"
        ],
        "required_ingredients": [
          "500g Chicken Lollipop",
          "1 raw egg",
          "50g Rich'n'Spicy Chicken Lollipop Instant Mix",
          "Orange red food color",
          "Oil for frying",
          "Rich'n'Spicy Schezwan sauce"
        ],
        "instructions": {
          "en": "Wash 500g Chicken lollipop with water thoroughly and drain out excess water. Marinate Chicken lollipop with 50g Rich'n'Spicy Chicken lollipop Instant mix, orange red color and 1 raw egg for 30 minutes. Heat oil in a pan and deep fry the chicken lollipops until golden brown. Serve hot with Rich'n'Spicy Schezwan sauce.",
          "gu": "૫૦૦ ગ્રામ ચીકન લોલીપોપને પાણીથી ધોઈ પાણી નિતારી લો. તેમાં ૫૦ ગ્રામ રીચ એન સ્પાઈસી ચીકન લોલીપોપ ઇન્સ્ટન્ટ મિક્સ, ઓરેન્જ રેડ કલર અને ૧ કાચું ઈંડું ઉમેરી ૩૦ મિનિટ મેરીનેટ કરો. કડાઈમાં તેલ ગરમ કરી લોલીપોપ સુવર્ણ રંગની ક્રિસ્પી થાય ત્યાં સુધી ડીપ ફ્રાય કરો. વધારાનું તેલ નિતારી રીચ એન સ્પાઈસી શેઝવાન સોસ સાથે ગરમા ગરમ સર્વ કરો."
        }
      },
      "manufacturer": {
        "name": "City Gruh Udhyog",
        "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
        "contact": "9898155726"
      }
    },
    {
      "id": "deepfry-chicken-popcorn-40g",
      "name": "Rich 'n' Spicy Chicken Popcorn Instant Mix",
      "brand": "Rich 'n' SP!CY",
      "category": "Deep Fry",
      "product_type": "Instant Mix",
      "tags": [
        "Deep Fry",
        "Chicken Popcorn",
        "Boneless Chicken",
        "Snack",
        "Crispy",
        "Instant Mix"
      ],
      "regional_names": {
        "gu": "ચીકન પોપકોર્ન"
      },
      "net_weight": {
        "value": 40,
        "unit": "g"
      },
      "pricing": {
        "mrp": null,
        "currency": "INR"
      },
      "packaging_type": "Printed Instant Mix Pouch with Window",
      "dietary": {
        "is_vegetarian_mix": true,
        "suggested_protein": [
          "Chicken"
        ]
      },
      "images": {
        "primary": "product images/deep fry/chicken popcorn.JPG",
        "filename": "chicken popcorn.JPG"
      },
      "recipe": {
        "serves_portion": "500g Boneless Chicken Chunks",
        "marination_time": "2 hours",
        "cooking_methods": [
          "Deep Fry"
        ],
        "required_ingredients": [
          "500g Boneless Chicken Chunks",
          "Bread crumbs",
          "2 eggs",
          "Oil for frying",
          "40g Rich'n'Spicy Chicken Popcorn Instant Mix"
        ],
        "instructions": {
          "en": "Wash small chunks of chicken with water thoroughly and pat dry. Marinate chicken chunks with Rich'n'Spicy chicken popcorn instant mix for 2 hours. Whip 2 eggs and dip the chicken pieces into it and coat the chicken with breadcrumbs. Heat oil and deep fry the chicken until golden brown and crunchy.",
          "gu": "૫૦૦ ગ્રામ બોનલેસ ચીકનના નાના ટુકડા ધોઈ કોરા કરી લો. તેમાં ૪૦ ગ્રામ રીચ એન સ્પાઈસી ચીકન પોપકોર્ન ઇન્સ્ટન્ટ મિક્સ ઉમેરી ૨ કલાક મેરીનેટ કરો. બાઉલમાં ૨ ઈંડા ફેંટી લો; ચીકનના ટુકડાને ઈંડામાં બોળી બ્રેડક્રમ્બ્સમાં રગદોળી કોટ કરો. કડાઈમાં તેલ ગરમ કરી ગોલ્ડન બ્રાઉન અને ક્રિસ્પી થાય ત્યાં સુધી ડીપ ફ્રાય કરો. સોસ સાથે ગરમા ગરમ પીરસો."
        }
      },
      "manufacturer": {
        "name": "City Gruh Udhyog",
        "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
        "contact": "9898155726"
      }
    },
    {
      "id": "deepfry-crispy-chicken-50g",
      "name": "Rich 'n' Spicy Crispy Chicken Instant Mix",
      "brand": "Rich 'n' SP!CY",
      "category": "Deep Fry",
      "product_type": "Instant Mix",
      "tags": [
        "Deep Fry",
        "Crispy Chicken",
        "Chicken Fingers",
        "Starter",
        "Chinese",
        "Instant Mix"
      ],
      "regional_names": {
        "gu": "ક્રીસ્પી ચિકન"
      },
      "net_weight": {
        "value": 50,
        "unit": "g"
      },
      "pricing": {
        "mrp": null,
        "currency": "INR"
      },
      "packaging_type": "Printed Instant Mix Pouch with Window",
      "dietary": {
        "is_vegetarian_mix": true,
        "suggested_protein": [
          "Chicken"
        ]
      },
      "images": {
        "primary": "product images/deep fry/crispy chicken.JPG",
        "filename": "crispy chicken.JPG"
      },
      "recipe": {
        "serves_portion": "500g Chicken Fingers",
        "marination_time": "2 hours",
        "cooking_methods": [
          "Deep Fry",
          "Stir Fry"
        ],
        "required_ingredients": [
          "500g Chicken fingers",
          "2 tbsp soya sauce",
          "2 tbsp chili sauce",
          "2 tbsp tomato sauce",
          "Bread crumbs",
          "1 raw egg",
          "2 Bell peppers (capsicum)",
          "1 onion",
          "Oil for frying",
          "50g Rich'n'Spicy Crispy Chicken Masala"
        ],
        "instructions": {
          "en": "Wash 500g Chicken fingers properly and drain excess water. Add soya sauce, chili sauce, tomato sauce, Rich'n'Spicy crispy chicken instant mix, 1 raw egg and allow it to marinate for 2 hours. Coat the chicken fingers with bread crumbs. Heat oil and deep fry the chicken till golden brown or crunchy. In a separate pan heat 2 tbsp oil. Add finely chopped onions, bell peppers and fry for 2 minutes. Add fried chicken fingers to it and toss the chicken with all the vegetables. Serve Hot!",
          "gu": "૫૦૦ ગ્રામ ચીકન ફિંગર્સ ધોઈ પાણી નિતારી લો. તેમાં સોયા સોસ, ચીલી સોસ, ટમેટો સોસ, ૫૦ ગ્રામ રીચ એન સ્પાઈસી ક્રીસ્પી ચિકન મસાલો અને ૧ કાચું ઈંડું ઉમેરી ૨ કલાક મેરીનેટ કરો. ચીકન ફિંગર્સ પર બ્રેડક્રમ્બ્સ લગાવી લો. તેલ ગરમ કરી ક્રિસ્પી ગોલ્ડન થાય ત્યાં સુધી ડીપ ફ્રાય કરો. બીજી પેનમાં ૨ ચમચી તેલ ગરમ કરી સમારેલી ડુંગળી અને કેપ્સિકમ ૨ મિનિટ સાંતળો, તેમાં તળેલા ચીકન ફિંગર્સ ઉમેરી બરાબર ટોસ કરો. ગરમા ગરમ સર્વ કરો."
        }
      },
      "manufacturer": {
        "name": "City Gruh Udhyog",
        "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
        "contact": "9898155726"
      }
    },
    {
      "id": "deepfry-mutton-chicken-fry-chaap-50g",
      "name": "Rich 'n' Spicy Mutton / Chicken Fry / Chaap Masala",
      "brand": "Rich 'n' SP!CY",
      "category": "Deep Fry",
      "product_type": "Dry Marinade / Spice Mix",
      "tags": [
        "Deep Fry",
        "Mutton Fry",
        "Chicken Fry",
        "Chaap",
        "Pan Fry"
      ],
      "regional_names": {
        "gu": "મટન ચીકન ફ્રાય / ચાંપ"
      },
      "net_weight": {
        "value": 50,
        "unit": "g"
      },
      "pricing": {
        "mrp": null,
        "currency": "INR"
      },
      "packaging_type": "Transparent Pouch with Full-Label Sticker",
      "dietary": {
        "is_vegetarian_mix": true,
        "suggested_protein": [
          "Mutton",
          "Chicken"
        ]
      },
      "images": {
        "primary": "product images/deep fry/mutton chicken fry.JPG",
        "filename": "mutton chicken fry.JPG"
      },
      "recipe": {
        "serves_portion": "500g Leg Piece / Mutton Ribs (Chaap)",
        "marination_time": "Boil until tender",
        "cooking_methods": [
          "Boil",
          "Pan Fry",
          "Shallow Fry"
        ],
        "required_ingredients": [
          "500g leg piece / mutton ribs (chaap)",
          "2 raw eggs",
          "Bread crumbs",
          "2-3 tbsp chili, ginger, garlic paste",
          "50g Rich'n'Spicy Mutton Chicken Fry / Chaap Masala",
          "Ghee for frying",
          "Rich'n'Spicy Schezwan sauce (for serving)"
        ],
        "instructions": {
          "en": "Wash 500g leg pieces or mutton ribs with water. Marinate mutton with 2-3 tbsp chili, ginger, garlic paste and boil it till tender. Add Rich'n'Spicy Mutton Chicken fry / chaap masala and cook it for 2-3 minutes. Allow the mixture to cool. Whip 2 raw eggs, dip the pieces into it and coat the leg pieces / mutton ribs with bread crumbs. Heat ghee in a pan and fry the pieces on both sides until golden brown and crisp. Serve hot with chutney or Rich'n'Spicy Schezwan sauce.",
          "gu": "૫૦૦ ગ્રામ લેગપીસ અથવા ચાંપ બરાબર ધોઇ તેમાં ૨ થી ૩ ચમચી આદુ, મરચા, લસણની પેસ્ટ નાંખી મટન ગળે ત્યાં સુધી બાફી લો. ત્યાર બાદ મિશ્રણમાં રીચ એન સ્પાઇસી મટન ચીકન ફ્રાય/ ચાંપ મસાલો નાખી ૨ થી ૩ મિનિટ પાકવા દો. મિશ્રણ ઠંડુ પડે પછી બટર/બ્રેડનો ભૂકો લેગપીસ અથવા ચાંપ પર નાંખી ઈંડામાં ડુબાડી ઘીમાં ફ્રાય કરો. શેઝવાન સોસ સાથે ગરમા ગરમ પીરસો."
        }
      },
      "manufacturer": {
        "name": "City Gruh Udhyog",
        "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
        "contact": "9898155726"
      }
    },
    {
      "id": "deepfry-mutton-kheema-samosa-40g",
      "name": "Rich 'n' Spicy Kheema Samosa Masala",
      "brand": "Rich 'n' SP!CY",
      "category": "Deep Fry",
      "product_type": "Dry Marinade / Spice Mix",
      "tags": [
        "Deep Fry",
        "Samosa",
        "Mutton Kheema",
        "Snack",
        "Appetizer"
      ],
      "regional_names": {
        "gu": "ખીમા સમોસા"
      },
      "net_weight": {
        "value": 40,
        "unit": "g"
      },
      "pricing": {
        "mrp": null,
        "currency": "INR"
      },
      "packaging_type": "Transparent Pouch with Full-Label Sticker",
      "dietary": {
        "is_vegetarian_mix": true,
        "suggested_protein": [
          "Mutton",
          "Chicken"
        ]
      },
      "images": {
        "primary": "product images/deep fry/Mutton kheema samosa.JPG",
        "filename": "Mutton kheema samosa.JPG"
      },
      "recipe": {
        "serves_portion": "500g Minced Mutton (Kheema)",
        "marination_time": "None",
        "cooking_methods": [
          "Deep Fry",
          "Sauté"
        ],
        "required_ingredients": [
          "500g minced mutton (kheema)",
          "500g chopped onions",
          "5-6 minced green chilies",
          "Fresh coriander leaves",
          "40g Rich'n'Spicy Kheema Samosa Instant Mix",
          "Wheat flour / pastry dough (for crust)",
          "Salt as per taste",
          "Water and oil as required"
        ],
        "instructions": {
          "en": "Wash 500g minced mutton properly and dry it. Heat 2 cups oil in a pan and add kheema to it and fry till it turns white. Add 500g chopped onions to it and cook on low flame for 5-7 minutes. Add 5-6 minced green chilies along with Rich'n'Spicy kheema samosa masala to it and mix well. Cook till it is done. Garnish with coriander leaves. Cool the mixture and wrap into cone shaped dough and seal the edges. Deep fry the samosas in hot oil till golden brown. Serve hot with chutney or ketchup.",
          "gu": "૫૦૦ ગ્રામ મટન ખીમાને ધોઈ પાણી નિતારી નાંખો. પેનમાં થોડું તેલ ગરમ કરી તેમાં ખીમો નાખી સફેદ થાય ત્યાં સુધી પકાવો. ત્યાર બાદ તેમાં ૫૦૦ ગ્રામ બારીક કાપેલા કાંદા નાખી ૫ થી ૭ મિનિટ ધીમી આંચ પર પકાવી તેમાં ૫ થી ૭ બારીક કાપેલા લીલા મરચા તથા રીચ એન સ્પાઇસી ખીમા સમોસા મસાલો નાખી પકાવો. કોથમરીથી સજાવો. મિશ્રણ ઠંડુ થાય ત્યાર બાદ લોટને સમોસાના આકારમાં બાંધી ખીમાના મિશ્રણથી સ્ટફિંગ કરવી. સમોસાને ઊંડા તેલમાં સોનેરી રંગના થાય ત્યાં સુધી ફ્રાય કરો."
        }
      },
      "manufacturer": {
        "name": "City Gruh Udhyog",
        "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
        "contact": "9898155726"
      }
    }
  ]
}"""
deepfry_catalog = json.loads(raw_json)

with open("deep_fry_products.json", "w", encoding="utf-8") as f:
    json.dump(deepfry_catalog, f, indent=2, ensure_ascii=False)
print("deep_fry_products.json generated successfully!")
