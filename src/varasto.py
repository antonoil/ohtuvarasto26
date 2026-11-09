"""Warehouse storage implementation used by the project tests and demo app."""


class Varasto:
    """Represent a storage space with capacity and current stock level."""

    def __init__(self, tilavuus, alku_saldo=0):
        """Initialize storage with a capacity and an initial balance."""
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # Ominaisuus voidaan laskea; erillistä kenttää ei tarvita.
    def paljonko_mahtuu(self):
        """Return the amount of free space left in the storage."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Add stock to the storage if the amount is valid and room exists."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Take stock out of the storage and return how much was removed."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """Return a human-readable status string describing the storage."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
