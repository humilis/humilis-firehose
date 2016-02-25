CREATE SCHEMA  if not exists _test;

DROP TABLE if exists _test.stream1 CASCADE;

CREATE TABLE _test.stream1
(
  event_id            VARCHAR(100),
  timestamp           VARCHAR(100),
  client_id           VARCHAR(100),
  url                 VARCHAR(100),
  referrer_url        VARCHAR(100),
  PRIMARY KEY (event_id)
)
DISTSTYLE ALL sortkey (event_id);


DROP TABLE if exists _test.stream2 CASCADE;

CREATE TABLE _test.stream2
(
  event_id            VARCHAR(100),
  timestamp           VARCHAR(100),
  client_id           VARCHAR(100),
  url                 VARCHAR(100),
  referrer_url        VARCHAR(100),
  PRIMARY KEY (event_id)
)
DISTSTYLE ALL sortkey (event_id);
