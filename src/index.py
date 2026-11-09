"""Demo program showing how the warehouse storage behaves."""

from varasto import Varasto


def print_storage_state(label, storage):
    """Print a label and the current state of a storage instance."""
    print(f"{label}: {storage}")


def print_invalid_cases():
    """Print the invalid initialization scenarios used in the demo."""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def print_variation_examples(mehua, olutta):
    """Print the add/remove examples used by the demo program."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    """Run the example scenario for the warehouse storage class."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print_storage_state("Mehuvarasto", mehua)
    print_storage_state("Olutvarasto", olutta)

    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print_storage_state("Mehuvarasto", mehua)
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print_storage_state("Mehuvarasto", mehua)

    print_invalid_cases()
    print_variation_examples(mehua, olutta)


if __name__ == "__main__":
    main()
