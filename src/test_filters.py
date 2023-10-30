from JustJoinIt import filter_data as fd_jj
from NoFluffJobs import filter_data as fd_nfj
import user_interaction as ui

"""
Local tests for each data filter algorithm.
Tested with local files ignored by .gitignore,
as to not show the project as an html project
"""


def test_justjoin():
    return fd_jj.local_test()


def test_nofluff():
    return fd_nfj.local_test()


def test_pracujpl():
    pass


def test_all():
    offers_jj = test_justjoin()
    offers_nofluff = test_nofluff()
    offers_pracujpl = test_pracujpl()

    total_offers = offers_jj + offers_nofluff + offers_pracujpl
    return total_offers


if __name__ == "__main__":
    ui.show_offers(test_justjoin())
