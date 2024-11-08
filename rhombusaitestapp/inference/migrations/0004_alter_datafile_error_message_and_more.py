# Generated by Django 5.1.2 on 2024-11-03 11:34

import inference.constants
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inference', '0003_alter_datafile_processing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafile',
            name='error_message',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='datafile',
            name='processing_status',
            field=models.CharField(choices=[(inference.constants.ProcessingStatus['IDLE'], 'Idle'), (inference.constants.ProcessingStatus['UPLOADING'], 'Uploading'), (inference.constants.ProcessingStatus['UPLOADED'], 'Upload Complete'), (inference.constants.ProcessingStatus['UPLOAD_FAILED'], 'Upload Failed'), (inference.constants.ProcessingStatus['INFERRING'], 'Inferring Types'), (inference.constants.ProcessingStatus['INFERRED'], 'Inference Complete'), (inference.constants.ProcessingStatus['INFERENCE_FAILED'], 'Inference Failed')], default=inference.constants.ProcessingStatus['IDLE'], max_length=20),
        ),
    ]
