# todo/models.py

from django.db import models
# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


'''class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
'''

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

class Tbatuc2I(models.Model):
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ncell_id = models.CharField(db_column='NCELL_ID', max_length=50)  # Field name made lowercase.
    ratio_all = models.FloatField(db_column='RATIO_ALL', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(db_column='RANK', blank=True, null=True)  # Field name made lowercase.
    cosite = models.SmallIntegerField(db_column='COSITE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUC2I'
        unique_together = (('sector_id', 'ncell_id'),)


class Tbatudata(models.Model):
    seq = models.BigIntegerField(primary_key=True)
    filename = models.CharField(db_column='FileName', max_length=255)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    cellid = models.CharField(db_column='CellID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tac = models.IntegerField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    pci = models.SmallIntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    rsrp = models.FloatField(db_column='RSRP', blank=True, null=True)  # Field name made lowercase.
    rs_sinr = models.FloatField(db_column='RS_SINR', blank=True, null=True)  # Field name made lowercase.
    ncell_id_1 = models.CharField(db_column='NCell_ID_1', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_1 = models.IntegerField(db_column='NCell_EARFCN_1', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_1 = models.SmallIntegerField(db_column='NCell_PCI_1', blank=True, null=True)  # Field name made lowercase.        
    ncell_rsrp_1 = models.FloatField(db_column='NCell_RSRP_1', blank=True, null=True)  # Field name made lowercase.
    ncell_id_2 = models.CharField(db_column='NCell_ID_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_2 = models.IntegerField(db_column='NCell_EARFCN_2', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_2 = models.SmallIntegerField(db_column='NCell_PCI_2', blank=True, null=True)  # Field name made lowercase.        
    ncell_rsrp_2 = models.FloatField(db_column='NCell_RSRP_2', blank=True, null=True)  # Field name made lowercase.
    ncell_id_3 = models.CharField(db_column='NCell_ID_3', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_3 = models.IntegerField(db_column='NCell_EARFCN_3', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_3 = models.SmallIntegerField(db_column='NCell_PCI_3', blank=True, null=True)  # Field name made lowercase.        
    ncell_rsrp_3 = models.FloatField(db_column='NCell_RSRP_3', blank=True, null=True)  # Field name made lowercase.
    ncell_id_4 = models.CharField(db_column='NCell_ID_4', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_4 = models.IntegerField(db_column='NCell_EARFCN_4', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_4 = models.SmallIntegerField(db_column='NCell_PCI_4', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_4 = models.FloatField(db_column='NCell_RSRP_4', blank=True, null=True)  # Field name made lowercase.
    ncell_id_5 = models.CharField(db_column='NCell_ID_5', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_5 = models.IntegerField(db_column='NCell_EARFCN_5', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_5 = models.SmallIntegerField(db_column='NCell_PCI_5', blank=True, null=True)  # Field name made lowercase.        
    ncell_rsrp_5 = models.FloatField(db_column='NCell_RSRP_5', blank=True, null=True)  # Field name made lowercase.
    ncell_id_6 = models.CharField(db_column='NCell_ID_6', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_6 = models.IntegerField(db_column='NCell_EARFCN_6', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_6 = models.SmallIntegerField(db_column='NCell_PCI_6', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_6 = models.FloatField(db_column='NCell_RSRP_6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUData'
        unique_together = (('seq', 'filename'),)


class Tbatuhandover(models.Model):
    ssector_id = models.CharField(db_column='SSECTOR_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    nsector_id = models.CharField(db_column='NSECTOR_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hoatt = models.IntegerField(db_column='HOATT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUHandOver'


class Tbadjcell(models.Model):
    s_sector_id = models.CharField(db_column='S_SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.      
    n_sector_id = models.CharField(db_column='N_SECTOR_ID', max_length=50)  # Field name made lowercase.
    s_earfcn = models.IntegerField(db_column='S_EARFCN', blank=True, null=True)  # Field name made lowercase.
    n_earfcn = models.IntegerField(db_column='N_EARFCN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbAdjCell'
        unique_together = (('s_sector_id', 'n_sector_id'),)


class Tbc2I(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scell = models.CharField(db_column='SCELL', primary_key=True, max_length=255)  # Field name made lowercase.
    ncell = models.CharField(db_column='NCELL', max_length=255)  # Field name made lowercase.
    prc2i9 = models.FloatField(db_column='PrC2I9', blank=True, null=True)  # Field name made lowercase.
    c2i_mean = models.FloatField(db_column='C2I_Mean', blank=True, null=True)  # Field name made lowercase.
    std = models.FloatField(db_column='Std', blank=True, null=True)  # Field name made lowercase.
    samplecount = models.FloatField(db_column='SampleCount', blank=True, null=True)  # Field name made lowercase.
    weightedc2i = models.FloatField(db_column='WeightedC2I', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbC2I'
        unique_together = (('scell', 'ncell'),)


class Tbcell(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', max_length=255)  # Field name made lowercase.
    enodebid = models.IntegerField(db_column='ENODEBID')  # Field name made lowercase.
    enodeb_name = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN')  # Field name made lowercase.
    pci = models.IntegerField(db_column='PCI')  # Field name made lowercase.
    pss = models.IntegerField(db_column='PSS', blank=True, null=True)  # Field name made lowercase.
    sss = models.IntegerField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    tac = models.IntegerField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='VENDOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE')  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE')  # Field name made lowercase.
    style = models.CharField(db_column='STYLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    azimuth = models.FloatField(db_column='AZIMUTH')  # Field name made lowercase.
    height = models.FloatField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    electtilt = models.FloatField(db_column='ELECTTILT', blank=True, null=True)  # Field name made lowercase.
    mechtilt = models.FloatField(db_column='MECHTILT', blank=True, null=True)  # Field name made lowercase.
    totletilt = models.FloatField(db_column='TOTLETILT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbCell'


class Tbhandover(models.Model):
    city = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scell = models.CharField(db_column='SCELL', primary_key=True, max_length=50)  # Field name made lowercase.
    ncell = models.CharField(db_column='NCELL', max_length=50)  # Field name made lowercase.
    hoatt = models.IntegerField(db_column='HOATT', blank=True, null=True)  # Field name made lowercase.
    hosucc = models.IntegerField(db_column='HOSUCC', blank=True, null=True)  # Field name made lowercase.
    hosuccrate = models.DecimalField(db_column='HOSUCCRATE', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbHandOver'
        unique_together = (('scell', 'ncell'),)


class Tbmrodata(models.Model):
    timestamp = models.CharField(db_column='TimeStamp', primary_key=True, max_length=30)  # Field name made lowercase.
    servingsector = models.CharField(db_column='ServingSector', max_length=50)  # Field name made lowercase.
    interferingsector = models.CharField(db_column='InterferingSector', max_length=50)  # Field name made lowercase.
    ltescrsrp = models.FloatField(db_column='LteScRSRP', blank=True, null=True)  # Field name made lowercase.
    ltencrsrp = models.FloatField(db_column='LteNcRSRP', blank=True, null=True)  # Field name made lowercase.
    ltencearfcn = models.IntegerField(db_column='LteNcEarfcn', blank=True, null=True)  # Field name made lowercase.
    ltencpci = models.SmallIntegerField(db_column='LteNcPci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbMROData'
        unique_together = (('timestamp', 'servingsector', 'interferingsector'),)


class Tboptcell(models.Model):
    sector_id = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    cell_type = models.CharField(db_column='CELL_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.     

    class Meta:
        managed = False
        db_table = 'tbOptCell'


class Tbpciassignment(models.Model):
    assign_id = models.SmallIntegerField(db_column='ASSIGN_ID', primary_key=True)  # Field name made lowercase.
    earfcn = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    sector_id = models.CharField(db_column='SECTOR_ID', max_length=50)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SECTOR_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    enodeb_id = models.IntegerField(db_column='ENODEB_ID', blank=True, null=True)  # Field name made lowercase.
    pci = models.IntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    pss = models.IntegerField(db_column='PSS', blank=True, null=True)  # Field name made lowercase.
    sss = models.IntegerField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    longititude = models.FloatField(db_column='LONGITITUDE', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='STYLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    opt_datetime = models.DateTimeField(db_column='OPT_DATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbPCIAssignment'
        unique_together = (('assign_id', 'sector_id'),)


class Tbsecadjcell(models.Model):
    s_sector_id = models.CharField(db_column='S_SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.      
    n_sector_id = models.CharField(db_column='N_SECTOR_ID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbSecAdjCell'
        unique_together = (('s_sector_id', 'n_sector_id'),)