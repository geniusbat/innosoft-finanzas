from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sugerencias',
            fields=[
                ('sugId', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugTipo', models.IntegerField(choices=[('tecnica'),('sugerenciaInnosoft')], default='tecnica')),
                ('sugUvus', models.CharField(max_length=10)),
                ('sugDescription', models.CharField(max_length=1000)),
            ],
        ),
    ]