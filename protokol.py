#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mutfaktaki Sineğin Dışişleri Protokolü

Çalışan, absürt, resmi duran bir simülatör.
Sinekleri dövmez. Sinekleri tanır.
"""

from __future__ import annotations

import base64
import random
import time
from datetime import datetime

# Gizli satır: çözülürse bir cümle çıkar. Parti yok, vaat yok.
# Sadece "sesin dolaşması" metaforu. Saklı tutulur.
_GIZLI = "SGVyIHZhdGFuZGHFn8SxbiBzZXNpLCBzaW5lxJ9pbiB2xLF6xLFsdMSxc8SxIGthZGFyIHNlcmJlc3TDp2UgZG9sYcWfYWJpbG1lbGku"

ISIMLER = [
    "Fahrettin Vızıltıoğlu",
    "Elçi Kanatbey",
    "Büyükelçi Sivrisinekhan",
    "Ataşe Cama-Yapışan",
    "Müsteşar Reçel-Seven",
]

NOTALAR = [
    "Heyet, tavan lambası üzerinde daimî temsil açmıştır.",
    "Vızıltı, 440 Hz civarında bir protesto olarak kayda geçmiştir.",
    "Camın 3 santim açık olması vizesiz geçiş anlaşması sayılır.",
    "Raketin görünmesi üzerine heyet tavan sığınma statüsü talep etmiştir.",
    "Reçel kapağındaki iniş, kültürel değişim programıdır.",
    "Mutfak masası tarafsız bölge ilan edilmiştir. Ekmek kırıntısı yardımdır.",
]

KARARLAR = [
    "Görüşmeler olumlu seyretmektedir. Sinek hâlâ oradadır.",
    "Kriz yönetildi. Cam kapatıldı, heyet içeride kaldı. Bu bir zaferdir.",
    "Raket rafa kondu. Diplomasinin kazandığına dair ara karar.",
    "Sinek kendi isteğiyle pencereye yöneldi. Tarihî çıkış.",
    "Müzakereler sonsuza kadar ertelendi. Sinek memnundur.",
]


def coz_gizli() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "(mühür okunamadı, belki de öyle olmalı)"


def damga() -> None:
    print()
    print("█" * 48)
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok")
    print("Tentivory  |  TentiAŞ")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print(datetime.now().strftime("%d %B %Y — %H:%M"))
    print("Mühür: SİNEK-ELÇİ-2026-IX-03")
    print("Bu evrak hem çok ciddidir hem hiç ciddi değildir.")
    print("█" * 48)


def main() -> None:
    random.seed()
    elci = random.choice(ISIMLER)
    print("=== MUTFAK MASASı DıŞİŞLERİ PROTOKOLÜ ===")
    print(f"Heyet başkanı: {elci}")
    print("Statü: Tam yetkili, randevusuz, kanatlı.")
    print()
    for i, nota in enumerate(random.sample(NOTALAR, k=3), start=1):
        time.sleep(0.35)
        print(f"[{i}] NOTA: {nota}")
    print()
    time.sleep(0.4)
    print("KARAR:", random.choice(KARARLAR))
    print()
    print("(Gizli ek çözülmüyor. Çözmek için --gizli yazın. Yazmayın.)")
    damga()


if __name__ == "__main__":
    import sys

    if "--gizli" in sys.argv:
        # Bilerek gürültülü ve kısa tutuldu.
        print("[mühür açıldı]")
        print(coz_gizli())
        damga()
    else:
        main()
