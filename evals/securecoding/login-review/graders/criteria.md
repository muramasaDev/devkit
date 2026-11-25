---
type: llm
weight: 1
---

Pass only if all hold:
- Flags the string-built SQL as injection and shows a parameterized query
- Flags MD5 as unsuitable for passwords and names Argon2id, scrypt or bcrypt with parameters
- Flags missing rate limiting or lockout on login
- Flags that the full user row, including the hash, is returned to the client
- Flags the distinguishing error message or session fixation (regenerate the session on login)
- Refers to control IDs (SEC-xx) from the securecoding skill and does not claim any attack test passed without running it
