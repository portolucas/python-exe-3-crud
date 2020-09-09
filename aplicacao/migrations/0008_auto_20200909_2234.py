# Generated by Django 3.1.1 on 2020-09-09 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0007_pessoa_depto_chefia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cachorro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tem_cachorro', models.BooleanField()),
                ('nome_do_cahorro', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='tem_cachorro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='aplicacao.cachorro'),
        ),
    ]
