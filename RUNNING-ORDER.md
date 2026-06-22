# OSIRIS.EXE — Running Order

**164 scenes** = 1 title card + 38 curated story panels + 125 bulk-imported extras.

> Sequence lives in the `ORDER` list inside `index.html` (after the `beats` array).
> Rearrange those lines to re-cut; every src in `beats` must appear in `ORDER` once.

## Story spine (curated)

| # | File | Panel |
|---|------|-------|
| — | *(built-in)* | **TITLE CARD** |
| 1 | 25-vieques-coldopen.webp | Cold open — Vieques 1999 + title plate |
| 2 | 27-prologue-cover.png | Prologue cover — "The Week Isn't Real" |
| 3 | 01-prologue.png | The archive opens |
| 4 | 30-card-game-manual.png | The card game was the manual |
| 5 | 03-school.png | The boy, 1987 |
| 6 | 05-questions.png | "Don't say anything crazy" |
| 7 | 04-cage.png | Some inherit silence |
| 8 | 33-justicia-memoria.webp | Justicia sin memoria es control |
| 9 | 23-signal-in-walls.webp | The signal was already inside the walls |
| 10 | 35-alley-watchers.jpg | Alley watchers |
| 11 | 28-syrena-profile.png | Syrena Sánchez — memory keeper |
| 12 | 12-syrena-terminals.png | They used the blueprint to make the game |
| 13 | 31-bloodline-dialogue.png | Someone else found the bloodline |
| 14 | 32-split-process-dialogue.png | A split process you don't have access to |
| 15 | 02-cooper-file.png | Behold a Pale Horse / the Cooper file |
| 16 | 13-ni-olvido.png | Ni olvido ni perdón |
| 17 | 07-judge-protocol.png | The justice engine |
| 18 | 19-enough-is-enough.webp | Enough is enough |
| 19 | 21-ser-boricua.webp | Ser boricua es un honor |
| 20 | 18-diskdarian-blackbook.webp | The youth are searching |
| 21 | 06-enmascarado.png | We learned to unthread the grid |
| 22 | 24-cheating-mask.webp | "That's cheating, you know?" |
| 23 | 11-enmascarado-unit.png | Enmascarado unit file |
| 24 | 26-vejigante-permiso.webp | El vejigante no pide permiso |
| 25 | 34-osiris-godform.jpg | Osiris godform — crook & flail |
| 26 | 16-duat-vessel.png | Keeper of the Duat / you were a vessel |
| 27 | 36-duat-godform.jpg | Cybernetic winged Duat god |
| 28 | 37-duat-cybergod.jpg | Duat cyber-deity |
| 29 | 14-desierto.png | El desierto no perdona |
| 30 | 10-mask-signal.png | The mask is the signal |
| 31 | 38-skull-confrontation.jpg | Skull-mask confrontation (climax lead-in) |
| 32 | 08-merge.png | Identity merge **(climax)** |
| 33 | 20-second-signal.webp | You thought it started with Frank **(twist)** |
| 34 | 15-body-changes.png | The body changes, the signal remains |
| 35 | 09-archive-rises.png | We are the archive |
| 36 | 17-archive-never-died.png | The archive never died, it remembered **(coda)** |
| 37 | 29-elenita-sheet.png | *Bonus* — Elenita de Jesús model sheet |
| 38 | 22-jdm-triptych.webp | *Bonus* — JDM triptych |

## Bulk import — pending curation (scenes 39–163)

Files **`39-extra.*` … `163-extra.*`** are the 125 images bulk-added in filename
order. They play *after* the spine above. These are **unsorted and unnamed** —
mixed in are duplicates-of-theme, reference shots, and phone photos.

**To curate:** open the comic, watch the tail, and for each one either
(a) move its `ORDER` line up into the story where it belongs and give the file a
real name, or (b) delete its `ORDER` + `beats` lines to drop it.

- Videos were moved out of the way to `assets/_videos/` (engine is image-only for now).
- A pre-bulk backup of the page is at `index.html.bak`.
