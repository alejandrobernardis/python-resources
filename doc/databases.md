# Databases

## Wikipedia says...

> A database is an organized collection of data, generally stored and accessed electronically from a computer system. Where databases are more complex they are often developed using formal design and modeling techniques.
>
> The database management system (DBMS) is the software that interacts with end users, applications, and the database itself to capture and analyze the data. The DBMS software additionally encompasses the core facilities provided to administer the database. The sum total of the database, the DBMS and the associated applications can be referred to as a "database system". Often the term "database" is also used to loosely refer to any of the DBMS, the database system or an application associated with the database.
>
> ...

Read more https://en.wikipedia.org/wiki/Database

## SQL

> SQL (/ˌɛsˌkjuːˈɛl/ (About this soundlisten) S-Q-L, /ˈsiːkwəl/ "sequel"; Structured Query Language) is a domain-specific language used in programming and designed for managing data held in a relational database management system (RDBMS), or for stream processing in a relational data stream management system (RDSMS). It is particularly useful in handling structured data, i.e. data incorporating relations among entities and variables.
>
> ...

Read more https://en.wikipedia.org/wiki/SQL

## Relational (RDBMS)

> A relational database is a digital database based on the relational model of data, as proposed by E. F. Codd in 1970. A software system used to maintain relational databases is a relational database management system (RDBMS). Many relational database systems have an option of using the SQL (Structured Query Language) for querying and maintaining the database.
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

> A NoSQL (originally referring to "non SQL" or "non relational") database provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases. Such databases have existed since the late 1960s, but did not obtain the "NoSQL" moniker until a surge of popularity in the early 21st century, triggered by the needs of Web 2.0 companies. NoSQL databases are increasingly used in big data and real-time web applications. NoSQL systems are also sometimes called "Not only SQL" to emphasize that they may support SQL-like query languages, or sit alongside SQL databases in polyglot persistent architectures.
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

### Comparison of Structured Storage Software

| Engine | Type | [Persistence][100] | [Replication][101] | [High Availability][102] | [Transactions][103] | Rack-locality Awareness | Implementation Language | License |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Apache Cassandra][110]      | Key-value | Yes | Yes | Distributed | Partial Only supports CAS (Check And Set) after 2.1.1 and later | Yes | Java | Apache 2.0 |
| [Apache HBase][111]          | Key-value | Yes. Major version upgrades require re-import. | Yes HDFS, Amazon S3 or Amazon Elastic Block Store. | Yes | Yes | See HDFS, S3 or EBS. | Java | Apache 2.0 |
| [Memcached][112]             | Key-value | No | No | No | Partial Only supports CAS (Check And Set - or Compare And Swap) | No | C | BSD-like permissive copyright by Danga |
| [MongoDB][113]               | Document (JSON) | Yes | Yes | fail-over | Partial Single document atomicity | No | C++ | GNU AGPL v3.0 |
| [Neo4j][114]                 | Graph database | Yes | Yes | Yes | Yes | No | Java | GNU GPL v3.0 |
| [Redis][115]                 | Key-value | Yes. But last few queries can be lost. | Yes | Yes | Yes | No | Ansi-C | BSD |
| [SimpleDB (Amazon.com)][116] | Document & Key-value | Yes | Yes (automatic) | Yes | Unknown | likely | Erlang | Amazon internal only |

Source https://en.wikipedia.org/wiki/Comparison_of_structured_storage_software

[100]: https://en.wikipedia.org/wiki/Persistence_(computer_science)
[101]: https://en.wikipedia.org/wiki/Replication_(computer_science)
[102]: https://en.wikipedia.org/wiki/High_Availability
[103]: https://en.wikipedia.org/wiki/Transaction_processing
[110]: https://en.wikipedia.org/wiki/Apache_Cassandra
[111]: https://en.wikipedia.org/wiki/Apache_HBase
[112]: https://en.wikipedia.org/wiki/Memcached
[113]: https://en.wikipedia.org/wiki/MongoDB
[114]: https://en.wikipedia.org/wiki/Neo4j
[115]: https://en.wikipedia.org/wiki/Redis
[116]: https://en.wikipedia.org/wiki/SimpleDB

### Performance

[Ben Scofield][200] rated different categories of NoSQL databases as follows:

| Data model | Performance | Scalability | Flexibility | Complexity | Functionality |
| --- | :-: | :-: | :-: | :-: | :-: |
| Key–value store | high | high | high | none | variable (none) |
| Column-oriented store | high | high | moderate | low | minimal |
| Document-oriented store | high | variable (high) | high | low | variable (low) |
| Graph database | variable | variable | high | high | graph theory |
| Relational database | variable | variable | low | moderate | relational algebra |

Source https://en.wikipedia.org/wiki/NoSQL#Performance

[200]: http://www.slideshare.net/bscofield/nosql-codemash-2010

## Data Warehouse

> In computing, a data warehouse (DW or DWH), also known as an enterprise data warehouse (EDW), is a system used for reporting and data analysis, and is considered a core component of business intelligence. DWs are central repositories of integrated data from one or more disparate sources. They store current and historical data in one single place that are used for creating analytical reports for workers throughout the enterprise.
>
> ..

Read more https://en.wikipedia.org/wiki/Data_warehouse

## Links

* **SQL**
    * PostgreSQL https://www.postgresql.org
    * MariaDB https://mariadb.org

* **NoSQL**
    * MongoDB https://www.mongodb.com/es
    * RethinkDB https://rethinkdb.com
    * Redis https://redis.io

* **Language**
    * SQL https://en.wikipedia.org/wiki/SQL
    * PL/SQL https://en.wikipedia.org/wiki/PL/SQL
    * DDL https://en.wikipedia.org/wiki/Data_definition_language
