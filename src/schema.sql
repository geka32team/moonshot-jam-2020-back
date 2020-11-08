-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  username      TEXT UNIQUE NOT NULL,
  password      TEXT NOT NULL,
  ip_address    TEXT NOT NULL,
  created_at    TEXT NOT NULL
);
