# Source Observations

Reference used for this child skill test:

- `https://www.notion.com/`

Captured local inputs:

- [`inputs/notion/index.html`](../../../inputs/notion/index.html)
- [`inputs/notion/home-top.png`](../../../inputs/notion/home-top.png)
- [`inputs/notion/home-full.png`](../../../inputs/notion/home-full.png)
- section verification screenshots under [`inputs/notion/`](../../../inputs/notion/)

Captured on 2026-06-11. HTML downloaded via curl; visual evidence comes from screenshots.

## Observed Facts

- Page title: "The AI workspace that works for you. | Notion".
- The current first viewport is not light-first. It uses a deep midnight-blue campaign hero.
- Hero headline: "Meet the night shift." Large, white, centered, heavy humanist sans.
- Supporting text explains Notion agents working 24/7.
- Primary CTA "Get Notion free" uses an indigo fill `#455dd3`, white text, compact radius, and medium weight.
- Secondary CTA "Request a demo" appears as a darker blue campaign button in the hero.
- The hero contains a large white product window showing a workspace / task board interface.
- Electric-blue hand-drawn track lines move behind and around the product window.
- Sticker-like agent badges and integration app badges sit on the tracks.
- A dark logo belt with white partner marks sits across the bottom of the hero.
- After the hero, the page returns to Notion's warm white/off-white productivity language.
- Lower sections use bento-like cards, rounded white panels, soft pastel feature cards, compact arrow controls, and large section headings.
- Text uses a NotionInter / Inter-like humanist sans stack.
- Shapes are consistently rounded: compact `8px` buttons, larger rounded product cards, and soft bento panels.

## Why This Reference Is Useful

This site is a strong UIgod test because it contains two style layers that an agent must not collapse:

- a current campaign skin: dark AI night-shift hero, stickers, tracks, product window
- a long-lived Notion base language: warm canvas, compact controls, bento product storytelling

The first Claude-generated test captured the base language but missed the campaign skin. That made the output feel like generic friendly SaaS rather than the current Notion homepage.

## Preserved vs Synthesized

Preserved directly from the source:

- dark midnight hero structure
- large centered white headline
- compact blue CTA system
- white product-window focal point
- hand-drawn blue track motif
- sticker-like agent accents
- dark partner-logo belt
- warm lower-page bento sections
- humanist sans type voice

Synthesized for the child skill:

- exact product-window contents
- sticker illustrations and partner logos
- reusable component HTML fragments
- normalized token definitions in `DESIGN.md`
- responsive and iteration guidance

## Known Uncertainty

- Exact Notion assets, video frames, and icon files are not bundled.
- Lower-page card copy and some section ordering are represented as style-equivalent examples rather than literal reconstruction.
- The child skill is currently optimized for campaign homepages, not pricing, docs, or in-product app screens.
