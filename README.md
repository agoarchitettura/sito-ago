# Sito di Ago Architettura

Sito statico (Astro). Contenuti in file di testo:

- `src/content/progetti/<nome>/index.md` + `img/` — una cartella per progetto (dati, sezioni, immagini);
- `src/data/*.yaml` — testi di Home, Servizi, Studio, Contatti e dati dello studio;
- `src/data/privacy.html`, `termini.html` — testi legali (gli indirizzi /privacy.html e /termini.html non vanno cambiati).

Comandi: `npm install`, `npm run dev` (anteprima), `npm run build` (sito in `dist/`).
Dopo la build, `tools/dopo-build.mjs` trasforma privacy e termini in file veri.
Le immagini si ottimizzano da sole in fase di build (WebP, più dimensioni).
