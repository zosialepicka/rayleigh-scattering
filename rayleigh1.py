import matplotlib.pyplot as plt
import numpy as np
import sys

def intensity(wavelength_nm, molecule_name, diameter_nm=None):
    molecule_constants = {
        'tlen': 1.0,
        'azot': 0.85,
        'argon': 0.6,
        'dwutlenek wegla': 0.7,
        'metan': 0.65
    }
    k = molecule_constants.get(molecule_name.lower(), 1.0)
    wavelength_m = wavelength_nm * 1e-9
    if diameter_nm:
        diameter_m = diameter_nm * 1e-9
        return k / wavelength_m**4 * diameter_m**6
    return k / wavelength_m**4

def draw_plot(molecule_name):
    wavelengths = np.linspace(380, 750, 100)
    intensities = [intensity(w, molecule_name) for w in wavelengths]

    plt.plot(wavelengths, intensities, label=f"I(λ) dla {molecule_name.title()}")
    plt.xlabel("Długość fali (nm)")
    plt.ylabel("Intensywność rozpraszania")
    plt.title("Rozpraszanie Rayleigha")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    print("Kliknij na wykresie [X], aby go zamknąć i kontynuować...\n")
    plt.show()

def calculate_intensity_user_input():
    wavelengths_map = {
        '1': (400, 'fioletowy'),
        '2': (450, 'niebieski'),
        '3': (500, 'zielony'),
        '4': (580, 'żółty'),
        '5': (650, 'czerwony')
    }

    # Pętla dla wyboru długości fali
    while True:
        print("\nWybierz długość fali światła:")
        for key, (value, color) in wavelengths_map.items():
            print(f"{key}. {color.title()} ({value} nm)")
        w_choice = input("Twój wybór (1–5): ").strip()
        if w_choice in wavelengths_map:
            wavelength = wavelengths_map[w_choice][0]
            wavelength_color = wavelengths_map[w_choice][1]
            break
        else:
            print("Nieprawidłowy wybór długości fali. Spróbuj ponownie.")

    molecules = ['azot', 'tlen', 'dwutlenek wegla', 'metan']
    # Pętla dla wyboru cząsteczki
    while True:
        print("\nDostępne cząsteczki:")
        for i, mol in enumerate(molecules, 1):
            print(f"{i}. {mol.title()}")
        m_choice = input("Wybierz cząsteczkę (1–4): ").strip()
        if m_choice in ['1', '2', '3', '4']:
            molecule = molecules[int(m_choice) - 1]
            break
        else:
            print("Nieprawidłowy wybór cząsteczki. Spróbuj ponownie.")

    diameters = {
        '1': 0.3,
        '2': 0.4,
        '3': 0.5,
        '': None
    }
    # Pętla dla wyboru średnicy cząsteczki
    while True:
        print("\nWybierz średnicę cząsteczki (nm):")
        print("1. 0.3 nm\n2. 0.4 nm\n3. 0.5 nm\n(naciśnij Enter, aby pominąć)")
        d_choice = input("Twój wybór: ").strip()
        if d_choice in diameters:
            diameter = diameters[d_choice]
            break
        else:
            print("Nieprawidłowy wybór średnicy. Spróbuj ponownie.")

    try:
        result = intensity(wavelength, molecule, diameter)
        print(f"\nDla długości fali {wavelength} nm ({wavelength_color}) "
              f"i cząsteczki {molecule.title()} → Intensywność: {result:.4e}")

    except Exception as e:
        print(f"Błąd: {e}")

def test_mode():
    print("Tryb testowy: sprawdzanie kilku przypadków...")
    test_data = [
        (500, 'tlen'),
        (600, 'azot'),
        (700, 'argon'),
        (550, 'dwutlenek wegla'),
        (380, 'metan')
    ]
    for wavelength, molecule in test_data:
        result = intensity(wavelength, molecule)
        print(f"{molecule.title()} przy {wavelength} nm → I = {result:.4e}")

def main_menu():
    first_run = True
    while True:
        if not first_run:
            print("\n\n")  # podwójny odstęp przed menu, ale nie przy pierwszym uruchomieniu
        else:
            first_run = False

        print("========== MENU GŁÓWNE ==========")
        print("1. Wykres I(λ) dla wybranej cząsteczki")
        print("2. Oblicz wartość I dla danych użytkownika")
        print("3. Tryb testowy (automatyczne testy)")
        print("0. Wyjście")
        print("=================================")
        choice = input("\nWybierz opcję (0–3): \n").strip()

        if choice == '1':
            available = ['tlen', 'azot', 'argon', 'dwutlenek wegla', 'metan']
            while True:
                print("\n Dostępne cząsteczki:")
                for m in available:
                    print(f" - {m.title()}")
                molecule = input("Wybierz cząsteczkę z listy: ").strip().lower()

                if molecule in available:
                    draw_plot(molecule)
                    break
                else:
                    print("Nieznana cząsteczka. Wybierz z podanej listy.\n")
        elif choice == '2':
            calculate_intensity_user_input()
        elif choice == '3':
            test_mode()
        elif choice == '0':
            print("Zamykam program.")
            sys.exit()
        else:
            print("\nNieprawidłowy wybór. Wpisz 0, 1, 2 lub 3.\n")

if __name__ == "__main__":
    main_menu()
