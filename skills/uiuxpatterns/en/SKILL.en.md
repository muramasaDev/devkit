Korean original: ../SKILL.md. Pattern IDs are identical.

Reference files other than defaults, snippets and korean-flows are Korean for now: links of the form `../references/...` point to the Korean originals, and `references/...` in this file means en/references/ (English).

# UI UX Patterns (90 UI/UX patterns, extended terms, web platform and agent screen criteria)

## Overview
- Skill for designing, implementing, reviewing and improving screens using 90 UI/UX patterns (10 categories), 69 extended terms, a web platform feature selection table, agent screen criteria and selection criteria
- Core principle: read the project context first and use only the patterns the user's goal needs. Do not apply patterns that are not needed
- Does not force a specific design style or library. The existing design system and tech stack take priority
- Category 09 (dark patterns) is not an implementation list but a target for detection and prevention

## When to use
- Screen design, UI implementation, UI review, UX check, refactoring, design system, pattern selection
- Choosing between toast, snackbar and modal; skeleton and spinner; pagination and infinite scroll; tab bar and drawer
- Deciding loading, empty screen, no results, error, form states, gestures, motion, navigation, design tokens
- Accessibility (WCAG 2.2 AA), responsive, dark pattern checks
- AI chatbot and agent screens (tool calls, human approval), ease-out, combobox, data table, inline edit, command palette, popover, view transitions, Enter during Hangul input (IME), Hick's law, INP
- When the name of a UI element or UX law is unknown
- Security checks use the `securecoding` skill, initial project setup uses the `kickoff` skill

## Execution order
1. Context Discovery: analyze the request, explore the tech stack, existing design system and components, decide the work scope. Pick the mode from the table below. For a new project with no code, skip exploration, write the stack and design system as `undecided` (`미정`), and design without tying to a stack (propose tokens only when asked) Ask with `AskUserQuestion` only about items that cannot be read from the code or the request and that change the result (multiple choice, at most 3 questions per call, with 'Not sure' and 'Proceed with defaults' options): service region and language (whether Korean law mapping applies), existing design system or not, target devices (mobile, desktop). Do not ask when the scope is small, such as choosing one pattern. If 'Proceed with defaults' is chosen, record the assumptions in the report
2. Pattern Retrieval: narrow candidates with `../references/decision-framework.md` (if the name is not among the 90, look in `../references/terms-extended.md`), open only the relevant category file, and compare When to Use and When Not to Use. If only one pattern is needed, do not read the whole file: Grep a heading such as `^## FB-02 ` (actual format `## FB-02 스낵바 (Snackbar)`) and read only that block (until the next `## `)
3. Design Decision: decide information structure, components, screen states (default, loading, empty, error, done), interaction and feedback, how tokens are applied
4. Implementation (modes B, D, E only): reuse existing components, working interactions, responsive, loading and error handling, accessibility. Markup examples are in `references/snippets.md`
5. Validation: check with `../references/quality-checklist.md` and actually run the available checks (build, types, tests, screen check). Write items that could not be run as `unverified` (`미검증`)
6. Reporting: goal of the work, selected patterns (IDs) and excluded patterns with reasons, main changes, validation results (distinguish how each was verified), remaining issues

## Modes

| Mode | When to pick | Code changes | Output format |
|---|---|---|---|
| A. UI Design | Design a new screen or flow | No | `../templates/ui-analysis.md` |
| B. UI Implementation | Implement a decided design in code | Yes | `../templates/ui-implementation.md` |
| C. UI Review | Diagnose the quality of one specified screen or flow | No (do not modify if only a review was requested) | `../templates/ui-audit.md` |
| D. UI Refactoring | Clean up structure and consistency while preserving design and function | Yes (no unintended behavior changes, check for regressions) | `../templates/ui-implementation.md` |
| E. Design System Creation | Basic structure for a project without a design system | Yes | structure of `../references/design-system.md` |
| F. UX Audit | Check a whole service (multiple screens and flows) | No | `../templates/ui-audit.md` |

- If the request is ambiguous, pick the one with the smaller change scope ('take a look' and 'check it' mean C or F)
- If design and then implementation are both requested, finish A and then move to B
- If a change is requested, as in 'improve it' or 'fix it': first make a defect list (from the viewpoint of C), then fix the defects named in the request and their causes (B). List the places where behavior changes in the report. Do not fix defects not in the request; report them
- When merging components in mode D: before merging, make a table of the property and behavior differences of each component (closing method, focus handling, etc.), and either preserve the differences or settle on one with user confirmation
- Accessibility violations in existing screens: parts newly made or fixed within the work scope must meet the criteria; violations outside the scope are not fixed but reported

## Reference files (open only what is needed)

| File | When to open |
|---|---|
| `../references/decision-framework.md` (Korean for now) | When choosing or recommending patterns (always, at step 2 of every mode) |
| `../references/pattern-catalog.md` (Korean for now) | When looking up pattern IDs, original names, reference images |
| `../references/feedback.md` (Korean for now) | Notifications, confirmation, error guidance, help (FB) |
| `../references/forms.md` (Korean for now) | Input elements and input states (FM) |
| `../references/loading.md` (Korean for now) | Waiting, progress, instant reflection (LD) |
| `../references/ai-interfaces.md` (Korean for now) | AI chat, generation, agent screens and AI trust principles (AI) |
| `../references/empty-states.md` (Korean for now) | No data, offline, permission, error, locked screens (ES) |
| `../references/gestures.md` (Korean for now) | Touch gestures and alternatives (GS) |
| `../references/motion.md` (Korean for now) | Easing curves, entrance, screen transitions (MO) |
| `../references/navigation.md` (Korean for now) | Tabs, drawer, breadcrumbs, list navigation (NV) |
| `../references/dark-patterns.md` (Korean for now) | When building or reviewing signup, consent, payment, cart, cancellation, solicitation flows (DP) |
| `../references/icon-terminology.md` (Korean for now) | Menu icon names and icon buttons (IC) |
| `../references/design-system.md` (Korean for now) | When finding or newly deciding tokens, states, themes (always for mode E) |
| `../references/accessibility.md` (Korean for now) | When deciding or checking accessibility items (always for modes B, C, D, F. For modes A and E, look first at the Accessibility item of the pattern file, and open this only when criteria must be decided) |
| `../references/responsive-design.md` (Korean for now) | Layout by screen size and pattern switching |
| `../references/quality-checklist.md` (Korean for now) | Step 5 validation and review (always for modes C and F) |
| `references/defaults.md` | When deciding the defaults left as `제품에서 정한다` (set per product): auto-close time, motion duration, debounce, threshold counts |
| `references/korean-flows.md` | When designing or reviewing Korean domestic service flows (mobile phone identity verification, payment, currency format, address input, Hangul input, personal information consent) |
| `references/snippets.md` | Markup examples (HTML, React, Vue 3) for toast, snackbar, modal, tooltip, text field, switch, tabs, button loading, streaming answer. When implementing |
| `../references/usage-examples.md` (Korean for now) | Call examples and files to read per scenario |
| `../references/glossary.md` (Korean for now) | Names to use when instructing or reviewing screens (9 each for empty screen, menu icon, screen transition, motion, loading), 7 check questions |
| `../references/pattern-keywords.csv` (Korean for now) | ID, Korean name, English name, aliases of the 90 patterns. For finding a pattern called by another name |
| `../references/terms-extended.md` (Korean for now) | Terms not among the 90: 31 components, 17 AI screens, 16 UX laws, 5 perceived-performance terms, and a synonym table. When the name is unknown |
| `../references/modern-web.md` (Korean for now) | When implementation can be solved with browser features such as dialog, popover, tabs, form validation, view transitions, container queries (modes B, D, E) |
| `../references/interaction-rules.md` (Korean for now) | Detailed behavior rules: disabled, validation timing, live regions, Enter during Hangul input, Esc, toast timers, chat scroll (implementation and review) |
| `../references/agent-ui.md` (Korean for now) | Display per agent event, human approval screen, tool call consent (when designing or reviewing AI agent screens) |

- The original images are not in the distribution. The file names in Reference Image items are the original image names, and the names and scenes are transcribed as text in `../references/pattern-catalog.md`

## Rules
- Existing project first: find and reuse components, tokens, styling method. Do not replace brand colors, fonts, spacing wholesale
- Do not add libraries that are not in the project on your own. If one is needed, present the grounds from comparison with the existing method and get user confirmation
- Do not use component, API or token names whose existence is unconfirmed
- Do not build fake interactions that do not work. Do not show progress that cannot be measured or AI steps that were not performed
- Separate UI state from business logic, and do not change structure or features outside the request scope
- Dark patterns (DP-01 ~ DP-09) are not implemented even when requested; propose an alternative UX
- Accessibility target is WCAG 2.2 AA
- Do not report unverified items as done. Distinguish what was seen on screen, what was only read in code, and what was only the user's description
- For elements not in the catalog (tables, charts, metric cards, etc.), do not invent pattern IDs: write `outside catalog` (`카탈로그 외`) and design from the principles of state, accessibility, responsive
- In modes C and F, do not modify files

## Extension
- Procedure for adding a pattern or category: `패턴 추가 방법` (How to add a pattern) in `../references/pattern-catalog.md`
