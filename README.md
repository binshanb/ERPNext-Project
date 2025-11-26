📦 Pharmacy App for ERPNext

Agency Management & Manufacturer–Item Mapping

A custom ERPNext application designed for Pharmacy operations, focusing on:

✅ Agency (Distributor) Management
✅ Manufacturer → Item Mapping
✅ Improved item sourcing workflows
✅ Ease of tracking suppliers, manufacturers & item relationships

This project was developed as part of a technical interview task.

🚀 Features
1️⃣ Agency Management Module

Manage and track pharmacy agency/distributor details, including:

Agency name & contact details

License & registration details

Linked items & manufacturers

Status (Active/Inactive)

2️⃣ Manufacturer–Item Mapping

A dedicated module to define:

Manufacturer

Related Item

Item Code / Item Name

Strength / Dosage

Packaging

Active/Inactive status

This ensures accurate tracking of which manufacturer supplies each medicine.

📁 Module Structure
pharmacy_app/
│
├── pharmacy_app/
│   ├── config/
│   ├── modules.txt
│   ├── pharma_app/
│   │   ├── doctype/
│   │   │   ├── agency_management/
│   │   │   ├── manufacturer_mapping/
│   │   │   └── ...
│   ├── public/
│   ├── templates/
│   └── README.md
│
└── setup.py

🛠️ Installation (Local Development)
1. Create a Frappe/ERPNext Bench
bench init erpnext-bench --frappe-branch version-14
cd erpnext-bench
bench get-app erpnext --branch version-14
bench new-site mysite.local
bench --site mysite.local install-app erpnext

2. Get This Custom App
bench get-app pharmacy_app https://github.com/binshanb/ERPNext-Project.git

3. Install the App on Your Site
bench --site mysite.local install-app pharmacy_app

📌 Using the App

Once installed:

Go to ERPNext Desk → Modules → Pharmacy App

You will see:

✔ Agency Management

Create new agencies/distributors.

✔ Manufacturer Mapping

Define manufacturer linked to each item.

🧪 Running Bench / Dev Commands
Start development server
bench start

Clear cache (useful during development)
bench clear-cache
bench --site mysite.local migrate


📜 License

This project is licensed under the MIT License.

👤 Author

Binshan B S
Full-Stack Developer (Python / ERPNext / Frappe)
📧 binshanb77@gmail.com

