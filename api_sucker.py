# AUTHOR Sven Schrodt<sven.schrodt@schrodt.club
# SINCE 2025-05-28
# LINK https://github.com/nevsglueckauf/smurf_api

import pandas as pd
import json
import urllib.parse
import requests
from pprint import pprint
from typing import Self


class GenericApiReader:
    """ Generischer API Reader
        - Hier: ausnahmsweise Kommentare in deutscher Sprache 
    Raises:
        ValueError: _description_

    """
    # Separator URI?Query String
    QRY_SEP = "?"
    # Payload als String
    payload: str = None
    # URI des letzten Requests
    lst_req_uri: str = None
    # letzte Response als Objekt
    lst_resp: requests.models.Response = None
    # Geparste letzte Response
    prsd_dta: list
    # Root Element der (JSON) Response
    json_root = "results"
    # Timeout
    timeout = 23

    def __init__(self):
        pass

    def generate_uri(self, params: dict = {}):
        return self.base_uri + self.QRY_SEP + urllib.parse.urlencode(params)

    def join_nos(self, nos: list):
        tmp = [str(x) for x in nos]
        return ", ".join(tmp)

    def get(self, uri: str) -> Self:
        print(self.lst_req_uri)
        self.lst_resp = requests.get(uri, timeout=self.timeout)
        self.payload = self.lst_resp.text
        self.prsd_dta = self.lst_resp.json()[self.json_root]
        return self

    def save(self, fn: str = "response.json"):
        if self.lst_resp is None:
            raise ValueError("Keine Reponse vorhanden!")
        else:
            with open(fn, "w") as f:
                f.write(self.payload)


class GutenbergApiSucker(GenericApiReader):
    base_uri = "https://gutendex.com/books"
    json_root = "results"

    def __init__(self):
        super().__init__()

    def by_ids(self, ids: list = []) -> Self:
        self.lst_req_uri = self.generate_uri({"ids": self.join_nos(ids)})
        return self.get(self.lst_req_uri)
    
    def search(self, q:str) ->Self:
        self.lst_req_uri = self.generate_uri({"search": q})
        
        return self


sucker = GutenbergApiSucker()
sucker.search('Victor Hugo Notre Dame')
print(sucker.lst_req_uri)



exit()
foo = sucker.by_ids([11, 84])
sucker.save()


print(sucker.payload)


dta = json.load(open("gutt.json", "r"))
pprint(dta)
exit()
