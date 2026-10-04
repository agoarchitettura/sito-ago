import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const voce = z.object({ voce: z.string(), valore: z.string() });

export const CATEGORIE = [
  'Restauro', 'Nuova edificazione', 'Arredo urbano e light design',
  'Architettura rurale', 'New rural', 'Sport', 'Interni',
] as const;

const progetti = defineCollection({
  loader: glob({ pattern: '*/index.md', base: './src/content/progetti' }),
  schema: ({ image }) => {
    const foto = z.object({ img: image(), didascalia: z.string() });
    return z.object({
      titolo: z.string(),
      sottotitolo: z.string(),
      sintesi: z.string(),
      categoria: z.enum(CATEGORIE),
      stato: z.enum(['Progetto', 'In costruzione', 'Realizzato']),
      luogo: z.string(),
      anni: z.string(),
      committente: z.string(),
      in_evidenza: z.boolean().default(false),
      ordine: z.number().default(100),
      copertina: image(),
      apertura: image(),
      carosello: z.array(image()).default([]),
      dati: z.array(voce),
      sezioni: z.array(z.object({
        titolo: z.string(),
        testo: z.array(z.string()),
        schizzi: z.array(foto).default([]),
        figure: z.array(foto).default([]),
        tuttoschermo: z.array(foto).default([]),
        tabella: z.array(voce).optional(),
        nota_tabella: z.string().optional(),
        inglese: z.array(z.string()).optional(),
        extra: z.enum(['struttura', 'energia', 'cronologia']).optional(),
      })),
      cronologia: z.array(z.object({
        data: z.string(), titolo: z.string(), testo: z.string(), img: image().optional(),
      })).default([]),
      disegni: z.array(foto).default([]),
      galleria: z.array(foto).default([]),
    });
  },
});

export const collections = { progetti };
