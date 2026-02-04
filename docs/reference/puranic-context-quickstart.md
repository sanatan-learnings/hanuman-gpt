# Puranic Context Boxes - Quick Start Guide

**Quick reference for adding Puranic context boxes to verse files.**

---

## 📋 Before You Start

1. **Read the full templates:** `puranic-context-template.md`
2. **Review design specs:** `puranic-context-design-guide.md`
3. **Have verse analysis ready:** See comprehensive analysis results

---

## 🚀 Quick Implementation Steps

### Step 1: Identify Which Boxes to Add

Use the analysis results to determine:
- Which verses need context boxes
- What type of boxes are needed
- Priority level for each box

### Step 2: Choose Template Type

| Use Case | Template Type |
|----------|--------------|
| Puranic episode/narrative | `story` |
| Theological concept/idea | `concept` |
| Important character/deity | `character` |
| Devotional practice/ritual | `practice` |
| Name/word etymology | `etymology` |
| Scripture connections | `cross_reference` |

### Step 3: Add to Verse File

Open the verse markdown file and add the `puranic_context` section to the front matter YAML.

---

## 📝 Complete Example

Here's **Verse 18** with multiple Puranic context boxes implemented:

```yaml
---
layout: verse
collection_key: "hanuman-chalisa"
permalink: /chalisa/verse_18/
title_en: "Childhood Leap to the Sun"
title_hi: "बचपन में सूर्य की ओर छलांग"
verse_number: 18
previous_verse: "/chalisa/verse_17"
next_verse: "/chalisa/verse_19"
image: "/images/hanuman-chalisa/modern-minimalist/verse-18.png"

devanagari: |
  युग सहस्त्र जोजन पर भानू।
  लील्यो ताहि मधुर फल जानू॥

transliteration: |
  Yuga sahasra yojana para bhaanu
  Leelyo taahi madhura phala jaanu

phonetic_notes:
  - word: "युग"
    phonetic: "yug"
    emphasis: "short and crisp"
  - word: "सहस्त्र"
    phonetic: "sa-has-tra"
    emphasis: "middle syllable"
  - word: "जोजन"
    phonetic: "yo-jan"
    emphasis: "first syllable"
  - word: "भानू"
    phonetic: "bhaa-nu"
    emphasis: "first syllable, elongated 'aa'"
  - word: "लील्यो"
    phonetic: "lee-lyo"
    emphasis: "first syllable"
  - word: "मधुर"
    phonetic: "ma-dhur"
    emphasis: "first syllable"

word_meanings:
  - word: "युग"
    roman: "Yuga"
    meaning:
      en: "age/era"
      hi: "युग"
  - word: "सहस्त्र"
    roman: "Sahasra"
    meaning:
      en: "thousand"
      hi: "हजार"
  - word: "जोजन"
    roman: "Yojana"
    meaning:
      en: "ancient measure of distance (~8 miles)"
      hi: "प्राचीन दूरी माप (~8 मील)"
  - word: "पर"
    roman: "Para"
    meaning:
      en: "away/distant"
      hi: "दूर"
  - word: "भानू"
    roman: "Bhaanu"
    meaning:
      en: "sun"
      hi: "सूर्य"
  - word: "लील्यो"
    roman: "Leelyo"
    meaning:
      en: "swallowed/consumed"
      hi: "निगल लिया"
  - word: "ताहि"
    roman: "Taahi"
    meaning:
      en: "that"
      hi: "उसे"
  - word: "मधुर"
    roman: "Madhura"
    meaning:
      en: "sweet"
      hi: "मधुर/मीठा"
  - word: "फल"
    roman: "Phala"
    meaning:
      en: "fruit"
      hi: "फल"
  - word: "जानू"
    roman: "Jaanu"
    meaning:
      en: "thinking/considering"
      hi: "समझकर"

literal_translation:
  en: "Thousands of yugas (ages) worth of yojanas (distance measure) away was the sun. Thinking it to be a sweet fruit, [you] swallowed it."
  hi: "हजारों युग की योजन दूरी पर सूर्य था। उसे मीठा फल समझकर, [आपने] उसे निगल लिया।"

interpretive_meaning:
  en: "The sun was at an incomprehensibly vast astronomical distance - thousands of ages worth of yojanas (each yojana being about 8 miles). Yet infant Hanuman, in his divine innocence and fearlessness, mistook the blazing sun for a ripe, sweet fruit and attempted to swallow it. This verse celebrates Hanuman's childhood courage and supernatural abilities that manifested even as a baby."
  hi: "सूर्य अकल्पनीय रूप से विशाल खगोलीय दूरी पर था - हजारों युगों के योजन (प्रत्येक योजन लगभग 8 मील)। फिर भी शिशु हनुमान ने अपनी दिव्य मासूमियत और निडरता में जलते सूर्य को पके, मीठे फल समझकर उसे निगलने का प्रयास किया। यह चौपाई हनुमान के बचपन के साहस और अलौकिक क्षमताओं का जश्न मनाती है जो एक शिशु के रूप में भी प्रकट हुईं।"

story:
  en: "This verse refers to one of the most famous episodes from Hanuman's childhood. As an infant, Hanuman saw the rising sun and, driven by hunger and innocence, mistook it for a ripe mango. Using his divine powers, he leaped across the vast distance of space toward the sun. The sun god, frightened by this unprecedented event, sought help from Indra, the king of gods. Indra struck the infant Hanuman with his thunderbolt (vajra), injuring Hanuman's jaw (hanu) and causing him to fall unconscious. This injury to his jaw is said to be the origin of his name 'Hanu-man' (one with a prominent/injured jaw). Enraged by this attack on his son, Vayu (the wind god) withdrew all air from the universe, threatening all life. The gods, desperate to appease Vayu and save the cosmos, blessed infant Hanuman with numerous divine boons: invincibility, immortality, strength, the ability to change form, and more. The verse uses 'yuga sahasra yojana' (thousands of ages of yojanas) to emphasize both the literal astronomical distance to the sun and the metaphorical infinite gap between mortal capability and divine achievement that only grace can bridge."
  hi: "यह चौपाई हनुमान के बचपन के सबसे प्रसिद्ध प्रसंगों में से एक को संदर्भित करती है। एक शिशु के रूप में, हनुमान ने उगते सूर्य को देखा और भूख और मासूमियत से प्रेरित होकर उसे पका हुआ आम समझ लिया। अपनी दिव्य शक्तियों का उपयोग करते हुए, उन्होंने सूर्य की ओर अंतरिक्ष की विशाल दूरी में छलांग लगाई। सूर्य देव इस अभूतपूर्व घटना से भयभीत होकर देवराज इंद्र से सहायता मांगी। इंद्र ने शिशु हनुमान पर अपने वज्र से प्रहार किया, जिससे हनुमान का जबड़ा (हनु) घायल हो गया और वे बेहोश हो गए। उनके जबड़े की इस चोट को उनके नाम 'हनुमान' (प्रमुख/घायल जबड़े वाला) की उत्पत्ति माना जाता है। अपने पुत्र पर इस हमले से क्रोधित होकर, वायु देव ने ब्रह्मांड से सारी हवा वापस ले ली, जिससे सभी जीवन को खतरा हो गया। देवता, वायु को शांत करने और ब्रह्मांड को बचाने के लिए बेताब होकर, शिशु हनुमान को अनेक दिव्य वरदान दिए: अजेयता, अमरता, शक्ति, रूप बदलने की क्षमता, और भी बहुत कुछ। यह चौपाई 'युग सहस्र योजन' का उपयोग करती है ताकि सूर्य की वास्तविक खगोलीय दूरी और नश्वर क्षमता और दिव्य उपलब्धि के बीच रूपक अनंत अंतराल दोनों पर जोर दिया जा सके जिसे केवल कृपा ही पाट सकती है।"

practical_application:
  teaching:
    en: "Like infant Hanuman who fearlessly reached for the impossible, approach your spiritual goals with innocent courage and divine trust. What seems astronomically distant becomes achievable through grace. Setbacks and obstacles (like Indra's strike) often lead to greater blessings and abilities when part of divine plan."
    hi: "शिशु हनुमान की तरह जिन्होंने निडरता से असंभव तक पहुंचने का प्रयास किया, अपने आध्यात्मिक लक्ष्यों की ओर मासूम साहस और दिव्य विश्वास के साथ बढ़ें। जो खगोलीय रूप से दूर लगता है वह कृपा के माध्यम से प्राप्य हो जाता है। असफलताएं और बाधाएं (जैसे इंद्र का प्रहार) अक्सर बड़े आशीर्वादों और क्षमताओं की ओर ले जाती हैं जब दिव्य योजना का हिस्सा हों।"
  when_to_use:
    en: "Recite this verse when facing seemingly impossible challenges, when you need courage to reach for distant goals, or when recovering from setbacks. It reminds you that divine grace makes the impossible possible and that obstacles often precede blessings."
    hi: "इस चौपाई का पाठ तब करें जब आप असंभव लगने वाली चुनौतियों का सामना कर रहे हों, जब आपको दूर के लक्ष्यों तक पहुंचने के लिए साहस की आवश्यकता हो, या जब असफलताओं से उबर रहे हों। यह आपको याद दिलाता है कि दिव्य कृपा असंभव को संभव बनाती है और बाधाएं अक्सर आशीर्वादों से पहले आती हैं।"

# ============================================================
# PURANIC CONTEXT BOXES START HERE
# ============================================================

puranic_context:
  # Primary Story Box - The Sun Episode
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
        This episode demonstrates Hanuman's fearless divine nature from birth. The cascade of blessings he received made him invincible and essential to Rama's mission. It teaches that setbacks often lead to greater blessings when divine will is at work, and that courage combined with innocence pleases the divine.
      hi: |
        यह प्रसंग जन्म से ही हनुमान के निडर दिव्य स्वभाव को प्रदर्शित करता है। उन्हें मिले वरदानों ने उन्हें अजेय बनाया और राम के मिशन के लिए अपरिहार्य बनाया। यह सिखाता है कि जब दैवीय इच्छा कार्यरत हो तो असफलताएं अक्सर बड़े आशीर्वादों की ओर ले जाती हैं, और साहस जब मासूमियत के साथ मिलता है तो परमात्मा को प्रसन्न करता है।

    practical_application:
      en: |
        When facing obstacles or setbacks, remember that they may be preparing you for greater purposes. Like Hanuman's injury led to divine blessings, our challenges often unlock hidden potential and prepare us for our true mission.
      hi: |
        जब बाधाओं या असफलताओं का सामना करना पड़े, याद रखें कि वे आपको बड़े उद्देश्यों के लिए तैयार कर रही हो सकती हैं। जैसे हनुमान की चोट ने दिव्य आशीर्वादों को जन्म दिया, वैसे ही हमारी चुनौतियां अक्सर छिपी क्षमता को खोलती हैं और हमें हमारे सच्चे मिशन के लिए तैयार करती हैं।

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

  # Etymology Box - Name Origin
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
        When Indra's thunderbolt struck infant Hanuman during the sun episode, it specifically injured his jaw (hanu), leaving a permanent mark. This injury became the basis for his most common name, literally meaning "one with a prominent/marked jaw." What began as a wound became his eternal identity.
      hi: |
        जब सूर्य प्रसंग के दौरान इंद्र के वज्र ने शिशु हनुमान पर प्रहार किया, तो उनका जबड़ा (हनु) विशेष रूप से घायल हो गया, जिससे स्थायी निशान रह गया। यह चोट उनके सबसे सामान्य नाम का आधार बनी, जिसका शाब्दिक अर्थ है "प्रमुख/चिह्नित जबड़े वाला।" जो घाव था, वह उनकी शाश्वत पहचान बन गया।

    alternative_names:
      - name: "Anjaneya"
        meaning:
          en: "Son of Anjana"
          hi: "अंजना का पुत्र"
        context: "Emphasizes maternal lineage and devotion"

      - name: "Pawanputra / Pavanasuta"
        meaning:
          en: "Son of Wind God (Pawan/Pavana)"
          hi: "पवन देव का पुत्र"
        context: "Emphasizes divine spiritual father Vayu"

      - name: "Maruti"
        meaning:
          en: "Son of Marut (another name for Vayu)"
          hi: "मारुत का पुत्र"
        context: "Popular in Maharashtra, emphasizes wind connection"

      - name: "Bajrang Bali"
        meaning:
          en: "Strong one with body like thunderbolt (vajra)"
          hi: "वज्र जैसे शरीर वाला बलवान"
        context: "Refers to blessing received from Indra after the incident"

    deeper_significance:
      en: |
        The name carries the story of divine intervention and blessing. What appeared as injury became identity, teaching that our scars and struggles define our purpose and strength. The mark of the thunderbolt became the mark of invincibility.
      hi: |
        यह नाम दैवीय हस्तक्षेप और आशीर्वाद की कहानी को साथ लेकर चलता है। जो चोट लगी, वही पहचान बन गई, यह सिखाता है कि हमारे घाव और संघर्ष हमारे उद्देश्य और शक्ति को परिभाषित करते हैं। वज्र का निशान अजेयता का निशान बन गया।

  # Concept Box - Distance Measurement
  - id: "yojana-measurement"
    type: "concept"
    priority: "medium"

    title:
      en: "Understanding Yojana - Ancient Distance Measurement"
      hi: "योजन - प्राचीन दूरी माप को समझना"

    icon: "📏"

    concept_explanation:
      en: |
        A yojana is an ancient Indian unit of distance, approximately 8 miles (13 kilometers). The phrase "yuga sahasra yojana" (thousands of yugas worth of yojanas) represents an incomprehensibly vast distance, emphasizing the miraculous nature of infant Hanuman's leap. It's both literal (the astronomical distance to the sun) and metaphorical (the infinite gap between mortal and divine that only grace can bridge).
      hi: |
        योजन प्राचीन भारतीय दूरी की इकाई है, लगभग 8 मील (13 किलोमीटर)। "युग सहस्र योजन" वाक्यांश अकल्पनीय विशाल दूरी को दर्शाता है, जो शिशु हनुमान की छलांग की चमत्कारी प्रकृति पर जोर देता है। यह शाब्दिक (सूर्य की खगोलीय दूरी) और रूपक (नश्वर और दिव्य के बीच अनंत अंतर जिसे केवल दिव्य कृपा ही पाट सकती है) दोनों है।

    scriptural_basis:
      en: |
        Ancient Indian astronomy texts like Surya Siddhanta used yojanas for cosmic distances. The Ramayana frequently uses yojanas to describe the scale of Hanuman's mighty deeds, including the 100-yojana leap to Lanka.
      hi: |
        सूर्य सिद्धांत जैसे प्राचीन भारतीय खगोल विज्ञान ग्रंथों में योजन का उपयोग ब्रह्मांडीय दूरियों के लिए किया गया था। रामायण में हनुमान के महान कार्यों के पैमाने का वर्णन करने के लिए योजन का अक्सर उपयोग किया गया है, जिसमें लंका के लिए 100-योजन की छलांग भी शामिल है।

    practical_application:
      en: |
        The enormous distance reminds devotees that no obstacle is too great when acting with faith and divine purpose. What seems impossibly distant becomes achievable through devotion and grace.
      hi: |
        विशाल दूरी भक्तों को याद दिलाती है कि विश्वास और दिव्य उद्देश्य के साथ कार्य करने पर कोई भी बाधा बहुत बड़ी नहीं है। जो असंभव रूप से दूर लगता है, वह भक्ति और कृपा के माध्यम से प्राप्य हो जाता है।

    key_terms:
      - term: "योजन"
        roman: "Yojana"
        meaning:
          en: "~8 miles or 13 km"
          hi: "लगभग 8 मील या 13 किमी"

      - term: "युग"
        roman: "Yuga"
        meaning:
          en: "Age/Era (vast period of time)"
          hi: "युग/काल (समय की विशाल अवधि)"

      - term: "सहस्र"
        roman: "Sahasra"
        meaning:
          en: "Thousand"
          hi: "हजार"

    related_concepts:
      - concept: "Lanka Ocean Crossing (100 yojanas)"
        verses: [19]

      - concept: "Cosmic Measurements in Vedic Literature"
        verses: []

  # Cross-Reference Box
  - id: "blessings-received"
    type: "cross_reference"
    priority: "medium"

    title:
      en: "Divine Blessings Received"
      hi: "प्राप्त दिव्य वरदान"

    icon: "🔗"

    primary_source:
      text: "Valmiki Ramayana"
      section: "Bala Kanda"
      summary:
        en: "Details the blessings each deity granted to infant Hanuman after Vayu withdrew air from universe"
        hi: "प्रत्येक देवता द्वारा शिशु हनुमान को दिए गए वरदानों का विवरण, वायु द्वारा ब्रह्मांड से वायु वापस लेने के बाद"

    related_texts:
      - text: "Hanuman Chalisa, Verse 3"
        author: "Tulsidas"
        section: "Bajrangi - Thunderbolt Body"
        relevance:
          en: "Explains the invincible body blessing received from Indra"
          hi: "इंद्र से प्राप्त अजेय शरीर के वरदान की व्याख्या करता है"

      - text: "Hanuman Chalisa, Verse 25"
        author: "Tulsidas"
        section: "Healer of All Suffering"
        relevance:
          en: "Connects to healing powers granted during this episode"
          hi: "इस प्रसंग के दौरान दिए गए उपचार शक्तियों से जुड़ता है"

    comparative_insights:
      en: |
        The blessings received after this episode are referenced throughout the Chalisa. His "vajra body" (Verse 3), healing abilities (Verse 25), and immortality (Verse 29) all trace back to this childhood incident, showing how one pivotal event shaped his entire divine destiny.
      hi: |
        इस प्रसंग के बाद प्राप्त वरदानों का संदर्भ पूरी चालीसा में मिलता है। उनका "वज्र शरीर" (चौपाई 3), उपचार क्षमताएं (चौपाई 25), और अमरता (चौपाई 29) सभी इस बचपन की घटना से जुड़े हैं, यह दर्शाते हुए कि एक महत्वपूर्ण घटना ने उनकी संपूर्ण दिव्य नियति को कैसे आकार दिया।

---
```

---

## 🎨 Visual Display

When rendered, these boxes will appear as:

**On Desktop:**
```
┌──────────────────────────────┐  ┌──────────────────────────────┐
│ ☀️ The Sun-Swallowing       │  │ 📚 Origin of Name            │
│    Episode                   │  │    'Hanuman'                 │
│ [Story content...]           │  │ [Etymology content...]       │
└──────────────────────────────┘  └──────────────────────────────┘

▼ More Context (2 additional boxes)
```

**On Mobile:**
```
┌────────────────────────────────┐
│ ▼ Puranic Contexts (4)         │
│                                │
│ ☀️ The Sun-Swallowing Episode │
│ 📚 Origin of Name 'Hanuman'   │
│ 📏 Understanding Yojana        │
│ 🔗 Divine Blessings Received   │
└────────────────────────────────┘
```

---

## ✅ Checklist for Adding Context Boxes

- [ ] Verse analysis completed
- [ ] Box type(s) identified
- [ ] Priority level assigned
- [ ] Bilingual content prepared (English + Hindi)
- [ ] Related verses identified
- [ ] Source texts cited
- [ ] Visual aids prepared (if applicable)
- [ ] YAML syntax validated
- [ ] Front matter properly formatted
- [ ] File saved and tested

---

## 🔄 Next Steps After Adding

1. **Test locally:** Run Jekyll and verify rendering
2. **Check responsiveness:** Test on desktop, tablet, mobile
3. **Verify links:** Ensure related verse chips navigate correctly
4. **Review content:** Proofread bilingual text
5. **Test dark mode:** Check color contrast
6. **Validate accessibility:** Keyboard navigation and screen readers

---

## 📚 Related Documentation

- **Full Templates:** `puranic-context-template.md`
- **Design Guide:** `puranic-context-design-guide.md`
- **Verse Analysis:** See comprehensive analysis results

---

Last updated: 2026-02-04
