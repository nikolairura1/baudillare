from pathlib import Path
from bs4 import BeautifulSoup
import json,html
r=Path(__file__).parent
for year in ('1845','1846'):
 cards=[]
 for f in sorted((r/'chapters').glob('*.html')):
  if f.name.startswith('1846-')!=(year=='1846'):continue
  for p in BeautifulSoup(f.read_text(),'html.parser').select('.insert-point'):
   d=json.loads(p.select_one('.marker-data').string or '{}')
   if not d.get('active'):continue
   images=[x for x in (r/d['folder']).glob('artwork.*') if x.is_file() and x.suffix.lower() in ('.jpg','.jpeg','.png','.webp','.gif')]
   if not images:continue
   a,t=d.get('artist',''),d.get('title_en') or d.get('title','')
   cards.append(f'<div class="gallery-entry" data-search="{html.escape((a+" "+t+" "+f.stem).lower(),quote=True)}"><a href="chapters/{f.name}#{p["data-marker-id"]}" title="Folder: {d["folder"]}"><img loading="lazy" src="{images[0].relative_to(r)}" alt="{html.escape(t)}"><strong>{html.escape(a)} — {html.escape(t)}</strong><small>{html.escape(f.stem)} · {html.escape(d["folder"])}</small></a></div>')
 page=f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="assets/site.css"><title>Salon {year} gallery</title></head><body><header class="top"><a href="index.html">Charles Baudelaire · The Salons</a></header><main class="salon-gallery"><a href="index.html">← Contents</a><h1>Salon of {year} · Illustrated gallery</h1><p>{len(cards)} illustrated works in this edition.</p><div class="gallery-controls"><input id="search" placeholder="Search artist, title, chapter"></div><div class="salon-gallery-grid">{"".join(cards)}</div></main><script>document.getElementById('search').addEventListener('input',e=>document.querySelectorAll('.gallery-entry').forEach(x=>x.hidden=!x.dataset.search.includes(e.target.value.toLowerCase())));</script></body></html>'''
 (r/f'gallery-{year}.html').write_text(page)
 print(year,len(cards))
