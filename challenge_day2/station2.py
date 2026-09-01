<<<<<<< HEAD
from datetime import date, datetime

DAYS_JA = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

def solution_station2(d):
    if isinstance(d, str):
        d = datetime.strptime(d, "%Y-%m-%d").date()
    return DAYS_JA[d.weekday()]

print(solution_station2("2024-10-12"))   
print(solution_station2(date.today()))
=======
def solution_station2():
>>>>>>> 48d8dc7c1135096c96abad1634b20296ce1e2e43
