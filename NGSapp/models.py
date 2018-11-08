from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models (tables in MySQL DB) here.

class Sample(models.Model):
    '''the sample describes the info about the sample before the library and RNAseq'''
    id = models.IntegerField(primary_key = True)
    # user = models.CharField(max_length=50)
    collectionDate = models.DateTimeField(blank=True, null = True)
    name = models.CharField(max_length=100, blank=True, null = True)
    organism = models.CharField(max_length=20, null=True)

class User(models.Model):
    id = models.IntegerField(primary_key = True)
    UserName = models.CharField(max_length = 50)
    UserRole = models.CharField(max_length = 50) 
    Email = models.CharField(max_length = 50)  
    Password = models.CharField(max_length = 50)  
    CreateTime = models.DateTimeField(max_length = 50) 
    ScientistInitials = models.CharField(max_length = 5) 

    '''tells us who is related to the experiment or 
    submitted the sequncing run'''

class LibraryIndex(models.Model):
    '''from sample to the corresponding library'''
    id = models.IntegerField(primary_key = True)
    IndexType = models.CharField(max_length = 50)

class LibraryPrep(models.Model):
    id = models.IntegerField(primary_key = True)
    LibraryPrepName = models.CharField(max_length = 200)

class Pool(models.Model):
    id = models.IntegerField(primary_key = True)
    PoolName = models.CharField(max_length = 200)

class Run(models.Model):
    '''A Next geenration sequncing run from NGS core'''
    id = models.IntegerField(primary_key = True)
    # user = models.CharField(max_length=50)
    runDate = models.DateTimeField(blank=True, null = True)
    FlowCell_ID = models.CharField(max_length = 10)
    ReagentsCartridge_Cycles = models.IntegerField
    ReagentsCartridge_Lot = models.CharField(max_length = 20)
    BufferCartridge_Lot = models.CharField(max_length = 20)
    Read_1 = models.IntegerField
    Read_2 = models.IntegerField
    Index_1 = models.IntegerField
    Index_2 = models.IntegerField
    RunName = models.CharField(max_length=100,   blank=True, null = True)
    ExportFolderName = models.CharField(max_length=100,   blank=True, null = True)
    PI = models.CharField(max_length=100, null=True)
    Investigator = models.CharField(max_length=50)
    ExperimentName = models.CharField(max_length=100)
    Reads = models.CharField(max_length=10)
    Assays = models.CharField(max_length=10)
    Protocol = models.CharField(max_length=10)
    ClusterDensity = models.CharField(max_length=10)
    Comments = models.CharField(max_length=300)
    Pool_id = models.ForeignKey(Pool, on_delete = models.CASCADE)