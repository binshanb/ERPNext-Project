import frappe


def setup_demo():
    """Create demo Manufacturer, Items, Agency and Manufacturer Items for quick presentation/demo. Idempotent.
    Run with: bench --site mysite.local execute pharmacy_app.pharmacy_app.scripts.demo_setup.setup_demo
    """
    # Create items if not exists
    def create_item(item_code, item_name=None):
        if not frappe.db.exists('Item', item_code):
            frappe.get_doc({'doctype': 'Item', 'item_code': item_code, 'item_name': item_name or item_code}).insert(ignore_permissions=True)

    create_item('ITEM-001', 'Painkiller 10mg')
    create_item('ITEM-002', 'Antibiotic 250mg')

    # Create manufacturer
    man_name = 'Acme Pharma'
    if not frappe.db.exists('Manufacturer', man_name):
        frappe.get_doc({'doctype': 'Manufacturer', 'manufacturer_name': man_name, 'gln': '12345', 'is_blocked': 0}).insert(ignore_permissions=True)

    # Add manufacturer items
    mi_exist = frappe.db.get_all('Manufacturer Item', filters={'manufacturer': man_name}, fields=['item_code'])
    existing_items = [d.item_code for d in mi_exist]
    if 'ITEM-001' not in existing_items:
        frappe.get_doc({'doctype': 'Manufacturer Item', 'manufacturer': man_name, 'item_code': 'ITEM-001', 'part_number': 'ACME-001', 'gtin': '0001'}).insert(ignore_permissions=True)
    if 'ITEM-002' not in existing_items:
        frappe.get_doc({'doctype': 'Manufacturer Item', 'manufacturer': man_name, 'item_code': 'ITEM-002', 'part_number': 'ACME-002', 'gtin': '0002'}).insert(ignore_permissions=True)

    # Create an Agency and agency items
    agency_name = 'Health Supplies'
    if not frappe.db.exists('Agency', agency_name):
        agency = frappe.get_doc({'doctype': 'Agency', 'agency_name': agency_name, 'territory': '', 'is_active': 1}).insert(ignore_permissions=True)
    else:
        agency = frappe.get_doc('Agency', agency_name)

    # Add agency items
    existing_ag_items = [r.item_code for r in agency.get('agency_items') or []]
    if 'ITEM-001' not in existing_ag_items:
        agency.append('agency_items', {'item_code': 'ITEM-001', 'min_order_qty': 10, 'lead_time_days': 5})
    if 'ITEM-002' not in existing_ag_items:
        agency.append('agency_items', {'item_code': 'ITEM-002', 'min_order_qty': 20, 'lead_time_days': 7})
    agency.save(ignore_permissions=True)

    frappe.db.commit()
    frappe.msgprint('Demo setup completed')
