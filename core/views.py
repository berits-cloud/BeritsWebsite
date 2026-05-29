from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import KontaktForm


LEISTUNGEN = [
    {
        "titel": "Landingpage",
        "kicker": "01 — Fokus",
        "beschreibung": (
            "Eine einzelne, sorgfältig komponierte Seite, die deine Idee auf den Punkt bringt — "
            "ideal für Coaches, Events oder Produktstarts."
        ),
        "umfang": ["Konzept & Text-Sparring", "Design & Umsetzung", "SEO-Grundlagen", "Hosting-Setup"],
        "ab_preis": "ab 890 €",
    },
    {
        "titel": "Business-Website",
        "kicker": "02 — Substanz",
        "beschreibung": (
            "Mehrseitige Website mit klarer Struktur, die deinem Unternehmen ein souveränes, "
            "ruhiges Auftreten gibt — zeitlos statt trendy."
        ),
        "umfang": ["Bis zu 6 Seiten", "Individuelles Design", "Kontaktformular", "Mobile-First"],
        "ab_preis": "ab 1.890 €",
    },
    {
        "titel": "Portfolio & Brand",
        "kicker": "03 — Charakter",
        "beschreibung": (
            "Für Fotograf*innen, Kreative und Studios: eine Bühne, die deine Arbeit groß "
            "wirken lässt — mit viel Weißraum und Liebe zum Detail."
        ),
        "umfang": ["Bildkonzept", "Galerien & Cases", "Typografie-System", "Pflege-Einweisung"],
        "ab_preis": "ab 2.490 €",
    },
]


PROJEKTE = [
    {
        "titel": "PharmaScienceHub",
        "kategorie": "Business · Pharma & Wissenschaft",
        "jahr": "2026",
        "farbe": "#7a8775",
        "url": "https://pharmasciencehub.com",
    },
    {
        "titel": "HappyFit",
        "kategorie": "Business · Fitness",
        "jahr": "2025",
        "farbe": "#cec7b5",
        "url": "https://happyfit-fitness.de",
    },
    {
        "titel": "Berit Andres Webdesign",
        "kategorie": "Portfolio · Eigene Website",
        "jahr": "2026",
        "farbe": "#b7c1b2",
    },
    {
        "titel": "Atelier Lina",
        "kategorie": "Portfolio · Keramik",
        "jahr": "2026",
        "farbe": "#cec7b5",
    },
    {
        "titel": "Nord & Salz",
        "kategorie": "Business · Gastronomie",
        "jahr": "2025",
        "farbe": "#b7c1b2",
    },
    {
        "titel": "Mira Coaching",
        "kategorie": "Landingpage · Coaching",
        "jahr": "2025",
        "farbe": "#7a8775",
    },
    {
        "titel": "Studio Hain",
        "kategorie": "Portfolio · Architektur",
        "jahr": "2024",
        "farbe": "#4e584c",
    },
    {
        "titel": "Fjord Apotheke",
        "kategorie": "Business · Gesundheit",
        "jahr": "2024",
        "farbe": "#3e0d17",
    },
    {
        "titel": "Hof Wiesentau",
        "kategorie": "Business · Landwirtschaft",
        "jahr": "2024",
        "farbe": "#cec7b5",
    },
]


def home(request):
    return render(
        request,
        "core/home.html",
        {
            "leistungen": LEISTUNGEN,
            "projekte": PROJEKTE[:3],
        },
    )


def leistungen(request):
    return render(request, "core/leistungen.html", {"leistungen": LEISTUNGEN})


def portfolio(request):
    return render(request, "core/portfolio.html", {"projekte": PROJEKTE})


def ueber(request):
    return render(request, "core/ueber.html")


def kontakt(request):
    if request.method == "POST":
        form = KontaktForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            body = (
                f"Name: {data['name']}\n"
                f"E-Mail: {data['email']}\n"
                f"Projektart: {data['projekt']}\n"
                f"Budget: {data.get('budget') or '—'}\n\n"
                f"Nachricht:\n{data['nachricht']}\n"
            )
            send_mail(
                subject=f"Neue Anfrage von {data['name']}",
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECIPIENT],
                fail_silently=True,
            )
            return redirect("core:kontakt_danke")
    else:
        form = KontaktForm()
    return render(request, "core/kontakt.html", {"form": form})


def kontakt_danke(request):
    return render(request, "core/kontakt_danke.html")


def impressum(request):
    return render(request, "core/impressum.html")


def datenschutz(request):
    return render(request, "core/datenschutz.html")
