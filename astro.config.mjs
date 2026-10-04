import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Sito statico. Definitivo: https://www.ago.archi
// Prova su GitHub Pages: SITE_URL=https://agoarchitettura.github.io SITE_BASE=/sito-ago PUBLIC_NOINDEX=1
export default defineConfig({
  site: process.env.SITE_URL || 'https://www.ago.archi',
  base: process.env.SITE_BASE || '/',
  integrations: [sitemap()],
  build: { format: 'directory' },
  compressHTML: true,
  image: { service: { entrypoint: 'astro/assets/services/sharp' } },
});
