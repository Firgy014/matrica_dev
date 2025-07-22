from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    pelanggan_baru = fields.Boolean(string="Pelanggan Baru?")
    segment_pelanggan = fields.Selection([
        ('konstruksi', 'Konstruksi'),
        ('perbankan', 'Perbankan'),
        ('pemerintahan', 'Pemerintahan'),
        ('bumn', 'BUMD/BUMN'),
        ('kementerian', 'Kementerian'),
        ('swasta', 'Swasta Lainnya')
    ], string='Segment Pelanggan')
    segment_product_id = fields.Many2one('crm.segment.product', string='Segment Product')
    task_progress_ids = fields.One2many('crm.task.progress', 'lead_id', string='Task Progress')


class CrmTaskProgress(models.Model):
    _name = 'crm.task.progress'
    _description = 'Task Progress'

    task = fields.Char(string='Task')
    deadline = fields.Date(string='Deadline')
    status = fields.Selection([
        ('todo', 'To Do'),
        ('progress', 'Progress'),
        ('done', 'Done')
    ], string='Status', default='todo')

    lead_id = fields.Many2one('crm.lead', string='Lead', ondelete='cascade')
    
    
class CrmSegmentProduct(models.Model):
    _name = 'crm.segment.product'
    _description = 'Segment Product'

    name = fields.Char(string='Segment Product', required=True)

    
    


