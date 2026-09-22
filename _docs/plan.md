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
- **Dashboard + API**: Next.js (App Router), deployed on Vercel
- **Slack bot**: Slack Bolt (JS), running as serverless/Edge functions (or a small Node process if socket mode is needed)
- **Database**: Supabase (Postgres) — also provides auth and an admin UI
- **Scheduler**: Vercel Cron or Supabase scheduled Edge Functions, for weekly prompts and reminders
- **LLM**: Claude API, called from a serverless function to generate the digest
