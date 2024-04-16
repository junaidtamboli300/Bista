from odoo import api,fields,models,tools

class Hopsitalinherit(models.Model):
    _inherit = ['sale.order']
    
    confirm_user_id = fields.Many2one("res.users")