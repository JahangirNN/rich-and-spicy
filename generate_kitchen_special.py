# generate_kitchen_special.py
import json
import os

MANUFACTURER_DEFAULT = {
    "name": "City Gruh Udhyog",
    "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
    "contact": "9898155726"
}

kitchen_special_catalog = {
    "category": "Kitchen Special",
    "total_products": 17,
    "generated_at": "2026-11-21",
    "brand": "Rich 'n' SP!CY",
    "manufacturer": MANUFACTURER_DEFAULT,
    "products": [
        {
            "id": "ks-amchur-powder-100g",
            "name": "Rich 'n' Spicy Amchur Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Amchur", "Dry Mango", "Tangy", "Pantry Essential"],
            "regional_names": {
                "gu": "આમચૂર પાવડર"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Vegetables", "Lentils", "Curries"]
            },
            "images": {
                "primary": "product images/Kitchen special/Amchur-powder.png",
                "filename": "Amchur-powder.png"
            },
            "recipe": {
                "serves_portion": "Pantry Seasoning (As needed)",
                "marination_time": "None",
                "cooking_methods": ["Seasoning", "Tadka"],
                "required_ingredients": [
                    "Sun-dried tart green mangoes (pure ground)",
                    "1-2 tsp added to curries, dals, chutneys or chaats"
                ],
                "instructions": {
                    "en": "Add ½ to 1 teaspoon of Rich 'n' Spicy Amchur Powder to curries, stir fries, paratha stuffings, or chutneys during the final stage of cooking to impart a bright, fruity, tart flavor without adding liquid.",
                    "gu": "રસોઈના અંતિમ તબક્કામાં દાળ, શાક, પરાઠાના મસાલા કે ચટણીમાં અડધીથી એક ચમચી રીચ એન સ્પાઈસી આમચૂર પાવડર ઉમેરી ખટાશ અને સુગંધ મેળવો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-athana-cut-mirchi-100g",
            "name": "Rich 'n' Spicy Athana Cut Mirchi Flakes",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Athana", "Pickle Mirchi", "Chilli Flakes", "Gujarati"],
            "regional_names": {
                "gu": "અથાણા કટ મરચું"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Pickles", "Salads", "Street Food"]
            },
            "images": {
                "primary": "product images/Kitchen special/athana cut mirchi.jpg",
                "filename": "athana cut mirchi.jpg"
            },
            "recipe": {
                "serves_portion": "Pickle & Seasoning Blend",
                "marination_time": "None",
                "cooking_methods": ["Mix", "Infuse"],
                "required_ingredients": [
                    "Coarsely cut dried red chillies (athana cut)",
                    "Mustard oil / Groundnut oil",
                    "Rai kuria (mustard dal) & salt"
                ],
                "instructions": {
                    "en": "Use coarsely cut Athana red chillies to prepare traditional Gujarati mango, lemon, or carrot pickles. Also excellent for infusing tadkas, theplas, or hot street snacks.",
                    "gu": "ગુજરાતી અથાણાં (કેરી, લીંબુ, ગાજર) બનાવવા માટે આ સ્પેશિયલ અથાણા કટ મરચું તેલ, રાઈના કુરિયા અને મીઠા સાથે ભેળવી વાપરો. થેપલા કે વઘાર માટે પણ શ્રેષ્ઠ."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-black-pepper-powder-50g",
            "name": "Rich 'n' Spicy Black Pepper Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Black Pepper", "Mari", "Seasoning", "Pantry Essential"],
            "regional_names": {
                "gu": "કાળા મરી પાવડર"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Soups", "Salads", "Eggs", "Chicken", "Paneer"]
            },
            "images": {
                "primary": "product images/Kitchen special/black-pepper-powder.jpg",
                "filename": "black-pepper-powder.jpg"
            },
            "recipe": {
                "serves_portion": "Seasoning (As needed)",
                "marination_time": "None",
                "cooking_methods": ["Sprinkle", "Simmer"],
                "required_ingredients": [
                    "Freshly ground Malabar black peppercorns",
                    "Pinch added to soups, eggs, steaks, or gravies"
                ],
                "instructions": {
                    "en": "Sprinkle Rich 'n' Spicy freshly ground Black Pepper Powder over hot soups, fried eggs, salads, pasta, or use in marinades for sharp, pungent warmth and aroma.",
                    "gu": "સૂપ, આમલેટ, સલાડ કે ગ્રેવીમાં તીખાશ અને સ્વાસ્થ્યપ્રદ સુગંધ માટે રીચ એન સ્પાઈસી કાળા મરી પાવડરનો ઉપયોગ કરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-coriander-powder-100g",
            "name": "Rich 'n' Spicy Coriander Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Coriander", "Dhana", "Curry Powder", "Pantry Essential"],
            "regional_names": {
                "gu": "ધાણા પાવડર"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Curries", "Dals", "Vegetables", "Meats"]
            },
            "images": {
                "primary": "product images/Kitchen special/coriander powder.jpg",
                "filename": "coriander powder.jpg"
            },
            "recipe": {
                "serves_portion": "Cooking Base (1-2 tbsp per dish)",
                "marination_time": "None",
                "cooking_methods": ["Saute", "Simmer"],
                "required_ingredients": [
                    "Finely ground roasted coriander seeds",
                    "1-2 tbsp for standard gravies and curries"
                ],
                "instructions": {
                    "en": "Add 1 to 2 tablespoons to sauteed onions, garlic, and ginger base while making vegetable, lentil, or meat curries to give texture, earthy citrus notes, and rich body to gravies.",
                    "gu": "શાક, દાળ કે નોન-વેજ ગ્રેવી બનાવતી વખતે વઘારમાં ૧-૨ ચમચી ધાણા પાવડર ઉમેરી સરસ ગ્રેવી અને સ્વાદિષ્ટ સુગંધ મેળવો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-cumin-powder-100g",
            "name": "Rich 'n' Spicy Cumin (Jeera) Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Jeera", "Cumin", "Roasted Cumin", "Pantry Essential"],
            "regional_names": {
                "gu": "જીરૂ પાવડર"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Chaas", "Raita", "Dals", "Curries"]
            },
            "images": {
                "primary": "product images/Kitchen special/cumin-powder-2.png",
                "filename": "cumin-powder-2.png"
            },
            "recipe": {
                "serves_portion": "Seasoning & Cooking (As needed)",
                "marination_time": "None",
                "cooking_methods": ["Saute", "Sprinkle"],
                "required_ingredients": [
                    "Roasted whole cumin seeds (slow ground)",
                    "Buttermilk, curd, or curry gravies"
                ],
                "instructions": {
                    "en": "Essential for Indian cooking. Dust over refreshing buttermilk (chaas), curd raitas, roasted potatoes, or stir into curries and tadkas for deep smoky earthy flavor.",
                    "gu": "છાસ, રાયતા, દહીંવડા કે ગ્રેવીમાં પૌષ્ટિક સ્વાદ અને પાચન સુધારવા માટે રીચ એન સ્પાઈસી શેકેલા જીરૂ પાવડરનો છંટકાવ કરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-dhania-jeera-powder-100g",
            "name": "Rich 'n' Spicy Dhania Jeera Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Dhania Jeera", "Gujarati Staple", "Curry Powder", "Pantry Essential"],
            "regional_names": {
                "gu": "ધાણાજીરૂ પાવડર"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["All Indian Curries", "Dals", "Sabzi"]
            },
            "images": {
                "primary": "product images/Kitchen special/dhania jeera powder.jpeg",
                "filename": "dhania jeera powder.jpeg"
            },
            "recipe": {
                "serves_portion": "Daily Cooking Staple",
                "marination_time": "None",
                "cooking_methods": ["Saute", "Simmer"],
                "required_ingredients": [
                    "Golden ratio blend of slow-roasted coriander and cumin seeds",
                    "Used daily in all vegetable and lentil preparations"
                ],
                "instructions": {
                    "en": "The iconic Gujarati and Indian kitchen backbone. Add 1-2 tablespoons to daily sabzis, dal fry, kadhi, or stuffed parathas for a perfectly balanced aromatics profile.",
                    "gu": "રોજિંદા શાક અને દાળનો આધારસ્તંભ. ઉત્તમ ગુણવત્તાવાળા ધાણા અને જીરૂનું સપ્રમાણ મિશ્રણ રોજિંદી રસોઈને બનાવે સ્વાદિષ્ટ અને સુગંધિત."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-garam-masala-powder-50g",
            "name": "Rich 'n' Spicy Garam Masala Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Garam Masala", "Royal Spice Blend", "Dry Marinade"],
            "regional_names": {
                "gu": "ગરમ મસાલો"
            },
            "net_weight": {
                "value": 50,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Curries", "Biryanis", "Paneer", "Meats"]
            },
            "images": {
                "primary": "product images/Kitchen special/GARAM-MASALA-POWDER.jpg",
                "filename": "GARAM-MASALA-POWDER.jpg"
            },
            "recipe": {
                "serves_portion": "Finishing Blend (½ - 1 tsp per dish)",
                "marination_time": "None",
                "cooking_methods": ["Simmer", "Finishing Touch"],
                "required_ingredients": [
                    "Cardamom, cloves, cinnamon, mace, nutmeg, black pepper, cumin",
                    "Add towards end of cooking"
                ],
                "instructions": {
                    "en": "Finely ground master blend of whole warming spices. Sprinkle ½ to 1 teaspoon into gravies, biryanis, and curries in the last 2 minutes of simmering to preserve delicate aromatic oils.",
                    "gu": "તજ, લવિંગ, એલચી, જાવંત્રી, જાયફળથી બનેલો શાહી ગરમ મસાલો. ગ્રેવી કે બિરયાનીમાં રસોઈના અંતે અડધી ચમચી ઉમેરી ઢાંકી દો જેથી ઉત્તમ મહેક જળવાઈ રહે."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-ginger-powder-sunth-50g",
            "name": "Rich 'n' Spicy Special Sunth (Dry Ginger) Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Sunth", "Dry Ginger", "Ayurvedic", "Tea Masala"],
            "regional_names": {
                "gu": "સ્પે. સૂંઠ પાવડર"
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
                "suggested_protein": ["Tea", "Sweets", "Curries", "Warm Milk"]
            },
            "images": {
                "primary": "product images/Kitchen special/Ginger powder.JPG",
                "filename": "Ginger powder.JPG"
            },
            "recipe": {
                "serves_portion": "Seasoning & Beverage Blend",
                "marination_time": "None",
                "cooking_methods": ["Boil", "Simmer"],
                "required_ingredients": [
                    "Sun-dried cured ginger roots (pure ground)",
                    "Tea, kadha, laddoos, or gingerbread"
                ],
                "instructions": {
                    "en": "Add a pinch of Rich 'n' Spicy Special Sunth Powder to morning masala chai, winter winter desserts (gundar pak, adadiya), or herbal concoctions for immune-boosting warmth.",
                    "gu": "મસાલા ચા, ઉકાળા, શિયાળુ પાક (અડદિયા, ગૂંદપાક) કે દૂધમાં ચપટી સૂંઠ પાવડર નાખી શરદી અને પાચન માટે ઉપયોગ કરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-hing-powder-asafoetida-50g",
            "name": "Rich 'n' Spicy Special Hing (Asafoetida) Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Hing", "Asafoetida", "Tadka", "Pantry Essential"],
            "regional_names": {
                "gu": "સ્પે. હીંગ પાવડર"
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
                "suggested_protein": ["Dals", "Sambhar", "Kadhi", "Vegetables"]
            },
            "images": {
                "primary": "product images/Kitchen special/hing powder.JPG",
                "filename": "hing powder.JPG"
            },
            "recipe": {
                "serves_portion": "Aromatic Tempering (Pinch per dish)",
                "marination_time": "None",
                "cooking_methods": ["Tadka / Tempering"],
                "required_ingredients": [
                    "Compounded premium asafoetida resin",
                    "A generous pinch in hot ghee/oil"
                ],
                "instructions": {
                    "en": "Add a generous pinch of Rich 'n' Spicy Special Hing Powder directly into hot oil or ghee during tadka. Releases unmatched savory allium aroma essential for dals, sambhar, and curries.",
                    "gu": "ગરમ તેલ અથવા ઘીમાં વઘાર કરતી વખતે ચપટી હીંગ ઉમેરો. દાળ, કઢી, સંભાર અને શાક માટે અનિવાર્ય સુગંધ અને ઉત્તમ પાચન ગુણધર્મ."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-jiralu-masala-50g",
            "name": "Rich 'n' Spicy Special Jiralu Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Jiralu", "Khakhra", "Poha", "Gujarati Staple"],
            "regional_names": {
                "gu": "સ્પે. જીરાળુ"
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
                "suggested_protein": ["Khakhra", "Poha", "Fruits", "Yogurt"]
            },
            "images": {
                "primary": "product images/Kitchen special/jiradu.JPG",
                "filename": "jiradu.JPG"
            },
            "recipe": {
                "serves_portion": "Tabletop Seasoning",
                "marination_time": "None",
                "cooking_methods": ["Sprinkle"],
                "required_ingredients": [
                    "Roasted cumin, black salt, dry ginger, hing, rock salt blend",
                    "Ready to sprinkle on snacks"
                ],
                "instructions": {
                    "en": "Classic Gujarati tabletop seasoning. Sprinkle generously over crispy ghee khakhras, steamed batata poha, sliced fruits, curd, or french fries for an irresistible zesty crunch.",
                    "gu": "ઘી વાળા ગરમ ખાખરા, બટાકા પૌંઆ, છાસ, રાયતું કે ફ્રુટ્સ પર રીચ એન સ્પાઈસી સ્પે. જીરાળુ મસાલો છાંટીને ચટાકેદાર સ્વાદ માણો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-kashmiri-red-chilli-powder-100g",
            "name": "Rich 'n' Spicy Kashmiri Red Chilli Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Kashmiri Mirch", "Natural Color", "Mild Spice"],
            "regional_names": {
                "gu": "કાશ્મીરી લાલ મરચું પાવડર"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Tandoori", "Gravies", "Paneer", "Chicken"]
            },
            "images": {
                "primary": "product images/Kitchen special/kashmiri red chilli powder.jpg",
                "filename": "kashmiri red chilli powder.jpg"
            },
            "recipe": {
                "serves_portion": "Color & Mild Heat (1-2 tbsp)",
                "marination_time": "None",
                "cooking_methods": ["Saute", "Marinade"],
                "required_ingredients": [
                    "Select stemless Kashmiri dry red chillies",
                    "Provides vibrant natural scarlet hue with gentle warmth"
                ],
                "instructions": {
                    "en": "Prized for its brilliant crimson red natural color and mild pleasant heat. Ideal for marinades, tandoori preparations, butter chicken, and rich restaurant-style gravies.",
                    "gu": "કુદરતી લાલ ચટક રંગ અને મધ્યમ તીખાશ આપતું કાશ્મીરી લાલ મરચું. તંદૂરી, પનીર ટીક્કા અને રોયલ ગ્રેવીમાં રંગ અને સ્વાદ માટે ઉત્તમ."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-koru-marchu-100g",
            "name": "Rich 'n' Spicy Koru Marchu Seasoning",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Koru Marchu", "Dry Red Chilli", "Seasoning"],
            "regional_names": {
                "gu": "કોરૂં મરચું"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Snacks", "Dal-Bhaat", "Khichdi"]
            },
            "images": {
                "primary": "product images/Kitchen special/koru marchu.jpg",
                "filename": "koru marchu.jpg"
            },
            "recipe": {
                "serves_portion": "Table Seasoning & Chutney Base",
                "marination_time": "None",
                "cooking_methods": ["Sprinkle", "Mix with Oil"],
                "required_ingredients": [
                    "Pounded sun-dried chillies with salt and spices",
                    "Groundnut oil or sesame oil"
                ],
                "instructions": {
                    "en": "Mix with cold-pressed peanut or sesame oil for an instant dry chutney dip, or dust over steaming dal-rice, khichdi, and dhokla for an authentic spicy rustic kick.",
                    "gu": "સીંગતેલ કે તલના તેલ સાથે મેળવી ઢોકળાં, મુઠીયા, ભાખરી કે દાળ-ભાત સાથે કોરા મરચાંની ટેસ્ટી ચટણી તરીકે માણો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-red-chilli-powder-100g",
            "name": "Rich 'n' Spicy Red Chilli Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Red Chilli", "Lal Marchu", "Fiery Heat", "Pantry Essential"],
            "regional_names": {
                "gu": "લાલ મરચું પાવડર"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["All Indian Curries", "Marinades"]
            },
            "images": {
                "primary": "product images/Kitchen special/red chilli powder.jpg",
                "filename": "red chilli powder.jpg"
            },
            "recipe": {
                "serves_portion": "Daily Heat & Spice (As per taste)",
                "marination_time": "None",
                "cooking_methods": ["Saute", "Simmer"],
                "required_ingredients": [
                    "Fine stone-ground Guntur & Reshampatti red chillies",
                    "Adds punchy heat and lively flavor"
                ],
                "instructions": {
                    "en": "High pungent, brightly aromatic pure red chilli powder. Use in marinades, tadkas, stir fries, and gravies according to desired heat level.",
                    "gu": "તીખી અને સ્વાદિષ્ટ ગુણવત્તાવાળા લાલ મરચાંનો શુદ્ધ પાવડર. રોજિંદા શાક અને મરીનેશનમાં તીખાશ અને કલર માટે વાપરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-sanchal-black-salt-powder-100g",
            "name": "Rich 'n' Spicy Sanchal (Black Salt) Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Sanchal", "Black Salt", "Kala Namak", "Digestive"],
            "regional_names": {
                "gu": "સંચળ પાવડર"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Chaat", "Lemonade", "Chaas", "Chutneys"]
            },
            "images": {
                "primary": "product images/Kitchen special/sanchal powder.jpg",
                "filename": "sanchal powder.jpg"
            },
            "recipe": {
                "serves_portion": "Digestive Mineral Salt (As needed)",
                "marination_time": "None",
                "cooking_methods": ["Sprinkle", "Dissolve"],
                "required_ingredients": [
                    "Himalayan volcanic rock salt (Kala Namak)",
                    "Sprinkled on beverages and street foods"
                ],
                "instructions": {
                    "en": "Sulfur-rich volcanic mineral salt famous for its distinct umami tang. Essential for nimbu pani, pani puri, chaat masala, jaljeera, and cooling summer digestive drinks.",
                    "gu": "લીંબુ પાણી, જલજીરા, પાણીપુરી, ચાટ અને સલાડમાં વિશિષ્ટ ચટપટો સ્વાદ અને પાચક ગુણધર્મ આપવા માટે સંચળ પાવડર ઉમેરો."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-sindhav-salt-rock-salt-100g",
            "name": "Rich 'n' Spicy Sindhav Salt (Rock Salt)",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Sindhav Salt", "Rock Salt", "Sendha Namak", "Fasting / Farali"],
            "regional_names": {
                "gu": "સિંધવ મીઠું"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["Farali Dishes", "Salads", "Daily Cooking"]
            },
            "images": {
                "primary": "product images/Kitchen special/sindhav salt.jpg",
                "filename": "sindhav salt.jpg"
            },
            "recipe": {
                "serves_portion": "Pure Mineral Fasting Salt",
                "marination_time": "None",
                "cooking_methods": ["Seasoning"],
                "required_ingredients": [
                    "Pure Himalayan unrefined pink/white rock salt (Sendha Namak)",
                    "Permitted for all Hindu religious fasting diets"
                ],
                "instructions": {
                    "en": "Unrefined pure crystal mineral rock salt, free from chemical processing. Approved for religious fasting (Vrat/Upvas) in sabudana khichdi, farali patties, fruit bowls, and health cooking.",
                    "gu": "ઉપવાસ-વ્રત (સાબુદાણા ખીચડી, મોરૈયો, ફરાળી પેટીસ) માટે શુદ્ધ સિંધવ મીઠું. કેમિકલ વગરનું કુદરતી ખનિજયુક્ત સ્વાસ્થ્યપ્રદ મીઠું."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-sp-tea-masala-50g",
            "name": "Rich 'n' Spicy Special Tea Masala",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Chai Masala", "Tea Masala", "Chah Masalo", "Aromatic"],
            "regional_names": {
                "gu": "સ્પે. ચાહ મસાલો"
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
                "suggested_protein": ["Milk Tea (Chai)", "Herbal Tea"]
            },
            "images": {
                "primary": "product images/Kitchen special/Tea masala.JPG",
                "filename": "Tea masala.JPG"
            },
            "recipe": {
                "serves_portion": "Chai Seasoning (¼ tsp for 2 cups)",
                "marination_time": "None",
                "cooking_methods": ["Boil", "Brew"],
                "required_ingredients": [
                    "Green cardamom, dry ginger (sunth), cinnamon, cloves, black pepper, nutmeg",
                    "Brewed in milk and black tea leaves"
                ],
                "instructions": {
                    "en": "Add ¼ teaspoon of Rich 'n' Spicy Special Tea Masala while boiling milk and tea leaves for 2 cups of chai. Brew for 2 minutes on low flame to infuse luxurious warmth, cardamom fragrance, and soothing comfort.",
                    "gu": "બે કપ ચા ઉકળતી વખતે ૧/૪ ચમચી રીચ એન સ્પાઈસી સ્પે. ચાહ મસાલો ઉમેરી ૨ મિનિટ ઉકાળો. તાજગીસભર ઈલાયચી અને સૂંઠની ઉત્તમ સુગંધવાળી કડક મસાલા ચા તૈયાર."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        },
        {
            "id": "ks-turmeric-powder-100g",
            "name": "Rich 'n' Spicy Turmeric (Haldi) Powder",
            "brand": "Rich 'n' SP!CY",
            "category": "Kitchen Special",
            "product_type": "Dry Marinade / Spice Mix",
            "tags": ["Kitchen Special", "Turmeric", "Haldi", "Golden Spice", "Pantry Essential"],
            "regional_names": {
                "gu": "હળદર પાવડર"
            },
            "net_weight": {
                "value": 100,
                "unit": "g"
            },
            "pricing": {
                "mrp": None,
                "currency": "INR"
            },
            "packaging_type": "Standard Retail Sealed Pack",
            "dietary": {
                "is_vegetarian_mix": True,
                "suggested_protein": ["All Curries", "Dals", "Golden Milk", "Marinades"]
            },
            "images": {
                "primary": "product images/Kitchen special/turmeric powder.jpg",
                "filename": "turmeric powder.jpg"
            },
            "recipe": {
                "serves_portion": "Daily Health & Color (½ tsp per dish)",
                "marination_time": "None",
                "cooking_methods": ["Tadka", "Simmer"],
                "required_ingredients": [
                    "High-curcumin Salem turmeric fingers (slow milled)",
                    "Essential for vibrant yellow hue and natural immunity"
                ],
                "instructions": {
                    "en": "High curcumin pure turmeric powder. Add ½ teaspoon to hot oil or ghee in every curry and dal, or whisk into warm milk for therapeutic golden milk (haldi doodh).",
                    "gu": "ઉચ્ચ કર્ક્યુમિનવાળી શુદ્ધ હળદર. રોજિંદા શાક, દાળના વઘારમાં અને ઔષધીય હળદરવાળા દૂધ (ગોલ્ડન મિલ્ક) માટે શ્રેષ્ઠ."
                }
            },
            "manufacturer": MANUFACTURER_DEFAULT
        }
    ]
}

with open("kitchen_special_products.json", "w", encoding="utf-8") as f:
    json.dump(kitchen_special_catalog, f, indent=2, ensure_ascii=False)

print(f"Generated kitchen_special_products.json with {len(kitchen_special_catalog['products'])} products.")
