
def show_project_info():
    """Project Atlas hakkinda temel bilgileri gosterir."""
    print("Proje: Project Atlas")
    print("Hedef: Yapay zeka ve yazilim gelistirme.")
    print("Mevcut asama: Python temelleri ve proje yapisi")


def calculate_weekly_hours(hours_per_day, days_per_week):
    """Haftalik calisma saatini hesaplar."""
    if hours_per_day < 0 or days_per_week < 0:
        raise ValueError("Calisma saatleri negatif olamaz.")

    return hours_per_day * days_per_week


def safe_calculate_weekly_hours(hours_per_day, days_per_week):
    """Hatali hesaplamalari kontrollu sekilde ele alir."""
    try:
        return calculate_weekly_hours(hours_per_day, days_per_week)
    except (TypeError, ValueError) as error:
        print(f"Hesaplama hatasi: {error}")
        return None
