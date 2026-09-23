---
name: deep-dive
description: Do a deep dive on a specific section of the Databricks exam. Use when the user asks to do a deep dive on a section or objective therein.
disable-model-invocation: true
metadata:
  author: mggp
  version: 1.0
---

Teach the user the requested subject. Use the $teach skill. Use official Databricks documentation (docs.databricks.com) and Databricks Academy materials as your sources. Cite the exact doc page URL next to each claim.

If you can't verify something in the official docs, say so rather than guessing.

Include: 
- core concept, 
- how it works on Databricks, 
- when to use vs. alternatives, 
- common mistakes, 
- one code example the user can run or a small task they can perform in the Databricks platform to support their learning.

