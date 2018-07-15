

## Flask-SQLAlchemy

```
pip install flask-sqlalchemy

sqlite3 test.db

CREATE TABLE todos
         (todo_id        INTEGER PRIMARY KEY,
         title           STRING    NOT NULL,
         text            STRING    NOT NULL,
         done            Boolean   NOT NULL,
         pub_date        DateTime   NOT NULL
         );

> select * from todos;
> .quit
```



## Usage

1. [Flask-SQLAlchemy — Flask-SQLAlchemy Documentation (2.3)](http://flask-sqlalchemy.pocoo.org/2.3/)

2. [快速入门 — Flask-SQLAlchemy 2.0 documentation](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)

3. [使用flask-sqlalchemy玩转MySQL | Wing's Tech Space](https://wing324.github.io/2017/02/25/%E4%BD%BF%E7%94%A8flask-sqlalchemy%E7%8E%A9%E8%BD%ACMySQL/)