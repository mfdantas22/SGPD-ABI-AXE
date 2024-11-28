# Generated by Django 5.1.1 on 2024-11-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abi', '0005_alter_agenda_age_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='pes_celular',
            field=models.CharField(default='00000000000', max_length=11, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='pes_email',
            field=models.CharField(default='example@example.com', max_length=255, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='pes_telefone',
            field=models.CharField(default='0000000000', max_length=10, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='age_descricao',
            field=models.TextField(max_length=500, verbose_name='Descrição'),
        ),
    ]