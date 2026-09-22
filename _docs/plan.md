# Weekly Project Feedback Tool — Scope

## Audience
All team members on a project, prompted weekly via Slack.

## Purpose
Track project health — progress, blockers, and risks. Not sentiment or morale.

## Setup (per project)
The project lead configures each project via a web dashboard:
- Custom questions (questions vary by project/team, not a fixed global set)
- Schedule: day/time the prompt goes out, and the response deadline
- Recipients
- Default attribution mode — named or anonymous, chosable per project

## Collection
- A Slack bot sends the project-specific questions to all team members weekly.
- The bot sends reminders to anyone who hasn't responded before the deadline.

## Digest
- An LLM aggregates all responses into a summary each week.
- The digest is posted to a broader group (e.g. team channel, stakeholders), not just the project lead.

## Dashboard
- Shows the latest digest.
- Shows trends over time — comparing digests week over week.

## Target
Built for internal use first, with an eye toward being a usable product for others.

## Tech Stack
- **Dashboard + API**: FastAPI (Python), managed with `uv`
- **Slack bot**: Slack Bolt for Python, running in the same app
- **Database**: Postgres (via SQLAlchemy) — Supabase can still host it, for auth and an admin UI
- **Scheduler**: APScheduler, for weekly prompts and reminders
- **LLM**: Claude API, called via the Python SDK to generate the digest
- **Tests**: pytest, run with `uv run pytest`
