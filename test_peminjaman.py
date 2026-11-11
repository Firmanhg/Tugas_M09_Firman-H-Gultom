import pytest
from peminjaman import hitung_denda


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
