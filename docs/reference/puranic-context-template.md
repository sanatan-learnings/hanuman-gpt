# Puranic Context Box Template

This document defines the standard template for adding Puranic context boxes to verse files.

## Template Structure

Puranic context boxes are added to verse markdown files in the front matter YAML section. Multiple context boxes can be added to a single verse.

---

## Template 1: Story-Based Context Box
*Used for specific Puranic episodes and narratives*

```yaml
puranic_context:
  - id: "unique-story-id"
    type: "story"
    priority: "high|medium|low"

    title:
      en: "English Title"
      hi: "हिंदी शीर्षक"

    icon: "🌟"  # Optional emoji icon

    story_summary:
      en: |
        Brief narrative of the Puranic episode (2-4 sentences).
        Focus on the core events and key characters.
      hi: |
        पौराणिक प्रसंग का संक्षिप्त वर्णन (2-4 वाक्य)।
        मुख्य घटनाओं और प्रमुख पात्रों पर ध्यान केंद्रित करें।

    theological_significance:
      en: |
        Why this story matters theologically (1-3 sentences).
        What deeper truths or principles it reveals.
      hi: |
        यह कथा धार्मिक दृष्टि से क्यों महत्वपूर्ण है (1-3 वाक्य)।
        कौन से गहरे सत्य या सिद्धांत प्रकट होते हैं।

    practical_application:
      en: |
        How devotees can apply this teaching in daily life (1-2 sentences).
      hi: |
        भक्त इस शिक्षा को दैनिक जीवन में कैसे लागू कर सकते हैं (1-2 वाक्य)।

    source_texts:
      - text: "Ramayana"
        section: "Sundara Kanda, Chapter X"
      - text: "Hanuman Chalisa"
        section: "Verse 18"

    related_verses:
      - verse_number: 3
        relationship: "references_same_event"
      - verse_number: 11
        relationship: "consequence_of"

    visual_aid:
      image: "/images/puranic/sun-episode.jpg"
      alt_text: "Hanuman leaping toward the sun as a child"
```

---

## Template 2: Concept-Based Context Box
*Used for theological concepts, traditions, and philosophical ideas*

```yaml
puranic_context:
  - id: "unique-concept-id"
    type: "concept"
    priority: "high|medium|low"

    title:
      en: "Concept Name"
      hi: "अवधारणा का नाम"

    icon: "🕉️"  # Optional emoji icon

    concept_explanation:
      en: |
        Clear explanation of the concept (2-4 sentences).
        Define key terms and their significance.
      hi: |
        अवधारणा की स्पष्ट व्याख्या (2-4 वाक्य)।
        प्रमुख शब्दों और उनके महत्व को परिभाषित करें।

    scriptural_basis:
      en: |
        Where this concept comes from in scriptures (1-2 sentences).
      hi: |
        शास्त्रों में यह अवधारणा कहाँ से आती है (1-2 वाक्य)।

    practical_application:
      en: |
        How this concept applies to modern devotees (1-2 sentences).
      hi: |
        यह अवधारणा आधुनिक भक्तों पर कैसे लागू होती है (1-2 वाक्य)।

    key_terms:
      - term: "Sanskrit/Hindi Term"
        roman: "Romanized"
        meaning:
          en: "English meaning"
          hi: "हिंदी अर्थ"

    related_concepts:
      - concept: "Related Concept Name"
        verses: [29, 33, 34]

    source_texts:
      - text: "Bhagavad Gita"
        section: "Chapter 4, Verse 7-8"
```

---

## Template 3: Deity/Character Context Box
*Used for introducing important characters, deities, or relationships*

```yaml
puranic_context:
  - id: "unique-character-id"
    type: "character"
    priority: "high|medium|low"

    title:
      en: "Character/Deity Name"
      hi: "चरित्र/देवता का नाम"

    icon: "🙏"  # Optional emoji icon

    character_introduction:
      en: |
        Who is this character? (2-3 sentences)
        Their role in the narrative or cosmology.
      hi: |
        यह चरित्र कौन है? (2-3 वाक्य)
        कथा या ब्रह्मांड विज्ञान में उनकी भूमिका।

    relationship_to_hanuman:
      en: |
        How this character relates to Hanuman (1-2 sentences).
      hi: |
        यह चरित्र हनुमान से कैसे संबंधित है (1-2 वाक्य)।

    key_attributes:
      - attribute:
          en: "Attribute name"
          hi: "गुण का नाम"
        description:
          en: "Brief description"
          hi: "संक्षिप्त विवरण"

    famous_episodes:
      - episode:
          en: "Episode name"
          hi: "प्रसंग का नाम"
        verse_reference: 12

    theological_significance:
      en: |
        Why this character/relationship matters (1-2 sentences).
      hi: |
        यह चरित्र/संबंध क्यों महत्वपूर्ण है (1-2 वाक्य)।
```

---

## Template 4: Practice/Tradition Context Box
*Used for explaining devotional practices, temple traditions, rituals*

```yaml
puranic_context:
  - id: "unique-practice-id"
    type: "practice"
    priority: "high|medium|low"

    title:
      en: "Practice/Tradition Name"
      hi: "प्रथा/परंपरा का नाम"

    icon: "🛕"  # Optional emoji icon

    practice_description:
      en: |
        What is this practice? (2-3 sentences)
        When and how is it performed?
      hi: |
        यह प्रथा क्या है? (2-3 वाक्य)
        कब और कैसे की जाती है?

    historical_origin:
      en: |
        How did this tradition begin? (1-2 sentences)
      hi: |
        यह परंपरा कैसे शुरू हुई? (1-2 वाक्य)

    spiritual_benefits:
      en: |
        What benefits does this practice provide? (1-2 sentences)
      hi: |
        इस प्रथा से क्या लाभ मिलते हैं? (1-2 वाक्य)

    how_to_practice:
      en: |
        Simple instructions for devotees (2-3 sentences).
      hi: |
        भक्तों के लिए सरल निर्देश (2-3 वाक्य)।

    associated_temples:
      - name: "Temple Name"
        location: "City, State"
        significance: "Why this temple is important"

    related_practices:
      - practice: "Related Practice Name"
        verses: [24, 25, 26]
```

---

## Template 5: Linguistic/Etymology Context Box
*Used for explaining name meanings, word origins, Sanskrit terms*

```yaml
puranic_context:
  - id: "unique-etymology-id"
    type: "etymology"
    priority: "high|medium|low"

    title:
      en: "Word/Name Etymology"
      hi: "शब्द/नाम की व्युत्पत्ति"

    icon: "📚"  # Optional emoji icon

    word_breakdown:
      original: "हनुमान"
      components:
        - part: "हनु"
          roman: "Hanu"
          meaning:
            en: "Jaw"
            hi: "जबड़ा"
        - part: "मान"
          roman: "Man"
          meaning:
            en: "Prominent/Marked"
            hi: "प्रमुख/चिह्नित"

    origin_story:
      en: |
        Story of how this name came to be (2-3 sentences).
      hi: |
        यह नाम कैसे प्राप्त हुआ, इसकी कहानी (2-3 वाक्य)।

    alternative_names:
      - name: "Anjaneya"
        meaning:
          en: "Son of Anjana"
          hi: "अंजना का पुत्र"
        context: "Emphasizes maternal lineage"
      - name: "Pawanputra"
        meaning:
          en: "Son of Wind God"
          hi: "पवन देव का पुत्र"
        context: "Emphasizes spiritual father"

    deeper_significance:
      en: |
        What the name reveals about character (1-2 sentences).
      hi: |
        नाम चरित्र के बारे में क्या प्रकट करता है (1-2 वाक्य)।
```

---

## Template 6: Cross-Reference Context Box
*Used for connecting verses to other scriptures or stories*

```yaml
puranic_context:
  - id: "unique-reference-id"
    type: "cross_reference"
    priority: "high|medium|low"

    title:
      en: "Connections to Other Texts"
      hi: "अन्य ग्रंथों से संबंध"

    icon: "🔗"  # Optional emoji icon

    primary_source:
      text: "Valmiki Ramayana"
      section: "Sundara Kanda, Sarga 1"
      summary:
        en: "Brief description of what this section contains"
        hi: "इस अनुभाग में क्या है, संक्षिप्त विवरण"

    related_texts:
      - text: "Ramcharitmanas"
        author: "Tulsidas"
        section: "Sundara Kanda"
        relevance:
          en: "How this text expands on the story"
          hi: "यह पाठ कहानी का विस्तार कैसे करता है"

      - text: "Hanuman Bahuk"
        author: "Tulsidas"
        section: "Verse 15"
        relevance:
          en: "Related theme or teaching"
          hi: "संबंधित विषय या शिक्षा"

    comparative_insights:
      en: |
        What we learn from comparing these versions (1-2 sentences).
      hi: |
        इन संस्करणों की तुलना से हम क्या सीखते हैं (1-2 वाक्य)।
```

---

## Usage Guidelines

### Priority Levels

- **high**: Essential for understanding the verse, should be prominently displayed
- **medium**: Enriches understanding, display in expandable section
- **low**: Interesting additional context, can be in footnote or "Learn More" section

### Multiple Context Boxes

A verse can have multiple context boxes. For example, Verse 18 might have:
1. Story-based box (sun episode) - Priority: high
2. Etymology box (name meaning) - Priority: high
3. Concept box (yojana measurement) - Priority: medium

### Display Order

When multiple boxes are present, display in this order:
1. Story boxes (type: "story")
2. Character boxes (type: "character")
3. Concept boxes (type: "concept")
4. Etymology boxes (type: "etymology")
5. Practice boxes (type: "practice")
6. Cross-reference boxes (type: "cross_reference")

Within each type, sort by priority (high → medium → low).

---

## Example: Complete Verse with Context Boxes

```yaml
---
layout: verse
collection_key: "hanuman-chalisa"
verse_number: 18
title_en: "Childhood Leap to the Sun"
title_hi: "बचपन में सूर्य की ओर छलांग"

# ... standard verse content ...

puranic_context:
  # Primary story
  - id: "sun-swallowing-episode"
    type: "story"
    priority: "high"
    title:
      en: "The Sun-Swallowing Episode"
      hi: "सूर्य निगलने का प्रसंग"
    icon: "☀️"
    story_summary:
      en: |
        As a baby, Hanuman mistook the rising sun for a ripe mango and leaped thousands of yojanas across the sky to grasp it. The sun god, frightened, appealed to Indra who struck infant Hanuman with his thunderbolt. The blow injured Hanuman's jaw (hanu), rendering him unconscious. Enraged, Vayu withdrew all air from the universe until the gods appeased him by granting Hanuman numerous divine boons and blessings.
      hi: |
        शिशु हनुमान ने उगते हुए सूर्य को पका हुआ आम समझकर उसे पकड़ने के लिए आकाश में हजारों योजन की छलांग लगाई। भयभीत सूर्य देव ने इंद्र से सहायता मांगी, जिन्होंने शिशु हनुमान पर अपने वज्र से प्रहार किया। इस प्रहार से हनुमान का जबड़ा (हनु) घायल हो गया और वे बेहोश हो गए। क्रोधित पवन देव ने ब्रह्मांड से सारी वायु वापस ले ली जब तक देवताओं ने हनुमान को अनेक दिव्य वरदान देकर उन्हें शांत नहीं किया।
    theological_significance:
      en: |
        This episode demonstrates Hanuman's fearless nature and divine destiny from birth. The cascade of blessings he received made him invincible and essential to Rama's mission. It teaches that setbacks often lead to greater blessings when divine will is at work.
      hi: |
        यह प्रसंग जन्म से ही हनुमान के निडर स्वभाव और दिव्य नियति को प्रदर्शित करता है। उन्हें मिले वरदानों ने उन्हें अजेय बनाया और राम के मिशन के लिए अपरिहार्य बनाया। यह सिखाता है कि जब दैवीय इच्छा कार्यरत हो तो असफलताएं अक्सर बड़े आशीर्वादों की ओर ले जाती हैं।
    practical_application:
      en: |
        When facing obstacles or setbacks, remember that they may be preparing you for greater purposes. Like Hanuman's injury led to divine blessings, our challenges often unlock hidden potential.
      hi: |
        जब बाधाओं या असफलताओं का सामना करना पड़े, याद रखें कि वे आपको बड़े उद्देश्यों के लिए तैयार कर रही हो सकती हैं। जैसे हनुमान की चोट ने दिव्य आशीर्वादों को जन्म दिया, वैसे ही हमारी चुनौतियां अक्सर छिपी क्षमता को खोलती हैं।
    source_texts:
      - text: "Valmiki Ramayana"
        section: "Bala Kanda"
      - text: "Hanuman Chalisa"
        section: "Verse 18"
    related_verses:
      - verse_number: 3
        relationship: "explains_blessing_received"
      - verse_number: 25
        relationship: "healing_power_origin"
    visual_aid:
      image: "/images/puranic/sun-episode.png"
      alt_text: "Baby Hanuman leaping toward the sun"

  # Etymology connection
  - id: "hanuman-name-etymology"
    type: "etymology"
    priority: "high"
    title:
      en: "Origin of the Name 'Hanuman'"
      hi: "'हनुमान' नाम की उत्पत्ति"
    icon: "📚"
    word_breakdown:
      original: "हनुमान"
      components:
        - part: "हनु"
          roman: "Hanu"
          meaning:
            en: "Jaw"
            hi: "जबड़ा"
        - part: "मान"
          roman: "Man"
          meaning:
            en: "Prominent/Marked/Having"
            hi: "प्रमुख/चिह्नित/युक्त"
    origin_story:
      en: |
        When Indra's thunderbolt struck infant Hanuman during the sun episode, it specifically injured his jaw (hanu), leaving a permanent mark. This injury became the basis for his most common name, literally meaning "one with a prominent/marked jaw."
      hi: |
        जब सूर्य प्रसंग के दौरान इंद्र के वज्र ने शिशु हनुमान पर प्रहार किया, तो उनका जबड़ा (हनु) विशेष रूप से घायल हो गया, जिससे स्थायी निशान रह गया। यह चोट उनके सबसे सामान्य नाम का आधार बनी, जिसका शाब्दिक अर्थ है "प्रमुख/चिह्नित जबड़े वाला।"
    alternative_names:
      - name: "Anjaneya"
        meaning:
          en: "Son of Anjana"
          hi: "अंजना का पुत्र"
        context: "Emphasizes maternal lineage and devotion"
      - name: "Pawanputra"
        meaning:
          en: "Son of Wind God (Pawan)"
          hi: "पवन देव का पुत्र"
        context: "Emphasizes divine spiritual father"
      - name: "Maruti"
        meaning:
          en: "Son of Marut (another name for Vayu)"
          hi: "मारुत का पुत्र"
        context: "Regional variation emphasizing wind connection"
    deeper_significance:
      en: |
        The name carries the story of divine intervention and blessing. What appeared as injury became identity, teaching that our scars and struggles define our purpose and strength.
      hi: |
        यह नाम दैवीय हस्तक्षेप और आशीर्वाद की कहानी को साथ लेकर चलता है। जो चोट लगी, वही पहचान बन गई, यह सिखाता है कि हमारे घाव और संघर्ष हमारे उद्देश्य और शक्ति को परिभाषित करते हैं।

  # Measurement context
  - id: "yojana-measurement"
    type: "concept"
    priority: "medium"
    title:
      en: "Understanding Yojana - Ancient Distance Measurement"
      hi: "योजन - प्राचीन दूरी माप को समझना"
    icon: "📏"
    concept_explanation:
      en: |
        A yojana is an ancient Indian unit of distance, approximately 8 miles (13 kilometers). The phrase "yuga sahasra yojana" (thousands of yugas worth of yojanas) in this verse represents an incomprehensibly vast distance, emphasizing the miraculous nature of infant Hanuman's leap. It's both literal (the astronomical distance to the sun) and metaphorical (the infinite gap between mortal and divine that only divine grace can bridge).
      hi: |
        योजन प्राचीन भारतीय दूरी की इकाई है, लगभग 8 मील (13 किलोमीटर)। इस चौपाई में "युग सहस्र योजन" वाक्यांश अकल्पनीय विशाल दूरी को दर्शाता है, जो शिशु हनुमान की छलांग की चमत्कारी प्रकृति पर जोर देता है। यह शाब्दिक (सूर्य की खगोलीय दूरी) और रूपक (नश्वर और दिव्य के बीच अनंत अंतर जिसे केवल दिव्य कृपा ही पाट सकती है) दोनों है।
    scriptural_basis:
      en: |
        Ancient Indian astronomy texts like Surya Siddhanta used yojanas for cosmic distances. The Ramayana frequently uses yojanas to describe the scale of Hanuman's mighty deeds.
      hi: |
        सूर्य सिद्धांत जैसे प्राचीन भारतीय खगोल विज्ञान ग्रंथों में योजन का उपयोग ब्रह्मांडीय दूरियों के लिए किया गया था। रामायण में हनुमान के महान कार्यों के पैमाने का वर्णन करने के लिए योजन का अक्सर उपयोग किया गया है।
    practical_application:
      en: |
        The enormous distance reminds devotees that no obstacle is too great when acting with faith and divine purpose. What seems impossible becomes achievable through devotion.
      hi: |
        विशाल दूरी भक्तों को याद दिलाती है कि विश्वास और दिव्य उद्देश्य के साथ कार्य करने पर कोई भी बाधा बहुत बड़ी नहीं है। जो असंभव लगता है, वह भक्ति के माध्यम से प्राप्य हो जाता है।
    key_terms:
      - term: "योजन"
        roman: "Yojana"
        meaning:
          en: "~8 miles or 13 km"
          hi: "लगभग 8 मील या 13 किमी"
      - term: "युग सहस्र"
        roman: "Yuga Sahasra"
        meaning:
          en: "Thousands of ages (immeasurable)"
          hi: "हजारों युग (अपरिमेय)"
    related_concepts:
      - concept: "Lanka Ocean Crossing (100 yojanas)"
        verses: [19]

---
```

---

## Technical Implementation Notes

### Front Matter Parsing

The Jekyll site will need to parse the `puranic_context` array and render each context box according to its type and priority.

### CSS Classes

Suggested CSS class structure:
```css
.puranic-context-box { /* Base styling */ }
.puranic-context-high { /* High priority styling */ }
.puranic-context-medium { /* Medium priority styling */ }
.puranic-context-low { /* Low priority styling */ }
.puranic-context-story { /* Story-specific styling */ }
.puranic-context-concept { /* Concept-specific styling */ }
/* etc. for each type */
```

### Responsive Display

- **Desktop**: Show high-priority boxes inline, medium in expandable sections
- **Mobile**: All context boxes in expandable accordion format to save space

### Accessibility

- Each context box should have proper ARIA labels
- Expandable sections need keyboard navigation support
- Icons should have alt text equivalents

---

## Version History

- **v1.0** (2026-02-04): Initial template creation with 6 box types
