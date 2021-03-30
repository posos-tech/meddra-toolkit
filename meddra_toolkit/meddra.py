import os
import re
from typing import Dict, List, Optional, Tuple, Type

from meddra_toolkit.asc import read_asc_file
from meddra_toolkit.models.concepts import (
    MeddraConcept,
    MeddraHLGT,
    MeddraHLT,
    MeddraLLT,
    MeddraPT,
    MeddraSOC,
)


class MeddraData:
    def __init__(self, path: str):
        self.path: str = path
        self.concepts: Dict[str, MeddraConcept] = {}

    def find(self, value: str, regex: bool = False):
        found = set([])
        compiled_regex = (
            re.compile(value, re.IGNORECASE + re.UNICODE) if regex else None
        )
        for code, concept in self.concepts.items():
            if (not compiled_regex and (code == value or concept.name == value)) or (
                compiled_regex and (re.search(compiled_regex, concept.name) is not None)
            ):
                if code != value and type(concept) == MeddraLLT:
                    found.add(concept.pt_code)
                else:
                    found.add(code)

        return list(map(lambda x: self.concepts[x], found))

    def load(self):
        self._load_concept(
            "soc.asc",
            concept=MeddraSOC,
            columns=["code", "name", "abbrev", "_", "_", "_", "_", "_", "_", "_", "_"],
        )
        self._load_concept(
            "hlgt.asc",
            concept=MeddraHLGT,
            columns=["code", "name", "_", "_", "_", "_", "_", "_", "_", "_"],
        )
        self._load_concept(
            "hlt.asc",
            concept=MeddraHLT,
            columns=["code", "name", "_", "_", "_", "_", "_", "_", "_", "_"],
        )
        self._load_concept(
            "pt.asc",
            concept=MeddraPT,
            columns=[
                "code",
                "name",
                "_",
                "soc_code",
                "_",
                "_",
                "_",
                "_",
                "_",
                "_",
                "_",
                "_",
            ],
            relations=[("soc_code", "soc")],
        )
        self._load_concept(
            "llt.asc",
            concept=MeddraLLT,
            columns=[
                "code",
                "name",
                "pt_code",
                "_",
                "_",
                "_",
                "_",
                "_",
                "_",
                "active",
                "_",
                "_",
            ],
            relations=[("pt_code", "pt")],
        )
        self._load_relation("soc_hlgt.asc")
        self._load_relation("hlgt_hlt.asc")
        self._load_relation("hlt_pt.asc")

    def _load_concept(
        self,
        file_name: str,
        columns: Optional[List[str]] = None,
        concept: Type[MeddraConcept] = MeddraConcept,
        relations: List[Tuple[str, str]] = [],
    ):
        for concept_line in read_asc_file(
            os.path.join(self.path, file_name), columns=columns
        ):

            for code_field, related_field in relations:
                if (
                    code_field in concept_line
                    and concept_line[code_field] in self.concepts
                ):
                    concept_line[related_field] = self.concepts[
                        concept_line[code_field]
                    ]
            concept_object = concept(**concept_line)
            if concept_object.code not in self.concepts:
                self.concepts[concept_object.code] = concept_object

    def _load_relation(self, file_name: str):
        for concept_line in read_asc_file(
            os.path.join(self.path, file_name), columns=["parent", "child", "_"]
        ):
            parent = concept_line["parent"]
            child = concept_line["child"]
            if parent in self.concepts:
                if child in self.concepts:
                    self.concepts[parent].children.append(self.concepts[child])
                    self.concepts[child].parents.append(self.concepts[parent])
                else:
                    raise ValueError(f"No child concept with code {child}")
            else:
                raise ValueError(f"No parent concept with code {parent}")

VERSION_24_0_FR = "data/24.0/fr"

class Meddra:
    def __init__(self, version: str, language: str, data: MeddraData):
        self.version = version
        self.language = language
        self.data = data
