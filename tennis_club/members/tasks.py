
from celery import Celery
from akismet import Akismet
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import Site
from . import models

app = Celery(broker='amqp://')

@app.task
def spam_filter(comment_id, remote_addr=None):
    logger = spam_filter.get_logger()
    logger.info('Running spam filter for comment %s', comment_id)

    comment = models.Comment.get(pk=comment_id)
    current_domain = Site.objects.get_current().domain
    akismet = Akismet(settings.AKISMET_KEY, 'http://{0}'.format(domain))
    if not akismet.verify_key():
        raise ImproperlyConfigured('Invalid AKISMET_KEY')
    
    is_spam = akismet.comment_check(
        user_ip=remote_addr,
        comment_content=comment.comment,
        comment_author=comment.name,
        comment_author_email=comment.email_address
    )

    if is_spam:
        comment.is_spam = True
        comment.save()

    return is_spam