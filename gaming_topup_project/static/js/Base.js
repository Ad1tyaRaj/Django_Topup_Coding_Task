// Add interactivity
document.addEventListener('DOMContentLoaded', function() {
    // Amount selection
    const amountBtns = document.querySelectorAll('.amount-btn');
    amountBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            amountBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Game card hover effects
    const gameCards = document.querySelectorAll('.game-card');
    gameCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Search functionality
    const searchInput = document.querySelector('.search-input');
    const searchBtn = document.querySelector('.search-btn');
    
    searchBtn.addEventListener('click', function() {
        const searchTerm = searchInput.value;
        if (searchTerm) {
            alert(`Searching for: ${searchTerm}`);
        }
    });

    // Top-up button clicks
    const topupBtns = document.querySelectorAll('.topup-btn');
    topupBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const gameName = this.parentElement.querySelector('.game-name').textContent;
            alert(`Opening ${gameName} top-up page...`);
        });
    });

    // Form submission
    const submitBtn = document.querySelector('.submit-btn');
    submitBtn.addEventListener('click', function() {
        alert('Redirecting to payment gateway...');
    });
});