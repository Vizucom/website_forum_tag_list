# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class Tag(osv.Model):
    _inherit = 'forum.tag'
    _order = 'name asc'
