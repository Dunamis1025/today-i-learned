# TIL: Microsoft Project Fundamentals

> Course: *Learning Microsoft Project* (LinkedIn Learning, instructor Bonnie Biafore)
> Certificate earned after completing all chapters.

## Why this matters
Microsoft Project is a **scheduling tool** for projects (unique work with a start/end and budget) — not for repeating operations. The core model is: **Tasks** (work to be done) + **Resources** (people/equipment/materials/cost) + **Dependencies** (links between tasks) → Project's scheduling engine calculates start/finish dates and total cost automatically.

---

## 1. Getting Started

### Create & save a project
- New blank project via `Blank Project` or `Ctrl+N`.
- Set the **project start date** in `Project tab → Project Information`. Everything schedules forward from this date (Schedule From = "Project Start Date").

### Define the work calendar
- `Project tab → Change Working Time` controls working days/hours.
- Built-in **Standard calendar**: Mon–Fri, 8:00–5:00 with 1-hour lunch (8 hrs/day).
- **Exceptions tab** = add holidays (non-working days) by name + date.
- `File → Options → Schedule`: calendar options (hours/day, hours/week, days/month) must match the working week — these define how *duration* converts to *work hours*.

---

## 2. Create & Modify Tasks

### Enter tasks
- Switch task mode to **Auto Scheduled** (bottom status bar) so Project calculates dates.
- Enable **"New tasks are effort driven"** (`File → Options → Schedule`) — total work stays constant regardless of how many resources are assigned.
- Type task name → `Enter` → next row. Right-click a task → `Insert Task` to add one mid-list.
- New tasks default to **1 day?** duration (the `?` = estimate not yet confirmed).

### Organize with summary tasks
- Select tasks → `Task tab → Insert → Summary` groups them under a new summary/header row (auto-indents children).
- Can also build top-down: insert a summary task first, then its subtasks.

### Add milestones
- Select the task above where the milestone should go → `Task tab → Insert → Milestone`.
- Milestones have **0-day duration** (don't add time/work) and render as a **black diamond** on the Gantt chart.
- Use the **outdent (green left arrow)** to place a milestone at the correct outline level (e.g., same level as its summary task).

### Put tasks into sequence (dependencies)
- Select 2+ tasks → `Link Tasks` (chain-link icon) → creates **Finish-to-Start** links (most common dependency type).
- Use `Ctrl+Click` to link non-adjacent tasks.
- Links appear as arrows in the Gantt timeline and as IDs in the **Predecessors** column.

### Add task duration
- Type values like `1d`, `5d` directly into the Duration column.
- Keep a trailing `?` (e.g., `5d?`) to mark an estimate that isn't finalized.
- `Ctrl+D` copies a cell's value down into other selected cells.
- A summary task's duration `?` disappears once **all** its subtasks have confirmed durations.

---

## 3. Assign Resources

### Create resources
- Done in the **Resource Sheet** view (`View tab → Resource Sheet`).
- Three resource types:
  | Type | Example | Key fields |
  |---|---|---|
  | Work | People, equipment (rented) | Standard Rate ($/hour), Max Units (%), Calendar |
  | Material | Cable, lumber | Material Label (unit of measure) + Standard Rate |
  | Cost | Permits, travel fees | Cost entered *at assignment time*, not on the sheet |
- Naming convention for people: `Lastname, Firstname` (no commas/brackets) for easy searching.
- **Max Units** = % availability to the project (100% = fully dedicated).

### Assign resources to tasks
- Simplest way: click the **Resource Names** cell on the Gantt chart → dropdown → check resource(s) → `Enter`. Defaults to 100% assignment.
- More control via the **Task Form** (`View tab → Details` checkbox): set partial units, exact work hours, add multiple resources (work + material + cost) to one task.
- For material resources, enter a **quantity** in the Units field (e.g., 5 cables).
- Cost resources: dollar amount is entered *after* assignment, via the **Cost table** in the Task Form.
- Project auto-calculates cost = rate × work (or quantity × unit price for materials).

### Resolve resource over-allocations
- `Resource tab → Leveling Options` — switch detection basis from week-by-week to **day-by-day** for short projects.
- Red "person" icons in the Indicators column flag over-allocated resources.
- **Resource Usage view** + `Over-allocated Resources` filter shows exactly which tasks clash (red text/cells).
- Two fixes:
  1. **Level Selection** — Project automatically pushes one task later.
  2. **Replace the resource** — swap the over-allocated resource for another available one directly in the assignment cell.
- Best practice: add a **note** (right-click → Note) documenting *why* a resource swap was made.

---

## 4. Communicate Your Plan

### Save a project baseline
- `Project tab → Set Baseline → Set Baseline` — snapshots start/finish/duration/work/cost as the "approved plan" (11 baseline slots available).
- The **Variance table** (`View → Tables → Variance`) compares baseline vs. current planned dates.

### Update your schedule
- Set the **Status Date** first (`Project tab → Status Date`) — the date through which work is considered complete.
- Use the **Tracking table** (`View → Tables → Tracking`) to enter Actual Duration / Remaining Duration / Actual Start.
- Or use `Task tab → Mark on Track ▾ → Update Tasks` dialog for a single task.
- Gantt bar shows both: light-blue = scheduled, dark-blue = actual progress.
- Can track by **Duration** or switch to **Work** (add a "Remaining Work" column).

### View the project schedule
Key built-in views:
| View | Best for |
|---|---|
| Gantt Chart | Default — table + timeline of task bars |
| Timeline (split view) | High-level overview; drag tasks/milestones onto it for a summary callout |
| Task Usage | See resource assignment breakdown per task, time-phased |
| Resource Usage | See workload per resource, spot over-allocations |
| Tracking Gantt | Gray bars = baseline, blue/red = current — visualize slippage |
- Switch tables via `View → Tables` (e.g., **Summary** table = duration, dates, work, cost, progress in one place).
- Right-click a column header → `Insert Column` to add fields like % Work Complete.

### Communicate results with reports
`Report tab` categories:
- **Dashboards → Burndown**: gray line = baseline work, blue = scheduled, orange = actual. Orange above the others = project behind schedule.
- **Resources → Resource Overview / Over-allocated Resources**: workload distribution and where clashes occur.
- **Cost → Cash Flow**: spending over time (editable timescale — e.g., switch to weekly).
- **In Progress → Slipping Tasks**: tasks whose finish date has moved past the baseline finish date.

---

## Key takeaway
The whole MS Project workflow boils down to a repeatable loop:
**Set up calendar → Enter & sequence tasks → Add durations → Assign resources → Level workload → Baseline the plan → Track actuals → Report status.**
