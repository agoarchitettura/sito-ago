import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { parse } from 'yaml';

/** Legge un file YAML di src/data/ (testi modificabili del sito). */
export function leggi<T = any>(nome: string): T {
  return parse(readFileSync(join(process.cwd(), 'src', 'data', `${nome}.yaml`), 'utf8')) as T;
}
