# Generated by Django 3.1.8 on 2021-05-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_zinnia', '0004_fix_empty_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryentriesplugin',
            name='template_to_render',
            field=models.CharField(
                blank=True,
                choices=[
                    ('cmsplugin_zinnia/entry_list.html', 'Entry list (default)'),
                    ('cmsplugin_zinnia/entry_detail.html', 'Entry detailed'),
                    ('cmsplugin_zinnia/entry_slider.html', 'Entry slider'),
                ],
                default='cmsplugin_zinnia/entry_list.html',
                help_text='template used to display the plugin',
                max_length=250,
                verbose_name='template',
            ),
        ),
        migrations.AlterField(
            model_name='randomentriesplugin',
            name='template_to_render',
            field=models.CharField(
                blank=True,
                choices=[
                    ('cmsplugin_zinnia/entry_list.html', 'Entry list (default)'),
                    ('cmsplugin_zinnia/entry_detail.html', 'Entry detailed'),
                    ('cmsplugin_zinnia/entry_slider.html', 'Entry slider'),
                ],
                default='cmsplugin_zinnia/entry_list.html',
                help_text='template used to display the plugin',
                max_length=250,
                verbose_name='template',
            ),
        ),
        migrations.AlterField(
            model_name='selectedentriesplugin',
            name='template_to_render',
            field=models.CharField(
                blank=True,
                choices=[
                    ('cmsplugin_zinnia/entry_list.html', 'Entry list (default)'),
                    ('cmsplugin_zinnia/entry_detail.html', 'Entry detailed'),
                    ('cmsplugin_zinnia/entry_slider.html', 'Entry slider'),
                ],
                default='cmsplugin_zinnia/entry_list.html',
                help_text='template used to display the plugin',
                max_length=250,
                verbose_name='template',
            ),
        ),
    ]
