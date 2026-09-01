from datetime import date, datetime

DAYS_JA = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

def weekday_ja(d):
    if isinstance(d, str):
        d = datetime.strptime(d, "%Y-%m-%d").date()
    return DAYS_JA[d.weekday()]

print(weekday_ja("2024-10-12"))   
print(weekday_ja(date.today()))