def calculate_sum_of_bonus(data):
    # Bonus Rule: 以 performance 為基準來計算獎金 % 數，above average = 10%，average = 5%，below average ＝ 3%
    # 每一位可以得到的獎金為自身的 salary * 獎金 % 數

    # 遍歷每位員工的資料，將薪水處理成整數，根據 performance 計算該員的獎金
    sum_bonus = 0
    for employee in data["employees"]:
        sum_bonus += salary_convert_to_int(employee["salary"]) * get_bonus_percent(employee["performance"])

    print(sum_bonus)


def salary_convert_to_int(salary):
    exchange_rate = 30
    if not isinstance(salary, int):
        replace_str = salary.replace(",", "").replace("USD", "")
        result = int(replace_str, 10)
        if "USD" in salary:
            result *= exchange_rate
        return result
    else:
        return salary


def get_bonus_percent(performance):
    if performance == "above average":
        return 0.1
    elif performance == "average":
        return 0.05
    elif performance == "below average":
        return 0.03
    else:
        return 1


calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})