from odoo import models, fields, api

class Siswa(models.Model):
    _name = 'sekolah.siswa'
    _description = 'Data Siswa'

    name = fields.Char(string='Display Name', compute='_compute_name', store=True)
    nis = fields.Char('NIS', required=True)
    nm_siswa = fields.Char('Nama Siswa', required=True)
    jns_kelamin = fields.Selection([('l', 'Laki-laki'), ('p', 'Perempuan')], string='Jenis Kelamin')
    tgl_lahir = fields.Date('Tanggal Lahir')
    agama = fields.Char('Agama')
    nm_ayah = fields.Char('Nama Ayah')
    nm_ibu = fields.Char('Nama Ibu')
    usia = fields.Integer('Usia')
    alamat = fields.Text('Alamat')
    kelas_id = fields.Many2one('sekolah.kelas', string='Kelas')
    
    @api.depends('nis', 'nm_siswa')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.nis or ''} - {rec.nm_siswa or ''}"
    
class Kelas(models.Model):
    _name = 'sekolah.kelas'
    _description = 'Data Kelas'

    nm_kelas = fields.Char('Nama Kelas', required=True)
    siswa_ids = fields.One2many('sekolah.siswa', 'kelas_id', string='Daftar Siswa')
    wali_kelas = fields.Many2one('sekolah.guru', string='Wali Kelas')
    
    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.nm_kelas}"
            result.append((rec.id, name))
        return result
    
class Guru(models.Model):
    _name = 'sekolah.guru'
    _description = 'Data Guru'

    name = fields.Char(string='Display Name', compute='_compute_name', store=True)
    nip = fields.Char('NIP', required=True)
    nm_guru = fields.Char('Nama Guru', required=True)
    jns_kelamin = fields.Selection([('l', 'Laki-laki'), ('p', 'Perempuan')], string='Jenis Kelamin')
    mata_pelajaran_id = fields.Many2one('sekolah.mata.pelajaran', string='Mata Pelajaran')
    usia = fields.Integer('Usia')
    no_telp = fields.Char('No Telp')
    alamat = fields.Text('Alamat')
    
    @api.depends('nip', 'nm_guru')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.nip or ''} - {rec.nm_guru or ''}"
    
class MataPelajaran(models.Model):
    _name = 'sekolah.mata.pelajaran'
    _description = 'Mata Pelajaran'

    name = fields.Char(string='Display Name', compute='_compute_name', store=True)
    nm_matapelajaran = fields.Char('Nama Mata Pelajaran', required=True)
    jurusan = fields.Char('Jurusan')
    
    @api.depends('nm_matapelajaran')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.nm_matapelajaran or ''}"
    
class Jadwal(models.Model):
    _name = 'sekolah.jadwal'
    _description = 'Jadwal Pelajaran'

    name = fields.Char(string='Display Name', compute='_compute_name', store=True)
    hari = fields.Selection([
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat')
    ], string='Hari')
    kelas_id = fields.Many2one('sekolah.kelas', string='Kelas')
    jam = fields.Char('Jam')
    mata_pelajaran_id = fields.Many2one('sekolah.mata.pelajaran', string='Mata Pelajaran')
    
    @api.depends('hari', 'jam')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.hari or ''} - {rec.jam or ''} "