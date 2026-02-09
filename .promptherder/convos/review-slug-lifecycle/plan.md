# Plan: review-slug-lifecycle

> **Status**: approved

## Goal

Ensure each review with a distinct scope gets its own slug, while plan→execute→review still shares a single slug.

## Plan

### 1. Add scope-awareness to review slug resolution

- **Files:** `workflows/review.md`
- **Change:** Replace the current 3-step slug resolution with scope-aware logic.
- **Verify:** Read the updated file.

### 2. Add overwrite guard to the review skill's persistence section

- **Files:** `skills/compound-v-review/SKILL.md`
- **Change:** Add overwrite guard to persistence section 4.
- **Verify:** Read the updated section.
