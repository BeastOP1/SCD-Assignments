from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

HRA_RATE = Decimal("0.10")
PF_RATE = Decimal("0.05")
OVERTIME_MULTIPLIER = Decimal("1.5")
HOURS_PER_MONTH = Decimal("160")
TAX_SLABS = [  # (annual upper limit, rate)
    (Decimal("600000"), Decimal("0")),
    (Decimal("1200000"), Decimal("0.05")),
    (None, Decimal("0.15")),
]


def money(x) -> Decimal:
    return Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass
class Employee:
    name: str
    base_salary: Decimal
    overtime_hours: Decimal = Decimal("0")
    bonus: Decimal = Decimal("0")
    is_active: bool = True
    months_in_service: int = 0
    performance_score: float = 0
    disciplinary_actions: int = 0
    attendance_rate: float = 0  # 0 to 1

    def is_active_employee(self) -> bool:
        return self.is_active

    def has_enough_service(self) -> bool:
        return self.months_in_service >= 12

    def has_good_performance(self) -> bool:
        return self.performance_score >= 3.0

    def has_disciplinary_actions(self) -> bool:
        return self.disciplinary_actions > 0

    def has_good_attendance(self) -> bool:
        return self.attendance_rate >= 0.90



def is_bonus_eligible(emp: Employee) -> bool:
    if not emp.is_active_employee():
        return False
    if not emp.has_enough_service():
        return False
    if not emp.has_good_performance():
        return False
    if emp.has_disciplinary_actions():
        return False
    if not emp.has_good_attendance():
        return False
    return True


def nested_bonus_rule(emp: Employee) -> bool:
    if emp.is_active_employee():
        if emp.has_enough_service():
            if emp.has_good_performance():
                if not emp.has_disciplinary_actions():
                    if emp.has_good_attendance():
                        return True
    return False


def monthly_tax(gross: Decimal) -> Decimal:
    annual, tax, lower = gross * 12, Decimal("0"), Decimal("0")
    for upper, rate in TAX_SLABS:
        if annual <= lower:
            break
        top = annual if upper is None else min(annual, upper)
        tax += (top - lower) * rate
        if upper is None:
            break
        lower = upper
    return money(tax / 12)


def calculate_salary(emp: Employee) -> dict:
    if emp.base_salary < 0:
        raise ValueError("base_salary negative nahi ho sakti")

    hra = money(emp.base_salary * HRA_RATE)
    overtime = money(emp.base_salary / HOURS_PER_MONTH * emp.overtime_hours * OVERTIME_MULTIPLIER)
    bonus = money(emp.bonus) if is_bonus_eligible(emp) else Decimal("0.00")

    gross = money(emp.base_salary) + hra + overtime + bonus
    pf = money(emp.base_salary * PF_RATE)
    tax = monthly_tax(gross)

    return {
        "gross": gross,
        "pf": pf,
        "tax": tax,
        "net": gross - pf - tax,
        "bonus_paid": bonus,
    }


if __name__ == "__main__":
    good = Employee(
        "Ali", Decimal("100000"), overtime_hours=Decimal("8"), bonus=Decimal("5000"),
        months_in_service=24, performance_score=4.2, attendance_rate=0.96,
    )
    for key, value in calculate_salary(good).items():
        print(f"{key:<10}{value:>12,.2f}")

    flagged = Employee("Sara", Decimal("90000"), bonus=Decimal("5000"), months_in_service=24,
                       performance_score=4.0, attendance_rate=0.95, disciplinary_actions=1)
    for e in (good, flagged):
        print(e.name, "| guard:", is_bonus_eligible(e), "| nested:", nested_bonus_rule(e))