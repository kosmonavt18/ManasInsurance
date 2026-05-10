from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('clients', '0001_initial')]
    operations = [
        migrations.AlterField(
            model_name='clientproduct',
            name='kind',
            field=models.CharField(
                choices=[
                    ('life', 'Страхование жизни'),
                    ('travel', 'Страхование путешествий'),
                    ('health', 'Медицинское страхование'),
                    ('property', 'Страхование имущества'),
                ],
                default='life', max_length=20, verbose_name='Вид',
            ),
        ),
    ]
