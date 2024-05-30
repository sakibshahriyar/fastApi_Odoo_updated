from app.config import models, uid


def fetch_odoo_data():
    partners = models.execute_kw('odoo_bmit', uid, 'admin', 'res.partner', 'search_read',
                                 [[['is_company', '=', True]]],
                                 {'fields': ['id', 'name', 'email', 'phone']})
    return partners


def fetch_partner_by_id(partner_id):
    partner = models.execute_kw('odoo_bmit', uid, 'admin', 'res.partner', 'search_read',
                                [[['id', '=', partner_id]]],
                                {'fields': ['id', 'name', 'email', 'phone'], 'limit': 1})
    if partner:
        return partner[0]
    else:
        return None


def create_partner(name, email, phone):
    partner_id = models.execute_kw('odoo_bmit', uid, 'admin', 'res.partner', 'create',
                                   [{'name': name, 'email': email, 'phone': phone}])
    return partner_id


def update_partner(partner_id, name=None, email=None, phone=None):
    vals = {}
    if name:
        vals['name'] = name
    if email:
        vals['email'] = email
    if phone:
        vals['phone'] = phone

    models.execute_kw('odoo_bmit', uid, 'admin', 'res.partner', 'write', [[partner_id], vals])


def delete_partner(partner_id):
    models.execute_kw('odoo_bmit', uid, 'admin', 'res.partner', 'unlink', [[partner_id]])


def fetch_purchase_orders():
    purchase_orders = models.execute_kw('odoo_bmit', uid, 'admin', 'purchase.order', 'search_read',
                                        [[]],
                                        {'fields': ['id', 'name', 'partner_id', 'amount_total']})
    return purchase_orders


def fetch_purchase_order_by_id(order_id):
    order = models.execute_kw('odoo_bmit', uid, 'admin', 'purchase.order', 'search_read',
                              [[['id', '=', order_id]]],
                              {'fields': ['id', 'name', 'partner_id', 'amount_total'], 'limit': 1})
    if order:
        return order[0]
    else:
        return None


def create_purchase_order(name, partner_id, amount_total):
    order_id = models.execute_kw('odoo_bmit', uid, 'admin', 'purchase.order', 'create',
                                 [{'name': name, 'partner_id': partner_id, 'amount_total': amount_total}])
    return order_id


def update_purchase_order(order_id, name=None, partner_id=None, amount_total=None):
    vals = {}
    if name:
        vals['name'] = name
    if partner_id:
        vals['partner_id'] = partner_id
    if amount_total:
        vals['amount_total'] = amount_total

    models.execute_kw('odoo_bmit', uid, 'admin', 'purchase.order', 'write', [[order_id], vals])


def delete_purchase_order(order_id):
    models.execute_kw('odoo_bmit', uid, 'admin', 'purchase.order', 'unlink', [[order_id]])
