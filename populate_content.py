import os
import django
import sys

# Setup Django environment
sys.path.append('f:/code/web/MMC/frontend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmccore.settings')
django.setup()

from web.models import Program, Testimonial, SiteSettings, BlogCategory, BlogPost, FAQ
from django.utils.text import slugify

def populate():
    # 1. Site Settings
    settings, created = SiteSettings.objects.get_or_create(id=1)
    settings.mission = "To empower women and girls, prevent and respond to sexual and gender-based violence, and support internally displaced and vulnerable communities through survivor-centered, inclusive, and community-driven interventions that promote dignity, resilience, and sustainable recovery."
    settings.vision = "Mulu Mesfin Charity (MMC) is guided by the principles of human dignity, gender equality, and social justice. We envision a society where safety, confidentiality, and respect are ensured for all survivors of sGBV."
    settings.core_values = "Human dignity, Gender equality, Social justice, Survivor-centered approach, Rights-based approach, Equity, Inclusion, Transparency, Accountability, Compassion, Solidarity."
    settings.about_text = "Mulu Mesfin Charity (MMC) is a non-governmental, non-profit organization founded in August 2024 by Sister Mulu Mesfin, a nursing professional serving at the One-Stop Center of Ayder Specialized Referral Hospital. Inspired by her frontline experience during the devastating conflict in Tigray, Sister Mulu emerged as a strong advocate and voice for women affected by sexual and gender-based violence (sGBV) through local and international media. MMC was established to respond to the urgent needs of survivors, vulnerable women, and internally displaced persons."
    settings.save()
    print("Site Settings updated.")

    # 2. Testimonials
    testimonials_data = [
        {"name": "Program Beneficiary", "role": "Beneficiary", "quote": "Because of Mulu Mesfin Charity, I received psychosocial support and skills training that helped me rebuild my life after displacement."},
        {"name": "Female Beneficiary", "role": "Beneficiary", "quote": "Through the support of Mulu Mesfin Charity, I received psychosocial assistance and guidance that helped me regain hope and confidence after displacement."},
        {"name": "sGBV Survivor", "role": "Survivor", "quote": "MMC listened to me without judgment and supported me when I felt completely alone. Their care helped me begin healing and rebuilding my future."},
        {"name": "IDP Community Member", "role": "Community Member", "quote": "Mulu Mesfin Charity stood with our community during a very difficult time. Their support for displaced women and families brought dignity and relief."},
        {"name": "Health Sector Partner", "role": "Partner", "quote": "MMC plays a vital role in supporting survivors of sexual and gender-based violence through a survivor-centered and ethical approach."},
        {"name": "MMC Volunteer", "role": "Volunteer", "quote": "Volunteering with MMC has been a meaningful experience. The organization truly prioritizes dignity, confidentiality, and empowerment of vulnerable women."}
    ]
    for t in testimonials_data:
        Testimonial.objects.get_or_create(name=t['name'], quote=t['quote'], defaults={'role': t['role']})
    print("Testimonials updated.")

    # 3. Programs (from projects implemented)
    programs_data = [
        {
            "title": "Survivor Care & Ethical Documentation",
            "description": "A Reset Program for Survivor Care, Ethical Documentation, and Practitioner Recovery in Mekelle, Ethiopia. Funded by Planet Humana.",
            "impact_stats": "60 sGBV survivors supported",
            "goal": 2094172.47
        },
        {
            "title": "Trauma Healing & Financial Support",
            "description": "Providing diverse forms of assistance including facilitating access to financial seed money support and providing trauma healing training to sGBV survivors. Funded by Together with Africa (TWAF).",
            "impact_stats": "1,508 Beneficiaries (IDP students, sGBV survivors, etc.)",
            "goal": 14366637.22
        },
        {
            "title": "Medical Assessment for sGBV Survivors",
            "description": "Arrangement of medical assessment for all sGBV in Tigray, Ethiopia. Supported by American Medical Center.",
            "impact_stats": "535 students and sex workers supported",
            "goal": 2100000.00
        },
        {
            "title": "Emergency Support for sGBV Survivors",
            "description": "Providing emergency cases support for sGBV survivors. Funded by Save the Children and individual humanitarians.",
            "impact_stats": "200+ survivors reached",
            "goal": 1189402.77
        }
    ]
    for p in programs_data:
        Program.objects.get_or_create(title=p['title'], defaults={
            'description': p['description'],
            'impact_stats': p['impact_stats'],
            'goal': p['goal'],
            'raised': p['goal'] * 0.4 # Placeholder raised amount
        })
    print("Programs updated.")

if __name__ == "__main__":
    populate()
