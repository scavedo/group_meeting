# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'meeting_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'meeting', ['UserProfile'])

        # Adding model 'Project'
        db.create_table(u'meeting_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['meeting.UserProfile'])),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'meeting', ['Project'])

        # Adding M2M table for field users on 'Project'
        m2m_table_name = db.shorten_name(u'meeting_project_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'meeting.project'], null=False)),
            ('userprofile', models.ForeignKey(orm[u'meeting.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'userprofile_id'])

        # Adding model 'Note'
        db.create_table(u'meeting_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 8, 0, 0))),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'meeting', ['Note'])

        # Adding model 'File'
        db.create_table(u'meeting_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 8, 0, 0))),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'meeting', ['File'])

        # Adding model 'Meeting'
        db.create_table(u'meeting_meeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 8, 0, 0))),
            ('date_begin', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_end', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'meeting', ['Meeting'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'meeting_userprofile')

        # Deleting model 'Project'
        db.delete_table(u'meeting_project')

        # Removing M2M table for field users on 'Project'
        db.delete_table(db.shorten_name(u'meeting_project_users'))

        # Deleting model 'Note'
        db.delete_table(u'meeting_note')

        # Deleting model 'File'
        db.delete_table(u'meeting_file')

        # Deleting model 'Meeting'
        db.delete_table(u'meeting_meeting')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'meeting.file': {
            'Meta': {'object_name': 'File'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 8, 0, 0)'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'meeting.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 8, 0, 0)'}),
            'date_begin': ('django.db.models.fields.DateTimeField', [], {}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'meeting.note': {
            'Meta': {'object_name': 'Note'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 8, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'meeting.project': {
            'Meta': {'object_name': 'Project'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['meeting.UserProfile']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users'", 'symmetrical': 'False', 'to': u"orm['meeting.UserProfile']"})
        },
        u'meeting.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['meeting']