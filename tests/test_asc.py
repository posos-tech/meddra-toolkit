# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

import pytest

from expecter import expect

from meddra_toolkit.asc import read_asc_file

def describe_asc():
    def describe_read_asc_file_reader():
        def when_no_columns():
            results = [x for x in read_asc_file("./tests/fixtures/sample.asc")]
            expect(len(results)) == 3
            expect(results[0][0]) == "10014698"
            expect(results[2][1]) == "Affections hépatobiliaires"
            expect(results[1][3]) == ""

        def when_columns():
            results = [x for x in read_asc_file("./tests/fixtures/sample.asc", columns=["code","name","abbrev","none", "none2"])]
            expect(len(results)) == 3
            expect(results[0]["code"]) == "10014698"
            expect(results[2]["name"]) == "Affections hépatobiliaires"
            expect(results[1]["none"]) == ""

        def when_bad_columns():
            with pytest.raises(ValueError):
                results = [x for x in read_asc_file("./tests/fixtures/sample.asc", columns=["code","name"])]
           
        def when_utf8_and_comma():
            results = [x for x in read_asc_file("./tests/fixtures/sample_utf8_comma.asc", encoding="utf-8", separator=",", columns=["code","name","abbrev","none", "none2"])]
            expect(len(results)) == 3
            expect(results[0]["code"]) == "10014698"
            expect(results[2]["name"]) == "Affections hépatobiliaires"
            expect(results[1]["none"]) == ""