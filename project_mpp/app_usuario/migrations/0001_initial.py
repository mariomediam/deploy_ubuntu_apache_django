# Generated by Django 3.2.9 on 2021-12-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('c_usuari_login', models.CharField(db_column='C_Usuari_Login', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.BinaryField(db_column='N_Usuari_Clave', max_length='max', null=True)),
                ('n_usuari_nombre', models.CharField(db_column='N_Usuari_Nombre', max_length=60)),
                ('is_active', models.BooleanField(db_column='F_Usuari_Activo', default=False)),
                ('is_staff', models.BooleanField(db_column='F_Usuari_Admin', default=False)),
                ('d_usuari_fecini', models.DateTimeField(db_column='D_Usuari_FecIni')),
                ('d_usuari_fecfin', models.DateTimeField(db_column='D_Usuari_FecFin')),
                ('c_usuari_resp', models.CharField(db_column='C_Usuari_Resp', max_length=20)),
                ('d_usuari_fecdig', models.DateTimeField(db_column='D_Usuari_FecDig')),
                ('c_usucodi', models.CharField(db_column='C_Usucodi', max_length=4, null=True)),
                ('c_usucold', models.CharField(db_column='C_UsuCold', max_length=6, null=True)),
                ('f_usuari_snp', models.BooleanField(db_column='F_Usuari_SNP', default=False, null=True)),
                ('m_usuari_dni', models.CharField(db_column='M_Usuari_DNI', max_length=8, null=True)),
                ('n_usuari_resppc', models.CharField(db_column='N_Usuari_RespPC', max_length=20, null=True)),
                ('n_usuari_clavesgad', models.CharField(db_column='N_Usuari_claveSGAD', max_length=150, null=True)),
                ('f_usuari_fiscal', models.BooleanField(db_column='F_Usuari_Fiscal', default=False)),
                ('last_login', models.DateTimeField(db_column='last_login')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
