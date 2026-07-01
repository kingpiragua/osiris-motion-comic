# OSIRIS.EXE // ARCHIVE 01 — Motion Comic

Vertical-scroll (webtoon-style) motion comic player for OSIRIS.EXE Issue #1.

## Run it
Open `index.html` in a browser, or serve the folder:
```
cd osiris-motion-comic
python3 -m http.server 8000
# visit http://localhost:8000
```
Scroll to descend through the issue. Ken Burns pan/zoom, CRT scanlines, and
signal-color glow (green→red) are driven by scroll position. The HUD and progress
bar shift from green to red as the story turns.

## Structure
```
osiris-motion-comic/
├── index.html        # the player (no build step, no dependencies)
├── config.js         # page order, captions, signal color per page — EDIT THIS
├── README.md
└── pages/            # both .webp (default, ~1.8MB total) and .png (full-res)
    ├── 00_cover
    ├── 01_cold_open
    ├── 02_room
    ├── 03_static
    ├── 04_dead_devices
    ├── 05_reception
    └── 06_seen
```

## Editing
- **Change captions / order / signal color:** edit `config.js`. Each page has
  `signal` ("neutral" | "green" | "green-red" | "red"), `pan` (start focal point),
  and `label` (caption).
- **Full-res vs. fast-load:** `config.js` → `ext:"webp"` (default, small) or
  `ext:"png"` (full quality). WebP is ~90% smaller — fixes the iPad payload/crash issue.
- **Add pages for #2:** drop images in `pages/`, add entries to `config.js`.

## Reading order (signal rhythm)
Cover → 1 cold open (⚫+green) → 2 room (⚫) → 3 static (🟢) →
4 dead devices (⚫→🔴) → 5 reception / the turn (🟢→🔴) → 6 seen (🔴) → TO BE CONTINUED

Companion docs: `STYLE_BIBLE_v1.6.md`, `ISSUE_01_BREAKDOWN.md`.

*DSB LABS // DISK DARIÁN — Memory is the oldest form of resistance.*
