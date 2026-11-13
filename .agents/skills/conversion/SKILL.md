---
name: conversion
description: >-
  Converts folders of product packaging images and companion recipe documents into
  standardized e-commerce JSON catalogs with bilingual details, dietary specs, and random sample validation.
---

# Conversion Skill: Product Image Folders to Structured E-Commerce Data

Use this skill to convert folders containing product packaging photos, recipe documents, and spice mix labels into structured, e-commerce-ready JSON datasets.

---

## Workflow Overview

```
Folder with Product Images + Recipe Docx
                 │
                 ▼
  [1] Inventory & Format Discovery
                 │
                 ▼
  [2] Visual Inspection & OCR / Label Reading
                 │
                 ▼
  [3] Cross-Reference Digital Writeup (Docx)
                 │
                 ▼
  [4] Assemble Standardized JSON (schema.json)
                 │
                 ▼
  [5] Random Sample Quality Verification (verify_catalog.py)
```

---

## Step-by-Step Procedure

### 1. Inventory & Asset Discovery
1. List all image files in the target category folder (e.g., `product images/<CATEGORY>/`).
2. Identify supported formats (`.jpg`, `.jpeg`, `.png`, etc.).
3. Check for accompanying documentation (e.g., `product images/website writeup - Copy.docx`) containing digital recipe texts, exact measurements, and marketing copy.

### 2. Label Inspection & Packaging Classification
Analyze each image to identify packaging structure:
* **Format A: Transparent Label Pouch**
  * Clear window bag with a full-face label sticker.
  * Contains printed manufacturer info (*City Gruh Udhyog*), contact, address, explicit Net Weight (e.g., 40g, 50g, 60g), English dish name, Gujarati script, and complete marinade recipes.
* **Format B: Printed Instant Mix Pouch**
  * Red-bordered branded pouch with yellow label banners.
  * Contains trademark logo (`Rich 'n' SP!CY`), `Instant Mix`, dietary indicator (green vegetarian dot), English title, Gujarati vernacular title, and spice window.
* **Format C: Specialty Packaging**
  * Custom shaped windows (e.g., shield cutout on Lemon Chicken) or dual-compartment packs (e.g., Machhi-Chicken with coconut + spice mix).

### 3. Data Field Extraction Standard
For each product, capture:
* **Identification:**
  * `id`: URL-safe kebab-case slug (e.g., `bbq-banjara-tikka-40g`).
  * `name`: Formal English title (e.g., `Rich 'n' Spicy Banjara Tikka Masala`).
  * `brand`: Brand name (`Rich 'n' SP!CY`).
  * `category`: Category name (`Barbecue`, `Biryani`, `Gravy`, etc.).
  * `product_type`: `Instant Mix` or `Dry Marinade / Spice Mix`.
  * `tags`: Descriptive keywords for searching and filtering.
* **Multilingual:**
  * `regional_names.gu`: Verified Gujarati script title (e.g., `બંજારા ટીક્કા`).
* **Specs:**
  * `net_weight`: Object with `value` (number) and `unit` (`g` or `kg`).
  * `pricing`: `{"mrp": null, "currency": "INR"}` (ready for pricing update).
  * `packaging_type`: Human-readable packaging description.
  * `dietary`: `is_vegetarian_mix` (boolean), `suggested_protein` (array).
* **Media:**
  * `images.primary`: Relative path to image file.
  * `images.filename`: Base file name.
* **Recipe & Instructions:**
  * `serves_portion`: Target quantity (e.g., `500g Chicken / Paneer`).
  * `marination_time`: Required resting time (e.g., `1 hour`).
  * `cooking_methods`: Array of techniques (`Pan Fry`, `Barbecue`, `Oven Roast`).
  * `required_ingredients`: Full list of additional pantry ingredients needed.
  * `instructions.en`: Complete preparation instructions in English.
  * `instructions.gu`: Complete preparation instructions in Gujarati.
* **Manufacturer:**
  * Name, registered address, and customer contact number.

### 4. JSON Generation
Validate the assembled structure against the schema located at:
[schema.json](./resources/schema.json)

Save output to `<category_slug>_products.json` in the root workspace.

### 5. Verification & Random Sampling
Run the verification script to confirm image path validity and check 5 random samples:
```powershell
python .agents/skills/conversion/scripts/verify_catalog.py <output_file.json>
```

Perform side-by-side verification:
1. Verify English title matches image.
2. Verify Gujarati script matches image.
3. Verify net weight matches image label.
4. Verify recipe instructions match image label text.
