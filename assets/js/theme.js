// Theme switching functionality for image themes

// Get collection key from the page
function getCurrentCollection() {
    // Try to extract collection from image paths on the page
    const firstImage = document.querySelector('img[src*="/images/"]');
    if (firstImage) {
        const match = firstImage.src.match(/\/images\/([^\/]+)\//);
        if (match) {
            return match[1];
        }
    }
    return null;
}

// Get current theme from localStorage for specific collection
function getCurrentTheme(collection) {
    if (!collection) return 'modern-minimalist';
    const key = `selectedTheme_${collection}`;
    return localStorage.getItem(key) || 'modern-minimalist';
}

// Set theme in localStorage for specific collection
function setCurrentTheme(collection, theme) {
    if (!collection) return;
    const key = `selectedTheme_${collection}`;
    localStorage.setItem(key, theme);
}

// Switch to a new theme
function switchTheme(theme) {
    const collection = getCurrentCollection();
    setCurrentTheme(collection, theme);
    applyTheme(collection, theme);
}

// Apply theme by updating all image sources for a specific collection
function applyTheme(collection, theme) {
    if (!collection) return;

    // Update all images that have src containing /images/{collection}/
    // EXCEPT theme preview thumbnails (those should stay fixed)
    const images = document.querySelectorAll(`img[src*="/images/${collection}/"]:not([data-theme-preview])`);

    images.forEach(img => {
        const currentSrc = img.getAttribute('src');
        // Replace the theme folder in the path for this specific collection
        // Pattern: /images/{collection}/{old-theme}/ -> /images/{collection}/{new-theme}/
        const pattern = new RegExp(`/images/${collection}/[^/]+/`);
        const newSrc = currentSrc.replace(pattern, `/images/${collection}/${theme}/`);
        img.setAttribute('src', newSrc);
    });
}

// Initialize theme on page load
function initializeTheme() {
    const collection = getCurrentCollection();
    const themeSelect = document.getElementById('themeSelect');

    // Only apply theme if there's a theme switcher on this page
    if (themeSelect && collection) {
        const theme = getCurrentTheme(collection);
        themeSelect.value = theme;
        applyTheme(collection, theme);
    }
}

// Run initialization when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeTheme);
} else {
    initializeTheme();
}
