// Arrow key navigation for verses
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on a verse page (verseNav should be defined)
    if (typeof window.verseNav !== 'undefined') {
        document.addEventListener('keydown', function(e) {
            // Ignore if user is typing in an input field
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
                return;
            }

            // Left arrow - previous verse
            if (e.keyCode === 37 && window.verseNav.previous) {
                window.location.href = window.verseNav.previous;
            }

            // Right arrow - next verse
            if (e.keyCode === 39 && window.verseNav.next) {
                window.location.href = window.verseNav.next;
            }

            // Home key or 'h' - go to home
            if (e.keyCode === 36 || e.keyCode === 72) {
                window.location.href = '/hanuman-chalisa/';
            }
        });

        // Add visual indicator for keyboard navigation
        const style = document.createElement('style');
        style.textContent = `
            .nav-button:focus {
                outline: 3px solid #ff6b35;
                outline-offset: 2px;
            }
        `;
        document.head.appendChild(style);
    }

    // Add keyboard shortcut help indicator
    const body = document.querySelector('body');
    if (body && typeof window.verseNav !== 'undefined') {
        const helpDiv = document.createElement('div');
        helpDiv.className = 'keyboard-help';
        helpDiv.innerHTML = `
            <style>
                .keyboard-help {
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    background: rgba(0,0,0,0.8);
                    color: white;
                    padding: 10px 15px;
                    border-radius: 4px;
                    font-size: 12px;
                    opacity: 0;
                    transition: opacity 0.3s;
                    pointer-events: none;
                    z-index: 1000;
                }
                .keyboard-help.show {
                    opacity: 1;
                }
            </style>
            <div>← → Navigate | H Home</div>
        `;
        body.appendChild(helpDiv);

        // Show help on first keypress
        let helpShown = false;
        document.addEventListener('keydown', function() {
            if (!helpShown) {
                helpDiv.classList.add('show');
                setTimeout(() => {
                    helpDiv.classList.remove('show');
                }, 3000);
                helpShown = true;
            }
        }, { once: true });
    }
});
