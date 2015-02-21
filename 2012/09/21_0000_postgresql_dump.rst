PostgreSQL dump
===============

Setup password according to `http://www.postgresql.org/docs/8.4/static/libpq-pgpass.html <http://www.postgresql.org/docs/8.4/static/libpq-pgpass.html>`__ to disable password prompt:

create .pgpass file in home directory and add next line:

::

    hostname:port:database:username:password

(default port: 5432)

Execute:

.. code-block:: bash

    chmod 0600 /home/iam/.pgpass

Backup bash script:

.. code-block:: bash

    #!/bin/sh

    BACKUPS_DIR=/path/to/backups/folder
    DB_NAME=my_db_name
    DB_USER=my_db_user

    filename="$BACKUPS_DIR/$DB_NAME_"`eval date +%Y_%m_%d`".dump.gz"
    pg_dump $DB_NAME --username $DB_USER | gzip -c > $filename

Add task to crontab:

.. code-block:: bash

    crontab -e

Restore data:

.. code-block:: bash

    gunzip dump_name.dump.gz
    psql -d db_name -f dump_name.dump


*UPD 2015-02-21*

Binary dump create:

.. code-block:: bash

    pg_dump -h {hostname} -U {username} -F c -b -v -f {path to destination file} {database name}

Restore binary dump:

.. code-block:: bash

    pg_restore -h {hostname} -d {database name} -c -U {username} {path to source file}

.. info::
    :tags: Databases
    :place: Alchevs'k, Ukraine
