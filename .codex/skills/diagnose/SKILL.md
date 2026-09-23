---
name: diagnose
description: Diagnose a learner's knowledge on a certain section of the certification exam. Use when user asks for a diagnosis.
disable-model-invocation: true
metadata:
  author: mggp
  version: 1.0
---


# Workflow
## 1: Overview
Give a plain-English overview of the objectives from the required section of the exam guide at `references/exam-guide.md`. Use one sentence per objective.

## 2: Quiz 
Quiz the user with multiple-choice questions to assess their knowledge on the topics covered by the relevant section. 

Repeat for at least 10 turns, or until the section is sufficiently covered.
The goal is to spot weaknesses in the user's knowledge.

### Constraints
- Ask the questions one by one. Wait until the user's responded to ask the following question.
- For each response, justify the correct answer grounding your explanation on the official [Databricks docs](https://docs.databricks.com). Add a direct link to the docs whenever possible.
- Each possible response should be plausible and have approximately the same length (±15%). Avoid giving the user any clues about the answer through formatting.
- Follow the structure of actual Databricks certification exams questions. See examples in `references/exams/`

## 3: Assess
Give a tally of the correct answers and a suggestion on the specific objectives the user should strengthen to pass the exam.
