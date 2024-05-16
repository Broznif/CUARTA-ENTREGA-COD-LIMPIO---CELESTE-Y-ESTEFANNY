CREATE TABLE IF NOT EXISTS cluster_data (
    id SERIAL PRIMARY KEY,
    data_text TEXT NOT NULL
);

INSERT INTO cluster_data (data_text)
VALUES ('aaaaaabccdddeeeeeeefghiiijkllmmnnnooooppqrrrssssttuuvwxyz!@#$%^&*().,AAAAAABCCDDDEEEEEEEFGHIIIJKLLMMNNNOOOOPPQRRRSSSSTTUUVWXYZ');

CREATE TABLE IF NOT EXISTS cluster_info (
    id SERIAL PRIMARY KEY,
    cluster_text TEXT NOT NULL,
    description TEXT NOT NULL
);
