# Plan: review-output-clarity

> **Status**: approved

## Goal

Make the review skill enforce explicit check coverage, prevent redundant detail on self-explanatory findings, and eliminate the double action menu problem.

## Plan

### 1. Add check coverage table to output format

- **Files:** `skills/compound-v-review/SKILL.md`
- **Change:** Insert a new `### 2. Check coverage` section between Strengths and Findings. Renumber Findings → 3, Verdict → 4.
- **Verify:** Read the file, confirm section numbering is consistent.

### 2. Strengthen the "skip details" rule

- **Files:** `skills/compound-v-review/SKILL.md`
- **Change:** Replace advisory phrasing with imperative decision rule.
- **Verify:** Read the updated section.

### 3. Fix double action menu — move persistence before verdict

- **Files:** `skills/compound-v-review/SKILL.md`
- **Change:** Move the Persistence section to happen BEFORE the Verdict in the output format. The verdict with its action menu becomes the absolute last thing in the response. Delete the standalone Persistence section at the bottom of the file.
- **Verify:** Read the full output format section, confirm persistence → verdict ordering.

### 4. Commit and mark future tasks done

- **Files:** `.promptherder/future-tasks.md`
- **Change:** Check off both items.
- **Verify:** `git log --oneline -1`
