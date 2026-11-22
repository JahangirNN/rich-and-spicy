# generate_others.py
import json
import os

MANUFACTURER_DEFAULT = {
    "name": "City Gruh Udhyog",
    "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
    "contact": "9898155726"
}

others_items = [
    # Root items (21)
    {
        "id": "others-tendercook-meat-tenderizer-100g",
        "name": "Tendercook Meat Tenderizer Powder",
        "rel_path": "product images/others/TendercookTenderizer.jpg",
        "fname": "TendercookTenderizer.jpg",
        "gu": "ટેન્ડરકૂક મીટ ટેન્ડરાઈઝર",
        "net_weight": 100,
        "tags": ["Others", "Pantry", "Meat Tenderizer", "Barbecue", "Dry Marinade"],
        "serves": "Meat Marinade Prep (1 tbsp per 1kg meat)",
        "desc_en": "Natural enzyme meat tenderizer. Rub over tough cuts of mutton or beef 30-45 minutes before cooking for melt-in-mouth succulent textures.",
        "desc_gu": "મટન કે બીફને નરમ અને રસદાર બનાવવા માટે રાંધવાના ૩૦-૪૫ મિનિટ પહેલાં લગાવો."
    },
    {
        "id": "others-black-soya-sauce-200g",
        "name": "Rich 'n' Spicy Black Soya Sauce",
        "rel_path": "product images/others/black soya sauce.JPG",
        "fname": "black soya sauce.JPG",
        "gu": "બ્લેક સોયા સોસ",
        "net_weight": 200,
        "tags": ["Others", "Sauces", "Soya Sauce", "Indo-Chinese", "Pantry"],
        "serves": "Indo-Chinese Cooking (1-2 tbsp)",
        "desc_en": "Rich fermented dark soya sauce. Perfect for authentic Indo-Chinese noodles, Manchurian, fried rice, and dipping sauces.",
        "desc_gu": "ચાઈનીઝ નુડલ્સ, મંચુરિયન, ફ્રાઈડ રાઈસ અને ચટણીમાં રંગ અને સ્વાદ આપતો ડાર્ક સોયા સોસ."
    },
    {
        "id": "others-cheese-popcorn-powder-50g",
        "name": "Rich 'n' Spicy Cheese Popcorn Seasoning Powder",
        "rel_path": "product images/others/cheese popcorn powder.jpg",
        "fname": "cheese popcorn powder.jpg",
        "gu": "ચીઝ પોપકોર્ન પાવડર",
        "net_weight": 50,
        "tags": ["Others", "Seasoning", "Cheese Powder", "Popcorn", "Snacks"],
        "serves": "Snack Dusting (1 tbsp per bowl)",
        "desc_en": "Savory cheese seasoning powder. Toss generously over fresh hot buttered popcorn, french fries, nachos, or potato crisps.",
        "desc_gu": "ગરમા ગરમ પોપકોર્ન, ફ્રેન્ચ ફ્રાઈસ અને નાચોસ પર છાંટીને સિનેમા હોલ જેવો ચીઝી સ્વાદ માણો."
    },
    {
        "id": "others-chilli-flakes-50g",
        "name": "Rich 'n' Spicy Red Chilli Flakes",
        "rel_path": "product images/others/chilli flakes.jpg",
        "fname": "chilli flakes.jpg",
        "gu": "ચીલી ફ્લેક્સ",
        "net_weight": 50,
        "tags": ["Others", "Seasoning", "Chilli Flakes", "Pizza", "Pasta"],
        "serves": "Tabletop Seasoning",
        "desc_en": "Crushed sun-ripened red pepper flakes with seeds. Sprinkle over pizzas, pasta, garlic bread, soups, and avocado toast.",
        "desc_gu": "પીત્ઝા, પાસ્તા, ગાર્લિક બ્રેડ અને સૂપ પર તીખાશ માટે છાંટવામાં આવતા લાલ મરચાંના ફ્લેક્સ."
    },
    {
        "id": "others-ef-kolahs-black-vinegar-500g",
        "name": "E.F. Kolah's Brewed Black Vinegar",
        "rel_path": "product images/others/ef kolah's black vinegar.jpg",
        "fname": "ef kolah's black vinegar.jpg",
        "gu": "ઈ.એફ. કોલાહ બ્લેક વિનેગર",
        "net_weight": 500,
        "tags": ["Others", "Parsi Cuisine", "Navsari Vinegar", "Cane Vinegar", "Pantry"],
        "serves": "Navsari Brewed Sugarcane Vinegar",
        "desc_en": "Authentic naturally fermented barrel-aged black sugarcane vinegar from Navsari. Essential for Parsi sali boti, vindaloo, and traditional pickling.",
        "desc_gu": "નવસારીનો અસલ કુદરતી શેરડીમાંથી આથેલો કાળો સરકો (વિનેગાર). પારસી સાલી બોટી, વિંદાલુ અને અથાણાં માટે પ્રખ્યાત."
    },
    {
        "id": "others-fried-onions-birista-100g",
        "name": "Rich 'n' Spicy Golden Fried Onions (Birista)",
        "rel_path": "product images/others/fried onions birista.jpg",
        "fname": "fried onions birista.jpg",
        "gu": "તળેલી ડુંગળી / બિરિસ્તા",
        "net_weight": 100,
        "tags": ["Others", "Birista", "Fried Onions", "Biryani Garnish", "Pantry"],
        "serves": "Biryani Layering & Gravy Garnish",
        "desc_en": "Crispy sweet golden fried sliced onions. Essential crunchy layer for dum biryanis, haleem, khichda, and Mughlai kormas.",
        "desc_gu": "બિરયાનીના થર, હલીમ, ખીચડા અને કોરમા માટે તૈયાર ક્રિસ્પી ગોલ્ડન તળેલી ડુંગળી (બિરિસ્તા)."
    },
    {
        "id": "others-gaay-chaap-besan-500g",
        "name": "Gaay Chaap Premium Besan (Gram Flour)",
        "rel_path": "product images/others/gaay chaap besan.jpg",
        "fname": "gaay chaap besan.jpg",
        "gu": "ગાય છાપ ચણાનો લોટ",
        "net_weight": 500,
        "tags": ["Others", "Besan", "Gram Flour", "Farsan", "Pantry Staple"],
        "serves": "Traditional Farsan & Sweets Base",
        "desc_en": "Finely milled pure chana dal gram flour. Ideal for authentic Gujarati kadhi, pakodas, dhokla, fafda, khandvi, and mohanthal.",
        "desc_gu": "કઢી, ભજીયાં, ખમણ, ખાંડવી, ફાફડા અને મોહનથાળ બનાવવા માટે શુદ્ધ ચણાદાળનો ગાય છાપ બેસન."
    },
    {
        "id": "others-garlic-powder-50g",
        "name": "Rich 'n' Spicy Dehydrated Garlic Powder",
        "rel_path": "product images/others/garlic powder.jpg",
        "fname": "garlic powder.jpg",
        "gu": "લસણ પાવડર",
        "net_weight": 50,
        "tags": ["Others", "Seasoning", "Garlic Powder", "Dehydrated", "Pantry"],
        "serves": "Instant Garlic Aromatics (1 tsp)",
        "desc_en": "Dehydrated premium garlic powder. Instant punchy savory garlic flavor for dry rubs, garlic bread, pasta sauces, dips, and marinades.",
        "desc_gu": "ગાર્લિક બ્રેડ, ડીપ્સ, સૂપ અને મરીનેશનમાં તાજા લસણ જેવો જ સ્વાદ અને સુગંધ આપતો શુદ્ધ લસણ પાવડર."
    },
    {
        "id": "others-green-chilli-sauce-200g",
        "name": "Rich 'n' Spicy Green Chilli Sauce",
        "rel_path": "product images/others/green chilli sauce.JPG",
        "fname": "green chilli sauce.JPG",
        "gu": "ગ્રીન ચીલી સોસ",
        "net_weight": 200,
        "tags": ["Others", "Sauces", "Green Chilli Sauce", "Indo-Chinese", "Street Food"],
        "serves": "Zesty Hot Condiment",
        "desc_en": "Zesty, spicy green chilli sauce. Perfect dipping and cooking condiment for samosas, noodles, rolls, frankies, and Indo-Chinese gravies.",
        "desc_gu": "સમોસા, ફ્રેન્કી, ચાઈનીઝ ભેલ અને નુડલ્સ માટે તીખો અને ચટપટો ગ્રીન ચીલી સોસ."
    },
    {
        "id": "others-kewra-water-600g",
        "name": "Pure Kewra Water 600ml",
        "rel_path": "product images/others/kewra 600 ml.jpeg",
        "fname": "kewra 600 ml.jpeg",
        "gu": "કેવડા જળ ૬૦૦ મિલી",
        "net_weight": 600,
        "tags": ["Others", "Aromatics", "Kewra Water", "Biryani Essence", "Mughlai"],
        "serves": "Mughlai Aromatic Floral Water",
        "desc_en": "Distilled fragrant pandanus flower water. Drizzle over dum biryani, shahi korma, rasgullas, and rabdi for unmatched royal festive aroma.",
        "desc_gu": "દમ બિરયાની, મુગલાઈ કોરમા, મીઠાઈ અને શરબતમાં રાજવી સુગંધ આપવા માટે શુદ્ધ કેવડા જળ."
    },
    {
        "id": "others-kewra-water-200g",
        "name": "Pure Kewra Water 200ml",
        "rel_path": "product images/others/kewra water 200 ml.jpg",
        "fname": "kewra water 200 ml.jpg",
        "gu": "કેવડા જળ ૨૦૦ મિલી",
        "net_weight": 200,
        "tags": ["Others", "Aromatics", "Kewra Water", "Biryani Essence", "Pantry"],
        "serves": "Mughlai Floral Water (Small)",
        "desc_en": "Convenient 200ml pack of distilled kewra water for everyday home biryanis, kebabs, kheer, and traditional desserts.",
        "desc_gu": "ઘરેલુ બિરયાની, કબાબ, ખીર અને મુગલાઈ વાનગીઓ માટે સુગંધિત કેવડા જળ."
    },
    {
        "id": "others-keybrand-rose-water-200g",
        "name": "Key Brand Pure Rose Water 200ml",
        "rel_path": "product images/others/keybrand_rosewater_200ml.jpg",
        "fname": "keybrand_rosewater_200ml.jpg",
        "gu": "ગુલાબ જળ ૨૦૦ મિલી",
        "net_weight": 200,
        "tags": ["Others", "Aromatics", "Rose Water", "Key Brand", "Desserts"],
        "serves": "Culinary Rose Distillate",
        "desc_en": "Pure culinary distilled rose petal water. Enhances gulab jamun syrup, falooda, lassi, kheer, and festive milk sweets.",
        "desc_gu": "ગુલાબ જાંબુની ચાસણી, ફાલુદા, લસ્સી અને દૂધની વાનગીઓમાં ગુલાબી મહેક ઉમેરતું ગુલાબ જળ."
    },
    {
        "id": "others-onion-powder-50g",
        "name": "Rich 'n' Spicy Dehydrated Onion Powder",
        "rel_path": "product images/others/onion powder.jpg",
        "fname": "onion powder.jpg",
        "gu": "ડુંગળી પાવડર",
        "net_weight": 50,
        "tags": ["Others", "Seasoning", "Onion Powder", "Dehydrated", "Pantry"],
        "serves": "Instant Sweet-Savory Allium Flavor",
        "desc_en": "Dehydrated golden onion powder. Essential for instant soup powders, burger patties, dips, seasoning blends, and smooth gravies.",
        "desc_gu": "સૂપ, બર્ગર, ડીપ્સ અને ગ્રેવીમાં ડુંગળીનો સ્વાદ અને મીઠાશ આપવા માટે શુદ્ધ ડુંગળી પાવડર."
    },
    {
        "id": "others-oregano-seasoning-30g",
        "name": "Rich 'n' Spicy Oregano Herb Seasoning",
        "rel_path": "product images/others/oregano.jpg",
        "fname": "oregano.jpg",
        "gu": "ઓરેગાનો",
        "net_weight": 30,
        "tags": ["Others", "Seasoning", "Oregano", "Italian Herb", "Pizza"],
        "serves": "Mediterranean Table Seasoning",
        "desc_en": "Dried Mediterranean wild oregano leaves. Essential for seasoning pizzas, pasta sauces, bruschetta, and roasted vegetables.",
        "desc_gu": "પીત્ઝા, પાસ્તા, ગાર્લિક બ્રેડ અને ઈટાલિયન વાનગીઓ માટે સુગંધિત ડ્રાય ઓરેગાનો પાંદડાં."
    },
    {
        "id": "others-red-chilli-sauce-200g",
        "name": "Rich 'n' Spicy Red Chilli Sauce",
        "rel_path": "product images/others/red chilli sauce.JPG",
        "fname": "red chilli sauce.JPG",
        "gu": "રેડ ચીલી સોસ",
        "net_weight": 200,
        "tags": ["Others", "Sauces", "Red Chilli Sauce", "Indo-Chinese", "Condiment"],
        "serves": "Spicy Tangy Condiment",
        "desc_en": "Fiery red chilli sauce with tangy notes. Essential for stir-frying Chinese Manchurian, schezwan rice, spring rolls, and noodles.",
        "desc_gu": "ચાઈનીઝ મંચુરિયન, શેઝવાન નુડલ્સ અને સ્પ્રિંગ રોલ માટે તીખો લાલ મરચાંનો સોસ."
    },
    {
        "id": "others-rose-water-600g",
        "name": "Pure Rose Water 600ml",
        "rel_path": "product images/others/rose water 600 ml.jpg",
        "fname": "rose water 600 ml.jpg",
        "gu": "ગુલાબ જળ ૬૦૦ મિલી",
        "net_weight": 600,
        "tags": ["Others", "Aromatics", "Rose Water", "Culinary Water", "Desserts"],
        "serves": "Pure Distilled Rose Essence (Large)",
        "desc_en": "Large 600ml bottle of pure distilled rose petal water. For sweet makers, catering, falooda, halwa, and refreshing sherbets.",
        "desc_gu": "મીઠાઈ, ફાલુદા, શરબત અને કેટરિંગ માટે મોટા પેકમાં શુદ્ધ સુગંધિત ગુલાબ જળ."
    },
    {
        "id": "others-sabudana-sago-500g",
        "name": "Rich 'n' Spicy Premium Sabudana (Tapioca Sago)",
        "rel_path": "product images/others/sabudana.jpg",
        "fname": "sabudana.jpg",
        "gu": "સાબુદાણા",
        "net_weight": 500,
        "tags": ["Others", "Sabudana", "Sago", "Fasting", "Farali Staple"],
        "serves": "Farali Fasting Staple (Serves 4-6)",
        "desc_en": "Pristine white, non-sticky tapioca pearls. Soaks evenly to create fluffy sabudana khichdi, crispy sabudana vadas, and creamy kheer.",
        "desc_gu": "એકદમ મોતી જેવા સફેદ સાબુદાણા. વ્રત-ઉપવાસ માટે ખીલેલી સાબુદાણા ખીચડી, વડા અને ખીર બનાવવા માટે બેસ્ટ."
    },
    {
        "id": "others-tomato-powder-50g",
        "name": "Rich 'n' Spicy Dehydrated Tomato Powder",
        "rel_path": "product images/others/tomato powder.jpg",
        "fname": "tomato powder.jpg",
        "gu": "ટામેટા પાવડર",
        "net_weight": 50,
        "tags": ["Others", "Seasoning", "Tomato Powder", "Dehydrated", "Tangy"],
        "serves": "Instant Tomato Flavor & Color",
        "desc_en": "Dehydrated pure ripe red tomato powder. Imparts instant tangy sweetness and color to instant soup blends, gravies, pasta, and snack dustings.",
        "desc_gu": "સૂપ, ગ્રેવી, પાસ્તા અને નાસ્તાના મસાલામાં ટામેટાંની કુદરતી ખટાશ અને લાલ રંગ આપતો પાવડર."
    },
    {
        "id": "others-uttam-maida-500g",
        "name": "Uttam Premium Maida (All Purpose Flour)",
        "rel_path": "product images/others/uttam maida.jpg",
        "fname": "uttam maida.jpg",
        "gu": "ઉત્તમ મેંદો",
        "net_weight": 500,
        "tags": ["Others", "Flour", "Maida", "Baking", "Samosa Dough"],
        "serves": "Pastry, Bhature & Naan Flour",
        "desc_en": "Super-refined wheat flour with ideal gluten stretch. Perfect for fluffy bhature, tandoori naan, samosa pastry crusts, and delicate cakes.",
        "desc_gu": "ભટુરે, નાન, સમોસાના પડ અને બેકિંગ માટે એકદમ ઝીણો ઉત્તમ ગુણવત્તાવાળો મેંદો."
    },
    {
        "id": "others-uttam-rava-sooji-500g",
        "name": "Uttam Premium Rava (Sooji / Semolina)",
        "rel_path": "product images/others/uttam-rava.jpg",
        "fname": "uttam-rava.jpg",
        "gu": "ઉત્તમ સોજી / રવો",
        "net_weight": 500,
        "tags": ["Others", "Rava", "Sooji", "Semolina", "Halwa / Upma"],
        "serves": "Halwa, Upma & Idli Batter",
        "desc_en": "Granular durum wheat semolina. Roasts to a fragrant golden aroma for comforting sooji halwa, vegetable upma, and rava dosa batter.",
        "desc_gu": "શીરો, રવા ઉપમા, રવા ઢોંસા અને ઈડલી માટે દાણાદાર અને સ્વાદિષ્ટ ઉત્તમ રવો/સોજી."
    },
    {
        "id": "others-white-cheddar-cheese-powder-50g",
        "name": "White Cheddar Cheese Seasoning Powder",
        "rel_path": "product images/others/white cheddar cheese powder.jpg",
        "fname": "white cheddar cheese powder.jpg",
        "gu": "વ્હાઈટ ચેડર ચીઝ પાવડર",
        "net_weight": 50,
        "tags": ["Others", "Cheese Powder", "White Cheddar", "Seasoning", "Snacks"],
        "serves": "Gourmet Cheese Dusting",
        "desc_en": "Premium sharp white cheddar cheese powder. Perfect gourmet dusting for makhana, chips, pasta, baked potatoes, and popcorn.",
        "desc_gu": "મખાના, પોપકોર્ન, પાસ્તા અને ચિપ્સ પર પ્રીમિયમ શાર્પ ચીઝનો સ્વાદ આપતો વ્હાઈટ ચેડર ચીઝ પાવડર."
    },

    # Colors (8)
    {
        "id": "others-anuja-lemon-yellow-10g",
        "name": "Anuja Lemon Yellow Food Colour",
        "rel_path": "product images/others/colors/anuja lemon yellow color.jpg",
        "fname": "anuja lemon yellow color.jpg",
        "gu": "અનુજા લેમન યલો કલર",
        "net_weight": 10,
        "tags": ["Others", "Food Color", "Lemon Yellow", "Mithai", "Baking"],
        "serves": "Food Color Powder (Pinch)",
        "desc_en": "Brilliant lemon yellow food color powder. For jalebi, motichoor laddoos, biryani rice, and bakery icings.",
        "desc_gu": "જલેબી, મોતીચૂર લાડુ, બિરયાની ચોખા અને આઈસિંગ માટે બ્રાઈટ લેમન યલો ફૂડ કલર."
    },
    {
        "id": "others-anuja-orange-red-10g",
        "name": "Anuja Orange Red Food Colour",
        "rel_path": "product images/others/colors/anuja orange red.gif",
        "fname": "anuja orange red.gif",
        "gu": "અનુજા ઓરેન્જ રેડ કલર",
        "net_weight": 10,
        "tags": ["Others", "Food Color", "Orange Red", "Tandoori", "Biryani"],
        "serves": "Food Color Powder (Pinch)",
        "desc_en": "Classic vibrant orange-red shade for tandoori marinades, chicken 65, and biryani rice garnish.",
        "desc_gu": "તંદૂરી ચિકન, ચિકન ૬૫ અને બિરયાની ગાર્નિશ માટે ક્લાસિક ઓરેન્જ રેડ રંગ."
    },
    {
        "id": "others-anuja-raspberry-red-10g",
        "name": "Anuja Raspberry Red Food Colour",
        "rel_path": "product images/others/colors/anuja-food-color- raspberry red.jpg",
        "fname": "anuja-food-color- raspberry red.jpg",
        "gu": "અનુજા રાસબેરી રેડ કલર",
        "net_weight": 10,
        "tags": ["Others", "Food Color", "Raspberry Red", "Syrups", "Beverages"],
        "serves": "Food Color Powder (Pinch)",
        "desc_en": "Deep berry red color for rose sharbat, ice candies, cakes, and mocktails.",
        "desc_gu": "ગુલાબ શરબત, આઈસ્ક્રીમ અને કેક માટે ઘેરો રાસબેરી રેડ રંગ."
    },
    {
        "id": "others-anuja-green-10g",
        "name": "Anuja Green Food Colour",
        "rel_path": "product images/others/colors/Anuja-Green-Colour-10gm-50pcs-.jpg",
        "fname": "Anuja-Green-Colour-10gm-50pcs-.jpg",
        "gu": "અનુજા ગ્રીન કલર",
        "net_weight": 10,
        "tags": ["Others", "Food Color", "Green", "Pista Kulfi", "Paan"],
        "serves": "Food Color Powder (Pinch)",
        "desc_en": "Lush green edible food coloring for pista kulfi, paan candies, and confectioneries.",
        "desc_gu": "પિસ્તા કુલ્ફી, પાન મિઠાઈ અને કન્ફેક્શનરી માટે સુંદર ગ્રીન કલર."
    },
    {
        "id": "others-apple-green-10g",
        "name": "Apple Green Food Colour",
        "rel_path": "product images/others/colors/apple green.jpg",
        "fname": "apple green.jpg",
        "gu": "એપલ ગ્રીન કલર",
        "net_weight": 10,
        "tags": ["Others", "Food Color", "Apple Green", "Desserts", "Bakery"],
        "serves": "Food Color Powder (Pinch)",
        "desc_en": "Refreshing light apple-green hue for beverages, syrups, and bakery decorations.",
        "desc_gu": "શરબત, બેકિંગ અને મીઠાઈ માટે આકર્ષક એપલ ગ્રીન કલર."
    },
    {
        "id": "others-bush-orange-red-10g",
        "name": "Bush Orange Red Food Colour",
        "rel_path": "product images/others/colors/bush orange red.jpg",
        "fname": "bush orange red.jpg",
        "gu": "બુશ ઓરેન્જ રેડ પાવડર",
        "net_weight": 10,
        "tags": ["Others", "Food Color", "Bush Brand", "Tandoori", "Restaurant Color"],
        "serves": "Food Color Powder (Pinch)",
        "desc_en": "Professional-grade food color preferred by commercial kitchens for consistent vivid orange-red tint.",
        "desc_gu": "રેસ્ટોરન્ટ અને કેટરિંગ માટે જાણીતી બુશ બ્રાન્ડનો ઓરેન્જ રેડ ફૂડ કલર."
    },
    {
        "id": "others-bush-kesari-powder-10g",
        "name": "Bush Kesari Food Colour Powder",
        "rel_path": "product images/others/colors/bush-kesari-powder-500x500.jpg",
        "fname": "bush-kesari-powder-500x500.jpg",
        "gu": "બુશ કેસરી પાવડર",
        "net_weight": 10,
        "tags": ["Others", "Food Color", "Kesari", "Saffron Yellow", "Halwa"],
        "serves": "Food Color Powder (Pinch)",
        "desc_en": "Warm saffron-kesari yellow food coloring for kesari halwa, biryanis, and traditional Indian sweets.",
        "desc_gu": "કેસરી ભાત, શીરો અને મીઠાઈ માટે સુંદર કેસરી પીળો રંગ."
    },
    {
        "id": "others-lemon-yellow-color-10g",
        "name": "Premium Lemon Yellow Food Colour",
        "rel_path": "product images/others/colors/Lemon-Yellow color.jpg",
        "fname": "Lemon-Yellow color.jpg",
        "gu": "લેમન યલો કલર",
        "net_weight": 10,
        "tags": ["Others", "Food Color", "Lemon Yellow", "Confectionery"],
        "serves": "Food Color Powder (Pinch)",
        "desc_en": "High solubility lemon yellow food dye for clear syrups, ice pops, and sweets.",
        "desc_gu": "શરબત અને મીઠાઈ માટે ઝડપથી ઓગળતો લેમન યલો કલર."
    },

    # Dry Fruits (10)
    {
        "id": "others-almonds-badam-100g",
        "name": "Rich 'n' Spicy Premium Almonds (Badam)",
        "rel_path": "product images/others/dry fruits/almonds.jpg",
        "fname": "almonds.jpg",
        "gu": "બદામ",
        "net_weight": 100,
        "tags": ["Others", "Dry Fruits", "Badam", "Almonds", "Healthy Snacks"],
        "serves": "Healthy Snacking & Sweet Garnish",
        "desc_en": "Crisp sweet California almonds. Slice for kheer, sheera, biryani garnish, or enjoy soaked in the morning.",
        "desc_gu": "રોજિંદા સ્વાસ્થ્ય માટે તેમજ શીરો, ખીર અને બિરયાનીમાં ગાર્નિશ કરવા માટે પ્રીમિયમ બદામ."
    },
    {
        "id": "others-anjeer-figs-100g",
        "name": "Rich 'n' Spicy Dried Figs (Anjeer)",
        "rel_path": "product images/others/dry fruits/anjeer.jpg",
        "fname": "anjeer.jpg",
        "gu": "અંજીર",
        "net_weight": 100,
        "tags": ["Others", "Dry Fruits", "Anjeer", "Dried Figs", "Fiber Rich"],
        "serves": "Nutritious Dry Fruit Snack",
        "desc_en": "Plump sun-dried figs packed with fiber and natural sweetness. Enjoy direct, blend into anjeer halwa, or add to rich milkshakes.",
        "desc_gu": "ફાઈબર અને કેલ્શિયમથી ભરપૂર મીઠા સૂકા અંજીર. અંજીર હલવો, મિલ્કશેક અને ડ્રાયફ્રૂટ બાઈટ્સ માટે શ્રેષ્ઠ."
    },
    {
        "id": "others-black-raisins-kali-draksh-100g",
        "name": "Rich 'n' Spicy Black Raisins (Kali Draksh)",
        "rel_path": "product images/others/dry fruits/black rasins.jpg",
        "fname": "black rasins.jpg",
        "gu": "કાળી દ્રાક્ષ",
        "net_weight": 100,
        "tags": ["Others", "Dry Fruits", "Kali Draksh", "Black Raisins", "Iron Rich"],
        "serves": "Iron-Rich Sweetness",
        "desc_en": "Naturally sweet seedless black raisins. Excellent for iron-boosting morning water, rich curries, and spiced rice pulao.",
        "desc_gu": "હિમોગ્લોબિન વધારવા માટે અને પુલાવ કે મીઠાઈમાં વાપરવા માટે મીઠી બી વગરની કાળી દ્રાક્ષ."
    },
    {
        "id": "others-broken-cashewnuts-kaju-tukda-100g",
        "name": "Rich 'n' Spicy Broken Cashewnuts (Kaju Tukda)",
        "rel_path": "product images/others/dry fruits/broken cashewnuts.jpg",
        "fname": "broken cashewnuts.jpg",
        "gu": "કાજુ ટુકડા",
        "net_weight": 100,
        "tags": ["Others", "Dry Fruits", "Kaju Tukda", "Cashew Pieces", "Gravy Base"],
        "serves": "Gravy Thickener & Baking",
        "desc_en": "Creamy broken cashew pieces. Cost-effective and ideal for blending smooth restaurant shahi gravies, korma pastes, and halwa.",
        "desc_gu": "શાહી ગ્રેવીને ઘટ્ટ કરવા પીસવા માટે અને શીરો-લાડુમાં વાપરવા માટે શ્રેષ્ઠ કાજુ ટુકડા."
    },
    {
        "id": "others-whole-cashewnuts-akha-kaju-100g",
        "name": "Rich 'n' Spicy Whole Cashewnuts (Akha Kaju)",
        "rel_path": "product images/others/dry fruits/cashewnuts.jpg",
        "fname": "cashewnuts.jpg",
        "gu": "આખા કાજુ",
        "net_weight": 100,
        "tags": ["Others", "Dry Fruits", "Akha Kaju", "Whole Cashews", "Kaju Curry"],
        "serves": "Whole Nut Sauté & Snacking",
        "desc_en": "Jumbo whole white cashew nuts. Fry in golden ghee for kaju curry, biryani topping, and roasted salted cocktail snacks.",
        "desc_gu": "કાજુ કરી, બિરયાનીના ગાર્નિશિંગ અને ઘીમાં શેકીને ખાવા માટે પ્રીમિયમ આખા કાજુ."
    },
    {
        "id": "others-charoli-chironji-50g",
        "name": "Rich 'n' Spicy Charoli (Chironji Nuts)",
        "rel_path": "product images/others/dry fruits/charoli.jpg",
        "fname": "charoli.jpg",
        "gu": "ચારોળી",
        "net_weight": 50,
        "tags": ["Others", "Dry Fruits", "Charoli", "Chironji", "Basundi Garnish"],
        "serves": "Traditional Sweet Nut Garnish",
        "desc_en": "Tiny nutty seeds with an almond-like delicate crunch. The indispensable classic topping for Gujarati basundi, kheer, and halwa.",
        "desc_gu": "બાસુંદી, ખીર અને શીરાના પરંપરાગત ગાર્નિશિંગ માટે અનિવાર્ય ચારોળી."
    },
    {
        "id": "others-jardalu-apricots-100g",
        "name": "Rich 'n' Spicy Dried Apricots (Jardalu)",
        "rel_path": "product images/others/dry fruits/jardaalu.jpg",
        "fname": "jardaalu.jpg",
        "gu": "જરદાળુ",
        "net_weight": 100,
        "tags": ["Others", "Dry Fruits", "Jardalu", "Apricots", "Parsi Cuisine"],
        "serves": "Sweet & Tart Dried Fruit",
        "desc_en": "Sun-dried golden apricots. Key ingredient in authentic Parsi Jardalu Ma Gosht / Chicken, fruit jams, and luxury dessert platters.",
        "desc_gu": "પારસી જરદાળુ મા ગોસ્ત તેમજ મીઠાઈ અને ડેઝર્ટ માટે સ્વાદિષ્ટ સૂકા જરદાળુ."
    },
    {
        "id": "others-kharek-dry-dates-200g",
        "name": "Rich 'n' Spicy Dry Dates (Kharek)",
        "rel_path": "product images/others/dry fruits/kharek.jpg",
        "fname": "kharek.jpg",
        "gu": "ખારેક",
        "net_weight": 200,
        "tags": ["Others", "Dry Fruits", "Kharek", "Dry Dates", "Winter Pak"],
        "serves": "Nutritious Sweet Energy",
        "desc_en": "Hard dried dates packed with minerals. Ground or soaked for traditional winter health tonics (pak), milk infusions, and energy bites.",
        "desc_gu": "શિયાળાના પૌષ્ટિક પાક (અડદિયા, ખારેક પાક) અને દૂધ સાથે ઉકાળીને પીવા માટે શુદ્ધ ખારેક."
    },
    {
        "id": "others-pista-pistachios-100g",
        "name": "Rich 'n' Spicy Premium Pistachios (Pista)",
        "rel_path": "product images/others/dry fruits/pista.jpg",
        "fname": "pista.jpg",
        "gu": "પિસ્તા",
        "net_weight": 100,
        "tags": ["Others", "Dry Fruits", "Pista", "Pistachios", "Royal Garnish"],
        "serves": "Emerald Nut Slivers for Sweets",
        "desc_en": "Vibrant green nutty pistachios. Sliver thinly to crown royal Indian sweets, kulfi, rabdi, and saffron biryanis.",
        "desc_gu": "મીઠાઈ, કુલ્ફી, રબડી અને બિરયાની પર સુંદર લીલો રંગ અને ક્રંચ આપવા માટે પ્રીમિયમ પિસ્તા."
    },
    {
        "id": "others-raisins-kismis-100g",
        "name": "Rich 'n' Spicy Golden Raisins (Kismis)",
        "rel_path": "product images/others/dry fruits/raisins.jpg",
        "fname": "raisins.jpg",
        "gu": "કિસમિસ",
        "net_weight": 100,
        "tags": ["Others", "Dry Fruits", "Kismis", "Raisins", "Sweet Garnish"],
        "serves": "Golden Sweet Pops",
        "desc_en": "Juicy golden dried grapes. Add delightful sweet bursts into rice pulaos, kheer, halwa, and homemade tea cakes.",
        "desc_gu": "પુલાવ, ખીર, શીરો અને બેકિંગમાં કુદરતી મીઠાશ આપતી સોનેરી કિસમિસ."
    },

    # Essence (7)
    {
        "id": "others-hajoori-kesar-kom-big-20g",
        "name": "Hajoori Kesar Kom Essence (Large)",
        "rel_path": "product images/others/essence/hajoori kesar kom big.jpg",
        "fname": "hajoori kesar kom big.jpg",
        "gu": "હજુરી કેસર કોમ એસેન્સ",
        "net_weight": 20,
        "tags": ["Others", "Essence", "Kesar", "Hajoori", "Saffron Aroma"],
        "serves": "High-Concentrate Kesar Aroma (Drops)",
        "desc_en": "Famous Surat Hajoori brand saffron essence. A few drops infuse unforgettable royal saffron aroma into sweets, milkshakes, and biryani.",
        "desc_gu": "સુરતની વિખ્યાત હજુરી બ્રાન્ડનું કેસર એસેન્સ. માત્ર બે ટીપાં મીઠાઈ, શરબત અને બિરયાનીમાં કેસરની મહેક ફેલાવે છે."
    },
    {
        "id": "others-hajoori-kesar-essence-20g",
        "name": "Hajoori Premium Kesar Essence",
        "rel_path": "product images/others/essence/hajoori-flavours-and-fragrancs-kesar-essence-500x500 (1).jpg",
        "fname": "hajoori-flavours-and-fragrancs-kesar-essence-500x500 (1).jpg",
        "gu": "હજુરી કેસર એસેન્સ",
        "net_weight": 20,
        "tags": ["Others", "Essence", "Kesar", "Hajoori", "Flavours"],
        "serves": "Culinary Kesar Flavor (Drops)",
        "desc_en": "Authentic liquid kesar flavoring for milk, shrikhand, basundi, ice cream, and traditional confectionery.",
        "desc_gu": "શ્રીખંડ, બાસુંદી, આઈસ્ક્રીમ અને દૂધની બનાવટો માટે અધિકૃત હજુરી કેસર ફ્લેવર."
    },
    {
        "id": "others-mixed-fruit-essence-20g",
        "name": "Rich 'n' Spicy Mixed Fruit Culinary Essence",
        "rel_path": "product images/others/essence/mixed fruit.png",
        "fname": "mixed fruit.png",
        "gu": "મિક્સ્ડ ફ્રુટ એસેન્સ",
        "net_weight": 20,
        "tags": ["Others", "Essence", "Mixed Fruit", "Baking", "Mocktails"],
        "serves": "Tutti Frutti / Tutti Fruit Flavor",
        "desc_en": "Tropical fruit blend essence for bakery cakes, jellies, ice creams, candies, and fruit mocktails.",
        "desc_gu": "કેક, પેસ્ટ્રી, જેલી, આઈસ્ક્રીમ અને મોકટેલ માટે મિક્સ ફ્રૂટની મીઠી સુગંધ."
    },
    {
        "id": "others-pineapple-essence-20g",
        "name": "Rich 'n' Spicy Pineapple Culinary Essence",
        "rel_path": "product images/others/essence/pineapple.jpg",
        "fname": "pineapple.jpg",
        "gu": "પાઈનેપલ એસેન્સ",
        "net_weight": 20,
        "tags": ["Others", "Essence", "Pineapple", "Halwa", "Baking"],
        "serves": "Zesty Tropical Pineapple Aroma",
        "desc_en": "Bright tangy pineapple flavor drops for pineapple sheera, cakes, pastries, fruit punch, and shaved ice golas.",
        "desc_gu": "પાઈનેપલ શીરો, કેક, આઈસ ગોલા અને શરબત માટે પાઈનેપલ એસેન્સ."
    },
    {
        "id": "others-shahi-biryani-essence-20g",
        "name": "Rich 'n' Spicy Shahi Biryani Aromatic Essence",
        "rel_path": "product images/others/essence/shahi biryani.jpg",
        "fname": "shahi biryani.jpg",
        "gu": "શાહી બિરયાની એસેન્સ",
        "net_weight": 20,
        "tags": ["Others", "Essence", "Biryani Essence", "Mughlai", "Dum Cooking"],
        "serves": "Royal Biryani Finishing Drops",
        "desc_en": "Secret master blend of kewra, saffron, and sweet aromatic notes. Sprinkle 2-3 drops over layered dum biryani before sealing the handi.",
        "desc_gu": "દમ બિરયાનીની હાંડી સીલ કરતાં પહેલાં ૨-૩ ટીપાં છાંટી લગ્નપ્રસંગ જેવી શાહી મહેક લાવો."
    },
    {
        "id": "others-vanilla-essence-20g",
        "name": "Rich 'n' Spicy Pure Vanilla Essence",
        "rel_path": "product images/others/essence/vanilla essence.jpg",
        "fname": "vanilla essence.jpg",
        "gu": "વેનીલા એસેન્સ",
        "net_weight": 20,
        "tags": ["Others", "Essence", "Vanilla", "Baking", "Custard"],
        "serves": "Baking & Dessert Staple",
        "desc_en": "Warm, creamy vanilla flavor. Essential for homemade cakes, cookies, custards, pancakes, and ice creams.",
        "desc_gu": "કેક, બિસ્કિટ, કસ્ટર્ડ અને આઈસ્ક્રીમ બનાવવા માટે અનિવાર્ય વેનીલા એસેન્સ."
    },
    {
        "id": "others-white-rose-essence-20g",
        "name": "Rich 'n' Spicy White Rose Culinary Essence",
        "rel_path": "product images/others/essence/white rose.jpg",
        "fname": "white rose.jpg",
        "gu": "વ્હાઈટ રોઝ એસેન્સ",
        "net_weight": 20,
        "tags": ["Others", "Essence", "White Rose", "Aromatics", "Mithai"],
        "serves": "Delicate Floral Essence",
        "desc_en": "Concentrated white rose petal aroma. Enhances rasmalai, sandesh, chilled lassi, and aristocratic sweet recipes.",
        "desc_gu": "રસમલાઈ, સંદેશ, લસ્સી અને બંગાળી મીઠાઈઓ માટે નાજુક ગુલાબી સુગંધ આપતું વ્હાઈટ રોઝ એસેન્સ."
    },

    # Pasta (3)
    {
        "id": "others-fusilli-pasta-500g",
        "name": "Rich 'n' Spicy Durum Wheat Fusilli Pasta",
        "rel_path": "product images/others/pasta/fusilli-pasta.jpg",
        "fname": "fusilli-pasta.jpg",
        "gu": "ફ્યુસિલી પાસ્તા",
        "net_weight": 500,
        "tags": ["Others", "Pasta", "Fusilli", "Durum Wheat", "Italian"],
        "serves": "Spiral Pasta (4-5 Servings)",
        "desc_en": "100% durum wheat semolina spiral pasta. Deep grooves capture thick tomato, cheese, or pesto sauces perfectly.",
        "desc_gu": "૧૦૦% ડુરમ ઘઉંની સોજીમાંથી બનેલા સ્પ્રિંગ આકારના ફ્યુસિલી પાસ્તા. ક્રીમી કે રેડ સોસ સાથે પકાવવા માટે શ્રેષ્ઠ."
    },
    {
        "id": "others-penne-pasta-500g",
        "name": "Rich 'n' Spicy Durum Wheat Penne Rigate Pasta",
        "rel_path": "product images/others/pasta/penne pasta.jpg",
        "fname": "penne pasta.jpg",
        "gu": "પેને પાસ્તા",
        "net_weight": 500,
        "tags": ["Others", "Pasta", "Penne", "Arrabbiata", "Durum Wheat"],
        "serves": "Ridged Penne Pasta (4-5 Servings)",
        "desc_en": "Tubular diagonally-cut ridged penne pasta. Holds rich spicy arrabbiata, alfredo, and baked cheese sauces wonderfully.",
        "desc_gu": "ચીઝી વાઈટ સોસ અથવા તીખા રેડ એરાબિયાટા સોસ સાથે બનાવવા માટે રીજ્ડ પેને પાસ્તા."
    },
    {
        "id": "others-pipe-rigate-pasta-500g",
        "name": "Rich 'n' Spicy Durum Wheat Pipe Rigate Pasta",
        "rel_path": "product images/others/pasta/pipe rigate pasta.jpg",
        "fname": "pipe rigate pasta.jpg",
        "gu": "પાઈપ રીગાટે પાસ્તા",
        "net_weight": 500,
        "tags": ["Others", "Pasta", "Pipe Rigate", "Macaroni", "Durum Wheat"],
        "serves": "Curved Elbow Pasta (4-5 Servings)",
        "desc_en": "Snailshell curved pipe rigate pasta. The hollow shape fills delightfully with melted cheese sauces, soups, and pasta salads.",
        "desc_gu": "મેક એન્ડ ચીઝ, પાસ્તા સલાડ અને સૂપ માટે અંદર સોસ ભરાઈ જાય તેવા પાઈપ રીગાટે પાસ્તા."
    }
]

products = []
for item in others_items:
    p = {
        "id": item["id"],
        "name": item["name"],
        "brand": "Rich 'n' SP!CY",
        "category": "Others",
        "product_type": "Dry Marinade / Spice Mix",
        "tags": item["tags"],
        "regional_names": {
            "gu": item["gu"]
        },
        "net_weight": {
            "value": item["net_weight"],
            "unit": "g"
        },
        "pricing": {
            "mrp": None,
            "currency": "INR"
        },
        "packaging_type": "Standard Retail Sealed Pack",
        "dietary": {
            "is_vegetarian_mix": True,
            "suggested_protein": ["Snacks", "Bakery", "Desserts", "Italian", "Mughlai"]
        },
        "images": {
            "primary": item["rel_path"],
            "filename": item["fname"]
        },
        "recipe": {
            "serves_portion": item["serves"],
            "marination_time": "None",
            "cooking_methods": ["Seasoning", "Baking", "Boil", "Blend"],
            "required_ingredients": [
                f"{item['name']}",
                "Use as instructed for culinary dishes"
            ],
            "instructions": {
                "en": item["desc_en"],
                "gu": item["desc_gu"]
            }
        },
        "manufacturer": MANUFACTURER_DEFAULT
    }
    products.append(p)

others_catalog = {
    "category": "Others",
    "total_products": len(products),
    "generated_at": "2026-11-21",
    "brand": "Rich 'n' SP!CY",
    "manufacturer": MANUFACTURER_DEFAULT,
    "products": products
}

with open("others_products.json", "w", encoding="utf-8") as f:
    json.dump(others_catalog, f, indent=2, ensure_ascii=False)

print(f"Generated others_products.json with {len(products)} products.")
