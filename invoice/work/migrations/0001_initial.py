# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Span'
        db.create_table(u'work_span', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'work', ['Span'])

        # Adding model 'Task'
        db.create_table(u'work_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'work', ['Task'])

        # Adding M2M table for field hours on 'Task'
        m2m_table_name = db.shorten_name(u'work_task_hours')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm[u'work.task'], null=False)),
            ('span', models.ForeignKey(orm[u'work.span'], null=False))
        ))
        db.create_unique(m2m_table_name, ['task_id', 'span_id'])

        # Adding model 'Contacts'
        db.create_table(u'work_contacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'work', ['Contacts'])

        # Adding model 'Company'
        db.create_table(u'work_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=125)),
        ))
        db.send_create_signal(u'work', ['Company'])

        # Adding M2M table for field contacts on 'Company'
        m2m_table_name = db.shorten_name(u'work_company_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'work.company'], null=False)),
            ('contacts', models.ForeignKey(orm[u'work.contacts'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'contacts_id'])

        # Adding model 'WorkDay'
        db.create_table(u'work_workday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['work.Company'])),
            ('hourly_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'work', ['WorkDay'])

        # Adding M2M table for field tasks on 'WorkDay'
        m2m_table_name = db.shorten_name(u'work_workday_tasks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workday', models.ForeignKey(orm[u'work.workday'], null=False)),
            ('task', models.ForeignKey(orm[u'work.task'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workday_id', 'task_id'])

        # Adding model 'WorkMonth'
        db.create_table(u'work_workmonth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('month', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'work', ['WorkMonth'])

        # Adding M2M table for field work_days on 'WorkMonth'
        m2m_table_name = db.shorten_name(u'work_workmonth_work_days')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workmonth', models.ForeignKey(orm[u'work.workmonth'], null=False)),
            ('workday', models.ForeignKey(orm[u'work.workday'], null=False))
        ))
        db.create_unique(m2m_table_name, ['workmonth_id', 'workday_id'])


    def backwards(self, orm):
        # Deleting model 'Span'
        db.delete_table(u'work_span')

        # Deleting model 'Task'
        db.delete_table(u'work_task')

        # Removing M2M table for field hours on 'Task'
        db.delete_table(db.shorten_name(u'work_task_hours'))

        # Deleting model 'Contacts'
        db.delete_table(u'work_contacts')

        # Deleting model 'Company'
        db.delete_table(u'work_company')

        # Removing M2M table for field contacts on 'Company'
        db.delete_table(db.shorten_name(u'work_company_contacts'))

        # Deleting model 'WorkDay'
        db.delete_table(u'work_workday')

        # Removing M2M table for field tasks on 'WorkDay'
        db.delete_table(db.shorten_name(u'work_workday_tasks'))

        # Deleting model 'WorkMonth'
        db.delete_table(u'work_workmonth')

        # Removing M2M table for field work_days on 'WorkMonth'
        db.delete_table(db.shorten_name(u'work_workmonth_work_days'))


    models = {
        u'work.company': {
            'Meta': {'object_name': 'Company'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['work.Contacts']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '125'})
        },
        u'work.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'work.span': {
            'Meta': {'object_name': 'Span'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'work.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'hours': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['work.Span']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        u'work.workday': {
            'Meta': {'object_name': 'WorkDay'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['work.Company']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'hourly_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'tasks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['work.Task']", 'symmetrical': 'False'})
        },
        u'work.workmonth': {
            'Meta': {'object_name': 'WorkMonth'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'work_days': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['work.WorkDay']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['work']