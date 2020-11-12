INSERT INTO users (username, password, ip_address, created_at)
VALUES
  ('test', 'pbkdf2:sha256:150000$bCXpzHVt$253731642e0dd23f7441708857a7f477203459a66a39d41adefafcbf0f70a093',
    '10.0.10.11', datetime('now')),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79',
    '10.0.12.12', datetime('2018-11-08 20:20:39'));
