from django.core.management.base import BaseCommand
from web.models import SiteSettings, Program, Testimonial, Partner, BlogCategory, BlogPost, Event, FAQ
from django.utils.text import slugify
from django.utils import timezone
from datetime import date, time

class Command(BaseCommand):
    help = 'Populate the database with real organizational data for MMC'

    def handle(self, *args, **options):
        self.stdout.write("Populating data...")

        # 1. Site Settings
        settings, created = SiteSettings.objects.get_or_create(id=1)
        settings.name = "Mulu Mesfin Charity (MMC)"
        settings.email = "contact@mulumesfincharity.org"
        settings.phone_1 = "+251 914 008 942"
        settings.address = "Mekelle, Ethiopia"
        settings.mission = (
            "To empower women and girls, prevent and respond to sexual and gender-based violence, "
            "and support internally displaced and vulnerable communities through survivor-centered, "
            "inclusive, and community-driven interventions that promote dignity, resilience, "
            "and sustainable recovery."
        )
        settings.vision = (
            "A safe and empowered society where every woman and girl has access to justice, "
            "healing, and opportunities."
        )
        settings.core_values = (
            "Mulu Mesfin Charity (MMC) is guided by the principles of human dignity, gender equality, "
            "and social justice. We adopt a survivor-centered and rights-based approach in addressing "
            "sexual and gender-based violence, ensuring safety, confidentiality, and respect for all "
            "survivors. MMC is committed to empowering vulnerable women and girls, promoting equity "
            "and inclusion, and prioritizing internally displaced persons and conflict-affected communities. "
            "Transparency, accountability, compassion, and solidarity guide all our programs."
        )
        settings.about_text = (
            "Mulu Mesfin Charity (MMC) is a non-governmental, non-profit organization founded in "
            "August 2024 by Sister Mulu Mesfin, a nursing professional serving at the One-Stop Center "
            "of Ayder Specialized Referral Hospital. Inspired by her frontline experience during the "
            "devastating conflict in Tigray, Sister Mulu emerged as a strong advocate and voice for "
            "women affected by sexual and gender-based violence (sGBV). MMC was established to respond "
            "to the urgent needs of survivors, vulnerable women, and internally displaced persons."
        )
        settings.founder_bio = (
            "Sister Mulu Mesfin has worked with more than 3,000 survivors over the past two years, "
            "providing therapy, medical care, shelter, and emotional support. Her dedication has "
            "earned national and international recognition."
        )
        settings.save()
        self.stdout.write(self.style.SUCCESS("SiteSettings updated."))

        # 2. Testimonials
        testimonials_data = [
            {
                "name": "Program Beneficiary",
                "role": "Beneficiary",
                "quote": "Because of Mulu Mesfin Charity, I received psychosocial support and skills training that helped me rebuild my life after displacement."
            },
            {
                "name": "Female beneficiary",
                "role": "Beneficiary",
                "quote": "Through the support of Mulu Mesfin Charity, I received psychosocial assistance and guidance that helped me regain hope and confidence after displacement."
            },
            {
                "name": "sGBV survivor",
                "role": "Survivor",
                "quote": "MMC listened to me without judgment and supported me when I felt completely alone. Their care helped me begin healing and rebuilding my future."
            },
            {
                "name": "IDP community member",
                "role": "Community Member",
                "quote": "Mulu Mesfin Charity stood with our community during a very difficult time. Their support for displaced women and families brought dignity and relief."
            },
            {
                "name": "Health sector partner",
                "role": "Partner",
                "quote": "MMC plays a vital role in supporting survivors of sexual and gender-based violence through a survivor-centered and ethical approach."
            }
        ]
        for t in testimonials_data:
            Testimonial.objects.get_or_create(name=t["name"], quote=t["quote"], defaults={"role": t["role"]})
        self.stdout.write(self.style.SUCCESS("Testimonials added."))

        # 3. Programs (Projects)
        programs_data = [
            {
                "title": "Survivor Care & Ethical Documentation",
                "description": "A Reset Program for Survivor Care, Ethical Documentation, and Practitioner Recovery in Mekelle, Ethiopia. Supporting 60 sGBV survivors.",
                "impact_stats": "60 Survivors Supported",
                "goal": 2094172.47,
                "raised": 0
            },
            {
                "title": "CRSV Research Project",
                "description": "Identifying motivating husband decision to stay with their wives who experienced conflict related sexual violence (crsv) in Tigray.",
                "impact_stats": "Community Research",
                "goal": 649240.00,
                "raised": 649240.00
            },
            {
                "title": "Medical Assessment for sGBV",
                "description": "Arrangement of medical assessment for all sGBV in Tigray, Ethiopia. Beneficiaries include college/university students and commercial sex workers.",
                "impact_stats": "535 Beneficiaries",
                "goal": 2100000.00,
                "raised": 2100000.00
            },
            {
                "title": "Trauma Healing & Financial Support",
                "description": "Providing trauma healing training and facilitating access to financial seed money support for sGBV survivors across Tigray.",
                "impact_stats": "1,508 Beneficiaries",
                "goal": 14366637.22,
                "raised": 0
            },
            {
                "title": "Emergency sGBV Support",
                "description": "Providing emergency assistance and support for survivors of sexual and gender-based violence in urgent cases.",
                "impact_stats": "100+ Survivors Supported",
                "goal": 613402.77,
                "raised": 613402.77
            }
        ]
        for p in programs_data:
            Program.objects.get_or_create(
                title=p["title"], 
                defaults={
                    "description": p["description"],
                    "impact_stats": p["impact_stats"],
                    "goal": p["goal"],
                    "raised": p["raised"]
                }
            )
        self.stdout.write(self.style.SUCCESS("Programs added."))

        # 4. Partners (Donors)
        partners_data = ["Planet Humana", "German embassy", "American Medical Center", "Together with Africa (TWAF)", "Save the children"]
        for name in partners_data:
            Partner.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("Partners added."))

        # 5. Blog Posts
        cat, _ = BlogCategory.objects.get_or_create(name="Humanitarian")
        BlogCategory.objects.get_or_create(name="SGBV Response")
        BlogCategory.objects.get_or_create(name="Empowerment")

        blog_data = [
            {
                "title": "The Founding of Mulu Mesfin Charity",
                "content": "Sister Mulu Mesfin founded MMC in August 2024 to respond to the urgent needs of survivors...",
                "status": "published"
            },
            {
                "title": "Healing Through Compassion",
                "content": "MMC adopts a survivor-centered and rights-based approach in addressing sexual and gender-based violence...",
                "status": "published"
            }
        ]
        for b in blog_data:
            BlogPost.objects.get_or_create(
                title=b["title"],
                defaults={
                    "content": b["content"],
                    "status": b["status"],
                    "category": cat
                }
            )
        self.stdout.write(self.style.SUCCESS("Blog posts added."))

        # 6. Events
        Event.objects.get_or_create(
            title="Community Awareness Workshop",
            date=date(2026, 3, 15),
            time=time(9, 0),
            location="Mekelle, Tigray",
            defaults={"description": "Advocacy and awareness campaign for gender justice."}
        )
        self.stdout.write(self.style.SUCCESS("Events added."))

        # 7. FAQs
        faq_data = [
            {"question": "What is MMC's focus?", "answer": "We focus on SGBV prevention, trauma healing, and economic empowerment for women."},
            {"question": "How can I volunteer?", "answer": "You can register through our volunteer form on the website."}
        ]
        for f in faq_data:
            FAQ.objects.get_or_create(question=f["question"], answer=f["answer"])
        self.stdout.write(self.style.SUCCESS("FAQs added."))

        self.stdout.write(self.style.SUCCESS("All data populated successfully."))
