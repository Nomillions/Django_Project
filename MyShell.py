import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django

django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

t = Topic.objects.get(id=1)
print(t)
entry = t.entry_set.all()

for entry in entries:
    print(entry)


"""
for t in topics:
    print(f"Topic ID: {t.id} and Topic Name: {t}")
    print(f"Date Added: {t.date_added}")

entries = Entry.objects.all()


for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Entry: {e.text}")
"""

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)