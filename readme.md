# In-Session Watch Loop

A small demo of the simplest kind of "heartbeat" in loop engineering: an **in-session loop** that repeats on a timer only while your session stays open, and stops the moment it's no longer needed.

## What it does
- `slow_task.sh` simulates a long-running job (sleeps, then writes a completion flag file).
- `watch_loop.sh` checks every 60 seconds whether the task has finished. The moment it has, it announces this once and exits cleanly — no polling forever, no manual watching required.

## Why this matters

This is Concept 4 of loop engineering: an in-session loop is like a kitchen timer — it only works while you're "in the kitchen" (session open). Close the session, and the watching stops. It's the simplest of the four heartbeats (in-session, conditional, scheduled, event-driven), and the first building block before moving to loops that run fully unattended.

## Run it

```bash
./slow_task.sh &
./watch_loop.sh
```

Walk away — no need to watch the terminal. It tells you the moment the task is done, then exits on its own.