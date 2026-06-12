# Source Observations

Reference used for this child skill:

- `https://www.studiobrot.de/`

Captured local inputs:

- [`inputs/studiobrot/index.html`](../../../inputs/studiobrot/index.html)
- [`inputs/studiobrot/home-full.png`](../../../inputs/studiobrot/home-full.png)
- [`inputs/studiobrot/home-top.png`](../../../inputs/studiobrot/home-top.png)
- [`inputs/studiobrot/home-delayed.png`](../../../inputs/studiobrot/home-delayed.png)

## Observed Facts

- Built with Kirby CMS, Astro frontend, and swup for page transitions.
- Uses smooth scroll wrapper (`#smooth-wrapper` / `#smooth-content`).
- Theme color meta tag: `#ff2a00` (brand red-orange).
- Homepage first screen: full-height hero with oversized headline "breaking bread with brands." followed by autoplay showreel video.
- Desktop showreel is landscape; mobile showreel is portrait.
- Intro section uses a two-column 6/6 grid (headline left, body right).
- Client logo marquee: two rows of grayscale SVG logos scrolling horizontally via CSS animation.
- Case studies section: portrait-oriented image or autoplay video, witty h2 headline, description paragraph, "zur Story" CTA link.
- Services section: Swiper carousel with pagination dots, SVG illustration + h3 + body per slide (Markenaufbau, Design, Kommunikation).
- Statement section: centered text → bold punchline "Leise ist kaputt."
- Contact section: team photo + personal founders intro + email/phone CTA buttons with SVG icons.
- Newsletter: "Breaking Newsletter" headline, email input, arrow submit button.
- Footer: logo, address, phone, email, social icons (LinkedIn, Instagram) with pink (#FFBEF1) fill.
- Bread GIF mascot sits in the header as a signature playful element.
- Navigation: Start, Arbeiten, Kontakt.
- Social icons are custom SVG, filled with a distinctive pink.
- Content language: German with frequent English wordplay.

## CSS Extraction

CSS source: fetched from `https://www.studiobrot.de/assets/dist/scss/main.css?v1.7`

### Custom Properties (CSS Variables)
The source CSS does not use `:root` custom properties for colors directly. Instead, it uses SASS variables compiled to literal values. The following were extracted from the compiled CSS:

- `--red`: `#ff2a00` (used as background for .home main, .footer, .default)
- `--pink`: `#FFBEF1` (used as background for .project-list, section.contact, .footer .social-icon path hover)
- No other CSS custom properties found — all values are literal.

### Fonts
- **Display**: `FKScreamer` (custom font by F37 Foundry, declared via `@font-face` as `FKScreamer`), fallback `Helvetica, Arial, sans-serif`
  - Used on: `.more-cases`, `.home .intro-headline` (FKScreamer is the primary display face)
  - Note: This is a licensed custom font — applied examples must use alternatives (Bebas Neue, Oswald 800, or Impact with tight tracking)
- **Body**: `Helvetica, Arial, sans-serif` (system stack, no custom body font)
- **Button text**: inherits body font, not display font (except .more-cases)
- **Header nav**: inherits body font

### Border Treatments
| Usage | Element | border-radius | border-width | box-shadow |
|-------|---------|---------------|--------------|------------|
| Buttons (primary) | `.button` | `45px` | `3.5px` solid #000 | `6px 8px #000` |
| Buttons (small/phone) | `.button.phone` | `45px` | `3.5px` solid #000 | `6px 8px #000` |
| "Mehr Cases" button | `.more-cases` | `150px` | `7px` solid #000 | `12px 16px #000` |
| Service cards | `.service` | `30px` | `6px` solid #000 | none |
| Newsletter input | `input[type="email"]` | `45px` | `3.5px` solid #000 | none |
| Image hover state | `.project-list img:hover` | `16px` (transition from 0) | none | none |
| Service card image | `.service .image` container | none | none | none |
| Newsltter submit button | `.input-wrapper .subscribe .button` | `45px` (inherited) | `3.5px` | none (no shadow) |
| Header nav links | `nav ul li a` | 0 (none) | `1px` bottom border | none |

### Button Hover Effect
```css
.button:hover {
  transform: translate(6px, 8px);
  box-shadow: 0 0 #000;
}
```
The press-down effect: button shifts right+down by its shadow offset, and the shadow disappears — simulating a physical button being pressed.

The `.more-cases` button uses a larger press-down:
```css
.more-cases:hover {
  transform: translate(12px, 16px);
  box-shadow: 0 0 #000;
}
```

### Section Background Colors
| Section | CSS Class/Element | Background Color |
|---------|------------------|-----------------|
| Header | `.header` | `#ffffff` (transparent bg, fixed) |
| Hero / Home | `.home main` | `#ff2a00` (brand red) |
| Showreel | `.videointro` | transparent (inherits red from .home main) |
| Intro text | `.intro` | `#ffffff` |
| Logo marquee | `.logos` | `#000000` |
| Case studies | `.project-list` | `#FFBEF1` (signal pink) |
| Services | `.services` | `#ffffff` |
| Statement | `.statement` | transparent (white bg) |
| Contact | `section.contact` | `#FFBEF1` (signal pink) |
| Newsletter | `.newsletter` | `#ffffff` |
| Footer | `.footer` | `#ff2a00` (brand red) |
| Project detail pages | `.projects main` | `#FFBEF1` |

**Note:** The site alternates between 4 background colors in a deliberate sequence: **red → white → black → pink → white → pink → white → red**.

### Typography Scale
| Usage | Selector | font-size | font-family | font-weight | line-height |
|-------|----------|-----------|-------------|-------------|-------------|
| Hero headline | `.home .intro-headline` | `clamp(20px, 19.5vw, 400px)` | FKScreamer | 800 (implied) | ~0.85 (implied) |
| Page h1 | `.home h1` | `clamp(60px, 9vw, 140px)` | Helvetica | 700 | 0.95 |
| Statement punch | `.statement h4` | `clamp(100px, 19vw, 388px)` | FKScreamer | 800 (implied) | 0.9 |
| "Mehr Cases" | `.more-cases` | `8vw` | FKScreamer | 800 (implied) | 1 |
| Case title (project page) | `.projects .intro h1` | `clamp(20px, 12vw, 220px)` | FKScreamer | 800 (implied) | ~0.9 |
| Project card h2 | `.project-list .content h2` | (inherited h2, no explicit override) | Helvetica | 700 | ~1.1 |
| Contact info | `.footer .contact-infos` | `28px` | Helvetica | 400 | ~1.4 |
| Body | body default (no explicit override) | `17px` (system default +1px) | Helvetica/Arial/system | 400 | 1.55 (modern-normalize) |

### Interactive Behaviors
- **Button press-down**: `transform: translate(6px, 8px)` + `box-shadow: 0 0` on hover
- **Image hover**: `border-radius` transitions from 0 to 16px over 0.5s on `.project-list img:hover`
- **Custom cursor**: mf-cursor library; on button hover shows pink background pill label with text
- **Page transitions**: swup library with `.transition-fade` class
- **Smooth scroll**: `#smooth-wrapper` / `#smooth-content` structure
- **Logo marquee**: CSS `@keyframes scroll-x` at 20s linear infinite (desktop), 10s (mobile)
- **Nav hover**: `text-decoration: underline`
- **Newsletter submit hover**: background turns black, arrow turns white

### Patterns
- **Navigation links**: `border-bottom: 1px solid #000`, `text-decoration: none`, inline-block with 50px spacing
- **CTA text links**: `border-bottom: 1px solid #000`, weight 500, text-decoration none; hover → red border + red text
- **Buttons**: pill shape, white bg, 3.5px black border, 6px 8px black shadow, inline-flex with space-between, SVG arrow icon
- **Newsletter input wrapper**: relative positioned, submit button absolute at top:7px right:9px
- **Logos section**: mask-image gradient for fade edges, multiple marquee divs

## Why This Reference Is Useful

This site is a good child-skill seed because it has:

- a strong, distinctive visual personality that is not generic "agency template"
- a clear and consistent color system with a single dominant accent
- playful typographic voice that is memorable
- multiple reusable component patterns (marquee, project card, swiper, statement, newsletter)
- a brand motif (bread / breaking) that ties the whole experience together

It is not just "white agency design." It has a crafted identity that translates well to other creative contexts.

## Preserved vs Synthesized

Preserved directly from the source:

- brand red (#ff2a00) as hero/footer background
- signal pink (#FFBEF1) as project/contact background
- black (#000) as marquee background
- **section background alternation** (red → white → black → pink → white → pink → white → red)
- FKScreamer display font at extreme scale (up to 400px / 19.5vw)
- pill-shaped buttons (45px radius) with 3.5px border and 6px 8px shadow
- press-down hover effect (translate + remove shadow)
- thick borders on service cards (6px)
- 30px card radius
- "zur Story" CTA pattern as text-link with bottom border
- client logo marquee on black bg with CSS mask fade
- showreel video hero pattern
- statement block with extreme punchline scale
- bread motif as personality signature
- circular pagination dots (15px black)
- active/hover CTA turns red

Synthesized for the child skill:

- generalized portfolio-ready examples
- reusable component HTML fragments
- normalized token definitions in `DESIGN.md`
- documented responsive and iteration guidance
- adapted bread motif as SVG/emoji equivalent for applied examples (since the original bread GIF is a specific asset)
- placeholder video posters instead of agency-specific showreel
