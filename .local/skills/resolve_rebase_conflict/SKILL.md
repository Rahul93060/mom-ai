---
name: resolve_rebase_conflict
description: Resolve git rebase conflicts when explicitly instructed to rebase or merge with the main branch.
---

# Resolve Rebase Conflict

Handle git rebase operations and resolve merge conflicts when rebasing onto the main branch.

## When to Use

Use this skill **only** when the user explicitly instructs you to:

- Rebase onto the main branch
- Merge changes from the main branch
- Resolve rebase conflicts

## When NOT to Use

- **Never** initiate a rebase unprompted
- Do not use for regular git operations (commit, push, pull)
- Do not use if the user has not explicitly asked for a rebase

## Available Functions

### startGitRebase()

Initiates a rebase onto the main repl's branch. This grants temporary permission to run git commands in the shell.

**Parameters:** None

**Returns:**

- `success` (bool): Whether the rebase started successfully
- `branch` (str): The branch being rebased onto
- `hasConflicts` (bool): Whether there are conflicts to resolve

### markRebaseCompleted({ success, majorDivergence, commitMessage })

Marks the rebase as complete and revokes git shell permissions.

**Parameters:**

- `success` (bool, required): Whether the rebase completed successfully
- `majorDivergence` (bool, optional): Set to `true` if conflict resolution significantly altered behavior
- `commitMessage` (str, optional): Summary of changes made during conflict resolution

**Returns:**

- `success` (bool): Whether the rebase completed successfully (echoes input)
- `majorDivergence` (bool): Echo of the majorDivergence parameter

## Conflict Resolution Procedure

1. Call `startGitRebase()` to begin the rebase
2. If `hasConflicts` is `true`:
   a. Check which files have conflicts using `git status` in the shell
   b. Read each conflicted file to understand the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
   c. Resolve conflicts by editing files to remove markers and keep the correct code
   d. Stage resolved files with `git add <file>`
   e. Continue the rebase with `git rebase --continue`
   f. Repeat steps a-e if more conflicts arise
3. Call `markRebaseCompleted({ success: true, commitMessage: "..." })` when done
4. If resolution is not possible, call `markRebaseCompleted({ success: false })` to abort

## Major Divergence Handling

If resolving conflicts requires changes that significantly alter the behavior of the code (not just trivial merge resolution), set `majorDivergence: true` when calling `markRebaseCompleted`. This signals that the changes should be reviewed carefully.
