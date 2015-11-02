# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class Forum(osv.Model):

    _inherit = 'forum.forum'

    _columns = {
        'tag_ids': fields.one2many('forum.tag', 'forum_id', 'Tags'),
    }
