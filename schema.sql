create table logo_detection
(
    id serial           not null primary key,
    logo_name           varchar not null,
    channel             varchar not null,
    "timestamp"         timestamp not null
);
