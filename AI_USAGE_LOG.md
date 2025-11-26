
---

## **AI_USAGE_LOG.md**

```markdown
# AI Usage Log

This document summarizes how AI-assisted the development of the **Pharmacy App** for ERPNext.

---

## **1. DocType Design & Validations**
- Designed **Agency**, **Agency Item**, **Manufacturer**, and **Manufacturer Item** DocTypes
- Applied validation rules:
  - Prevent deactivating Agencies with linked items
  - Block adding Manufacturer Items if the manufacturer is marked as blocked
  - Ensure unique `(manufacturer, item_code)` pairs
  - Auto-fill `part_number` if left blank

---

## **2. Reports**
- Generated **Agency Lead Times** report:
  - Displays agency, item, minimum order quantity, lead time
- Generated **Items by Manufacturer** report:
  - Shows all items linked to manufacturers

---

## **3. REST API**
- Created API endpoint to fetch all manufacturer mappings for a given `item_code`
- Ensured proper access and data formatting

---

## **4. Workflow & Buttons**
- Added **Create Supplier** button on Agency DocType
- Integrated logic to auto-generate Supplier records from Agency records

---

## **5. Testing**
- Suggested and structured unit tests for DocTypes, validations, and API
- Ensured all tests pass using ERPNext/Frappe testing framework

---

## **6. Documentation**
- Assisted in drafting README.md
- Structured setup instructions, module descriptions, and testing guidance

-----------------------------------------------------------------------------
