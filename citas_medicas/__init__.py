import requests
import json
from . import models
from odoo import api, SUPERUSER_ID


def _post_init_presidents(cr, registry):
    """
        Iniciador de los presidentes
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    if "res.partner" in env:
        res_partner = env['res.partner']
        data = json.loads(requests.get("https://api-colombia.com/api/v1/President/").text)
        for president in data:
            res_partner.create({
                "name": president['name'] + " " + president['lastName'],
                "es_doctor": True,
                "especialidad": "No configurada"
            })