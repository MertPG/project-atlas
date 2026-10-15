import logging


logging.basicConfig(
    filename="project_atlas.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def show_project_info():
    """Project Atlas hakkinda temel bilgileri gosterir."""
    logger.info("Proje bilgileri gosteriliyor.")

    print("Proje: Project Atlas")
    print("Hedef: Yapay zeka ve yazilim gelistirme.")
    print("Mevcut asama: Python temelleri ve proje yapisi")


def calculate_weekly_hours(hours_per_day, days_per_week):
    """Haftalik toplam calisma saatini hesaplar."""
    if not isinstance(hours_per_day, (int, float)) or isinstance(
        hours_per_day, bool
    ):
        logger.warning("Gecersiz gunluk saat degeri alindi.")
        raise TypeError("Gunluk saat sayisal olmalidir.")

    if not isinstance(days_per_week, int) or isinstance(days_per_week, bool):
        logger.warning("Gecersiz haftalik gun sayisi alindi.")
        raise TypeError("Haftalik gun sayisi tam sayi olmalidir.")

    if hours_per_day < 0:
        logger.warning("Negatif gunluk calisma saati girildi.")
        raise ValueError("Gunluk calisma saati negatif olamaz.")

    if days_per_week < 0 or days_per_week > 7:
        logger.warning("Gecersiz haftalik gun sayisi girildi.")
        raise ValueError("Haftalik gun sayisi 0 ile 7 arasinda olmalidir.")

    total_hours = hours_per_day * days_per_week
    logger.info("Haftalik calisma hedefi hesaplandi: %s saat", total_hours)

    return total_hours


def safe_calculate_weekly_hours(hours_per_day, days_per_week):
    """Hesaplama hatalarini kontrollu sekilde ele alir."""
    try:
        return calculate_weekly_hours(hours_per_day, days_per_week)
    except (TypeError, ValueError) as error:
        logger.error("Hesaplama hatasi: %s", error)
        print(f"Hesaplama hatasi: {error}")
        return None
