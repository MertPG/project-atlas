
def show_project_info():
    """Project Atlas hakkinda temel bilgileri gosterir."""
    print("Proje: Project Atlas")
    print("Hedef: Yapay zeka ve yazilim gelistirme.")
    print("Mevcut asama: Python temelleri ve proje yapisi")


def calculate_weekly_hours(hours_per_day, days_per_week):
    """Haftalik toplam calisma saatini hesaplar."""
    if not isinstance(hours_per_day, (int, float)):
        raise TypeError("Gunluk saat sayisal olmalidir.")

    if isinstance(hours_per_day, bool):
        raise TypeError("Gunluk saat sayisal olmalidir.")

    if not isinstance(days_per_week, int) or isinstance(days_per_week, bool):
        raise TypeError("Haftalik gun sayisi tam sayi olmalidir.")

    if hours_per_day < 0:
        raise ValueError("Gunluk calisma saati negatif olamaz.")

    if days_per_week < 0 or days_per_week > 7:
        raise ValueError("Haftalik gun sayisi 0 ile 7 arasinda olmalidir.")

    return hours_per_day * days_per_week


def safe_calculate_weekly_hours(hours_per_day, days_per_week):
    """Hesaplama hatalarini kontrollu sekilde ele alir."""
    try:
        return calculate_weekly_hours(hours_per_day, days_per_week)
    except (TypeError, ValueError) as error:
        print(f"Hesaplama hatasi: {error}")
        return None
