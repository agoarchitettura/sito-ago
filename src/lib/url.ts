/** Prefisso del sito (vuoto in produzione su www.ago.archi; "/sito-ago" nella prova su GitHub Pages). */
export const base = import.meta.env.BASE_URL.replace(/\/$/, '');
export const u = (percorso: string) => base + percorso;
