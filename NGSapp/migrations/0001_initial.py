# Generated by Django 2.0.8 on 2018-11-08 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryIndex',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('IndexType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryPrep',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('LibraryPrepName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('PoolName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('runDate', models.DateTimeField(blank=True, null=True)),
                ('FlowCell_ID', models.CharField(max_length=10)),
                ('ReagentsCartridge_Lot', models.CharField(max_length=20)),
                ('BufferCartridge_Lot', models.CharField(max_length=20)),
                ('RunName', models.CharField(blank=True, max_length=100, null=True)),
                ('ExportFolderName', models.CharField(blank=True, max_length=100, null=True)),
                ('PI', models.CharField(max_length=100, null=True)),
                ('Investigator', models.CharField(max_length=50)),
                ('ExperimentName', models.CharField(max_length=100)),
                ('Reads', models.CharField(max_length=10)),
                ('Assays', models.CharField(max_length=10)),
                ('Protocol', models.CharField(max_length=10)),
                ('ClusterDensity', models.CharField(max_length=10)),
                ('Comments', models.CharField(max_length=300)),
                ('Pool_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NGSapp.Pool')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('collectionDate', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('organism', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=50)),
                ('UserRole', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('CreateTime', models.DateTimeField(max_length=50)),
                ('ScientistInitials', models.CharField(max_length=5)),
            ],
        ),
    ]
