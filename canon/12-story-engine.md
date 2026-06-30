# 12 · Story Engine

How the comic tells itself. This is the *mechanism* layer — grounded entirely in
`../index.html`.

## The format
A single-file, dependency-free, self-running motion comic. 116 scenes = 1 title
card + 115 panels. Auto-advances; each panel holds a few seconds with a slow
Ken-Burns drift, then cuts to the next. Runs online or offline, desktop or mobile.

## Two data structures drive everything
- **`beats`** — one object per panel: `src`, `ratio` (w÷h), `duration` (ms),
  `mode` (`"green"` | `"red"`), optional `motion`, and optional overlay text
  (`hud`, `title`, `text`, `terminal`). Most panels bake text into the art, so
  overlays are usually omitted.
- **`ORDER`** — the play sequence (a list of filenames). The engine sorts `beats`
  by this list, so **to re-cut the story you just rearrange `ORDER`.**

[`../RUNNING-ORDER.md`](../RUNNING-ORDER.md) mirrors the current sequence with titles.

## Performance model
- Virtual window: only 3 scenes mounted in the DOM at once (current ±1).
- Ken-Burns + filters run **only on the active panel** to free GPU memory
  (critical on iPad Safari). Images are `decoding="async"`.

## Authoring
- **Add a panel:** drop art in `assets/`, add a `beats` entry, insert its
  filename into `ORDER`.
- **Re-cut:** reorder the lines in `ORDER`.
- **Color a beat:** `mode: "green"` or `"red"` (see [Symbol Dictionary](05-symbol-dictionary.md)).

## Accessibility
- `prefers-reduced-motion`: holds each panel still, keeps the look, drops drift /
  flicker / noise / glitch.
- Keyboard: `←` / `→` / `Space`; on-screen prev / play-pause / next.

## TODO
- [ ] Keep this in sync if the engine in `index.html` changes.
