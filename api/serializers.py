from ninja import Schema


class Category(Schema):
    name: str


class Author(Schema):
    name: str


class NewsSchema(Schema):
    title: str
    author: Author
    page_views: int
    image: str
    status: str
    category: Category
