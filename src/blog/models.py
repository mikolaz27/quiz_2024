from datetime import datetime

from django.db import models

from mongoengine import (Document, EmbeddedDocument, StringField, IntField, ListField,
                         DateTimeField, EmbeddedDocumentField)


# key1 =  { 1:1 }
#
# key2 = { 1:{1:1} }
#
# key3 = "fdsafjsdklfjksl"
#
# key4 = 123214

class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()
    author = StringField(max_length=255)
    rating = IntField(default=10)

    def __str__(self):
        return f"{self.name}"


class Entity(Document):
    blog = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=datetime.now())
    last_update = DateTimeField(default=datetime.now())
    headline = StringField(max_length=255)

    def __str__(self):
        return f"{self.headline}"
