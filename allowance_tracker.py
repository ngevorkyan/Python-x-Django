from functools import reduce

def get_weekly_allowances(num_weeks):
    allowances = []
    for i in range(1, num_weeks + 1):
        amount = float(input(f"Week {i} allowance: "))
        allowances.append(amount)
    return allowances


def add_bonuses(allowances, bonus):
    return list(map(lambda x: x + bonus, allowances))


def calculate_total(amounts):
    return reduce(lambda a, b: a + b, amounts)


def calculate_average(amounts):
    total = reduce(lambda a, b: a + b, amounts)
    return total / len(amounts)


def find_good_weeks(amounts, threshold):
    week_numbers = range(1, len(amounts) + 1)
    return [(i, amt) for i, amt in zip(week_numbers, amounts) if amt > threshold]


def display_results(original, with_bonus, bonus, total, average, good_weeks, best_week):
    print("\n--- ALLOWANCE SUMMARY ---\n")
    print("Weekly Earnings:")
    for i, (orig, total_amt) in enumerate(zip(original, with_bonus), start=1):
        if bonus > 0:
            print(f"  Week {i}: ${orig:.2f} + ${bonus:.2f} bonus = ${total_amt:.2f}")
        else:
            print(f"  Week {i}: ${orig:.2f}")

    print(f"\nTotal Earned: ${total:.2f}")
    print(f"Average Per Week: ${average:.2f}\n")

    print("Good Weeks (above $12): ")
    for week, amt in good_weeks:
        print(f"  Week {week}: ${amt:.2f}")

    print(f"\nBest Week: Week {best_week[0]} with ${best_week[1]:.2f}!")


# პიცის პროექტში არასწორად მქონდა მეინი გამოყენებული, მგონი ახლა სწორად ვაკეთებ
def main():
    print("ALLOWANCE TRACKER\n")

    num_weeks = int(input("How many weeks to track? "))
    allowances = get_weekly_allowances(num_weeks)

    bonus_choice = input("\nAdd bonus? (yes/no): ").strip().lower()
    bonus = 0
    if bonus_choice == "yes":
        bonus = float(input("Bonus amount per week: "))

    with_bonus = add_bonuses(allowances, bonus)
    total = calculate_total(with_bonus)
    average = calculate_average(with_bonus)
    threshold = 12
    good_weeks = find_good_weeks(with_bonus, threshold)

    week_numbers = range(1, len(with_bonus) + 1)
    best_week = max(zip(week_numbers, with_bonus), key=lambda x: x[1])

    display_results(allowances, with_bonus, bonus, total, average, good_weeks, best_week)


if __name__ == "__main__":
    main()
