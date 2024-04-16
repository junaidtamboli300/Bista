from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Product_fields(models.Model):
    _name = 'product.inheritance'
    
    name = fields.Char(string = "Name",required = True)
    codes = fields.Integer(string='Codes', required=True)

    _sql_constraints = [
        ('codes', 'unique(codes)', 'The value of Your Field must be unique!'),
    ]
    product_master = fields.Many2one('product.inheritance',string = "Product Master")
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High') ],string = 'Priority')
    
    

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'
    
    product_style = fields.Many2one('product.style', string='Product Style')
    
