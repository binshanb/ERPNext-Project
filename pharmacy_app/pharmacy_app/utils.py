import frappe


def ai_suggest_lead_time_for_item(item_code):
    """Placeholder AI helper. Uses a simple heuristic now, can be replaced with external API call (OpenAI) if enabled.

    Heuristic: average of Agency Item lead_time_days, fallback 7.
    """
    lead_times = frappe.db.get_all('Agency Item', filters={'item_code': item_code}, fields=['lead_time_days'])
    nums = [d.lead_time_days for d in lead_times if d.lead_time_days]
    if nums:
        return int(sum(nums) / len(nums))
    return 7
