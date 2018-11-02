# -*- coding: utf-8 -*-

from odoo import models, fields, api

class myconf(models.Model):
    _name='myconferences.myconf'
    _description='a model for a conference'
    namabarang=fields.Char('Article' , Required=True)
    category=fields.Char('Category' , Required=True)
    indexed=fields.Boolean('Variant', Required=True)
    startdate=fields.Date('Start Date', Required=True)
    enddate=fields.Date('End Date', Required=True)    
    fee=fields.Float('Registration Fee', Required=True)

# class felino(models.Model):
#     _name = 'felino.felino'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100