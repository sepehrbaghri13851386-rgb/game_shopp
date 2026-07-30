from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_remove_profile_avatar_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        # حذف ستون سرکش 'dis' که در تاریخچه migration ها وجود نداشت
        # ولی به صورت دستی/ناقص روی دیتابیس واقعی (Render) ساخته شده بود
        migrations.RunSQL(
            sql='ALTER TABLE login_app_profile DROP COLUMN IF EXISTS dis;',
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]