# Reference Analysis Guide

When UIgod receives a design reference (URL, screenshot, code snippet, or text description), this guide defines how to systematically extract design tokens before generating a child skill.

The goal is to ensure that every token in `DESIGN.md` traces back to an actual reference value — not an LLM approximation.

## 1. If a URL Is Provided

### Step 1: Fetch the Page

Use `web_fetch` to retrieve the HTML. If the page contains inline CSS or references external stylesheets, fetch those too.

### Step 2: Extract CSS Custom Properties

Search the CSS for `:root` or `html` blocks that define custom properties:

```css
:root {
  --color-primary: #ff2a00;
  --font-display: "FK Screamer", Helvetica, Arial, sans-serif;
  --radius-pill: 45px;
}
```

Document all custom properties found. These are the most reliable source of design tokens.

### Step 3: Extract @font-face Declarations

```css
@font-face {
  font-family: "FK Screamer";
  src: url(...) format("woff2");
}
```

Document the font-family name and fallback stack. If it's a custom/licensed font, note that applied examples must use a close approximation.

### Step 4: Map Border Treatments

Search the CSS for every distinct `border-radius`, `border-width`, and `box-shadow` value. Group them by usage:

| Property | Value | Used On |
|----------|-------|---------|
| border-radius | 45px | Buttons, inputs (.button, input[type="email"]) |
| border-radius | 150px | "Mehr Cases" button |
| border-radius | 30px | Service cards |
| border-radius | 16px | Image hover state |
| border-width | 3.5px | Buttons, inputs |
| border-width | 6px | Service cards |
| border-width | 7px | "Mehr Cases" button |
| box-shadow | 6px 8px #000 | Standard buttons |
| box-shadow | 12px 16px #000 | "Mehr Cases" button |

### Step 5: Map Section Background Colors

Identify each distinct section in the HTML and its background color:

| Section | Background | CSS Source |
|---------|-----------|------------|
| Header | #ffffff | .header |
| Hero | #ff2a00 | .home main |
| Logo marquee | #000000 | .logos |
| Case studies | #FFBEF1 | .project-list |
| Contact | #FFBEF1 | section.contact |
| Footer | #ff2a00 | .footer |

Note how sections **alternate** — this is a critical style characteristic.

### Step 6: Extract Typography Scale

Find all font-size declarations, especially `clamp()` values — they reveal the responsive typography system:

```css
.home .intro-headline { font-size: clamp(20px, 19.5vw, 400px); }
.home h1 { font-size: clamp(60px, 9vw, 140px); }
.statement h4 { font-size: clamp(100px, 19vw, 388px); }
```

Document every distinct font-size, font-family, font-weight, line-height, and letter-spacing.

### Step 7: Document Interactive Behaviors

- Hover effects (button press-down, image border-radius transition)
- Animation durations and timing functions
- Custom cursor behavior
- Page transition effects (swup)
- Smooth scroll setup

### Step 8: Document Patterns

- Navigation link style (`border-bottom: 1px solid #000`)
- CTA text link with underline
- Pill input with absolute-positioned submit button
- etc.

## 2. If Only Screenshots Are Available

Without CSS, you cannot extract exact values. Follow this approach:

1. **Infer** hex colors by using known brand colors (e.g., inspect theme-color meta tag, or use a color picker reference).
2. **Approximate** font stacks by identifying the typeface foundry and finding its closest web-safe equivalent.
3. **Estimate** border-radius, border-width, and shadow values from visual evidence.
4. **Mark everything as `[inferred]`** in source-observations.md under a `## Inferred Values` section.
5. **Do not invent** precise values — use ranges or note uncertainty (e.g., `border-radius: ≈40–48px [inferred]`).

## 3. If Code Snippets Are Provided

Extract tokens directly from the provided code. This is the fastest path:

1. Read CSS custom properties if present.
2. Read inline style values.
3. Read Tailwind/ utility class configurations if applicable.
4. Document the framework context if it influences the style (e.g., Astro, Tailwind, styled-components).

## 4. What to Write in source-observations.md

After completing the extraction, write a `## CSS Extraction` section in `references/source-observations.md` that contains:

````markdown
## CSS Extraction

### Custom Properties
- `--red`: #ff2a00
- `--pink`: #FFBEF1
- etc.

### Fonts
- Display: "FK Screamer" (custom) → fallback: Helvetica, Arial, sans-serif
- Body: Helvetica, Arial, sans-serif (system stack)

### Border Treatments
| Usage | border-radius | border-width | box-shadow |
|-------|---------------|--------------|------------|
| Buttons | 45px | 3.5px | 6px 8px #000 |
| "Mehr Cases" | 150px | 7px | 12px 16px #000 |
| Service cards | 30px | 6px | none |

### Section Backgrounds
| Section | Color |
|---------|-------|
| Hero | #ff2a00 |
| Marquee | #000000 |
| Case studies | #FFBEF1 |
| ... | ... |

### Typography Scale
- Hero headline: clamp(20px, 19.5vw, 400px) — FKScreamer
- h1: clamp(60px, 9vw, 140px) — Helvetica Bold
- Statement: clamp(100px, 19vw, 388px) — FKScreamer
- Body: 17px — Helvetica

### Interactive Behaviors
- Button hover: translate(6px, 8px), box-shadow → 0 0
- Image hover: border-radius 0 → 16px
- ...etc.

### Extracted vs Synthesized
- All values above were [extracted from CSS] / [inferred from screenshot] / [provided in code]
- The following tokens were [synthesized]: ...
````

## 5. Common Pitfalls to Avoid

| Pitfall | Why It Happens | How to Avoid |
|---------|---------------|--------------|
| Wrong font family | LLM assumes a common font like Inter or Syne | Always check @font-face and font-family declarations in the actual CSS |
| Underestimating scale | LLM defaults to "reasonable" sizes | Read the actual clamp() values — they may be extreme (e.g., up to 400px) |
| Missing section alternation | LLM focuses on one color | Map every section's background color systematically |
| Making borders/subtle | LLM gravitates toward minimalism | Search for every border-width and border-radius in the CSS |
| Inventing shadow values | LLM doesn't verify box-shadow | Extract box-shadow values from CSS directly |
| Wrong button shape | LLM assumes modern flat/rect | Check border-radius on button elements specifically |
| Missing hover effects | LLM only reads static styles | Check :hover, :focus, :active pseudo-classes in CSS |
| Using wrong hex codes | LLM approximates colors | Extract from CSS custom properties or direct color values |
