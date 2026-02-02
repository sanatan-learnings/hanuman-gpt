// Theme switching functionality for image themes

// Get current theme from localStorage or use default
function getCurrentTheme() {
    return localStorage.getItem('selectedTheme') || 'modern-minimalist';
}

// Set theme in localStorage
function setCurrentTheme(theme) {
    localStorage.setItem('selectedTheme', theme);
}

// Switch to a new theme
function switchTheme(theme) {
    setCurrentTheme(theme);
    applyTheme(theme);
}

// Apply theme by updating all image sources
function applyTheme(theme) {
    // Update all images that have src containing /images/
    // EXCEPT theme preview thumbnails (those should stay fixed)
    const images = document.querySelectorAll('img[src*="/images/"]:not([data-theme-preview])');

    images.forEach(img => {
        const currentSrc = img.getAttribute('src');
        // Replace the theme folder in the path while preserving collection
        // Pattern: /images/{collection}/{old-theme}/ -> /images/{collection}/{new-theme}/
        const newSrc = currentSrc.replace(/\/images\/([^\/]+)\/[^\/]+\//, `/images/$1/${theme}/`);
        img.setAttribute('src', newSrc);
    });
}

// Initialize theme on page load
function initializeTheme() {
    const theme = getCurrentTheme();
    const themeSelect = document.getElementById('themeSelect');

    if (themeSelect) {
        themeSelect.value = theme;
    }

    // Apply the current theme to all images
    applyTheme(theme);
}

// Run initialization when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeTheme);
} else {
    initializeTheme();
}
