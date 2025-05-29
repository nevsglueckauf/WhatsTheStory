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
        - Sammlung wiederverwendbarer Methode 
        - Tippp: Für jede API eine konkrete Klasse, die mich beerbt
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
    # Reset Parameter nach Request? 
    auto_rst_param:bool = True

    def __init__(self):
        pass

    def generate_uri(self, params: dict = {}):
        return self.base_uri + self.QRY_SEP + urllib.parse.urlencode(params)

    def join_nos(self, nos: list):
        tmp = [str(x) for x in nos]
        return ", ".join(tmp)

    def get(self, uri: str) -> Self:
        """ FIXME - replace with genereric "method" method

        Args:
            uri (str): _description_

        Returns:
            Self: _description_
        """
        print(self.lst_req_uri)
        self.lst_resp = requests.get(uri, timeout=self.timeout)
        self.payload = self.lst_resp.text
        self.prsd_dta = self.lst_resp.json()[self.json_root]
        if self.auto_rst_param:
            self
        return self.dft_params()

    def dft_params(self) ->Self:
        self.params = {
            "count": self.max_results 
        }    
        return self
    
    def save(self, fn: str = "response.json") ->Self:
        if self.lst_resp is None:
            raise ValueError("Keine Reponse vorhanden!")
        else:
            with open(fn, "w") as f:
                f.write(self.payload)
        return self


class GutenbergApiUser(GenericApiReader):
    """  Konkrete API Klasse für Gutendex
        FIXME: Requests sind aus kommentiert!
    Args:
        GenericApiReader (_type_): _description_
    """
    base_uri:str = "https://gutendex.com/books"
    json_root:str = "results"
    
    max_results:int = 32
    
    params:dict = {}
   
      
    

    def __init__(self):
        super().__init__()
        self.dft_params()
        print(self.params)

    def by_ids(self, ids: list = []) -> Self:
        
        self.params["ids"] =  self.join_nos(ids)
        self.lst_req_uri = self.generate_uri( self.params)
        #return self.get(self.lst_req_uri)
    
    
    
    def search(self, q:str) ->Self:
        self.params['search'] = q
        self.lst_req_uri = self.generate_uri(self.params)
        
        #return self.get(self.lst_req_uri)


sucker = GutenbergApiUser()
#sucker.by_ids({55,66,77})
sucker.search('Victor Hugo Notre Dame')
print(sucker.lst_req_uri)
print(sucker.params)
#sucker.dft_params()

print(sucker.params)
exit()

pprint(sucker.prsd_dta)

