# -*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask(models.Model):
    _inherit = 'todo.task'
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="What needs to be done?")

    # Aksi ini akan mengoverride aksi "toggle_done" di module "todo_apps"
    # dan hanya akan melakukan toggle jika user login saat ini sesuai dengan
    # user responsible pada data record yang diedit / dikelola
    @api.one
    def do_toggle_done(self):
        # Jika user responsible pada record tidak sama dengan user login saat ini
        if self.user_id != self.env.user:
            # Muncul notifikasi hanya user responsible yang berhak
            raise Exception('Only the responsible can do this!')
        # selain kondisi di atas
        else:
            # gunakan fungsi parent(super) do_toggle_done() TodoTask dari Module ipin_todo_apps (dependency) 
            return super(TodoTask, self).do_toggle_done()
    
    # Aksi ini akan mengoverride aksi "clear_done" di module "todo_apps"
    # dan hanya akan melakukan clear data record user responsible sesuai user login saat ini
    @api.multi
    def do_clear_done(self):
        domain = [
            ('is_done', '=', True),
            # dibawah ini  "or" atau "|" akan mempengaruhi 2 kondisi setelah tanda tersebut
            # "is_done = True and (user_id=self.env.uid or user_id=False)" 
            '|', ('user_id', '=', self.env.uid),('user_id', '=', False)
        ]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True
