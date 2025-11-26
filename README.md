# Pharmacy App

A custom ERPNext app with two modules: **Agency Management** and **Manufacturer–Item Mapping**.

[![ERPNext](https://img.shields.io/badge/ERPNext-14.x-blue)](https://erpnext.com)
[![Frappe](https://img.shields.io/badge/Frappe-14.x-orange)](https://frappeframework.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## **Modules**

### 1. Agency Management

- **DocTypes**

  - `Agency`: `agency_name`, `territory`, `primary_contact`, `is_active`
  - `Agency Item` (child table): `item_code`, `min_order_qty`, `lead_time_days`

- **Features**

  - Prevent deactivating an Agency if it has linked items
  - Button **Create Supplier** to generate a Supplier from an Agency
  - Inactive Agencies display in red on list view
- **Report:** Agency Lead Times (Agency, Item, Min Order Qty, Lead Time)

### 2. Manufacturer–Item Mapping

- **DocTypes**

  - `Manufacturer`: `manufacturer_name`, `gln`, `is_blocked`
  - `Manufacturer Item`: `manufacturer`, `item_code`, `part_number`, `gtin`

- **Features**

  - Block adding Manufacturer Items if Manufacturer is marked blocked
  - Ensure `(manufacturer, item_code)` pair is unique
  - Auto-fill `part_number` if left blank
- **REST API:** Return all manufacturer mappings for a given `item_code`
- **Report:** Items by Manufacturer

---

## **Installation**

1. Get this app :

```bash
bench get-app pharmacy_app https://github.com/binshanb/ERPNext-Project.git


Create a new site:


bench new-site mysite.local


Install the app:

bench --site mysite.local install-app pharmacy_app

Start the server:

bench start
Sample Data / Fixtures
Included in the fixtures/ folder:

2 Agencies

3 Items

2 Manufacturers

Testing
Run unit tests:

bench --site mysite.local run-tests --app pharmacy_app

Documentation

DocTypes and validation logic inside pharmacy_app/pharmacy_app/doctype/

Custom reports inside pharmacy_app/pharmacy_app/report/

REST API endpoints inside pharmacy_app/pharmacy_app/api.py

AI Usage documented in AI_USAGE_LOG.md

