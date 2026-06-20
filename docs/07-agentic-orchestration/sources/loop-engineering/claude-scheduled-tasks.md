> ## Documentation Index
> Fetch the complete documentation index at: [/docs/llms.txt](https://code.claude.com/docs/llms.txt)
> Use this file to discover all available pages before exploring further.
[Skip to main content](https://code.claude.com/docs/en/scheduled-tasks#content-area)
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
English
Search...
⌘KAsk Assistant
  * [Claude Developer Platform](https://platform.claude.com/)
  * [Claude Code on the Web](https://claude.ai/code)
  * [Claude Code on the Web](https://claude.ai/code)


Search...
Navigation
Automation
Run prompts on a schedule
[Getting started](https://code.claude.com/docs/en/overview)[Build with Claude Code](https://code.claude.com/docs/en/agents)[Administration](https://code.claude.com/docs/en/admin-setup)[Configuration](https://code.claude.com/docs/en/settings)[Reference](https://code.claude.com/docs/en/cli-reference)[Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)[What's New](https://code.claude.com/docs/en/whats-new)[Resources](https://code.claude.com/docs/en/legal-and-compliance)
### Agents and parallel work
  * [Overview](https://code.claude.com/docs/en/agents)
  * [Create custom subagents](https://code.claude.com/docs/en/sub-agents)
  * [Agent view](https://code.claude.com/docs/en/agent-view)
  * [Run agent teams](https://code.claude.com/docs/en/agent-teams)
  * [Dynamic workflows](https://code.claude.com/docs/en/workflows)
  * [Isolate sessions with worktrees](https://code.claude.com/docs/en/worktrees)


### MCP
  * [Quickstart](https://code.claude.com/docs/en/mcp-quickstart)
  * [Reference](https://code.claude.com/docs/en/mcp)


### Skills
  * [Extend Claude with skills](https://code.claude.com/docs/en/skills)


### Plugins
  * [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)
  * [Create plugins](https://code.claude.com/docs/en/plugins)


### Artifacts
  * [Share session output as artifacts](https://code.claude.com/docs/en/artifacts)


### Automation
  * [Automate with hooks](https://code.claude.com/docs/en/hooks-guide)
  * [Push external events to Claude](https://code.claude.com/docs/en/channels)
  * [Run prompts on a schedule](https://code.claude.com/docs/en/scheduled-tasks)
  * [Goals](https://code.claude.com/docs/en/goal)
  * [Programmatic usage](https://code.claude.com/docs/en/headless)
  * [Launch sessions from links](https://code.claude.com/docs/en/deep-links)


### Guides
  * [Monorepos and large repos](https://code.claude.com/docs/en/large-codebases)


### Troubleshooting
  * [Troubleshoot installation and login](https://code.claude.com/docs/en/troubleshoot-install)
  * [Troubleshoot performance and stability](https://code.claude.com/docs/en/troubleshooting)
  * [Debug configuration](https://code.claude.com/docs/en/debug-your-config)
  * [Error reference](https://code.claude.com/docs/en/errors)


## On this page
  * [Compare scheduling options](https://code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options)
  * [Run a prompt repeatedly with /loop](https://code.claude.com/docs/en/scheduled-tasks#run-a-prompt-repeatedly-with-%2Floop)
    * [Run on a fixed interval](https://code.claude.com/docs/en/scheduled-tasks#run-on-a-fixed-interval)
    * [Let Claude choose the interval](https://code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval)
    * [Run the built-in maintenance prompt](https://code.claude.com/docs/en/scheduled-tasks#run-the-built-in-maintenance-prompt)
    * [Customize the default prompt with loop.md](https://code.claude.com/docs/en/scheduled-tasks#customize-the-default-prompt-with-loop-md)
    * [Stop a loop](https://code.claude.com/docs/en/scheduled-tasks#stop-a-loop)
  * [Set a one-time reminder](https://code.claude.com/docs/en/scheduled-tasks#set-a-one-time-reminder)
  * [Manage scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks#manage-scheduled-tasks)
  * [How scheduled tasks run](https://code.claude.com/docs/en/scheduled-tasks#how-scheduled-tasks-run)
    * [Jitter](https://code.claude.com/docs/en/scheduled-tasks#jitter)
    * [Seven-day expiry](https://code.claude.com/docs/en/scheduled-tasks#seven-day-expiry)
  * [Cron expression reference](https://code.claude.com/docs/en/scheduled-tasks#cron-expression-reference)
  * [Disable scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks#disable-scheduled-tasks)
  * [Limitations](https://code.claude.com/docs/en/scheduled-tasks#limitations)


Automation
# Run prompts on a schedule
Copy page
Use /loop and the cron scheduling tools to run prompts repeatedly, poll for status, or set one-time reminders within a Claude Code session.
Copy page
Scheduled tasks require Claude Code v2.1.72 or later. Check your version with `claude --version`.
Scheduled tasks let Claude re-run a prompt automatically on an interval. Use them to poll a deployment, babysit a PR, check back on a long-running build, or remind yourself to do something later in the session. To react to events as they happen instead of polling, see [Channels](https://code.claude.com/docs/en/channels): your CI can push the failure into the session directly. To keep the session working turn after turn until a condition is met rather than on an interval, see [`/goal`](https://code.claude.com/docs/en/goal). Tasks are session-scoped: they live in the current conversation and stop when you start a new one. Resuming with `--resume` or `--continue` brings back any task that hasn’t [expired](https://code.claude.com/docs/en/scheduled-tasks#seven-day-expiry): a recurring task created within the last 7 days, or a one-shot whose scheduled time hasn’t passed yet. For scheduling that survives independently of any session, use [Routines](https://code.claude.com/docs/en/routines) to create a routine on Anthropic-managed infrastructure, set up a [Desktop scheduled task](https://code.claude.com/docs/en/desktop-scheduled-tasks), or use [GitHub Actions](https://code.claude.com/docs/en/github-actions).
## 
[​](https://code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options)
Compare scheduling options
Claude Code offers three ways to schedule recurring or one-off work:  
|   | [Cloud](https://code.claude.com/docs/en/routines)  | [Desktop](https://code.claude.com/docs/en/desktop-scheduled-tasks)  | [`/loop`](https://code.claude.com/docs/en/scheduled-tasks)  |  
| --- | --- | --- | --- |  
| Runs on  | Anthropic cloud  | Your machine  | Your machine  |  
| Requires machine on  | No  | Yes  | Yes  |  
| Requires open session  | No  | No  | Yes  |  
| Persistent across restarts  | Yes  | Yes  | Restored on `--resume` if unexpired  |  
| Access to local files  | No (fresh clone)  | Yes  | Yes  |  
| MCP servers  | Connectors configured per task  |  [Config files](https://code.claude.com/docs/en/mcp) and connectors  | Inherits from session  |  
| Permission prompts  | No (runs autonomously)  | Configurable per task  | Inherits from session  |  
| Customizable schedule  | Via `/schedule` in the CLI  | Yes  | Yes  |  
| Minimum interval  | 1 hour  | 1 minute  | 1 minute  |  
Use **cloud tasks** for work that should run reliably without your machine. Use **Desktop tasks** when you need access to local files and tools. Use **`/loop`**for quick polling during a session.
## 
[​](https://code.claude.com/docs/en/scheduled-tasks#run-a-prompt-repeatedly-with-/loop)
Run a prompt repeatedly with /loop
The `/loop` [bundled skill](https://code.claude.com/docs/en/commands) is the quickest way to run a prompt on repeat while the session stays open. Both the interval and the prompt are optional, and what you provide determines how the loop behaves.  
| What you provide  | Example  | What happens  |  
| --- | --- | --- |  
| Interval and prompt  | `/loop 5m check the deploy`  | Your prompt runs on a [fixed schedule](https://code.claude.com/docs/en/scheduled-tasks#run-on-a-fixed-interval)  |  
| Prompt only  | `/loop check the deploy`  | Your prompt runs at an [interval Claude chooses](https://code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval) each iteration  |  
| Interval only, or nothing  | `/loop`  | The [built-in maintenance prompt](https://code.claude.com/docs/en/scheduled-tasks#run-the-built-in-maintenance-prompt) runs, or your `loop.md` if one exists  |  
You can also pass another command as the prompt, for example `/loop 20m /review-pr 1234`, to re-run a saved skill or command each iteration.
### 
[​](https://code.claude.com/docs/en/scheduled-tasks#run-on-a-fixed-interval)
Run on a fixed interval
When you supply an interval, Claude converts it to a cron expression, schedules the job, and confirms the cadence and job ID.

```
/loop 5m check if the deployment finished and tell me what happened

```

The interval can lead the prompt as a bare token like `30m`, or trail it as a clause like `every 2 hours`. Supported units are `s` for seconds, `m` for minutes, `h` for hours, and `d` for days. Seconds are rounded up to the nearest minute since cron has one-minute granularity. Intervals that don’t map to a clean cron step, such as `7m` or `90m`, are rounded to the nearest interval that does and Claude tells you what it picked.
### 
[​](https://code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval)
Let Claude choose the interval
When you omit the interval, Claude chooses one dynamically instead of running on a fixed cron schedule. After each iteration it picks a delay between one minute and one hour based on what it observed: short waits while a build is finishing or a PR is active, longer waits when nothing is pending. The chosen delay and the reason for it are printed at the end of each iteration. The example below checks CI and review comments, with Claude waiting longer between iterations once the PR goes quiet:

```
/loop check whether CI passed and address any review comments

```

When you ask for a dynamic `/loop` schedule, Claude may use the [Monitor tool](https://code.claude.com/docs/en/tools-reference#monitor-tool) directly. Monitor runs a background script and streams each output line back, which avoids polling altogether and is often more token-efficient and responsive than re-running a prompt on an interval. A dynamically scheduled loop appears in your [scheduled task list](https://code.claude.com/docs/en/scheduled-tasks#manage-scheduled-tasks) like any other task, so you can list or cancel it the same way. The [jitter rules](https://code.claude.com/docs/en/scheduled-tasks#jitter) don’t apply to it, but the [seven-day expiry](https://code.claude.com/docs/en/scheduled-tasks#seven-day-expiry) does: the loop ends automatically seven days after you start it.
On Bedrock, Vertex AI, and Microsoft Foundry, a prompt with no interval runs on a fixed 10-minute schedule instead.
### 
[​](https://code.claude.com/docs/en/scheduled-tasks#run-the-built-in-maintenance-prompt)
Run the built-in maintenance prompt
When you omit the prompt, Claude uses a built-in maintenance prompt instead of one you supply. On each iteration it works through the following, in order:
  * continue any unfinished work from the conversation
  * tend to the current branch’s pull request: review comments, failed CI runs, merge conflicts
  * run cleanup passes such as bug hunts or simplification when nothing else is pending

Claude does not start new initiatives outside that scope, and irreversible actions such as pushing or deleting only proceed when they continue something the transcript already authorized.

```
/loop

```

A bare `/loop` runs this prompt at a [dynamically chosen interval](https://code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval). Add an interval, for example `/loop 15m`, to run it on a fixed schedule instead. To replace the built-in prompt with your own default, see [Customize the default prompt with loop.md](https://code.claude.com/docs/en/scheduled-tasks#customize-the-default-prompt-with-loop-md).
On Bedrock, Vertex AI, and Microsoft Foundry, `/loop` with no prompt prints the usage message instead of running the maintenance prompt.
### 
[​](https://code.claude.com/docs/en/scheduled-tasks#customize-the-default-prompt-with-loop-md)
Customize the default prompt with loop.md
A `loop.md` file replaces the built-in maintenance prompt with your own instructions. It defines a single default prompt for bare `/loop`, not a list of separate scheduled tasks, and is ignored whenever you supply a prompt on the command line. To schedule additional prompts alongside it, use `/loop <prompt>` or [ask Claude directly](https://code.claude.com/docs/en/scheduled-tasks#manage-scheduled-tasks). Claude looks for the file in two locations and uses the first one it finds.  
| Path  | Scope  |  
| --- | --- |  
| `.claude/loop.md`  | Project-level. Takes precedence when both files exist.  |  
| `~/.claude/loop.md`  | User-level. Applies in any project that does not define its own.  |  
The file is plain Markdown with no required structure. Write it as if you were typing the `/loop` prompt directly. The following example keeps a release branch healthy:
.claude/loop.md

```
Check the `release/next` PR. If CI is red, pull the failing job log,
diagnose, and push a minimal fix. If new review comments have arrived,
address each one and resolve the thread. If everything is green and
quiet, say so in one line.

```

Edits to `loop.md` take effect on the next iteration, so you can refine the instructions while a loop is running. When no `loop.md` exists in either location, the loop falls back to the built-in maintenance prompt. Keep the file concise: content beyond 25,000 bytes is truncated.
On Bedrock, Vertex AI, and Microsoft Foundry, `loop.md` isn’t read and `/loop` with no prompt prints the usage message instead.
### 
[​](https://code.claude.com/docs/en/scheduled-tasks#stop-a-loop)
Stop a loop
To stop a `/loop` while it is waiting for the next iteration, press `Esc`. This clears the pending wakeup so the loop does not fire again. Tasks you scheduled by [asking Claude directly](https://code.claude.com/docs/en/scheduled-tasks#manage-scheduled-tasks) are not affected by `Esc` and stay in place until you delete them. In [self-paced mode](https://code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval), Claude can also end the loop on its own by not scheduling the next wakeup once the task is provably complete. Loops on a fixed interval keep running until you stop them or [seven days elapse](https://code.claude.com/docs/en/scheduled-tasks#seven-day-expiry).
## 
[​](https://code.claude.com/docs/en/scheduled-tasks#set-a-one-time-reminder)
Set a one-time reminder
For one-shot reminders, describe what you want in natural language instead of using `/loop`. Claude schedules a single-fire task that deletes itself after running.

```
remind me at 3pm to push the release branch

```


```
in 45 minutes, check whether the integration tests passed

```

Claude pins the fire time to a specific minute and hour using a cron expression and confirms when it will fire.
## 
[​](https://code.claude.com/docs/en/scheduled-tasks#manage-scheduled-tasks)
Manage scheduled tasks
Ask Claude in natural language to list or cancel tasks, or reference the underlying tools directly.

```
what scheduled tasks do I have?

```


```
cancel the deploy check job

```

Under the hood, Claude uses these tools:  
| Tool  | Purpose  |  
| --- | --- |  
| `CronCreate`  | Schedule a new task. Accepts a 5-field cron expression, the prompt to run, and whether it recurs or fires once.  |  
| `CronList`  | List all scheduled tasks with their IDs, schedules, and prompts.  |  
| `CronDelete`  | Cancel a task by ID.  |  
Each scheduled task has an 8-character ID you can pass to `CronDelete`. A session can hold up to 50 scheduled tasks at once.
## 
[​](https://code.claude.com/docs/en/scheduled-tasks#how-scheduled-tasks-run)
How scheduled tasks run
The scheduler checks every second for due tasks and enqueues them at low priority. A scheduled prompt fires between your turns, not while Claude is mid-response. If Claude is busy when a task comes due, the prompt waits until the current turn ends. All times are interpreted in your local timezone. A cron expression like `0 9 * * *` means 9am wherever you’re running Claude Code, not UTC.
### 
[​](https://code.claude.com/docs/en/scheduled-tasks#jitter)
Jitter
To avoid every session hitting the API at the same wall-clock moment, the scheduler adds a deterministic offset to fire times:
  * Recurring tasks fire up to 30 minutes after the scheduled time (or up to half the interval, for tasks that run more often than hourly). An hourly job scheduled for `:00` may fire anywhere up to `:30`.
  * One-shot tasks scheduled for the top or bottom of the hour fire up to 90 seconds early.

The offset is derived from the task ID, so the same task always gets the same offset. If exact timing matters, pick a minute that is not `:00` or `:30`, for example `3 9 * * *` instead of `0 9 * * *`, and the one-shot jitter will not apply.
### 
[​](https://code.claude.com/docs/en/scheduled-tasks#seven-day-expiry)
Seven-day expiry
Recurring tasks automatically expire 7 days after creation. The task fires one final time, then deletes itself. This bounds how long a forgotten loop can run. If you need a recurring task to last longer, cancel and recreate it before it expires, or use [Routines](https://code.claude.com/docs/en/routines) or [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks) for durable scheduling.
## 
[​](https://code.claude.com/docs/en/scheduled-tasks#cron-expression-reference)
Cron expression reference
`CronCreate` accepts standard 5-field cron expressions: `minute hour day-of-month month day-of-week`. All fields support wildcards (`*`), single values (`5`), steps (`*/15`), ranges (`1-5`), and comma-separated lists (`1,15,30`).  
| Example  | Meaning  |  
| --- | --- |  
| `*/5 * * * *`  | Every 5 minutes  |  
| `0 * * * *`  | Every hour on the hour  |  
| `7 * * * *`  | Every hour at 7 minutes past  |  
| `0 9 * * *`  | Every day at 9am local  |  
| `0 9 * * 1-5`  | Weekdays at 9am local  |  
| `30 14 15 3 *`  | March 15 at 2:30pm local  |  
Day-of-week uses `0` or `7` for Sunday through `6` for Saturday. Extended syntax like `L`, `W`, `?`, and name aliases such as `MON` or `JAN` is not supported. When both day-of-month and day-of-week are constrained, a date matches if either field matches. This follows standard vixie-cron semantics.
## 
[​](https://code.claude.com/docs/en/scheduled-tasks#disable-scheduled-tasks)
Disable scheduled tasks
Set `CLAUDE_CODE_DISABLE_CRON=1` in your environment to disable the scheduler entirely. The cron tools and `/loop` become unavailable, and any already-scheduled tasks stop firing. See [Environment variables](https://code.claude.com/docs/en/env-vars) for the full list of disable flags.
## 
[​](https://code.claude.com/docs/en/scheduled-tasks#limitations)
Limitations
Session-scoped scheduling has inherent constraints:
  * Tasks only fire while Claude Code is running and idle. Closing the terminal or letting the session exit stops them firing.
  * No catch-up for missed fires. If a task’s scheduled time passes while Claude is busy on a long-running request, it fires once when Claude becomes idle, not once per missed interval.
  * Starting a fresh conversation clears all session-scoped tasks. Resuming with `claude --resume` or `claude --continue` restores tasks that have not expired: recurring tasks within seven days of creation, and one-shot tasks whose scheduled time has not yet passed. Background Bash and monitor tasks are never restored on resume.

For cron-driven automation that needs to run unattended:
  * [Routines](https://code.claude.com/docs/en/routines): run on Anthropic-managed infrastructure on a schedule, via API call, or on GitHub events
  * [GitHub Actions](https://code.claude.com/docs/en/github-actions): use a `schedule` trigger in CI
  * [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks): run locally on your machine


Was this page helpful?
YesNo
[Push external events to Claude](https://code.claude.com/docs/en/channels)[Goals](https://code.claude.com/docs/en/goal)
⌘I
[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
Company
[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)
Help and security
[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)
Learn
[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)
Terms and policies
[Privacy choices](https://www.anthropic.com/legal/privacy)[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)
Assistant
Responses are generated using AI and may contain mistakes.

