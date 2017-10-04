from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    type = models.IntegerField()
    name = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()
    user = models.IntegerField()
    flag_del = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        db_table = 'articles'


class FlamplayerArtist(models.Model):
    id_artist = models.AutoField(primary_key=True)
    name_artist = models.CharField(max_length=40)
    email_artist = models.CharField(max_length=100, blank=True, null=True)
    website_artist = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'flamplayer_artists'


class FlamplayerMusic(models.Model):
    id_music = models.AutoField(primary_key=True)
    fk_artist = models.IntegerField()
    title_music = models.CharField(max_length=200)
    filename_music = models.CharField(max_length=255)
    playlist_music = models.CharField(max_length=16)
    date_music = models.DateTimeField()
    active_music = models.CharField(max_length=8)

    class Meta:
        db_table = 'flamplayer_musics'


class Keyword(models.Model):
    key = models.CharField(max_length=63)

    class Meta:
        db_table = 'keywords'


class Qwest(models.Model):
    type = models.IntegerField(blank=True, null=True)
    user = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    branch = models.IntegerField()
    top = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    flag_del = models.IntegerField()

    class Meta:
        db_table = 'qwests'


class StrArticle(models.Model):
    type = models.IntegerField()
    name = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()
    user = models.IntegerField()
    flag_del = models.IntegerField()
    count = models.IntegerField()
    view = models.IntegerField()
    plus = models.IntegerField()
    minus = models.IntegerField()
    money = models.IntegerField()
    flags = models.CharField(max_length=6)
    date_r = models.DateTimeField()

    class Meta:
        db_table = 'str_articles'


class StrComment(models.Model):
    text = models.TextField()

    class Meta:
        db_table = 'str_comments'


class StrErrorLog(models.Model):
    date = models.DateTimeField()
    status = models.IntegerField()
    text = models.TextField()
    arg = models.CharField(max_length=511)
    user = models.IntegerField()
    ip = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'str_error_log'


class StrKeyword(models.Model):
    key = models.CharField(max_length=63)

    class Meta:
        db_table = 'str_keywords'


class StrMoneyLog(models.Model):
    type = models.IntegerField()
    user_from = models.IntegerField()
    user_to = models.IntegerField()
    sum = models.IntegerField()
    point = models.IntegerField()
    date = models.DateTimeField()
    comment = models.IntegerField()
    story = models.IntegerField()

    class Meta:
        db_table = 'str_money_log'


class StrQwest(models.Model):
    type = models.IntegerField(blank=True, null=True)
    user = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    branch = models.IntegerField()
    top = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    flag_del = models.IntegerField()

    class Meta:
        db_table = 'str_qwests'


class StrResobj(models.Model):
    id_story = models.IntegerField()
    id_user = models.IntegerField()
    type = models.IntegerField()
    date = models.DateTimeField()
    expans = models.CharField(max_length=5)
    comment = models.CharField(max_length=255)
    date_r = models.DateTimeField()
    cluster = models.IntegerField()

    class Meta:
        db_table = 'str_resobj'


class StrText(models.Model):
    type = models.IntegerField()
    date = models.DateTimeField()
    user = models.IntegerField()
    name = models.TextField()
    text = models.TextField()
    flag_del = models.IntegerField()

    class Meta:
        db_table = 'str_texts'


class StrTooltip(models.Model):
    word = models.CharField(max_length=511)
    text = models.CharField(max_length=1023)
    flag_del = models.IntegerField()
    max_show = models.IntegerField()

    class Meta:
        db_table = 'str_tooltips'


class StrUser(models.Model):
    nick = models.CharField(max_length=63)
    date_reg = models.DateTimeField()
    first = models.CharField(max_length=63)
    last = models.CharField(max_length=63)
    pass_field = models.CharField(db_column='pass', max_length=80, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    session = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField()
    status = models.CharField(max_length=4)
    flag_del = models.IntegerField()
    wait = models.IntegerField()
    last_g = models.CharField(max_length=64)
    phone = models.CharField(max_length=63)
    favorit = models.IntegerField()
    money = models.IntegerField()

    class Meta:
        db_table = 'str_users'


class StrVisitorsWay(models.Model):
    sess_id = models.IntegerField(blank=True, null=True)
    referer = models.CharField(max_length=127)
    ip = models.CharField(max_length=12)
    user_id = models.IntegerField()
    time = models.DateTimeField()
    gg_id = models.IntegerField()
    article_id = models.IntegerField()

    class Meta:
        db_table = 'str_visitors_way'


class WkpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'wkp_commentmeta'


class WkpComment(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        db_table = 'wkp_comments'


class WkpLink(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        db_table = 'wkp_links'


class WkpOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    blog_id = models.IntegerField()
    option_name = models.CharField(unique=True, max_length=64)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        db_table = 'wkp_options'


class WkpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'wkp_postmeta'


class WkpPost(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        db_table = 'wkp_posts'


class WkpTermRelationship(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        db_table = 'wkp_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class WkpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        db_table = 'wkp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class WkpTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        db_table = 'wkp_terms'


class WkpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'wkp_usermeta'


class WkpUser(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=64)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=60)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        db_table = 'wkp_users'
