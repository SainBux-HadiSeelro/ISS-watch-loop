# 📡 ISS Watch Loop — Telemetry & Data Schema Specification
**Document ID:** `SCHEMA-LOOP-004-ISS`  
**Classification:** Telemetry Data Contracts & Interface Schemas  
**Applies to:** `iss_watch.py`, `index.html`, `iss_watch.log`, `iss_watch_err.log`  

---

## 1. Upstream Oracle Contracts

### 1.1 WhereTheISS.at REST API v1
- **Endpoint:** `GET https://api.wheretheiss.at/v1/satellites/25544`
- **Cadence / Limit:** Max 1 req/sec recommended (Loop consumes at 1 req/60s in Python, 1 req/3s in Web HUD)
- **Protocol:** HTTPS / TLS 1.3
- **Socket Timeout:** 30 seconds

#### Payload Schema (JSON)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ISSStateVector",
  "type": "object",
  "required": [
    "name",
    "id",
    "latitude",
    "longitude",
    "altitude",
    "velocity",
    "visibility",
    "footprint",
    "timestamp",
    "daynum",
    "solar_lat",
    "solar_lon",
    "units"
  ],
  "properties": {
    "name": { "type": "string", "example": "iss" },
    "id": { "type": "integer", "example": 25544 },
    "latitude": { "type": "number", "minimum": -90.0, "maximum": 90.0 },
    "longitude": { "type": "number", "minimum": -180.0, "maximum": 180.0 },
    "altitude": { "type": "number", "description": "Altitude in kilometers", "example": 418.23 },
    "velocity": { "type": "number", "description": "Velocity in km/h", "example": 27612.45 },
    "visibility": { "type": "string", "enum": ["daylight", "eclipsed"] },
    "footprint": { "type": "number", "description": "Ground footprint diameter in km" },
    "timestamp": { "type": "integer", "description": "Unix epoch seconds" },
    "daynum": { "type": "number" },
    "solar_lat": { "type": "number" },
    "solar_lon": { "type": "number" },
    "units": { "type": "string", "enum": ["kilometers", "miles"] }
  }
}
```

---

### 1.2 BigDataCloud Reverse Geocoding Client
- **Endpoint:** `GET https://api.bigdatacloud.net/data/reverse-geocode-client`
- **Query Parameters:**
  - `latitude`: Float (`-90.0` to `90.0`)
  - `longitude`: Float (`-180.0` to `180.0`)
  - `localityLanguage`: String (default: `"en"`)
- **Protocol:** HTTPS

#### Normalized Output Mapping
The agent normalizes varying international administrative divisions according to the following priority cascade:

```
locality ─────────► [Priority 1]
    │
    ▼ (null/empty)
city ─────────────► [Priority 2]
    │
    ▼ (null/empty)
principalSubdivision ──► [Priority 3]
    │
    ▼ (null/empty)
"over an ocean or remote area" [Default Fallback]
```

---

## 2. Telemetry Persistence Formats

The agent produces two persistent append-only log channels:

### 2.1 Standard Telemetry Stream (`iss_watch.log`)
Each line represents an atomic, processed observation event formatted as follows:

```
<TIMESTAMP_UTC> UTC | Lat: <LATITUDE> | Lon: <LONGITUDE> | Location: <LOCATION_SYNTHESIS>
```

#### Field Specifications:
| Field | Type | Precision / Format | Example |
| :--- | :--- | :--- | :--- |
| `TIMESTAMP_UTC` | String | `YYYY-MM-DD HH:MM:SS` (UTC) | `2026-11-14 04:15:30` |
| `LATITUDE` | Float | 4 decimal places (`{lat:.4f}`) | `-23.4192` |
| `LONGITUDE` | Float | 4 decimal places (`{lon:.4f}`) | `132.8941` |
| `LOCATION_SYNTHESIS` | String | Formatted geopolitical descriptor | `near Alice Springs, Australia` |

#### Sample Log Slice:
```log
2026-11-14 04:14:28 UTC | Lat: -21.4920 | Lon: 130.1492 | Location: near Tanami, Australia
2026-11-14 04:15:28 UTC | Lat: -25.2911 | Lon: 134.8104 | Location: near Finke, Australia
2026-11-14 04:16:28 UTC | Lat: -29.0118 | Lon: 139.7820 | Location: over an ocean or remote area
```

---

### 2.2 Error Audit Stream (`iss_watch_err.log`)
Each line captures trapped exceptions to ensure the host loop process remains active:

```
<TIMESTAMP_UTC> UTC | Error: <EXCEPTION_STRING>
```

#### Sample Error Slice:
```log
2026-11-14 04:10:12 UTC | Error: <urlopen error [Errno 11001] getaddrinfo failed>
2026-11-14 04:11:15 UTC | Error: HTTP Error 503: Service Unavailable
```

---

## 3. Web Telemetry Client State Model (`index.html`)

The client HUD maintains an in-memory reactive telemetry state:

```typescript
interface ISSClientState {
  currentLat: number;             // Instantaneous latitude
  currentLon: number;             // Instantaneous longitude
  prevLat: number | null;         // Preceding latitude for delta calculation
  prevLon: number | null;         // Preceding longitude for delta calculation
  totalDistanceMovedKm: number;   // Cumulative Haversine displacement
  altitudeKm: number;             // Radial altitude above WGS84 ellipsoid
  velocityKmh: number;            // Instantaneous orbital speed
  visibility: 'daylight' | 'eclipsed';
  solarCoordinates: {
    lat: number;
    lon: number;
  };
  pingCount: number;              // Total poll cycles performed in session
  cadenceSeconds: number;         // Active polling frequency (default: 3)
}
```
