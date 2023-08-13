CREATE TABLE IF NOT EXISTS users(
id SMALLSERIAL PRIMARY KEY,
is_blocked BOOLEAN default(false),
balance FLOAT, language_id SMALLINT NOT NULL,
FOREIGN KEY (language_id) REFERENCES languages(id) ON DELETE CASCADE;