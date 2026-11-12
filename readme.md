# ISS Watch Loop // Autonomous Telemetry & Orbit Tracker

A high-tech demonstration of **Concept 4: In-Session Loops** in Loop Engineering. This project pairs an autonomous terminal heartbeat loop with a modern, glassmorphic mission-control web dashboard tracking the International Space Station (ISS) in real time.

---

## 🛰️ 1. Interactive Web Dashboard (`index.html`)

A futuristic, cyber-themed space mission-control interface built for real-time orbital visualization and telemetry monitoring:

- **Live CartoDB Dark Matter Map**: High-performance interactive world map powered by Leaflet.js with custom ISS radar pulse marker and historic trajectory trail.
- **Autonomous Telemetry Loop**: Configurable polling heartbeat (`2s`, `5s`, `10s`, `30s`, `60s`) with smooth progress indicator.
- **Subsatellite Telemetry**: Real-time Latitude & Longitude (Decimal & DMS), Orbital Velocity (km/h, mph, km/s), Altitude (LEO), and Footprint diameter.
- **Dynamic Reverse Geocoding**: Real-time territory resolution detecting whether the ISS is over a specific country/region or open ocean waters.
- **Solar Visibility State**: Computes daylight vs eclipsed (nighttime) orbital phases.
- **Autonomous Watcher Feed**: Live terminal streaming each cycle's telemetry packets.
- **Web Audio Sci-Fi Chirp**: Synthesized acoustic feedback on coordinate locks.
- **Session Export**: Export flight telemetry logs directly to JSON.

### How to Run the Frontend
You can open `index.html` directly in any web browser:

```bash
# On Windows PowerShell:
Start-Process index.html

# Or run a quick local server:
python -m http.server 8000
```
Then visit `http://localhost:8000` in your browser. It also deploys directly to **GitHub Pages** with zero build configuration!

---

## 🐍 2. Python In-Session Watch Loop (`iss_watch.py`)

A pure-Python terminal loop showcasing an unattended heartbeat:

```bash
python iss_watch.py
```

### What it does:
- Queries the ISS state from `https://api.wheretheiss.at/v1/satellites/25544` on a 60-second interval.
- Resolves geographical coordinates to land territories via BigDataCloud reverse geocoding.
- Appends telemetry logs to `iss_watch.log` and errors to `iss_watch_err.log`.

---

## 🧠 Why This Matters (Loop Engineering Concept 4)

An **in-session loop** operates like a responsive kitchen timer — executing unattended autonomous cycles while the session stays open, and closing cleanly when no longer needed. It forms the foundational stepping stone between manual polling and fully decoupled autonomous agentic workflows.
