import frappe


@frappe.whitelist()
def create_supplier_from_agency(agency_name):
    """Create a Supplier from Agency docname"""
    if not agency_name:
        frappe.throw('agency_name is required')
    agency = frappe.get_doc('Agency', agency_name)
    supplier_name = agency.agency_name
    exists = frappe.db.exists('Supplier', supplier_name)
    if exists:
        return {'status': 'exists', 'message': f'Supplier {supplier_name} already exists.'}
    supplier = frappe.get_doc({
        'doctype': 'Supplier',
        'supplier_name': supplier_name,
        'disabled': 0
    })
    supplier.insert(ignore_permissions=True)
    return {'status': 'created', 'supplier': supplier.name}


@frappe.whitelist()
def get_manufacturer_mappings(item_code):
    """Return all Manufacturer Item mappings for a given item_code"""
    if not item_code:
        frappe.throw('item_code is required')
    mappings = frappe.db.get_all('Manufacturer Item', filters={'item_code': item_code}, fields=['manufacturer', 'part_number', 'gtin'])
    return mappings


@frappe.whitelist()
def suggest_lead_time(agency_name, item_code):
    """Wrapper to call Agency.suggest_lead_time from client side (frappe.call)"""
    agency = frappe.get_doc('Agency', agency_name)
    return agency.suggest_lead_time(item_code)

