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
    docfile = models.FileField()

class Post(models.Model):
    file = models.FileField(upload_to='media/', null=True)

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

class Tbatuc2I(models.Model):
    SECTOR_ID = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    ncell_id = models.CharField(db_column='ncell_id', max_length=50)  # Field name made lowercase.
    RATIO_ALL = models.FloatField(db_column='RATIO_ALL', blank=True, null=True)  # Field name made lowercase.
    RANK = models.IntegerField(db_column='RANK', blank=True, null=True)  # Field name made lowercase.
    COSITE = models.SmallIntegerField(db_column='COSITE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUC2I'
        unique_together = (('SECTOR_ID', 'ncell_id'),)


class Tbatudata(models.Model):
    seq = models.BigIntegerField(primary_key=True)
    filename = models.CharField(db_column='FileName', max_length=255)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    cellid = models.CharField(db_column='CellID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tac = models.IntegerField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    EARFCN = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    PCI = models.SmallIntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    rsrp = models.FloatField(db_column='RSRP', blank=True, null=True)  # Field name made lowercase.
    rs_sinr = models.FloatField(db_column='RS_SINR', blank=True, null=True)  # Field name made lowercase.
    ncell_id_1 = models.CharField(db_column='ncell_id_1', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_1 = models.IntegerField(db_column='NCell_EARFCN_1', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_1 = models.SmallIntegerField(db_column='NCell_PCI_1', blank=True, null=True)  # Field name made lowercase.        
    ncell_rsrp_1 = models.FloatField(db_column='NCell_RSRP_1', blank=True, null=True)  # Field name made lowercase.
    ncell_id_2 = models.CharField(db_column='ncell_id_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ncell_earfcn_2 = models.IntegerField(db_column='NCell_EARFCN_2', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_2 = models.SmallIntegerField(db_column='NCell_PCI_2', blank=True, null=True)  # Field name made lowercase.        
    ncell_rsrp_2 = models.FloatField(db_column='NCell_RSRP_2', blank=True, null=True)  # Field name made lowercase.
    ncell_id_3 = models.CharField(db_column='ncell_id_3', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_3 = models.IntegerField(db_column='NCell_EARFCN_3', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_3 = models.SmallIntegerField(db_column='NCell_PCI_3', blank=True, null=True)  # Field name made lowercase.        
    ncell_rsrp_3 = models.FloatField(db_column='NCell_RSRP_3', blank=True, null=True)  # Field name made lowercase.
    ncell_id_4 = models.CharField(db_column='ncell_id_4', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_4 = models.IntegerField(db_column='NCell_EARFCN_4', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_4 = models.SmallIntegerField(db_column='NCell_PCI_4', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_4 = models.FloatField(db_column='NCell_RSRP_4', blank=True, null=True)  # Field name made lowercase.
    ncell_id_5 = models.CharField(db_column='ncell_id_5', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_5 = models.IntegerField(db_column='NCell_EARFCN_5', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_5 = models.SmallIntegerField(db_column='NCell_PCI_5', blank=True, null=True)  # Field name made lowercase.        
    ncell_rsrp_5 = models.FloatField(db_column='NCell_RSRP_5', blank=True, null=True)  # Field name made lowercase.
    ncell_id_6 = models.CharField(db_column='ncell_id_6', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    ncell_earfcn_6 = models.IntegerField(db_column='NCell_EARFCN_6', blank=True, null=True)  # Field name made lowercase.       
    ncell_pci_6 = models.SmallIntegerField(db_column='NCell_PCI_6', blank=True, null=True)  # Field name made lowercase.
    ncell_rsrp_6 = models.FloatField(db_column='NCell_RSRP_6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUData'
        unique_together = (('seq', 'filename'),)


class Tbatuhandover(models.Model):
    SSECTOR_ID = models.CharField(db_column='SSECTOR_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.   
    NSECTOR_ID = models.CharField(db_column='NSECTOR_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    HOATT = models.IntegerField(db_column='HOATT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbATUHandOver'


class Tbadjcell(models.Model):
    S_SECTOR_ID = models.CharField(db_column='S_SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.      
    N_SECTOR_ID = models.CharField(db_column='N_SECTOR_ID', max_length=50)  # Field name made lowercase.
    S_EARFCN = models.IntegerField(db_column='S_EARFCN', blank=True, null=True)  # Field name made lowercase.
    N_EARFCN = models.IntegerField(db_column='N_EARFCN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbAdjCell'
        unique_together = (('S_SECTOR_ID', 'N_SECTOR_ID'),)


class Tbc2I(models.Model):
    CITY = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    SCELL = models.CharField(db_column='SCELL', primary_key=True, max_length=255)  # Field name made lowercase.
    NCELL = models.CharField(db_column='NCELL', max_length=255)  # Field name made lowercase.
    PrC2I9 = models.FloatField(db_column='PrC2I9', blank=True, null=True)  # Field name made lowercase.
    C2I_Mean = models.FloatField(db_column='C2I_Mean', blank=True, null=True)  # Field name made lowercase.
    Std = models.FloatField(db_column='Std', blank=True, null=True)  # Field name made lowercase.
    SampleCount = models.FloatField(db_column='SampleCount', blank=True, null=True)  # Field name made lowercase.
    WeightedC2I = models.FloatField(db_column='WeightedC2I', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbC2I'
        unique_together = (('SCELL', 'NCELL'),)


class Tbcell(models.Model):
    CITY = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    SECTOR_ID = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    SECTOR_NAME = models.CharField(db_column='SECTOR_NAME', max_length=255)  # Field name made lowercase.
    ENODEBID = models.IntegerField(db_column='ENODEBID')  # Field name made lowercase.
    ENODEB_NAME = models.CharField(db_column='ENODEB_NAME', max_length=255)  # Field name made lowercase.
    EARFCN = models.IntegerField(db_column='EARFCN')  # Field name made lowercase.
    PCI = models.IntegerField(db_column='PCI')  # Field name made lowercase.
    PSS = models.IntegerField(db_column='PSS', blank=True, null=True)  # Field name made lowercase.
    SSS = models.IntegerField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    TAC = models.IntegerField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    VENDOR = models.CharField(db_column='VENDOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    LONGITUDE = models.FloatField(db_column='LONGITUDE')  # Field name made lowercase.
    LATITUDE = models.FloatField(db_column='LATITUDE')  # Field name made lowercase.
    STYLE = models.CharField(db_column='STYLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    AZIMUTH = models.FloatField(db_column='AZIMUTH')  # Field name made lowercase.
    HEIGHT = models.FloatField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    ELECTTILT = models.FloatField(db_column='ELECTTILT', blank=True, null=True)  # Field name made lowercase.
    MECHTILT = models.FloatField(db_column='MECHTILT', blank=True, null=True)  # Field name made lowercase.
    TOTLETILT = models.FloatField(db_column='TOTLETILT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbCell'


class Tbhandover(models.Model):
    CITY = models.CharField(db_column='CITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    SCELL = models.CharField(db_column='SCELL', primary_key=True, max_length=50)  # Field name made lowercase.
    NCELL = models.CharField(db_column='NCELL', max_length=50)  # Field name made lowercase.
    HOATT = models.IntegerField(db_column='HOATT', blank=True, null=True)  # Field name made lowercase.
    HOSUCC = models.IntegerField(db_column='HOSUCC', blank=True, null=True)  # Field name made lowercase.
    HOSUCCRATE = models.DecimalField(db_column='HOSUCCRATE', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbHandOver'
        unique_together = (('SCELL', 'NCELL'),)


class Tbmrodata(models.Model):
    TimeStamp = models.CharField(db_column='TimeStamp', primary_key=True, max_length=30)  # Field name made lowercase.
    ServingSector = models.CharField(db_column='ServingSector', max_length=50)  # Field name made lowercase.
    InterferingSector = models.CharField(db_column='InterferingSector', max_length=50)  # Field name made lowercase.
    LteScRSRP = models.FloatField(db_column='LteScRSRP', blank=True, null=True)  # Field name made lowercase.
    LteNcRSRP = models.FloatField(db_column='LteNcRSRP', blank=True, null=True)  # Field name made lowercase.
    LteNcEarfcn = models.IntegerField(db_column='LteNcEarfcn', blank=True, null=True)  # Field name made lowercase.
    LteNcPci = models.SmallIntegerField(db_column='LteNcPci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbMROData'
        unique_together = (('TimeStamp', 'ServingSector', 'InterferingSector'),)


class Tboptcell(models.Model):
    SECTOR_ID = models.CharField(db_column='SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    EARFCN = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    cell_type = models.CharField(db_column='CELL_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.     

    class Meta:
        managed = False
        db_table = 'tbOptCell'


class Tbpciassignment(models.Model):
    ASSIGN_ID = models.SmallIntegerField(db_column='ASSIGN_ID', primary_key=True)  # Field name made lowercase.
    EARFCN = models.IntegerField(db_column='EARFCN', blank=True, null=True)  # Field name made lowercase.
    SECTOR_ID = models.CharField(db_column='SECTOR_ID', max_length=50)  # Field name made lowercase.
    SECTOR_NAME = models.CharField(db_column='SECTOR_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ENODEB_ID = models.IntegerField(db_column='ENODEB_ID', blank=True, null=True)  # Field name made lowercase.
    PCI = models.IntegerField(db_column='PCI', blank=True, null=True)  # Field name made lowercase.
    PSS = models.IntegerField(db_column='PSS', blank=True, null=True)  # Field name made lowercase.
    SSS = models.IntegerField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    LONGITITUDE = models.FloatField(db_column='LONGITITUDE', blank=True, null=True)  # Field name made lowercase.
    STYLE = models.CharField(db_column='STYLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    OPT_DATETIME = models.DateTimeField(db_column='OPT_DATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbPCIAssignment'
        unique_together = (('ASSIGN_ID', 'SECTOR_ID'),)


class Tbsecadjcell(models.Model):
    S_SECTOR_ID = models.CharField(db_column='S_SECTOR_ID', primary_key=True, max_length=50)  # Field name made lowercase.      
    N_SECTOR_ID = models.CharField(db_column='N_SECTOR_ID', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbSecAdjCell'
        unique_together = (('S_SECTOR_ID', 'N_SECTOR_ID'),)

class Tbprb(models.Model):
    起始时间 = models.CharField(max_length=255, blank=True, primary_key =True)
    周期 = models.CharField(max_length=255, blank=True, null=True)
    网元名称 = models.CharField(max_length=255, blank=True, null=True)
    小区 = models.CharField(max_length=255, blank=True, null=True)
    小区名 = models.CharField(max_length=255, blank=True, null=True)
    第0个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第0个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第1个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第1个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第2个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第2个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第3个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第3个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第4个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第4个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第5个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第5个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第6个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第6个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第7个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第7个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第8个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第8个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第9个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第9个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第10个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第10个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第11个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第11个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第12个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第12个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第13个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第13个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第14个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第14个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第15个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第15个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第16个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第16个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第17个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第17个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第18个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第18个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第19个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第19个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第20个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第20个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第21个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第21个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第22个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第22个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第23个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第23个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第24个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第24个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第25个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第25个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第26个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第26个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第27个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第27个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第28个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第28个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第29个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第29个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第30个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第30个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第31个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第31个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第32个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第32个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第33个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第33个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第34个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第34个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第35个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第35个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第36个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第36个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第37个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第37个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第38个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第38个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第39个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第39个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第40个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第40个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第41个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第41个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第42个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第42个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第43个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第43个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第44个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第44个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第45个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第45个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第46个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第46个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第47个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第47个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第48个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第48个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第49个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第49个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第50个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第50个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第51个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第51个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第52个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第52个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第53个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第53个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第54个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第54个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第55个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第55个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第56个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第56个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第57个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第57个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第58个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第58个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第59个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第59个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第60个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第60个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第61个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第61个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第62个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第62个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第63个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第63个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第64个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第64个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第65个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第65个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第66个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第66个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第67个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第67个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第68个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第68个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第69个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第69个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第70个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第70个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第71个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第71个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第72个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第72个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第73个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第73个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第74个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第74个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第75个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第75个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第76个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第76个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第77个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第77个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第78个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第78个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第79个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第79个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第80个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第80个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第81个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第81个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第82个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第82个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第83个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第83个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第84个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第84个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第85个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第85个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第86个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第86个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第87个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第87个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第88个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第88个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第89个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第89个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第90个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第90个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第91个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第91个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第92个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第92个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第93个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第93个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第94个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第94个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第95个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第95个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第96个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第96个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第97个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第97个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第98个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第98个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    第99个prb上检测到的干扰噪声的平均值_field = models.CharField(db_column='第99个PRB上检测到的干扰噪声的平均值_field', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbPRB'
        unique_together = (('起始时间',	'周期',	'网元名称',	'小区',	'小区名'), )

class Tbkpi(models.Model):
    起始时间 = models.CharField(max_length=255, blank=True, primary_key=True)
    周期 = models.CharField(max_length=255, blank=True, null=True)
    网元名称 = models.CharField(max_length=255, blank=True, null=True)
    小区 = models.CharField(max_length=255, blank=True, null=True)
    小区1 = models.CharField(max_length=255, blank=True, null=True)
    rrc连接建立完成次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    rrc连接请求次数_包括重发_无_field = models.CharField(max_length=255, blank=True, null=True)
    rrc建立成功率qf_field = models.CharField(max_length=255, blank=True, null=True)
    e_rab建立成功总次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    e_rab建立尝试总次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    e_rab建立成功率2_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb触发的e_rab异常释放总次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    小区切换出e_rab异常释放总次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    e_rab掉线率_新_field = models.CharField(max_length=255, blank=True, null=True)
    无线接通率ay_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb发起的s1_reset导致的ue_context释放次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    ue_context异常释放次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    ue_context建立成功总次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    无线掉线率_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb内异频切换出成功次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb内异频切换出尝试次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb内同频切换出成功次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb内同频切换出尝试次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb间异频切换出成功次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb间异频切换出尝试次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb间同频切换出成功次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enodeb间同频切换出尝试次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enb内切换成功率_field = models.CharField(max_length=255, blank=True, null=True)
    enb间切换成功率_field = models.CharField(max_length=255, blank=True, null=True)
    同频切换成功率zsp_field = models.CharField(max_length=255, blank=True, null=True)
    异频切换成功率zsp_field = models.CharField(max_length=255, blank=True, null=True)
    切换成功率_field = models.CharField(max_length=255, blank=True, null=True)
    小区pdcp层所接收到的上行数据的总吞吐量_比特_field = models.CharField(max_length=255, blank=True, null=True)
    小区pdcp层所发送的下行数据的总吞吐量_比特_field = models.CharField(max_length=255, blank=True, null=True)
    rrc重建请求次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    rrc连接重建比率_field = models.CharField(max_length=255, blank=True, null=True)
    通过重建回源小区的enodeb间同频切换出执行成功次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    通过重建回源小区的enodeb间异频切换出执行成功次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    通过重建回源小区的enodeb内同频切换出执行成功次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    通过重建回源小区的enodeb内异频切换出执行成功次数_无_field = models.CharField(max_length=255, blank=True, null=True)
    enb内切换出成功次数_次_field = models.CharField(max_length=255, blank=True, null=True)
    enb内切换出请求次数_次_field = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbKPI'
        unique_together = (('起始时间',	'周期',	'网元名称',	'小区',	'小区1'),)
