# The Information schema

An information schema is a virtual database that provides information about the structure of the actual databases that a database management system manages. It is typically implemented as a set of tables, views, and procedures that allow database administrators and developers to query and analyze metadata about database objects, such as tables, columns, constraints, indexes, and views.

select table_name from information_schema.tables where table_schema='security';

The above query will return every table name in the database security.

