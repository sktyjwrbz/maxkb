# Generated by Django 4.2.15 on 2024-11-22 14:44
from django.db.models import QuerySet

from django.db import migrations, models

import dataset
from common.event import ListenerManagement
from dataset.models import State, TaskType

sql = """
UPDATE "document"
SET status ="replace"("replace"("replace"(status, '2', '3'),'0','3'),'1','2')
"""
sql_paragraph = """
UPDATE "paragraph"
SET status ="replace"("replace"("replace"(status, '2', '3'),'0','3'),'1','2')
"""


def updateDocumentStatus(apps, schema_editor):
    DocumentModel = apps.get_model('dataset', 'Document')
    ListenerManagement.get_aggregation_document_status_by_query_set(QuerySet(DocumentModel))()


class Migration(migrations.Migration):
    dependencies = [
        ('dataset', '0010_file_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status_meta',
            field=models.JSONField(default=dataset.models.data_set.default_status_meta, verbose_name='状态统计数据'),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='status_meta',
            field=models.JSONField(default=dataset.models.data_set.default_status_meta, verbose_name='状态数据'),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(default=dataset.models.data_set.Status.__str__, max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='status',
            field=models.CharField(default=dataset.models.data_set.Status.__str__, max_length=20, verbose_name='状态'),
        ),
        migrations.RunSQL(sql_paragraph),
        migrations.RunSQL(sql),
        migrations.RunPython(updateDocumentStatus)
    ]
