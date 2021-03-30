# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned
from expecter import expect

from meddra_toolkit.meddra import MeddraData


def describe_meddra_data():
    def describe_find_value():
        def when_find_by_exact_name():
            med = MeddraData("./tests/fixtures/data/")
            med.load()
            fd = med.find("Anémie")
            # print(list(map(lambda x: str(x), fd)))
            expect(len(fd)) == 1
            expect(fd[0].code) == "10002034"

        def when_find_by_code():
            med = MeddraData("./tests/fixtures/data/")
            med.load()
            fd = med.find("10000004")
            expect(len(fd)) == 1
            expect(fd[0].code) == "10000004"

        def when_find_by_regex():
            med = MeddraData("./tests/fixtures/data/")
            med.load()
            fd = med.find("Anémie.*", regex=True)
            expect(len(fd)) == 83
            fd = med.find("anémie.*", regex=True)
            expect(len(fd)) == 83
            fd = med.find("anemie.*", regex=True)
            expect(len(fd)) == 83
            fd = med.find(".*sucré.*", regex=True)
            expect(len(fd)) == 24

    def describe_load_data():
        def when_load_everything():
            med = MeddraData("./tests/fixtures/data/")
            med.load()
            expect(len(med.concepts.values())) == 85392
            expect(med.concepts["10007541"].name) == "Affections cardiaques"
            expect(
                med.concepts["10018865"].name
            ) == "Tumeurs hématopoïétiques (excl leucémies et lymphomes)"
            expect(med.concepts["10053567"].name) == "Coagulopathies"
            expect(med.concepts["10002915"].name) == "Insuffisance aortique"
            expect(med.concepts["10053871"].soc_code) == "10010331"

            expect(med.concepts["10053871"].soc.name) == med.concepts["10010331"].name
            expect(med.concepts["10020972"].pt_code) == "10020969"
            expect(med.concepts["10020972"].pt.name) == med.concepts["10020969"].name
            expect(med.concepts["10020972"].name) == "Anémie microcytaire hypochrome"
            expect(med.concepts["10020972"].active) == True
            expect(med.concepts["10010375"].active) == False

            expect(len(med.concepts["10010331"].children)) == 19
            expect(med.concepts["10010331"].children[0].parents[0].code) == "10010331"
