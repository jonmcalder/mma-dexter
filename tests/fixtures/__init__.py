import datetime

from fixture import DataSet, NamedDataStyle, SQLAlchemyFixture

from dexter.models import db, Person, Entity, Author, Document, User, Role

class PersonData(DataSet):
    class joe_author:
        name = 'Joe Author'
        gender_id = 2
        race_id = 1

    class zuma:
        name = 'Jacob Zuma'
        gender_id = 2
        race_id = 2

    class sue_no_gender:
        name = 'Sue'

class EntityData(DataSet):
    class joe_author:
        name = 'Joe Author'
        group = 'person'
        person = PersonData.joe_author

    class zuma:
        name = 'Jacob Zuma'
        group = 'person'
        person = PersonData.zuma

    class sue_no_gender:
        name = 'Sue'
        group = 'person'
        person = PersonData.sue_no_gender

class AuthorData(DataSet):
    class joe_author:
        name = 'Joe Author'
        author_type_id = 1
        person = PersonData.joe_author

class RoleData(DataSet):
    class monitor:
        name = 'monitor'
        description = 'monitor'

class UserData(DataSet):
    class user:
        first_name = 'User'
        last_name  = 'Smith'
        email = 'user@example.com'
        country_id = 1
        password = 'foo'
        admin = 1

    class user2:
        first_name = 'Joe'
        last_name  = 'Bloggs'
        email = 'joe@example.com'
        country_id = 1
        password = 'foo'
        admin = 0

class DocumentData(DataSet):
    class simple:
        url = 'http://mg.co.za/articles/2012-01-01-foo'
        title = 'Title'
        summary = 'A document summary'
        text = 'Today, we do fun things.'
        published_at = datetime.datetime(2012, 1, 1)
        medium_id = 1
        document_type_id = 1
        author = AuthorData.joe_author
        created_by = UserData.user
        country_id = 1

    class simple2:
        url = 'http://mg.co.za/articles/2012-03-03-bar'
        title = 'Another title'
        summary = 'Another document summary'
        text = 'Today, we do fun things.'
        published_at = datetime.datetime(2012, 3, 3)
        medium_id = 1
        document_type_id = 1
        author = AuthorData.joe_author
        created_by = UserData.user
        country_id = 1


dbfixture = SQLAlchemyFixture(
    env=globals(),
    style=NamedDataStyle(),
    engine=db.engine)
