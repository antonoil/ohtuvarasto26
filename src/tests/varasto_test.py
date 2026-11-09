"""Unit tests for the warehouse storage behavior."""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Verify the storage class follows the required rules."""

    def setUp(self):
        """Create a default empty storage before each test."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """The new storage should start empty."""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """The storage should have the configured capacity."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_merkkijono_esittaa_saldon_ja_vapaan_tilan(self):
        """String representation should include current stock and free space."""
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_virheellinen_tilavuus_nollataan(self):
        """An invalid capacity should be reset to zero."""
        varasto = Varasto(0)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollataan(self):
        """A negative initial balance should be treated as zero."""
        varasto = Varasto(10, -1)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_liian_suuri_alkusaldo_tayttaa_varaston(self):
        """An oversized initial balance should fill the storage."""
        varasto = Varasto(10, 12)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        """Adding a valid amount should increase the stock."""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivista_maaraa_ei_lisata(self):
        """Negative additions should be ignored."""
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Adding stock should decrease the amount of free space."""
        self.varasto.lisaa_varastoon(8)

        # Vapaata tilaa pitäisi olla jäljellä 2.
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Removing stock should return the amount taken out."""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        """A negative removal should return zero without changing state."""
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_lisaa_tilaa(self):
        """Removing stock should increase the available free space."""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varasto_ei_anna_lisata_liikaa_tavaraa(self):
        """The storage must never exceed its maximum capacity."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(3)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_kaiken_jos_otetaan_liikaa(self):
        """If too much is removed, all remaining stock should be returned."""
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
