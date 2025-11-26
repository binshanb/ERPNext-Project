frappe.ui.form.on('Manufacturer', {
    validate: function(frm) {
        // If manufacturer is blocked, prevent saving if manufacturer items present
        if (frm.doc.is_blocked && frm.doc.manufacturer_items && frm.doc.manufacturer_items.length) {
            frappe.throw('Cannot keep Manufacturer blocked while it has Manufacturer Items. Remove them first.');
        }
    }
});

frappe.ui.form.on('Manufacturer Item', {
    item_code: function(frm, cdt, cdn) {
        let row = frappe.get_doc(cdt, cdn);
        // Auto-fill part_number with item_code when empty
        if (!row.part_number && row.item_code) {
            frappe.model.set_value(cdt, cdn, 'part_number', row.item_code)
        }
        // Check manufacturer blocked state client-side
        if (frm.doc.is_blocked) {
            frappe.msgprint('Cannot add Manufacturer Item because Manufacturer is marked blocked.');
            // Clear the row
            frappe.model.set_value(cdt, cdn, 'item_code', '');
        }
    }
});
