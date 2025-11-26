import frappe


def execute(filters=None):
    columns = [
        ("Manufacturer:Link/Manufacturer:200"),
        ("Item:Link/Item:200"),
        ("Part Number:Data:150"),
        ("GTIN:Data:150")
    ]

    data = frappe.db.sql(
        """
        select m.name as manufacturer, mi.item_code, mi.part_number, mi.gtin
        from `tabManufacturer Item` mi
        join `tabManufacturer` m on mi.manufacturer = m.name
        where ifnull(m.is_blocked, 0) = 0
        """,
        as_dict=True
    )
    rows = []
    for d in data:
        rows.append([d.manufacturer, d.item_code, d.part_number, d.gtin])
    return columns, rows
