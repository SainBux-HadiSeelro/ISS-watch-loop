# 🛰️ ISS Watch Loop // Live Space Station Tracker

[![Live Demo](https://img.shields.io/badge/Live_Demo-iss--watch--loop.vercel.app-0284c7?style=for-the-badge&logo=vercel&logoColor=white)](https://iss-watch-loop.vercel.app)
[![Auto Deploy](https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel)](https://iss-watch-loop.vercel.app)

> 🔴 **Live Demo Website**: [**https://iss-watch-loop.vercel.app**](https://iss-watch-loop.vercel.app)  
> Track where the International Space Station (ISS) and astronauts are right now in real time!

---

A high-tech demonstration of **Concept 4: In-Session Loops** in Loop Engineering. This project pairs an autonomous terminal heartbeat loop with a modern, intuitive, and non-technical friendly web dashboard.

---

## 🌍 1. Live Interactive Web Dashboard

Check the live demo at [**iss-watch-loop.vercel.app**](https://iss-watch-loop.vercel.app) — built to be simple and engaging for everyone:

- 📍 **Instant Location**: Instantly shows whether astronauts are flying over a specific country or open ocean.
- 🚀 **Travel Speed**: Real-time speed (~27,600 km/h) with easy-to-understand context (*circles Earth every 90 mins!*).
- 📏 **Height Above Earth**: ~420 km altitude (*40x higher than airplanes*).
- ☀️ **Astronauts' View**: Shows daylight vs night view (*astronauts see 16 sunrises and sunsets a day*).
- 🗺️ **World Map**: Smooth dark map powered by Leaflet.js showing the Station marker, radar ring, and flight trajectory path.
- 👨‍🚀 **Space Facts**: Fun bite-sized facts about the ISS for curious minds.
- ⚙️ **Technical Details Toggle**: Dropdown for developers & space enthusiasts who want exact coordinates, ground footprint, and satellite telemetry.

### Run Locally
You can also run or open `index.html` locally:

```bash
# On Windows PowerShell:
Start-Process index.html

# Or run a local python server:
python -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

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
