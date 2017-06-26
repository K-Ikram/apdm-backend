from __future__ import absolute_import
from project.celery import app as celery_app
import sys

reload(sys)
sys.setdefaultencoding('utf8')

__all__ = ['celery_app']
