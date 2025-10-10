/**
 * Equacare LLC - Main JavaScript
 * Interactive features and functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // ===================================
    // Mobile Menu Toggle
    // ===================================
    
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.classList.toggle('active');
        });
        
        // Close mobile menu when clicking on a link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            });
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideMenu = navMenu.contains(event.target);
            const isClickOnToggle = mobileMenuToggle.contains(event.target);
            
            if (!isClickInsideMenu && !isClickOnToggle && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            }
        });
    }
    
    // ===================================
    // Navbar Scroll Effect
    // ===================================
    
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });
    
    // ===================================
    // Smooth Scrolling for Anchor Links
    // ===================================
    
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href !== '#' && href.length > 1) {
                const target = document.querySelector(href);
                
                if (target) {
                    e.preventDefault();
                    const offsetTop = target.offsetTop - 80;
                    
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // ===================================
    // Scroll to Top Button
    // ===================================
    
    const scrollTopBtn = document.getElementById('scrollTopBtn');
    
    if (scrollTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        });
        
        scrollTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // ===================================
    // Hero Scroll Arrow
    // ===================================
    
    const heroScroll = document.querySelector('.hero-scroll');
    
    if (heroScroll) {
        heroScroll.addEventListener('click', function() {
            const nextSection = document.querySelector('.features') || document.querySelector('.about-preview');
            
            if (nextSection) {
                const offsetTop = nextSection.offsetTop - 80;
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    }
    
    // ===================================
    // Intersection Observer for Animations
    // ===================================
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const animateOnScroll = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Apply fade-in animation to cards
    const cards = document.querySelectorAll('.feature-card, .service-card, .testimonial-card, .mission-card, .service-detail-card');
    
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        animateOnScroll.observe(card);
    });
    
    // ===================================
    // Form Validation Enhancement
    // ===================================
    
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        
        inputs.forEach(input => {
            // Add real-time validation feedback
            input.addEventListener('blur', function() {
                validateInput(this);
            });
            
            // Remove error styling on input
            input.addEventListener('input', function() {
                if (this.classList.contains('error')) {
                    this.classList.remove('error');
                }
            });
        });
    });
    
    function validateInput(input) {
        const value = input.value.trim();
        
        if (input.hasAttribute('required') && value === '') {
            input.classList.add('error');
            return false;
        }
        
        if (input.type === 'email' && value !== '') {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                input.classList.add('error');
                return false;
            }
        }
        
        if (input.type === 'tel' && value !== '') {
            const phoneRegex = /^[\d\s\-\+\(\)]+$/;
            if (!phoneRegex.test(value)) {
                input.classList.add('error');
                return false;
            }
        }
        
        input.classList.remove('error');
        return true;
    }
    
    // ===================================
    // Testimonial Slider (if multiple testimonials)
    // ===================================
    
    const testimonialsGrid = document.querySelector('.testimonials-grid');
    
    if (testimonialsGrid) {
        const testimonialCards = testimonialsGrid.querySelectorAll('.testimonial-card');
        
        // Auto-rotate testimonials on mobile
        if (window.innerWidth < 768 && testimonialCards.length > 1) {
            let currentIndex = 0;
            
            function showTestimonial(index) {
                testimonialCards.forEach((card, i) => {
                    if (i === index) {
                        card.style.display = 'block';
                        card.style.animation = 'fadeInUp 0.6s ease';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }
            
            function nextTestimonial() {
                currentIndex = (currentIndex + 1) % testimonialCards.length;
                showTestimonial(currentIndex);
            }
            
            // Initialize
            showTestimonial(0);
            
            // Auto-rotate every 5 seconds
            setInterval(nextTestimonial, 5000);
            
            // Add navigation dots (optional)
            const dotsContainer = document.createElement('div');
            dotsContainer.className = 'testimonial-dots';
            dotsContainer.style.cssText = 'display: flex; justify-content: center; gap: 10px; margin-top: 20px;';
            
            testimonialCards.forEach((_, i) => {
                const dot = document.createElement('button');
                dot.style.cssText = 'width: 10px; height: 10px; border-radius: 50%; border: 2px solid var(--primary-color); background: transparent; cursor: pointer; transition: all 0.3s ease;';
                dot.addEventListener('click', () => {
                    currentIndex = i;
                    showTestimonial(i);
                    updateDots();
                });
                dotsContainer.appendChild(dot);
            });
            
            function updateDots() {
                const dots = dotsContainer.querySelectorAll('button');
                dots.forEach((dot, i) => {
                    if (i === currentIndex) {
                        dot.style.background = 'var(--primary-color)';
                    } else {
                        dot.style.background = 'transparent';
                    }
                });
            }
            
            testimonialsGrid.parentNode.appendChild(dotsContainer);
            updateDots();
        }
    }
    
    // ===================================
    // Service Cards Hover Effect Enhancement
    // ===================================
    
    const serviceCards = document.querySelectorAll('.service-card, .service-detail-card');
    
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // ===================================
    // Loading Animation for Images
    // ===================================
    
    const images = document.querySelectorAll('img');
    
    images.forEach(img => {
        if (!img.complete) {
            img.style.opacity = '0';
            img.addEventListener('load', function() {
                this.style.transition = 'opacity 0.5s ease';
                this.style.opacity = '1';
            });
        }
    });
    
    // ===================================
    // CTA Button Pulse Effect
    // ===================================
    
    const ctaButtons = document.querySelectorAll('.cta .btn-primary');
    
    ctaButtons.forEach(button => {
        setInterval(() => {
            button.style.animation = 'pulse 1s ease';
            setTimeout(() => {
                button.style.animation = '';
            }, 1000);
        }, 5000);
    });
    
    // ===================================
    // Accessibility: Keyboard Navigation
    // ===================================
    
    // Allow Enter key to submit forms
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && e.target.tagName !== 'TEXTAREA') {
            const form = e.target.closest('form');
            if (form) {
                const submitBtn = form.querySelector('button[type="submit"]');
                if (submitBtn && !submitBtn.disabled) {
                    e.preventDefault();
                    submitBtn.click();
                }
            }
        }
    });
    
    // ===================================
    // Print Styles Helper
    // ===================================
    
    window.addEventListener('beforeprint', function() {
        // Expand all collapsed sections before printing
        const collapsedElements = document.querySelectorAll('[aria-expanded="false"]');
        collapsedElements.forEach(el => {
            el.setAttribute('aria-expanded', 'true');
        });
    });
    
    // ===================================
    // Performance: Lazy Loading for Background Images
    // ===================================
    
    const lazyBackgrounds = document.querySelectorAll('[data-bg]');
    
    if ('IntersectionObserver' in window) {
        const bgObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const element = entry.target;
                    element.style.backgroundImage = `url(${element.dataset.bg})`;
                    element.removeAttribute('data-bg');
                    bgObserver.unobserve(element);
                }
            });
        });
        
        lazyBackgrounds.forEach(bg => bgObserver.observe(bg));
    }
    
    // ===================================
    // Console Welcome Message
    // ===================================
    
    console.log('%c👋 Welcome to Equacare LLC!', 'color: #2563eb; font-size: 20px; font-weight: bold;');
    console.log('%cBuilt with ❤️ using Django & JavaScript', 'color: #10b981; font-size: 14px;');
    
});

// ===================================
// CSS Animation Keyframes (added via JS)
// ===================================

const style = document.createElement('style');
style.textContent = `
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    input.error, textarea.error, select.error {
        border-color: #ef4444 !important;
        box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1) !important;
    }
`;
document.head.appendChild(style);

// ===================================
// Utility Functions
// ===================================

// Debounce function for performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function for scroll events
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Export functions for use in other scripts
window.EquacareUtils = {
    debounce,
    throttle
};

