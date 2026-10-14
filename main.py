
from project_utils import (
    show_project_info,
    safe_calculate_weekly_hours,
)


def main():
    print("Project Atlas basladi!")
    print("-" * 35)

    show_project_info()

    print("-" * 35)

    try:
        hours_per_day = float(input("Gunluk kac saat calisacaksin? "))
        days_per_week = int(input("Haftada kac gun calisacaksin? "))
    except ValueError:
        print("Hatali giris! Lutfen sayisal degerler gir.")
        return

    weekly_hours = safe_calculate_weekly_hours(
        hours_per_day,
        days_per_week,
    )

    if weekly_hours is not None:
        print("-" * 35)
        print(f"Haftalik toplam calisma hedefi: {weekly_hours:g} saat")


if __name__ == "__main__":
    main()
