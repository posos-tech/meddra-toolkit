from typing import ForwardRef, List

from pydantic import BaseModel


MeddraConcept = ForwardRef('MeddraConcept')


class MeddraConcept(BaseModel):
    code: str
    name: str
    parents: List[MeddraConcept] = []
    children: List[MeddraConcept] = []

    def concept_type(self):
        return self.__class__.__name__[6:]

    def __str__(self):
        return f"{self.concept_type()}/{self.code} > {self.name}"

    def __repr__(self):
        return self.__str__() + f" >> [{','.join(list(map(lambda x: x.code, self.parents)))}]"


MeddraConcept.update_forward_refs()


class MeddraSOC(MeddraConcept):
    abbrev: str


class MeddraHLGT(MeddraConcept):
    pass


class MeddraHLT(MeddraConcept):
    pass


class MeddraPT(MeddraConcept):
    soc_code: str
    soc: MeddraSOC


class MeddraLLT(MeddraConcept):
    active: bool
    pt_code: str
    pt: MeddraPT
