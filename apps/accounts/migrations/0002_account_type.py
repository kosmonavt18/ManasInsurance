from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('accounts', '0001_initial')]
    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(
                choices=[('individual', 'Физическое лицо'), ('company', 'Компания')],
                default='individual', max_length=20, verbose_name='Тип аккаунта'),
        ),
        migrations.AddField(
            model_name='user',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название компании'),
        ),
    ]
