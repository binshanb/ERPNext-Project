frappe.listview_settings['Agency'] = {
    get_indicator: function(doc) {
        if (doc.is_active === 0 || doc.is_active === '0' || doc.is_active === false) {
            return [__('Inactive'), 'red', 'is_active,=,0'];
        }
        return [__('Active'), 'green', 'is_active,=,1'];
    }
};
