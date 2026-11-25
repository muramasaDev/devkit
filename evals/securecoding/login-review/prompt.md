---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Review this Express login handler for security problems and tell me what to change.

```js
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const h = crypto.createHash('md5').update(password).digest('hex');
  const rows = await db.query("SELECT * FROM users WHERE email='" + email + "' AND pw='" + h + "'");
  if (rows.length) { req.session.uid = rows[0].id; return res.json(rows[0]); }
  res.status(401).json({ error: 'no such user or wrong password' });
});
```
