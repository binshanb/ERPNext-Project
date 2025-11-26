import frappe


def execute(filters=None):
    columns = [
        ("Agency:Link/Agency:200"),
        ("Item:Link/Item:200"),
        ("Min Order Qty:Float:120"),
        ("Lead Time (Days):Int:120")
    ]

    data = frappe.db.sql(
        """
        select ag.name as agency, ai.item_code, ai.min_order_qty, ai.lead_time_days
        from `tabAgency Item` ai
        join `tabAgency` ag on ai.parent = ag.name
        where ifnull(ag.disabled, 0) = 0
        """,
        as_dict=True
    )
    rows = []
    for d in data:
        rows.append([d.agency, d.item_code, d.min_order_qty, d.lead_time_days])
    return columns, rows
