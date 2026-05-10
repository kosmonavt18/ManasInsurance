from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('applications', '0001_initial')]
    operations = [
        migrations.AddField(
            model_name='application',
            name='tech_passport',
            field=models.ImageField(blank=True, null=True, upload_to='tech_passports/',
                                    verbose_name='Тех. паспорт (для авто)'),
        ),
    ]
