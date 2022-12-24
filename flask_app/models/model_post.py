from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_user import User

db = 'resources-project'


class Post:

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.likes = None
        self.author = None

    @classmethod
    def get_all_posts(cls):

        query = """SELECT * FROM blogs
                    JOIN users 
                    ON blogs.user_id = users.id;"""

        results = connectToMySQL(db).query_db(query)
        
        posts = []

        for result in results:
            post = cls(result)

            author_info = {
                'id': result['user_id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'email': result['email'],
                'password': result['password'],
                'created_at': result['users.created_at'],
                'updated_at': result['users.updated_at']
            }
            user = User(author_info)
            post.author = user
            posts.append(post)

        return posts
    
    @classmethod
    def add_blog(cls, data):
        
        query = """
                INSERT INTO blogs(title, content, user_id)
                VALUES (%(title)s, %(content)s, %(user_id)s)
                """

        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):

        query = """DELETE FROM blogs WHERE id = %(blog_id)s"""

        return connectToMySQL(db).query_db(query, data)
    
    @classmethod
    def get_post(cls, data):

        query = """SELECT * FROM blogs WHERE blogs.id = %(blog_id)s"""
        result = connectToMySQL(db).query_db(query, data)
        return result[0]

    @classmethod
    def update_the_blog(cls, data):

        query = """
                UPDATE blogs
                SET title = %(title)s, content = %(content)s
                WHERE blogs.id = %(blog_id)s;
                """
        return connectToMySQL(db).query_db(query, data)