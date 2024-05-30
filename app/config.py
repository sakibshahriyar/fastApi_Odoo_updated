import xmlrpc.client
from fastapi import HTTPException


class OdooConfig:
    url = 'http://127.0.0.1:8069'
    db = 'odoo_bmit'
    username = 'sakib@bmitodoo.com'
    password = 'admin'

    @classmethod
    def get_odoo_models(cls):
        common = xmlrpc.client.ServerProxy(f'{cls.url}/xmlrpc/2/common')
        uid = common.authenticate(cls.db, cls.username, cls.password, {})
        if not uid:
            raise HTTPException(status_code=500, detail="Unable to authenticate with Odoo")
        models = xmlrpc.client.ServerProxy(f'{cls.url}/xmlrpc/2/object')
        return models, uid


models, uid = OdooConfig.get_odoo_models()
