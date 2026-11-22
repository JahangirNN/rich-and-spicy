# generate_whole_spices.py
import json
import os

MANUFACTURER_DEFAULT = {
    "name": "City Gruh Udhyog",
    "address": "10/2573 City Masala Bhagatalao, opposite Hafiz Brothers, Surat-395003",
    "contact": "9898155726"
}

whole_spices_data = [
    {
        "id": "ws-ajino-moto-100g",
        "name": "Rich 'n' Spicy Ajinomoto (Monosodium Glutamate)",
        "fname": "ajino moto.jpg",
        "gu": "અજીનો મોટો",
        "net_weight": 100,
        "tags": ["Whole Spices", "Ajinomoto", "Umami", "Indo-Chinese", "Seasoning"],
        "serves": "Culinary Umami Seasoning (Pinch)",
        "desc_en": "Crystalline seasoning for Indo-Chinese fried rice, soups, gravies, and marinades, providing intense savory umami depth.",
        "desc_gu": "ઈન્ડો-ચાઈનીઝ ફ્રાઈડ રાઈસ, સૂપ, મંચુરિયન અને મરીનેશનમાં ઉમામી સ્વાદ આપવા માટે ચપટી વાપરો."
    },
    {
        "id": "ws-bay-leaves-tej-patta-50g",
        "name": "Rich 'n' Spicy Bay Leaves (Tej Patta)",
        "fname": "bay leaves.jpg",
        "gu": "તજ પત્તા",
        "net_weight": 50,
        "tags": ["Whole Spices", "Tej Patta", "Bay Leaves", "Khada Masala", "Aromatic"],
        "serves": "Whole Spice Infusion (1-2 leaves)",
        "desc_en": "Dried aromatic sweet laurel leaves. Lightly crackle in hot oil or ghee to infuse biryanis, pulaos, kormas, and gravies with herbal warmth.",
        "desc_gu": "બિરયાની, પુલાવ, કઢી અને દાળ-શાકના વઘારમાં ૧-૨ તમાલપત્ર સાંતળી મધુર સુગંધ મેળવો."
    },
    {
        "id": "ws-black-cardamom-badi-elaichi-50g",
        "name": "Rich 'n' Spicy Black Cardamom (Badi Elaichi)",
        "fname": "black cardamom.jpg",
        "gu": "મોટી ઈલાયચી",
        "net_weight": 50,
        "tags": ["Whole Spices", "Badi Elaichi", "Black Cardamom", "Smoky", "Khada Masala"],
        "serves": "Aromatic Pod Infusion (1-2 pods)",
        "desc_en": "Whole pods dried over open flames to produce bold camphoraceous, smoky aroma. Essential for slow-cooked meat gravies, dal makhani, and biryani.",
        "desc_gu": "ધીમી આંચે પકવાતી મટન, ચીકન ગ્રેવી, દાલ મખની અને શાહી બિરયાનીમાં સ્મોકી અને ઘેરી સુગંધ આપવા માટે ૧-૨ મોટી એલચી ઉમેરો."
    },
    {
        "id": "ws-black-cumin-kali-jeeri-50g",
        "name": "Rich 'n' Spicy Black Cumin Seeds (Kali Jeeri)",
        "fname": "black cumin seeds kali jeera.jpg",
        "gu": "કાળી જીરી",
        "net_weight": 50,
        "tags": ["Whole Spices", "Kali Jeeri", "Black Cumin", "Ayurvedic", "Digestive"],
        "serves": "Medicinal & Culinary Seeds",
        "desc_en": "Rare pungent black cumin seeds known for their potent Ayurvedic healing, detoxifying, and digestive properties. Ideal in specialized curries and herbal decoctions.",
        "desc_gu": "પાચન અને વજન નિયંત્રણ માટે આયુર્વેદમાં જાણીતી કાળી જીરી. ઉકાળા, ચૂર્ણ અને ખાસ મસાલા માટે ઉત્તમ."
    },
    {
        "id": "ws-green-cardamom-elaichi-50g",
        "name": "Rich 'n' Spicy Green Cardamom (Hari Elaichi)",
        "fname": "cardamom.jpg",
        "gu": "લીલી ઈલાયચી",
        "net_weight": 50,
        "tags": ["Whole Spices", "Green Cardamom", "Elaichi", "Queen of Spices", "Dessert"],
        "serves": "Fragrant Pods & Seeds",
        "desc_en": "Plump aromatic green pods packed with essential oils. Crush pods into masala chai, royal curries, biryanis, halwa, kheer, and shrikhand.",
        "desc_gu": "મસાલા ચા, મીઠાઈ (શીરો, ખીર, શ્રીખંડ) અને શાહી ગ્રેવીમાં રાણી સમી અદ્ભુત સુગંધ આપતી પસંદગીની લીલી એલચી."
    },
    {
        "id": "ws-cinnamon-sticks-taj-50g",
        "name": "Rich 'n' Spicy Cinnamon Sticks (Taj)",
        "fname": "cinnamon stick.jpg",
        "gu": "તજ",
        "net_weight": 50,
        "tags": ["Whole Spices", "Cinnamon", "Taj", "Sweet Bark", "Khada Masala"],
        "serves": "Whole Bark Infusion (1-2 sticks)",
        "desc_en": "Naturally sweet, aromatic rolled tree bark. Crackle whole in ghee for fragrant pulao and meat curries, or powder into desserts and spiced tea.",
        "desc_gu": "પુલાવ, બિરયાની, મસાલા ચા અને ગ્રેવીના વઘારમાં ૧-૨ તજના ટુકડા ઉમેરી મીઠી સુગંધિત સ્વાદિષ્ટ મહેક આપો."
    },
    {
        "id": "ws-citric-acid-limbu-phool-100g",
        "name": "Rich 'n' Spicy Citric Acid (Limbu Phool)",
        "fname": "citric acid limbu phool.png",
        "gu": "લીંબુના ફૂલ",
        "net_weight": 100,
        "tags": ["Whole Spices", "Limbu Phool", "Citric Acid", "Khaman", "Preservative"],
        "serves": "Pure Sour Crystals (¼ - ½ tsp)",
        "desc_en": "Food-grade sour crystals essential for spongy Surati nylon khaman, dhokla, tart syrups, pickles, and beverages.",
        "desc_gu": "સુરતી નાયલોન ખમણ, ઢોકળાં, શરબત, અથાણાં અને ચટણીમાં સપ્રમાણ ખટાશ અને આથો લાવવા માટે લીંબુના ફૂલ વાપરો."
    },
    {
        "id": "ws-cloves-laving-50g",
        "name": "Rich 'n' Spicy Whole Cloves (Laving)",
        "fname": "Cloves.jpg",
        "gu": "લવિંગ",
        "net_weight": 50,
        "tags": ["Whole Spices", "Cloves", "Laving", "Warm Spice", "Khada Masala"],
        "serves": "Whole Flower Buds (3-4 pieces)",
        "desc_en": "Intensely aromatic dried flower buds bursting with eugenol. Essential in biryani tadkas, garam masala, chai, and dental health remedies.",
        "desc_gu": "બિરયાની, પુલાવ, ગરમ મસાલા અને મસાલા ચા માટે ઉત્તમ તીવ્ર સુગંધિત આખા લવિંગ."
    },
    {
        "id": "ws-coriander-seeds-akha-dhana-100g",
        "name": "Rich 'n' Spicy Whole Coriander Seeds (Akha Dhana)",
        "fname": "coriander seeds.jpg",
        "gu": "આખા ધાણા",
        "net_weight": 100,
        "tags": ["Whole Spices", "Coriander Seeds", "Akha Dhana", "Kadhai", "Samosa"],
        "serves": "Whole & Crushed Spice",
        "desc_en": "Crisp dried coriander seeds. Coarsely crush for kadhai paneer, samosa stuffings, kachori, and roasted spice masalas.",
        "desc_gu": "કડાઈ પનીર, સમોસા, કચોરીના મસાલા અને વઘાર માટે અધકચરા વાટીને વાપરવા માટે ઉત્તમ આખા ધાણા."
    },
    {
        "id": "ws-cumin-seeds-akha-jeera-100g",
        "name": "Rich 'n' Spicy Cumin Seeds (Akha Jeera)",
        "fname": "cumin-seed-jeera.jpg",
        "gu": "આખું જીરૂ",
        "net_weight": 100,
        "tags": ["Whole Spices", "Jeera", "Cumin Seeds", "Tadka Staple", "Pantry Essential"],
        "serves": "Daily Tempering (1 tsp per dish)",
        "desc_en": "Fragrant slender seeds that crackle in hot ghee to form the quintessential Indian culinary foundation. Essential for jeera rice, dals, and curries.",
        "desc_gu": "જીરા રાઈસ, દાળ-શાકના વઘાર અને રોજિંદી ભારતીય રસોઈનો સર્વોચ્ચ વઘાર મસાલો."
    },
    {
        "id": "ws-desiccated-coconut-kopra-chhin-100g",
        "name": "Rich 'n' Spicy Desiccated Coconut (Kopra Chhin)",
        "fname": "desiccated coconut.jpg",
        "gu": "કોપરા છીણ",
        "net_weight": 100,
        "tags": ["Whole Spices", "Desiccated Coconut", "Kopra Chhin", "Laddoo", "Garnish"],
        "serves": "Baking, Sweets & Gravy Thickener",
        "desc_en": "Finely grated, dried pure coconut meat. Ideal for rolling laddoos, thickening rich gravies, kormas, and garnishing Gujarati snacks like khandvi and patra.",
        "desc_gu": "ખાંડવી, પાત્રાના ગાર્નિશિંગ, નારિયેળના લાડુ, મીઠાઈ અને ગ્રેવીને ઘટ્ટ કરવા માટે શુદ્ધ કોપરા છીણ."
    },
    {
        "id": "ws-dhana-dal-roasted-100g",
        "name": "Rich 'n' Spicy Roasted Dhana Dal",
        "fname": "dhana dal.jpg",
        "gu": "ધાણાદાળ",
        "net_weight": 100,
        "tags": ["Whole Spices", "Dhana Dal", "Mukhwas", "Digestive", "After-Meal"],
        "serves": "Traditional Mukhwas Mouth Freshener",
        "desc_en": "Husked, roasted, and salted coriander seed kernels. The quintessential after-meal Indian digestive mouth freshener.",
        "desc_gu": "જમ્યા પછી મુખવાસ તરીકે મોં સાફ અને પાચન દુરસ્ત રાખતી પરંપરાગત શેકેલી ધાણાદાળ."
    },
    {
        "id": "ws-dry-boriya-red-chillies-100g",
        "name": "Rich 'n' Spicy Dry Boriya Red Chillies",
        "fname": "dry boriya red chillies.jpg",
        "gu": "ગોળ બોરીયા મરચાં",
        "net_weight": 100,
        "tags": ["Whole Spices", "Boriya Marcha", "Round Chillies", "Tadka", "Sambhar"],
        "serves": "Whole Chilli Tadka",
        "desc_en": "Round, berry-shaped dry red chillies with bold pungent flavor. Drop whole into hot oil for sambhar, rasam, kadhi, and dal tadkas.",
        "desc_gu": "દાળ, કઢી, સંભાર અને રસમના વઘાર માટે વિશિષ્ટ ગોળ બોરીયા લાલ મરચાં."
    },
    {
        "id": "ws-dry-red-chillies-akha-marcha-100g",
        "name": "Rich 'n' Spicy Dry Red Chillies (Akha Lal Marcha)",
        "fname": "dry chillies.jpg",
        "gu": "આખા લાલ મરચાં",
        "net_weight": 100,
        "tags": ["Whole Spices", "Akha Marcha", "Dry Chillies", "Tadka", "Pantry Essential"],
        "serves": "Whole Chilli Tempering",
        "desc_en": "Sun-dried long red chillies with glossy red skin. Fry whole in ghee or oil for curries, dal tadka, chutneys, and homemade spice pastes.",
        "desc_gu": "દાળ-શાકના વઘાર, અથાણાં અને ચટણી બનાવવા માટે ઉત્તમ ગુણવત્તાવાળા આખા લાલ સૂકાં મરચાં."
    },
    {
        "id": "ws-fennel-seeds-variyali-100g",
        "name": "Rich 'n' Spicy Fennel Seeds (Variyali)",
        "fname": "fennel-seeds-variyali-500x500.png",
        "gu": "વરિયાળી",
        "net_weight": 100,
        "tags": ["Whole Spices", "Fennel Seeds", "Variyali", "Saunf", "Cooling"],
        "serves": "Mukhwas & Spice Base",
        "desc_en": "Sweet, cooling, anise-flavored green fennel seeds. Widely used in Gujarati pickle masalas, kashmiri gravies, cooling summer sharbats, and after-meal mukhwas.",
        "desc_gu": "મુખવાસ, વરિયાળી શરબત, અથાણાંના મસાલા અને કાશ્મીરી વાનગીઓ માટે સુગંધિત મીઠી વરિયાળી."
    },
    {
        "id": "ws-grated-coconut-sukhu-kopru-100g",
        "name": "Rich 'n' Spicy Grated Dry Coconut (Sukhu Kopru)",
        "fname": "grated coconut.jpg",
        "gu": "સૂકું કોપરું",
        "net_weight": 100,
        "tags": ["Whole Spices", "Sukhu Kopru", "Grated Coconut", "Undhiyu", "Pantry Essential"],
        "serves": "Traditional Cooking & Sweets",
        "desc_en": "Coarsely grated dry coconut kernel. Vital component in traditional Surati undhiyu masala, muthiya, coconut laddoos, and coastal curries.",
        "desc_gu": "સુરતી ઊંધિયું, મુઠીયા, કોપરા પાક અને વઘાર માટે વિશિષ્ટ સ્વાદ આપતું સૂકું છીણેલું કોપરું."
    },
    {
        "id": "ws-kasuri-methi-50g",
        "name": "Rich 'n' Spicy Kasuri Methi (Dried Fenugreek Leaves)",
        "fname": "Kasuri-Methi.jpeg",
        "gu": "કસુરી મેથી",
        "net_weight": 50,
        "tags": ["Whole Spices", "Kasuri Methi", "Fenugreek Leaves", "Restaurant Secret", "Aromatic"],
        "serves": "Crushed Finishing Herb (1 tbsp)",
        "desc_en": "Sun-dried fragrant fenugreek leaves from Nagaur, Rajasthan. Rub between palms and sprinkle over butter chicken, paneer butter masala, and dal makhani for signature restaurant aroma.",
        "desc_gu": "પનીર બટર મસાલા, બટર ચીકન અને દાલ મખનીમાં રેસ્ટોરન્ટ જેવી અદ્ભુત સુગંધ લાવવા હથેળીથી મસળીને છેલ્લે કસુરી મેથી ઉમેરો."
    },
    {
        "id": "ws-kokum-amsul-100g",
        "name": "Rich 'n' Spicy Kokum (Amsul)",
        "fname": "kokum.jpg",
        "gu": "કોકમ",
        "net_weight": 100,
        "tags": ["Whole Spices", "Kokum", "Amsul", "Solkadhi", "Coastal Sour"],
        "serves": "Tangy Coastal Enhancer (3-4 pieces)",
        "desc_en": "Dark purple sun-dried rind of Garcinia indica. Infuses beautiful ruby-red color and pleasant fruity sourness into Gujarati dal, fish curries, and soothing solkadhi.",
        "desc_gu": "ગુજરાતી દાળ, ફિશ કરી અને સોલકઢીમાં કુદરતી ખટાશ અને ગુલાબી રંગ આપવા માટે ૩-૪ કોકમ ઉમેરો."
    },
    {
        "id": "ws-lotus-seed-phool-makhana-100g",
        "name": "Rich 'n' Spicy Lotus Seeds (Phool Makhana)",
        "fname": "lotus seed-makhana.jpg",
        "gu": "ફૂલ મખાના",
        "net_weight": 100,
        "tags": ["Whole Spices", "Phool Makhana", "Fox Nuts", "Fasting", "Superfood"],
        "serves": "Nutritious Roasted Snack & Curries",
        "desc_en": "Nutrient-dense popped lotus seeds (fox nuts). Roast in ghee with rock salt and black pepper for healthy snacks, or simmer in rich shahi makhana kaju curry and kheer.",
        "desc_gu": "ઘીમાં શેકીને વ્રત-ઉપવાસના પૌષ્ટિક નાસ્તા તરીકે તેમજ શાહી મખાના-કાજુની શાક અને ખીરમાં વાપરવા માટે ઉત્તમ."
    },
    {
        "id": "ws-mace-javantri-50g",
        "name": "Rich 'n' Spicy Whole Mace (Javantri)",
        "fname": "mace.jpg",
        "gu": "જાવંત્રી",
        "net_weight": 50,
        "tags": ["Whole Spices", "Mace", "Javantri", "Mughlai", "Biryani Spice"],
        "serves": "Royal Aromatic Blades",
        "desc_en": "Lacy crimson-golden outer aril of nutmeg. Delivers refined, sweet, floral and peppery notes into Mughlai biryanis, nihari, and shahi gravies.",
        "desc_gu": "શાહી બિરયાની, નિહારી અને મુગલાઈ વાનગીઓમાં નાજુક સુગંધ અને સોનેરી સ્વાદ ઉમેરવા માટે જાવંત્રી વાપરો."
    },
    {
        "id": "ws-fenugreek-seeds-methi-dana-100g",
        "name": "Rich 'n' Spicy Fenugreek Seeds (Methi Dana)",
        "fname": "Methi-Fenugreek-Seeds.jpg",
        "gu": "મેથી દાણા",
        "net_weight": 100,
        "tags": ["Whole Spices", "Methi Dana", "Fenugreek", "Pickle Tadka", "Digestive"],
        "serves": "Tempering & Pickle Base",
        "desc_en": "Golden bitter-sweet fenugreek seeds. Essential in South Indian sambhar tadkas, Gujarati kadhi, methi papad sabzi, and digestive winter remedies.",
        "desc_gu": "સંભાર, કઢી, મેથી-પાપડનું શાક અને અથાણાંના વઘાર માટે ગુણકારી પીળા મેથી દાણા."
    },
    {
        "id": "ws-mustard-dal-rai-kuria-100g",
        "name": "Rich 'n' Spicy Mustard Dal (Rai Kuria)",
        "fname": "mustard dal rai dal rai kuriya.jpeg",
        "gu": "રાઈના કુરિયા",
        "net_weight": 100,
        "tags": ["Whole Spices", "Rai Kuria", "Mustard Dal", "Pickle Staple", "Gujarati"],
        "serves": "Achar / Pickle Masala Base",
        "desc_en": "Split and dehusked yellow mustard seeds. The non-negotiable core ingredient of authentic Gujarati mango, chili, and lemon sambharo pickles.",
        "desc_gu": "ગુજરાતી અથાણાં (મેથીયા કેરી, અથાણાં મરચાં, રાયતા મરચાં) બનાવવાનો મુખ્ય આધારસ્તંભ."
    },
    {
        "id": "ws-mustard-seeds-rai-100g",
        "name": "Rich 'n' Spicy Whole Mustard Seeds (Rai)",
        "fname": "mustard seeds rai.jpg",
        "gu": "રાઈ",
        "net_weight": 100,
        "tags": ["Whole Spices", "Mustard Seeds", "Rai", "Tadka Essential", "Pantry Staple"],
        "serves": "Daily Tempering (1 tsp per dish)",
        "desc_en": "Tiny pungent dark mustard seeds. Crackle in hot oil to unlock nutty, peppery aroma for vegetable curries, dals, chutneys, and sambhar.",
        "desc_gu": "દાળ, શાક, કઢી અને ચટણીના વઘાર માટે તેલમાં ફૂટતી સુગંધિત કાળી રાઈ."
    },
    {
        "id": "ws-nigella-seeds-kalonji-50g",
        "name": "Rich 'n' Spicy Nigella Seeds (Kalonji)",
        "fname": "nigella seeds kalonji.jpg",
        "gu": "કાલોંજી",
        "net_weight": 50,
        "tags": ["Whole Spices", "Kalonji", "Nigella Seeds", "Naan", "Pickle Spice"],
        "serves": "Baking & Pickle Seasoning",
        "desc_en": "Matte-black tear-drop seeds featuring an herbal, slightly bitter, onion-oregano profile. Top on garlic naan, samosa dough, or add into pickles.",
        "desc_gu": "ગાર્લિક નાન, સમોસાના પડ, કચોરી અને અથાણાંમાં વિશિષ્ટ કાંદા જેવો સ્વાદ ઉમેરતી કાલોંજી."
    },
    {
        "id": "ws-whole-nutmeg-jaiphal-50g",
        "name": "Rich 'n' Spicy Whole Nutmeg (Jaiphal)",
        "fname": "nutmeg.jpeg",
        "gu": "જાયફળ",
        "net_weight": 50,
        "tags": ["Whole Spices", "Nutmeg", "Jaiphal", "Sweets", "Ayurvedic"],
        "serves": "Grated Whole Nut (Pinch)",
        "desc_en": "Whole aromatic nuts of Myristica fragrans. Grate freshly into basundi, shrikhand, biryani, and warm spiced milk for sweet calming comfort.",
        "desc_gu": "બાસુંદી, શ્રીખંડ, દૂધપાક, બિરયાની અને ગરમ દૂધમાં ચપટી છીણીને નાખવા માટે સુગંધિત આખું જાયફળ."
    },
    {
        "id": "ws-shah-jeera-black-cumin-50g",
        "name": "Rich 'n' Spicy Shah Jeera (Black Cumin)",
        "fname": "shah jeera -black cumin.jpg",
        "gu": "શાહ જીરૂ",
        "net_weight": 50,
        "tags": ["Whole Spices", "Shah Jeera", "Royal Cumin", "Biryani", "Korma"],
        "serves": "Royal Rice & Gravy Seasoning",
        "desc_en": "Slender dark seeds with a distinct sweet anise-like herbal aroma. The royal secret ingredient in Dum Biryanis, Khepsa rice, and Mutton Kormas.",
        "desc_gu": "શાહી દમ બિરયાની, ખેપ્સા રાઈસ અને મુગલાઈ કોરમામાં ખાસ સુગંધ ઉમેરતું શાહ જીરૂ."
    },
    {
        "id": "ws-peanuts-singdana-200g",
        "name": "Rich 'n' Spicy Raw Peanuts (Singdana)",
        "fname": "singh dana peanuts.jpg",
        "gu": "સીંગદાણા",
        "net_weight": 200,
        "tags": ["Whole Spices", "Singdana", "Peanuts", "Poha", "Fasting"],
        "serves": "Nutty Crunch & Gravy Base",
        "desc_en": "Premium raw groundnuts with red skin. Fry for crunchy poha, sabudana khichdi, Gujarati sweet-and-sour dal, or grind into rich nutty curries.",
        "desc_gu": "બટાકા પૌંઆ, સાબુદાણા ખીચડી, ગુજરાતી દાળ અને ગ્રેવી માટે પસંદગીના સ્વાદિષ્ટ કાચા સીંગદાણા."
    },
    {
        "id": "ws-star-anise-chakraphool-50g",
        "name": "Rich 'n' Spicy Star Anise (Chakraphool)",
        "fname": "star ainse.jpg",
        "gu": "ચક્રફૂલ",
        "net_weight": 50,
        "tags": ["Whole Spices", "Star Anise", "Chakraphool", "Biryani", "Khada Masala"],
        "serves": "Star Pod Infusion (1-2 stars)",
        "desc_en": "Eight-pointed star pods with sweet licorice-like aroma. Essential in boiling water for basmati biryani rice, Chinese master stocks, and nihari.",
        "desc_gu": "બિરયાનીના ચોખા ઉકાળતી વખતે અને મટન નિહારીમાં મીઠી લિકોરીસ સુગંધ આપવા માટે ૧-૨ ચક્રફૂલ ઉમેરો."
    },
    {
        "id": "ws-stone-flower-dagadphool-50g",
        "name": "Rich 'n' Spicy Stone Flower (Dagad Phool / Kalpasi)",
        "fname": "stone flower-dagadphool.jpg",
        "gu": "પથ્થર ફૂલ",
        "net_weight": 50,
        "tags": ["Whole Spices", "Dagad Phool", "Stone Flower", "Kalpasi", "Maharashtrian"],
        "serves": "Earthy Secret Spice",
        "desc_en": "Dried lichen species used in Maharashtrian Goda masala, Chettinad curries, and meat gravies to impart an intense earthy, woody musk.",
        "desc_gu": "ગોડા મસાલા, ચેટીનાડ કરી અને મટન ગ્રેવીમાં અનોખી જંગલી સોડમ અને સ્વાદ ઉમેરતું પથ્થર ફૂલ (દગડ ફૂલ)."
    },
    {
        "id": "ws-suva-seeds-dill-100g",
        "name": "Rich 'n' Spicy Dill Seeds (Suva Dana)",
        "fname": "suva seeds.jpg",
        "gu": "સુવા દાણા",
        "net_weight": 100,
        "tags": ["Whole Spices", "Suva Dana", "Dill Seeds", "Mukhwas", "Post-Natal"],
        "serves": "Digestive Mukhwas & Herb",
        "desc_en": "Crisp aromatic dill seeds renowned in Gujarati households for post-meal digestion, postnatal tonic foods, and roasted mukhwas blends.",
        "desc_gu": "જમ્યા પછી મુખવાસ માટે શેકીને ખાવા તેમજ સુવાવડી સ્ત્રીઓ માટે આયુર્વેદિક ગુણોથી ભરપૂર સુવા દાણા."
    },
    {
        "id": "ws-sesame-seeds-safed-tal-100g",
        "name": "Rich 'n' Spicy White Sesame Seeds (Safed Tal)",
        "fname": "tal sesame-seeds.jpg",
        "gu": "સફેદ તલ",
        "net_weight": 100,
        "tags": ["Whole Spices", "Sesame Seeds", "Safed Tal", "Makar Sankranti", "Tadka"],
        "serves": "Toasted Garnish & Tadka",
        "desc_en": "Clean white sesame seeds rich in healthy oils and calcium. Crackle in tadka for dhokla, muthiya, thepla, or make festive til chikki and laddoos.",
        "desc_gu": "ઢોકળાં, હાંડવો, થેપલાના વઘારમાં અને ઉત્તરાયણની તલસાંકળી-ચીક્કી માટે કેલ્શિયમથી ભરપૂર સફેદ તલ."
    },
    {
        "id": "ws-watermelon-seeds-magajtari-100g",
        "name": "Rich 'n' Spicy Watermelon Seeds (Magajtari)",
        "fname": "water melon seeds magajtari.jpg",
        "gu": "મગજતરી બી",
        "net_weight": 100,
        "tags": ["Whole Spices", "Magajtari", "Watermelon Seeds", "Shahi Gravy", "Thickener"],
        "serves": "Puree for Creamy Gravies",
        "desc_en": "Peeled white watermelon melon kernels. Soak and blend with cashews to form the silky, sweet, rich white foundation of Shahi Mughlai curries.",
        "desc_gu": "કાજુ સાથે પલાળીને પીસી શાહી પનીર, મલાઈ કોફતા અને મુગલાઈ ગ્રેવીને ક્રીમી ઘટ્ટ બનાવવા માટે મગજતરી બી."
    },
    {
        "id": "ws-white-pepper-safed-mari-50g",
        "name": "Rich 'n' Spicy White Pepper (Safed Mari)",
        "fname": "white pepper safed mari.jpg",
        "gu": "સફેદ મરી",
        "net_weight": 50,
        "tags": ["Whole Spices", "White Pepper", "Safed Mari", "White Sauce", "Subtle Heat"],
        "serves": "Subtle Pungent Seasoning",
        "desc_en": "Dehusked ripe peppercorns delivering clean heat and earthy bite without dark specks. Essential for white gravies, cream soups, and mayonnaise.",
        "desc_gu": "વ્હાઈટ ચીકન/મટન ગ્રેવી, ક્રીમ સૂપ અને સફેદ સોસમાં કાળા ડાઘા વગર તીખાશ આપવા માટે સફેદ મરી વાપરો."
    }
]

products = []
for item in whole_spices_data:
    p = {
        "id": item["id"],
        "name": item["name"],
        "brand": "Rich 'n' SP!CY",
        "category": "Whole Spices",
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
            "suggested_protein": ["All Indian Curries", "Vegetables", "Rice", "Biryani"]
        },
        "images": {
            "primary": f"product images/whole spices/{item['fname']}",
            "filename": item["fname"]
        },
        "recipe": {
            "serves_portion": item["serves"],
            "marination_time": "None",
            "cooking_methods": ["Tadka / Tempering", "Roast & Grind", "Infusion"],
            "required_ingredients": [
                f"Whole {item['name']}",
                "Hot cooking oil or desi ghee for tempering"
            ],
            "instructions": {
                "en": item["desc_en"],
                "gu": item["desc_gu"]
            }
        },
        "manufacturer": MANUFACTURER_DEFAULT
    }
    products.append(p)

whole_spices_catalog = {
    "category": "Whole Spices",
    "total_products": len(products),
    "generated_at": "2026-11-21",
    "brand": "Rich 'n' SP!CY",
    "manufacturer": MANUFACTURER_DEFAULT,
    "products": products
}

with open("whole_spices_products.json", "w", encoding="utf-8") as f:
    json.dump(whole_spices_catalog, f, indent=2, ensure_ascii=False)

print(f"Generated whole_spices_products.json with {len(products)} products.")
