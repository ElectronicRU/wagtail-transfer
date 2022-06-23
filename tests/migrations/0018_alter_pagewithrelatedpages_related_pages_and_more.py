# Generated by Django 4.0 on 2022-06-09 15:17

from django.db import migrations, models
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    import wagtail.blocks as wagtail_blocks
    import wagtail.fields as wagtail_fields
else:
    import wagtail.core.blocks as wagtail_blocks
    import wagtail.core.fields as wagtail_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0017_correctmodeltypes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagewithrelatedpages',
            name='related_pages',
            field=models.ManyToManyField(related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='pagewithstreamfield',
            name='body',
            field=wagtail_fields.StreamField([('link_block', wagtail_blocks.StructBlock([('page', wagtail_blocks.PageChooserBlock(required=False)), ('text', wagtail_blocks.CharBlock(max_length=250))])), ('integer', wagtail_blocks.IntegerBlock(required=True)), ('page', wagtail_blocks.PageChooserBlock()), ('stream', wagtail_blocks.StreamBlock([('page', wagtail_blocks.PageChooserBlock())])), ('rich_text', wagtail_blocks.RichTextBlock()), ('list_of_pages', wagtail_blocks.ListBlock(wagtail_blocks.PageChooserBlock())), ('list_of_captioned_pages', wagtail_blocks.ListBlock(wagtail_blocks.StructBlock([('page', wagtail_blocks.PageChooserBlock(required=False)), ('text', wagtail_blocks.CharBlock(max_length=250))])))], blank=True, verbose_name='Page body'),
        ),
    ]