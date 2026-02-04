# Puranic Context Box - Design Guide

This document provides visual design specifications and implementation examples for Puranic context boxes.

---

## Visual Design Specifications

### Layout Structure

```
┌─────────────────────────────────────────────────────────┐
│ 🌟 Story Title (English / हिंदी)                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ [Story Summary Section]                                 │
│ Brief narrative in both languages...                    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 💡 Theological Significance                            │
│ Why this matters...                                     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 🎯 Practical Application                               │
│ How to apply this teaching...                           │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 🔗 Related: Verses 3, 11, 25                           │
│ 📖 Source: Valmiki Ramayana (Bala Kanda)              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Color Scheme by Priority

**High Priority:**
- Border: Warm orange/saffron (#ff6b35)
- Background: Very light orange/cream (#fff8f0)
- Icon color: Orange gradient
- Accent: Deep saffron (#f7931e)

**Medium Priority:**
- Border: Soft purple (#8b5cf6)
- Background: Very light purple (#f5f3ff)
- Icon color: Purple gradient
- Accent: Deep purple (#7c3aed)

**Low Priority:**
- Border: Soft gray (#94a3b8)
- Background: Very light gray (#f8fafc)
- Icon color: Gray gradient
- Accent: Dark gray (#64748b)

### Typography

**Title:**
- Font size: 1.1rem
- Font weight: 600
- Color: Match border color
- Letter spacing: 0.5px

**Body Text:**
- Font size: 0.95rem
- Line height: 1.6
- Color: #333 (light mode) / #e5e5e5 (dark mode)

**Labels (Theological, Practical, etc.):**
- Font size: 0.85rem
- Font weight: 500
- Color: Accent color
- Text transform: None
- Icon + text layout

**Meta Information (Sources, Related):**
- Font size: 0.8rem
- Font style: Italic
- Color: #666 (light mode) / #aaa (dark mode)

### Spacing

- Box padding: 1.25rem
- Section spacing: 1rem
- Between boxes: 1.5rem
- Icon-text gap: 0.5rem

### Borders & Shadows

- Border width: 2px
- Border style: solid
- Border radius: 8px
- Box shadow: 0 2px 8px rgba(0,0,0,0.08)
- Hover shadow: 0 4px 12px rgba(0,0,0,0.12)

---

## Box Type Visual Variations

### 1. Story Box

```
┌─────────────────────────────────────────────────────────┐
│ ☀️ The Sun-Swallowing Episode                          │
│    सूर्य निगलने का प्रसंग                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 📖 THE STORY                                            │
│ As a baby, Hanuman mistook the rising sun for a        │
│ ripe mango and leaped thousands of yojanas...          │
│                                                         │
│ शिशु हनुमान ने उगते हुए सूर्य को पका आम समझकर...     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 💡 WHY THIS MATTERS                                     │
│ This episode demonstrates Hanuman's fearless           │
│ nature and divine destiny from birth...                │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 🎯 APPLY THIS TEACHING                                 │
│ When facing obstacles, remember they may be            │
│ preparing you for greater purposes...                  │
│                                                         │
├─────────────────────────────────────────────────────────┤
│ 🔗 Related Verses: 3, 25 | 📚 Source: Valmiki Ramayana │
└─────────────────────────────────────────────────────────┘
```

**Visual Features:**
- Large icon at top (2rem)
- Bilingual title side-by-side or stacked
- Clear section headers with icons
- Meta information at bottom in smaller text

### 2. Concept Box

```
┌─────────────────────────────────────────────────────────┐
│ 🕉️ Sankat Mochan - The Remover of Obstacles           │
│    संकट मोचन - विघ्न हर्ता                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 💭 UNDERSTANDING THE CONCEPT                            │
│ "Sankat Mochan" literally means "remover of            │
│ troubles" (sankat = crisis, mochan = liberation)...    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 📜 SCRIPTURAL BASIS                                     │
│ This concept derives from Hanuman's role in            │
│ repeatedly rescuing Rama and his allies...             │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 🎯 HOW TO APPLY                                         │
│ Chant these verses during difficult times...           │
│                                                         │
├─────────────────────────────────────────────────────────┤
│ 🏛️ Famous Temples: Varanasi, Delhi | 🔗 Verses: 20-26  │
└─────────────────────────────────────────────────────────┘
```

**Visual Features:**
- Concept-focused (less narrative)
- Key terms highlighted
- Temple/tradition information included
- May include mini glossary

### 3. Character Box

```
┌─────────────────────────────────────────────────────────┐
│ 🙏 Bharata - The Ideal Brother                         │
│    भरत - आदर्श भाई                                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 👤 WHO IS BHARATA?                                      │
│ Rama's younger brother who refused the throne          │
│ and ruled as regent for 14 years...                    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 🤝 RELATIONSHIP TO HANUMAN                              │
│ Rama compared Hanuman's devotion to Bharata's          │
│ selfless service - the highest praise...               │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ ⭐ KEY ATTRIBUTES                                        │
│ • Selfless devotion | • Dharma over power              │
│ • Perfect regent   | • Model of sacrifice              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Visual Features:**
- Character introduction prominent
- Relationship clearly explained
- Attributes in list/grid format
- Person icon at top

### 4. Etymology Box

```
┌─────────────────────────────────────────────────────────┐
│ 📚 The Name "Hanuman" - Origin & Meaning                │
│    "हनुमान" नाम - उत्पत्ति और अर्थ                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 🔤 WORD BREAKDOWN                                       │
│                                                         │
│    हनु (Hanu) = Jaw                                     │
│    मान (Man) = Prominent/Marked                        │
│    ─────────────────────                               │
│    हनुमान = "One with marked jaw"                      │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 📖 ORIGIN STORY                                         │
│ When Indra's thunderbolt struck infant Hanuman         │
│ during the sun episode, it injured his jaw...          │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ 🏷️ OTHER NAMES                                          │
│ • Anjaneya (Son of Anjana)                             │
│ • Pawanputra (Son of Wind)                             │
│ • Maruti (Son of Marut/Vayu)                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Visual Features:**
- Word breakdown visually displayed
- Etymology tree or component breakdown
- Alternative names with meanings
- Language/grammar focus

---

## Responsive Design

### Desktop (>768px)

```
┌─────────────────────────────────────────────────────────┐
│                    VERSE CONTENT                        │
│                                                         │
│  Devanagari, transliteration, meanings, etc.           │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────┐  ┌──────────────────────┐   │
│  │  PURANIC CONTEXT 1   │  │  PURANIC CONTEXT 2   │   │
│  │  (High Priority)     │  │  (High Priority)     │   │
│  │                      │  │                      │   │
│  └──────────────────────┘  └──────────────────────┘   │
│                                                         │
│  [Expandable: Medium Priority Contexts]                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Features:**
- Side-by-side layout for multiple high-priority boxes
- Sticky positioning possible for long contexts
- Full content visible

### Tablet (481px - 768px)

```
┌──────────────────────────────────────┐
│        VERSE CONTENT                 │
│                                      │
├──────────────────────────────────────┤
│  ┌────────────────────────────────┐ │
│  │   PURANIC CONTEXT 1            │ │
│  │   (High Priority)              │ │
│  └────────────────────────────────┘ │
│                                      │
│  ┌────────────────────────────────┐ │
│  │   PURANIC CONTEXT 2            │ │
│  │   (High Priority)              │ │
│  └────────────────────────────────┘ │
│                                      │
│  [Expandable: Medium Priority]      │
└──────────────────────────────────────┘
```

**Features:**
- Stacked layout
- Full-width boxes
- Collapsible sections for medium/low priority

### Mobile (<480px)

```
┌────────────────────────────┐
│    VERSE CONTENT           │
│                            │
├────────────────────────────┤
│  ▼ PURANIC CONTEXTS (2)   │
│                            │
│  [Tap to expand]           │
│                            │
│  ▼ Context 1: Sun Episode │
│  ▼ Context 2: Name Origin │
│                            │
└────────────────────────────┘
```

**Features:**
- Accordion/drawer format
- Show count badge
- Icons visible even when collapsed
- Tap to expand individual contexts
- Auto-collapse after reading

---

## Interactive Elements

### Expand/Collapse

**Collapsed State:**
```
┌─────────────────────────────────────────────────────────┐
│ ▶ ☀️ The Sun-Swallowing Episode                        │
│    Brief one-line summary...                     [+]    │
└─────────────────────────────────────────────────────────┘
```

**Expanded State:**
```
┌─────────────────────────────────────────────────────────┐
│ ▼ ☀️ The Sun-Swallowing Episode                  [-]   │
├─────────────────────────────────────────────────────────┤
│ [Full content visible]                                  │
│ ...                                                     │
└─────────────────────────────────────────────────────────┘
```

### Hover States

- Subtle lift effect (translateY: -2px)
- Enhanced shadow
- Border color intensifies slightly
- Cursor: pointer (for expandable sections)

### Related Verse Links

```
🔗 Related Verses: [3] [11] [25]
              ↑ Clickable chips that navigate to verses
```

**Chip styling:**
- Small rounded buttons
- Match accent color
- Hover: slight scale and color change
- Click: Navigate with smooth scroll

---

## Accessibility Features

### Keyboard Navigation

- **Tab**: Focus next context box
- **Shift+Tab**: Focus previous context box
- **Enter/Space**: Expand/collapse focused box
- **Escape**: Collapse all boxes

### Screen Reader Support

```html
<div class="puranic-context-box"
     role="complementary"
     aria-label="Puranic context: The Sun-Swallowing Episode">

  <button aria-expanded="false"
          aria-controls="context-sun-episode">
    ☀️ The Sun-Swallowing Episode
  </button>

  <div id="context-sun-episode"
       aria-hidden="true">
    <!-- Content -->
  </div>
</div>
```

### Focus Indicators

- Clear focus ring (2px solid, high contrast)
- Focus visible on all interactive elements
- Skip link to jump past context boxes if desired

---

## Animation & Transitions

### Expand/Collapse Animation

```css
.context-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out,
              opacity 0.3s ease-out;
  opacity: 0;
}

.context-content.expanded {
  max-height: 2000px; /* Large enough for content */
  opacity: 1;
}
```

### Entrance Animation (on page load)

```css
.puranic-context-box {
  animation: fadeInUp 0.5s ease-out;
  animation-fill-mode: both;
}

.puranic-context-box:nth-child(1) { animation-delay: 0.1s; }
.puranic-context-box:nth-child(2) { animation-delay: 0.2s; }
.puranic-context-box:nth-child(3) { animation-delay: 0.3s; }

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

## Dark Mode Considerations

### Color Adjustments

**High Priority (Dark):**
- Border: Lighter orange (#ffa366)
- Background: Very dark orange (#2d1810)
- Text: Light cream (#f5f5dc)

**Medium Priority (Dark):**
- Border: Lighter purple (#a78bfa)
- Background: Very dark purple (#1e1535)
- Text: Light gray (#e5e5e5)

### Contrast Requirements

- Minimum contrast ratio: 4.5:1 for normal text
- Minimum contrast ratio: 3:1 for large text
- Icon colors adjusted for visibility
- Border colors remain distinguishable

---

## Print Styles

When printing:
- Remove expandable behavior (show all content)
- Simplify colors (more print-friendly)
- Add page break avoidance for boxes
- Include source citations prominently

```css
@media print {
  .puranic-context-box {
    break-inside: avoid;
    border: 1px solid #666;
    background: #f9f9f9;
    page-break-inside: avoid;
  }

  .context-content {
    max-height: none !important;
    opacity: 1 !important;
  }

  .expand-button {
    display: none;
  }
}
```

---

## Implementation Priority

### Phase 1: Core Boxes (High Priority Only)
- Implement Story, Etymology, and Character box types
- Single column layout on all devices
- Basic expand/collapse functionality
- Priority: Verses 18, 8, 6, 11

### Phase 2: Enhanced Boxes
- Add Concept, Practice, and Cross-reference types
- Responsive multi-column layout
- Smooth animations
- All high and medium priority contexts

### Phase 3: Full Features
- Low priority contexts
- Advanced filtering (show/hide by type)
- Cross-linking between verses
- User preferences (collapse all by default, etc.)

---

## Example CSS Scaffolding

```css
/* Base Context Box */
.puranic-context-box {
  border: 2px solid var(--context-border-color);
  background: var(--context-bg-color);
  border-radius: 8px;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.puranic-context-box:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
  transform: translateY(-2px);
}

/* Priority Variants */
.context-high {
  --context-border-color: #ff6b35;
  --context-bg-color: #fff8f0;
  --context-accent-color: #f7931e;
}

.context-medium {
  --context-border-color: #8b5cf6;
  --context-bg-color: #f5f3ff;
  --context-accent-color: #7c3aed;
}

.context-low {
  --context-border-color: #94a3b8;
  --context-bg-color: #f8fafc;
  --context-accent-color: #64748b;
}

/* Dark Mode */
[data-theme="dark"] .context-high {
  --context-border-color: #ffa366;
  --context-bg-color: #2d1810;
  --context-accent-color: #ffb380;
}

/* Title */
.context-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--context-border-color);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.context-icon {
  font-size: 1.5rem;
}

/* Sections */
.context-section {
  margin-bottom: 1rem;
}

.context-section:last-child {
  margin-bottom: 0;
}

.context-section-label {
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--context-accent-color);
  display: flex;
  align-items: center;
  gap: 0.3rem;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.context-section-content {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-color);
}

/* Bilingual Layout */
.context-bilingual {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.75rem;
}

@media (min-width: 768px) {
  .context-bilingual {
    grid-template-columns: 1fr 1fr;
  }
}

/* Meta Information */
.context-meta {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  font-size: 0.8rem;
  color: #666;
  font-style: italic;
}

/* Related Links */
.context-related-verses {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.verse-chip {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: var(--context-accent-color);
  color: white;
  border-radius: 12px;
  text-decoration: none;
  font-size: 0.85rem;
  transition: background 0.2s ease, transform 0.2s ease;
}

.verse-chip:hover {
  background: var(--context-border-color);
  transform: scale(1.05);
}

/* Responsive */
@media (max-width: 768px) {
  .puranic-context-box {
    padding: 1rem;
  }

  .context-title {
    font-size: 1rem;
  }

  .context-section-content {
    font-size: 0.9rem;
  }
}
```

---

## Testing Checklist

- [ ] All box types render correctly
- [ ] Bilingual content displays properly
- [ ] Expand/collapse works smoothly
- [ ] Related verse links navigate correctly
- [ ] Responsive layout adapts at all breakpoints
- [ ] Dark mode colors are accessible
- [ ] Keyboard navigation works completely
- [ ] Screen reader announces content correctly
- [ ] Print styles show all content
- [ ] Animations are smooth and not jarring
- [ ] Focus indicators are visible
- [ ] Touch targets are minimum 44×44px (mobile)

---

Last updated: 2026-02-04
