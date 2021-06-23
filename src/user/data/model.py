from mongoengine.document import Document
from mongoengine.errors import ValidationError
from mongoengine.fields import  StringField, EmailField


def _not_empty(val):
    if not val:
        raise ValidationError('value can not be empty')

class UserModel(Document):
    first_name = StringField(validation=_not_empty)
    last_name = StringField()
    email= StringField()
    password = StringField()
    role = StringField()






"""

this is only for update reference

# post = BlogPost(title='Test', page_views=0, tags=['database'])
# post.save()
# BlogPost.objects(id=post.id).update_one(inc__page_views=1)
# post.reload()  # the document has been changed, so we need to reload it
# post.page_views
# 1
# BlogPost.objects(id=post.id).update_one(set__title='Example Post')
# post.reload()
# post.title
# 'Example Post'
# BlogPost.objects(id=post.id).update_one(push__tags='nosql')
# post.reload()
# post.tags
# ['database', 'nosql']

"""