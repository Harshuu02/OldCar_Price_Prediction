document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (!form) return;

    form.addEventListener('submit', function() {
        const btn = form.querySelector('button[type="submit"]');
        if (btn) {
            btn.disabled = true;

            // Create spinner
            const spinner = document.createElement('span');
            spinner.className = 'spinner-border spinner-border-sm me-2';
            spinner.setAttribute('role', 'status');
            spinner.setAttribute('aria-hidden', 'true');

            // Smooth fade-in
            spinner.style.opacity = 0;
            spinner.style.transition = "opacity 0.3s ease";
            btn.textContent = ' Predicting...';
            btn.prepend(spinner);

            setTimeout(() => {
                spinner.style.opacity = 1;
            }, 50);
        }
    });
});