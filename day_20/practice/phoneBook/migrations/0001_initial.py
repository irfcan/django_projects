# Generated by Django 5.0.4 on 2024-04-29 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                "verbose_name": "Kategori",
                "verbose_name_plural": "Kategoriler",
            },
        ),
        migrations.CreateModel(
            name="Phone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ad", models.CharField(max_length=100)),
                ("soyad", models.CharField(max_length=100)),
                (
                    "telefon",
                    models.CharField(
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be in the format: '0(XXX) XXX-XXXX'",
                                regex="^0\\(\\d{3}\\) \\d{3}-\\d{4}$",
                            )
                        ],
                    ),
                ),
                ("email", models.EmailField(blank=True, default="", max_length=50)),
                (
                    "image",
                    models.ImageField(blank=True, default="", upload_to="image/"),
                ),
                ("adres", models.TextField(blank=True, default="", max_length=1000)),
                (
                    "sehir",
                    models.CharField(
                        choices=[
                            ("01", "ADANA"),
                            ("02", "ADIYAMAN"),
                            ("03", "AFYONKARAHİSAR"),
                            ("04", "AĞRI"),
                            ("05", "AMASYA"),
                            ("06", "ANKARA"),
                            ("07", "ANTALYA"),
                            ("08", "ARTVİN"),
                            ("09", "AYDIN"),
                            ("10", "BALIKESİR"),
                            ("11", "BİLECİK"),
                            ("12", "BİNGÖL"),
                            ("13", "BİTLİS"),
                            ("14", "BOLU"),
                            ("15", "BURDUR"),
                            ("16", "BURSA"),
                            ("17", "ÇANAKKALE"),
                            ("18", "ÇANKIRI"),
                            ("19", "ÇORUM"),
                            ("20", "DENİZLİ"),
                            ("21", "DİYARBAKIR"),
                            ("22", "EDİRNE"),
                            ("23", "ELAZIĞ"),
                            ("24", "ERZİNCAN"),
                            ("25", "ERZURUM"),
                            ("26", "ESKİŞEHİR"),
                            ("27", "GAZİANTEP"),
                            ("28", "GİRESUN"),
                            ("29", "GÜMÜŞHANE"),
                            ("30", "HAKKARİ"),
                            ("31", "HATAY"),
                            ("32", "ISPARTA"),
                            ("33", "İÇEL (MERSİN)"),
                            ("34", "İSTANBUL"),
                            ("35", "İZMİR"),
                            ("36", "KARS"),
                            ("37", "KASTAMONU"),
                            ("38", "KAYSERİ"),
                            ("39", "KIRKLARELİ"),
                            ("40", "KIRŞEHİR"),
                            ("41", "KOCAELİ (İZMİT)"),
                            ("42", "KONYA"),
                            ("43", "KÜTAHYA"),
                            ("44", "MALATYA"),
                            ("45", "MANİSA"),
                            ("46", "KAHRAMANMARAŞ"),
                            ("47", "MARDİN"),
                            ("48", "MUĞLA"),
                            ("49", "MUŞ"),
                            ("50", "NEVŞEHİR"),
                            ("51", "NİĞDE"),
                            ("52", "ORDU"),
                            ("53", "RİZE"),
                            ("54", "SAKARYA (ADAPAZARI)"),
                            ("55", "SAMSUN"),
                            ("56", "SİİRT"),
                            ("57", "SİNOP"),
                            ("58", "SİVAS"),
                            ("59", "TEKİRDAĞ"),
                            ("60", "TOKAT"),
                            ("61", "TRABZON"),
                            ("62", "TUNCELİ"),
                            ("63", "ŞANLIURFA"),
                            ("64", "UŞAK"),
                            ("65", "VAN"),
                            ("66", "YOZGAT"),
                            ("67", "ZONGULDAK"),
                            ("68", "AKSARAY"),
                            ("69", "BAYBURT"),
                            ("70", "KARAMAN"),
                            ("71", "KIRIKKALE"),
                            ("72", "BATMAN"),
                            ("73", "ŞIRNAK"),
                            ("74", "BARTIN"),
                            ("75", "ARDAHAN"),
                            ("76", "IĞDIR"),
                            ("77", "YALOVA"),
                            ("78", "KARABÜK"),
                            ("79", "KİLİS"),
                            ("80", "OSMANİYE"),
                            ("81", "DÜZCE"),
                        ],
                        max_length=25,
                    ),
                ),
                ("lokasyon", models.CharField(blank=True, default="", max_length=25)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("activate", models.BooleanField(default=True)),
                ("isHome", models.BooleanField(default=False)),
                (
                    "kategori",
                    models.ManyToManyField(
                        related_name="phone", to="phoneBook.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Telefon Numarası",
                "verbose_name_plural": "Telefon Numaraları",
            },
        ),
    ]
