#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line

    from polls.models import *
    from django.utils import timezone
    import datetime
    time = timezone.now() + datetime.timedelta(days=-2)
    Question.objects.create(question_text='The other question', pub_date=time)
