drop table if exists post;
     create table post (
          id integer primary key autoincrement,
          Firstname text not NULL,
          Lastname text not Null,
          username text not NULL,
          password text not NULL,
          confirm_password text not NULL

);          