import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skola.settings')
django.setup()

from kruzky.models import Veduci, Kruzok

print("--- Spúšťam import dát ---")

try:
    with open('udaje.txt', 'r', encoding='utf-8') as file:
        # Premažeme staré dáta
        Kruzok.objects.all().delete()
        Veduci.objects.all().delete()
        
        pocet_pridanych = 0

        for cislo_riadku, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            
            casti = line.split(';')
            
            if len(casti) == 5:
                # Všetko je v poriadku, ukladáme
                v, created = Veduci.objects.get_or_create(
                    meno=casti[0].strip(), 
                    defaults={'email': casti[1].strip()}
                )
                Kruzok.objects.create(
                    nazov=casti[2].strip(), 
                    den=casti[3].strip(), 
                    miestnost=casti[4].strip(), 
                    veduci=v
                )
                pocet_pridanych += 1
            else:
                # Tu ti skript presne povie, kde je v texte chyba
                print(f"[CHYBA] Riadok {cislo_riadku} bol preskočený! Očakávalo sa 5 častí (oddelených bodkočiarkou), ale našlo sa ich {len(casti)}.")
                print(f"        Obsah riadku: {casti}")

    print(f"--- Hotovo! Úspešne pridaných {pocet_pridanych} krúžkov. ---")

except FileNotFoundError:
    print("[KRITICKÁ CHYBA] Súbor 'udaje.txt' sa nenašiel! Uisti sa, že je v rovnakej zložke ako tento skript.")