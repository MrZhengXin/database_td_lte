# Generated by Django 2.1.15 on 2020-07-31 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbadjcell',
            fields=[
                ('s_sector_id', models.CharField(db_column='S_SECTOR_ID', max_length=50, primary_key=True, serialize=False)),
                ('n_sector_id', models.CharField(db_column='N_SECTOR_ID', max_length=50)),
                ('s_earfcn', models.IntegerField(blank=True, db_column='S_EARFCN', null=True)),
                ('n_earfcn', models.IntegerField(blank=True, db_column='N_EARFCN', null=True)),
            ],
            options={
                'db_table': 'tbAdjCell',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbatuc2I',
            fields=[
                ('sector_id', models.CharField(db_column='SECTOR_ID', max_length=50, primary_key=True, serialize=False)),
                ('ncell_id', models.CharField(db_column='NCELL_ID', max_length=50)),
                ('ratio_all', models.FloatField(blank=True, db_column='RATIO_ALL', null=True)),
                ('rank', models.IntegerField(blank=True, db_column='RANK', null=True)),
                ('cosite', models.SmallIntegerField(blank=True, db_column='COSITE', null=True)),
            ],
            options={
                'db_table': 'tbATUC2I',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbatudata',
            fields=[
                ('seq', models.BigIntegerField(primary_key=True, serialize=False)),
                ('filename', models.CharField(db_column='FileName', max_length=255)),
                ('time', models.CharField(blank=True, db_column='Time', max_length=100, null=True)),
                ('longitude', models.FloatField(blank=True, db_column='Longitude', null=True)),
                ('latitude', models.FloatField(blank=True, db_column='Latitude', null=True)),
                ('cellid', models.CharField(blank=True, db_column='CellID', max_length=50, null=True)),
                ('tac', models.IntegerField(blank=True, db_column='TAC', null=True)),
                ('earfcn', models.IntegerField(blank=True, db_column='EARFCN', null=True)),
                ('pci', models.SmallIntegerField(blank=True, db_column='PCI', null=True)),
                ('rsrp', models.FloatField(blank=True, db_column='RSRP', null=True)),
                ('rs_sinr', models.FloatField(blank=True, db_column='RS_SINR', null=True)),
                ('ncell_id_1', models.CharField(blank=True, db_column='NCell_ID_1', max_length=50, null=True)),
                ('ncell_earfcn_1', models.IntegerField(blank=True, db_column='NCell_EARFCN_1', null=True)),
                ('ncell_pci_1', models.SmallIntegerField(blank=True, db_column='NCell_PCI_1', null=True)),
                ('ncell_rsrp_1', models.FloatField(blank=True, db_column='NCell_RSRP_1', null=True)),
                ('ncell_id_2', models.CharField(blank=True, db_column='NCell_ID_2', max_length=50, null=True)),
                ('ncell_earfcn_2', models.IntegerField(blank=True, db_column='NCell_EARFCN_2', null=True)),
                ('ncell_pci_2', models.SmallIntegerField(blank=True, db_column='NCell_PCI_2', null=True)),
                ('ncell_rsrp_2', models.FloatField(blank=True, db_column='NCell_RSRP_2', null=True)),
                ('ncell_id_3', models.CharField(blank=True, db_column='NCell_ID_3', max_length=50, null=True)),
                ('ncell_earfcn_3', models.IntegerField(blank=True, db_column='NCell_EARFCN_3', null=True)),
                ('ncell_pci_3', models.SmallIntegerField(blank=True, db_column='NCell_PCI_3', null=True)),
                ('ncell_rsrp_3', models.FloatField(blank=True, db_column='NCell_RSRP_3', null=True)),
                ('ncell_id_4', models.CharField(blank=True, db_column='NCell_ID_4', max_length=50, null=True)),
                ('ncell_earfcn_4', models.IntegerField(blank=True, db_column='NCell_EARFCN_4', null=True)),
                ('ncell_pci_4', models.SmallIntegerField(blank=True, db_column='NCell_PCI_4', null=True)),
                ('ncell_rsrp_4', models.FloatField(blank=True, db_column='NCell_RSRP_4', null=True)),
                ('ncell_id_5', models.CharField(blank=True, db_column='NCell_ID_5', max_length=50, null=True)),
                ('ncell_earfcn_5', models.IntegerField(blank=True, db_column='NCell_EARFCN_5', null=True)),
                ('ncell_pci_5', models.SmallIntegerField(blank=True, db_column='NCell_PCI_5', null=True)),
                ('ncell_rsrp_5', models.FloatField(blank=True, db_column='NCell_RSRP_5', null=True)),
                ('ncell_id_6', models.CharField(blank=True, db_column='NCell_ID_6', max_length=50, null=True)),
                ('ncell_earfcn_6', models.IntegerField(blank=True, db_column='NCell_EARFCN_6', null=True)),
                ('ncell_pci_6', models.SmallIntegerField(blank=True, db_column='NCell_PCI_6', null=True)),
                ('ncell_rsrp_6', models.FloatField(blank=True, db_column='NCell_RSRP_6', null=True)),
            ],
            options={
                'db_table': 'tbATUData',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbatuhandover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssector_id', models.CharField(blank=True, db_column='SSECTOR_ID', max_length=50, null=True)),
                ('nsector_id', models.CharField(blank=True, db_column='NSECTOR_ID', max_length=50, null=True)),
                ('hoatt', models.IntegerField(blank=True, db_column='HOATT', null=True)),
            ],
            options={
                'db_table': 'tbATUHandOver',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbc2I',
            fields=[
                ('city', models.CharField(blank=True, db_column='CITY', max_length=255, null=True)),
                ('scell', models.CharField(db_column='SCELL', max_length=255, primary_key=True, serialize=False)),
                ('ncell', models.CharField(db_column='NCELL', max_length=255)),
                ('prc2i9', models.FloatField(blank=True, db_column='PrC2I9', null=True)),
                ('c2i_mean', models.FloatField(blank=True, db_column='C2I_Mean', null=True)),
                ('std', models.FloatField(blank=True, db_column='Std', null=True)),
                ('samplecount', models.FloatField(blank=True, db_column='SampleCount', null=True)),
                ('weightedc2i', models.FloatField(blank=True, db_column='WeightedC2I', null=True)),
            ],
            options={
                'db_table': 'tbC2I',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbcell',
            fields=[
                ('city', models.CharField(blank=True, db_column='CITY', max_length=255, null=True)),
                ('sector_id', models.CharField(db_column='SECTOR_ID', max_length=50, primary_key=True, serialize=False)),
                ('sector_name', models.CharField(db_column='SECTOR_NAME', max_length=255)),
                ('enodebid', models.IntegerField(db_column='ENODEBID')),
                ('enodeb_name', models.CharField(db_column='ENODEB_NAME', max_length=255)),
                ('earfcn', models.IntegerField(db_column='EARFCN')),
                ('pci', models.IntegerField(db_column='PCI')),
                ('pss', models.IntegerField(blank=True, db_column='PSS', null=True)),
                ('sss', models.IntegerField(blank=True, db_column='SSS', null=True)),
                ('tac', models.IntegerField(blank=True, db_column='TAC', null=True)),
                ('vendor', models.CharField(blank=True, db_column='VENDOR', max_length=255, null=True)),
                ('longitude', models.FloatField(db_column='LONGITUDE')),
                ('latitude', models.FloatField(db_column='LATITUDE')),
                ('style', models.CharField(blank=True, db_column='STYLE', max_length=255, null=True)),
                ('azimuth', models.FloatField(db_column='AZIMUTH')),
                ('height', models.FloatField(blank=True, db_column='HEIGHT', null=True)),
                ('electtilt', models.FloatField(blank=True, db_column='ELECTTILT', null=True)),
                ('mechtilt', models.FloatField(blank=True, db_column='MECHTILT', null=True)),
                ('totletilt', models.FloatField(db_column='TOTLETILT')),
            ],
            options={
                'db_table': 'tbCell',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbhandover',
            fields=[
                ('city', models.CharField(blank=True, db_column='CITY', max_length=255, null=True)),
                ('scell', models.CharField(db_column='SCELL', max_length=50, primary_key=True, serialize=False)),
                ('ncell', models.CharField(db_column='NCELL', max_length=50)),
                ('hoatt', models.IntegerField(blank=True, db_column='HOATT', null=True)),
                ('hosucc', models.IntegerField(blank=True, db_column='HOSUCC', null=True)),
                ('hosuccrate', models.DecimalField(blank=True, db_column='HOSUCCRATE', decimal_places=4, max_digits=7, null=True)),
            ],
            options={
                'db_table': 'tbHandOver',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbmrodata',
            fields=[
                ('timestamp', models.CharField(db_column='TimeStamp', max_length=30, primary_key=True, serialize=False)),
                ('servingsector', models.CharField(db_column='ServingSector', max_length=50)),
                ('interferingsector', models.CharField(db_column='InterferingSector', max_length=50)),
                ('ltescrsrp', models.FloatField(blank=True, db_column='LteScRSRP', null=True)),
                ('ltencrsrp', models.FloatField(blank=True, db_column='LteNcRSRP', null=True)),
                ('ltencearfcn', models.IntegerField(blank=True, db_column='LteNcEarfcn', null=True)),
                ('ltencpci', models.SmallIntegerField(blank=True, db_column='LteNcPci', null=True)),
            ],
            options={
                'db_table': 'tbMROData',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tboptcell',
            fields=[
                ('sector_id', models.CharField(db_column='SECTOR_ID', max_length=50, primary_key=True, serialize=False)),
                ('earfcn', models.IntegerField(blank=True, db_column='EARFCN', null=True)),
                ('cell_type', models.CharField(blank=True, db_column='CELL_TYPE', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tbOptCell',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbpciassignment',
            fields=[
                ('assign_id', models.SmallIntegerField(db_column='ASSIGN_ID', primary_key=True, serialize=False)),
                ('earfcn', models.IntegerField(blank=True, db_column='EARFCN', null=True)),
                ('sector_id', models.CharField(db_column='SECTOR_ID', max_length=50)),
                ('sector_name', models.CharField(blank=True, db_column='SECTOR_NAME', max_length=200, null=True)),
                ('enodeb_id', models.IntegerField(blank=True, db_column='ENODEB_ID', null=True)),
                ('pci', models.IntegerField(blank=True, db_column='PCI', null=True)),
                ('pss', models.IntegerField(blank=True, db_column='PSS', null=True)),
                ('sss', models.IntegerField(blank=True, db_column='SSS', null=True)),
                ('longititude', models.FloatField(blank=True, db_column='LONGITITUDE', null=True)),
                ('style', models.CharField(blank=True, db_column='STYLE', max_length=50, null=True)),
                ('opt_datetime', models.DateTimeField(blank=True, db_column='OPT_DATETIME', null=True)),
            ],
            options={
                'db_table': 'tbPCIAssignment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tbsecadjcell',
            fields=[
                ('s_sector_id', models.CharField(db_column='S_SECTOR_ID', max_length=50, primary_key=True, serialize=False)),
                ('n_sector_id', models.CharField(db_column='N_SECTOR_ID', max_length=50)),
            ],
            options={
                'db_table': 'tbSecAdjCell',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
