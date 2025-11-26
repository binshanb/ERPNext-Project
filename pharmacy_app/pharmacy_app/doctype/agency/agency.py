import frappe
from frappe.model.document import Document


class Agency(Document):
    def validate(self):
        # Prevent deactivating Agency if it has linked items
        if not self.is_active:
            if self.get('agency_items'):
                if len(self.agency_items) > 0:
                    frappe.throw("Cannot deactivate Agency with linked items. Remove items first.")

    @frappe.whitelist()
    def create_supplier(self):
        """Create a Supplier from Agency data"""
        # Check if Supplier already exists with same name
        supplier_name = self.agency_name
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
    def suggest_lead_time(self, item_code):
        """Use the ai helper to suggest a lead time (pluggable to external AI services)
        Currently uses a simple heuristic.
        """
        from pharmacy_app.pharmacy_app.pharmacy_app.utils import ai_suggest_lead_time_for_item
        return ai_suggest_lead_time_for_item(item_code)
