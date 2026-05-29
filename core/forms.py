from django import forms


class KontaktForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=120,
        widget=forms.TextInput(attrs={"placeholder": "Dein Name"}),
    )
    email = forms.EmailField(
        label="E-Mail",
        widget=forms.EmailInput(attrs={"placeholder": "name@beispiel.de"}),
    )
    projekt = forms.ChoiceField(
        label="Projektart",
        choices=[
            ("", "Bitte wählen"),
            ("landingpage", "Landingpage"),
            ("business", "Business-Website"),
            ("portfolio", "Portfolio-Website"),
            ("relaunch", "Relaunch / Redesign"),
            ("sonstiges", "Etwas anderes"),
        ],
    )
    budget = forms.ChoiceField(
        label="Budgetrahmen",
        required=False,
        choices=[
            ("", "Keine Angabe"),
            ("bis-1500", "bis 1.500 €"),
            ("1500-3500", "1.500 – 3.500 €"),
            ("3500-6000", "3.500 – 6.000 €"),
            ("offen", "Noch offen"),
        ],
    )
    nachricht = forms.CharField(
        label="Deine Nachricht",
        widget=forms.Textarea(attrs={"rows": 6, "placeholder": "Erzähl mir kurz von deinem Vorhaben …"}),
    )
    # Honeypot gegen Bots
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_website(self):
        value = self.cleaned_data.get("website")
        if value:
            raise forms.ValidationError("Spam erkannt.")
        return value
