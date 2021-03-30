import csv
import json
import sys
from typing import Any, List

from meddra_toolkit.models.concepts import MeddraConcept


class FormattedPrinter:
    def __init__(self, hierarchy: bool):
        self.hierarchy = hierarchy

    def onResult(self, result: MeddraConcept):
        if self.hierarchy:
            self._print_hierarchy(0, result)
            print("")
        else:
            print(result)

    def output(self):
        return None

    def _print_hierarchy(self, tab: int, element: MeddraConcept):
        print("\t" * tab + f"{element}")
        for p in element.parents:
            self._print_hierarchy(tab + 1, p)


class CSVPrinter:
    def __init__(self):
        self.csv_writer = csv.writer(sys.stdout)

    def onResult(self, result):
        self.csv_writer.writerow([result.concept_type(), result.code, result.name])

    def output(self):
        return None


class JSONPrinter:
    def __init__(self, pretty: bool = False):
        self.results: List[Any] = []
        self.pretty = pretty

    def onResult(self, result):
        concept = self._get_hierarchy_as_dict(result)
        self.results.append(concept)

    def _get_hierarchy_as_dict(self, result):
        return {
            "concept_type": result.concept_type(),
            "code": result.code,
            "name": result.name,
            "parents": list(
                map(lambda x: self._get_hierarchy_as_dict(x), result.parents)
            ),
        }

    def output(self):
        return json.dumps(
            self.results, indent=(4 if self.pretty else None), ensure_ascii=False
        )
