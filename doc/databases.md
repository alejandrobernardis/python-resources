# Databases

## Wikipedia says...

> A database is an organized collection of data, generally stored and accessed electronically from a computer system. Where databases are more complex they are often developed using formal design and modeling techniques.
>
> The database management system (DBMS) is the software that interacts with end users, applications, and the database itself to capture and analyze the data. The DBMS software additionally encompasses the core facilities provided to administer the database. The sum total of the database, the DBMS and the associated applications can be referred to as a "database system". Often the term "database" is also used to loosely refer to any of the DBMS, the database system or an application associated with the database.
>
> ...

Read more https://en.wikipedia.org/wiki/Database

## SQL

> SQL (/ˌɛsˌkjuːˈɛl/ (About this soundlisten) S-Q-L,[4] /ˈsiːkwəl/ "sequel"; Structured Query Language)[5][6][7] is a domain-specific language used in programming and designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS). It is particularly useful in handling structured data, i.e. data incorporating relations among entities and variables.
>
> ...

Read more https://en.wikipedia.org/wiki/SQL

## Relational (RDBMS)

> A relational database is a digital database based on the relational model of data, as proposed by E. F. Codd in 1970.[1] A software system used to maintain relational databases is a relational database management system (RDBMS). Many relational database systems have an option of using the SQL (Structured Query Language) for querying and maintaining the database.[2]
>
> ...

Read more https://en.wikipedia.org/wiki/Relational_database

### Comparison of Relational Database Management Systems

| Engine | Maintainer | First public release date | Latest stable version | License | Public issues list |
| --- | :-: | :-: | :-: | :-: | :-: |
| [DB2][1]                  | IBM | 1983 | 11.1 | Proprietary | No |
| [Firebird][10]            | Firebird project | 2000-07-25 | 3.0.4 | IPL and IDPL | Yes |
| [MariaDB][2]              | MariaDB Community | 2010-02-01 | 10.4.10 | GPL v2, LGPL | Yes |
| [Microsoft SQL Server][3] | Microsoft | 1989 | 2017 (14) | Proprietary | No |
| [MySQL][4]                | Oracle Corporation | 1995-11 | 8.0.18 | GPL v2 or Proprietary | Yes |
| [Oracle DB][5]            | Oracle Corporation | 1979-11 | 18.1.0.0 | Proprietary | No |
| [PostgreSQL][6]           | PostgreSQL Global Development Group | 1989-06 | 12 | PostgreSQL Licence  | No |
| [SAP HANA][7]             | SAP AG | 2010 | 2.0 SPS04 | Proprietary | No |
| [SQL Anywhere][8]         | SAP AG | 1992 | 17.0.0.48 | Proprietary | No |
| [SQLite][9]               | D. Richard Hipp | 2000-09-12 | 3.28.0 | Public domain | Yes |

Source https://en.wikipedia.org/wiki/Comparison_of_relational_database_management_systems

[1]: https://en.wikipedia.org/wiki/IBM_DB2
[2]: https://en.wikipedia.org/wiki/MariaDB
[3]: https://en.wikipedia.org/wiki/Microsoft_SQL_Server
[4]: https://en.wikipedia.org/wiki/MySQL
[5]: https://en.wikipedia.org/wiki/Oracle_Database
[6]: https://en.wikipedia.org/wiki/PostgreSQL
[7]: https://en.wikipedia.org/wiki/SAP_HANA
[8]: https://en.wikipedia.org/wiki/SQL_Anywhere
[9]: https://en.wikipedia.org/wiki/SQLite
[10]: https://en.wikipedia.org/wiki/Firebird_(database_server)

## No Relational (NOSQL)

> A NoSQL (originally referring to "non SQL" or "non relational")[1] database provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases. Such databases have existed since the late 1960s, but did not obtain the "NoSQL" moniker until a surge of popularity in the early 21st century,[2] triggered by the needs of Web 2.0 companies.[3][4] NoSQL databases are increasingly used in big data and real-time web applications.[5] NoSQL systems are also sometimes called "Not only SQL" to emphasize that they may support SQL-like query languages, or sit alongside SQL databases in polyglot persistent architectures.[6][7]
>
> ...

Read more https://en.wikipedia.org/wiki/NoSQL

### Types

There are various ways to classify NoSQL databases, with different categories and subcategories, some of which overlap. What follows is a basic classification by data model, with examples:

* **Column:** Accumulo, Cassandra, Scylla, HBase.
* **Document:** Apache CouchDB, ArangoDB, BaseX, Clusterpoint, Couchbase, Cosmos DB, IBM Domino, MarkLogic, MongoDB, OrientDB, Qizx, RethinkDB
* **Key-value:** Aerospike, Apache Ignite, ArangoDB, Berkeley DB, Couchbase, Dynamo, FoundationDB, InfinityDB, MemcacheDB, MUMPS, Oracle NoSQL Database, OrientDB, Redis, Riak, SciDB, SDBM/Flat File dbm, ZooKeeper
* **Graph:** AllegroGraph, ArangoDB, InfiniteGraph, Apache Giraph, MarkLogic, Neo4J, OrientDB, Virtuoso

A more detailed classification is the following, based on one from Stephen Yen:

| Type | Notable examples of this type |
| --- | --- |
| Key-Value                               | Cache Apache Ignite, Coherence, eXtreme Scale, Hazelcast, Infinispan, Memcached, Velocity |
| Key-Value Store                         | ArangoDB, Aerospike |
| Key-Value Store (Eventually-Consistent) | Oracle NoSQL Database, Dynamo, Riak, Voldemort |
| Key-Value Store (Ordered)               | FoundationDB, InfinityDB, LMDB, MemcacheDB |
| Data-Structures Server                  | Redis |
| Tuple Store                             | Apache River, GigaSpaces |
| Object Database                         | Objectivity/DB, Perst, ZopeDB |
| Document Store                          | ArangoDB, BaseX, Clusterpoint, Couchbase, CouchDB, DocumentDB, IBM Domino, MarkLogic, MongoDB, Qizx, RethinkDB, Elasticsearch |
| Wide Column Store                       | Amazon DynamoDB, Bigtable, Cassandra, Scylla, HBase, Hypertable |
| Native Multi-model Database             | ArangoDB, Cosmos DB, OrientDB, MarkLogic |

Source https://en.wikipedia.org/wiki/NoSQL#Types_and_examples
