import pytest
from peminjaman import (
    hitung_denda,
    cek_kelayakan_pinjam,
    BATAS_REGULER,
    BATAS_PREMIUM
)


@pytest.fixture
def batas_peminjaman():
    return {
        "reguler": BATAS_REGULER,
        "premium": BATAS_PREMIUM
    }


@pytest.mark.parametrize("hari, harapan", [
    (0, 0),
    (1, 0),
    (2, 500),
    (3, 1000),
    (60, 25000)
])
def test_hitung_denda(hari, harapan):
    assert hitung_denda(hari) == harapan


def test_hari_negatif_ditolak():
    with pytest.raises(ValueError):
        hitung_denda(-1)


from peminjaman import cek_kelayakan_pinjam


@pytest.mark.parametrize("tier, jumlah, harapan", [
    ("Reguler", 0, True),
    ("Reguler", 4, True),
    ("Reguler", 5, False),
    ("Premium", 6, True),
    ("Premium", 7, False),
    ("premium", 3, True),
    ("PREMIUM", 3, True)
])
def test_cek_kelayakan_pinjam(tier, jumlah, harapan):
    assert cek_kelayakan_pinjam(tier, jumlah) is harapan


def test_jumlah_negatif_ditolak():
    with pytest.raises(ValueError):
        cek_kelayakan_pinjam("Reguler", -1)


def test_tier_tidak_valid_ditolak():
    with pytest.raises(ValueError):
        cek_kelayakan_pinjam("VIP", 2)


def test_batas_reguler(batas_peminjaman):
    assert cek_kelayakan_pinjam(
        "Reguler", batas_peminjaman["reguler"]
    ) is False


def test_batas_premium(batas_peminjaman):
    assert cek_kelayakan_pinjam(
        "Premium", batas_peminjaman["premium"]
    ) is False
