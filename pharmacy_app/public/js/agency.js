frappe.ui.form.on('Agency', {
    refresh: function(frm) {
        if (!frm.doc.__islocal) {
            frm.add_custom_button('Create Supplier', function() {
                frappe.call({
                    method: 'pharmacy_app.pharmacy_app.pharmacy_app.api.create_supplier_from_agency',
                    args: { 'agency_name': frm.doc.name },
                    callback: function(r) {
                        if (r.message) {
                            if (r.message.status === 'created') {
                                frappe.msgprint('Supplier created: ' + r.message.supplier);
                            } else {
                                frappe.msgprint(r.message.message || JSON.stringify(r.message));
                            }
                        }
                    }
                });
            });
            frm.add_custom_button('Suggest Lead Time', function() {
                let item_code = frm.get_field('agency_items').grid.get_selected_children()[0]?.item_code;
                if (!item_code) {
                    frappe.msgprint('Please select an Agency Item first in the table.');
                    return;
                }
                frappe.call({
                    method: 'pharmacy_app.pharmacy_app.pharmacy_app.api.suggest_lead_time',
                    args: { 'agency_name': frm.doc.name, 'item_code': item_code },
                    callback: function(r) {
                        if (r.message) {
                            frappe.msgprint('Suggested Lead Time (days): ' + r.message);
                        }
                    }
                });
            });
        }
    }
});
