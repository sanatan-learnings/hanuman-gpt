// Language switching functionality

function switchLanguage(lang) {
    const currentUrl = new URL(window.location.href);
    currentUrl.searchParams.set('lang', lang);

    // Store preference
    localStorage.setItem('preferredLanguage', lang);

    // Reload page with new language parameter
    window.location.href = currentUrl.toString();
}

// Get current language from URL or localStorage
function getCurrentLanguage() {
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    const storedLang = localStorage.getItem('preferredLanguage');
    return urlLang || storedLang || 'en';
}

// Update all navigation links to preserve language parameter
function updateNavigationLinks() {
    const lang = getCurrentLanguage();

    // Update all internal links to include/update lang parameter
    document.querySelectorAll('a[href^="/"], a[href^="./"], a[href^="../"]').forEach(link => {
        let href = link.getAttribute('href');
        if (href && !href.includes('#')) {
            // Remove existing lang parameter if present
            href = href.replace(/[?&]lang=[^&]*/, '');
            // Remove trailing ? or & if left behind
            href = href.replace(/[?&]$/, '');
            // Add current language parameter
            const separator = href.includes('?') ? '&' : '?';
            link.setAttribute('href', href + separator + 'lang=' + lang);
        }
    });
}

// Show content in the selected language
function displayLanguageContent() {
    const lang = getCurrentLanguage();

    // Update language selector
    const select = document.getElementById('languageSelect');
    if (select) {
        select.value = lang;
    }

    // Show/hide language-specific content
    document.querySelectorAll('[data-lang]').forEach(el => {
        if (el.getAttribute('data-lang') === lang) {
            el.style.display = '';
        } else {
            el.style.display = 'none';
        }
    });
}

// Initialize on page load
function initLanguage() {
    displayLanguageContent();
    updateNavigationLinks();
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', initLanguage);
