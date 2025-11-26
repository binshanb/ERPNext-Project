import frappe
from frappe.model.document import Document


class ManufacturerItem(Document):
    def validate(self):
        # Block adding manufacturer items if manufacturer is blocked
        if self.manufacturer:
            is_blocked = frappe.db.get_value('Manufacturer', self.manufacturer, 'is_blocked')
            if is_blocked:
                frappe.throw(f"Cannot add Manufacturer Item because Manufacturer '{self.manufacturer}' is blocked.")

        # Unique (manufacturer, item_code) pair
        if self.manufacturer and self.item_code:
            existing = frappe.db.exists('Manufacturer Item', {
                'manufacturer': self.manufacturer,
                'item_code': self.item_code
            })
            if existing and existing != self.name:
                frappe.throw('Manufacturer & Item pair must be unique.')

        # Auto-fill part_number with item_code if empty
        if not self.part_number and self.item_code:
            self.part_number = self.item_code
