import frappe
from frappe.model.document import Document


class Manufacturer(Document):
    def validate(self):
        # Prevent blocking a Manufacturer if it has Manufacturer Items
        if self.is_blocked and self.get('manufacturer_items'):
            if len(self.manufacturer_items) > 0:
                frappe.throw('Cannot block Manufacturer while it has Manufacturer Items. Remove them first.')
