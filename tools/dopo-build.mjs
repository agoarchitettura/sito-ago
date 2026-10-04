// Dopo la build: privacy.html e termini.html devono essere veri file (non cartelle),
// perché gli indirizzi /privacy.html e /termini.html sono registrati in Google Cloud per l'app di Hal.
import { existsSync, statSync, renameSync, rmSync } from 'node:fs';
import { join } from 'node:path';
const out = process.argv[2] || 'dist';
for (const n of ['privacy', 'termini']) {
  const cartella = join(out, `${n}.html`);
  if (existsSync(cartella) && statSync(cartella).isDirectory()) {
    renameSync(join(cartella, 'index.html'), join(out, `${n}.tmp`));
    rmSync(cartella, { recursive: true });
    renameSync(join(out, `${n}.tmp`), cartella);
    console.log(`${n}.html -> file`);
  }
}
