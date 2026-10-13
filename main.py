
from project_utils import show_project_info, calculate_weekly_hours


def main():
    print("Project Atlas basladi!")
    print("-" * 35)

    show_project_info()

    print("-" * 35)

    hours = calculate_weekly_hours(5, 6)
    print(f"Haftalik toplam calisma hedefi: {hours} saat")


if __name__ == "__main__":
    main()
