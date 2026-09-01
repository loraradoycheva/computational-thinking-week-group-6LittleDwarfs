from datetime import date, datetime

DAYS_JA = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

def solution_station2(d):
    if isinstance(d, str):
        d = datetime.strptime(d, "%Y-%m-%d").date()
    return DAYS_JA[d.weekday()]


if __name__ == "__main__":
    user_date = input("Enter a date (YYYY-MM-DD): ")
    print(solution_station2(user_date))