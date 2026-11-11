DENDA_PER_HARI = 500
GRACE_PERIOD = 1
DENDA_MAKS = 25000

BATAS_REGULER = 5
BATAS_PREMIUM = 7


def hitung_denda(hari_terlambat):
    if hari_terlambat < 0:
        raise ValueError("Hari terlambat tidak boleh negatif")

    if hari_terlambat <= GRACE_PERIOD:
        return 0

    denda = (hari_terlambat - GRACE_PERIOD) * DENDA_PER_HARI

    return min(denda, DENDA_MAKS)

    