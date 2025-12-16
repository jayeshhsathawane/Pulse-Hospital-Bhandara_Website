// pulsehospital/static/script.js

// ----------------------------------------------------------------------
// GLOBAL MODAL FUNCTIONS (CRITICAL FOR ONCLICK ATTRIBUTES LIKE CLOSE BUTTONS)
// Functions must be defined globally to be accessible by HTML 'onclick'.
// ----------------------------------------------------------------------

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeDoctorModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
}

function openGalleryModal(imageSrc) {
    const modal = document.getElementById('galleryModal');
    const modalImage = document.getElementById('galleryModalImage');
    if (modal && modalImage) {
        modalImage.src = imageSrc;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeGalleryModal() {
    const modal = document.getElementById('galleryModal');
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
}

// Make critical functions globally available (for HTML 'onclick' on CLOSE buttons)
window.openDoctorModal = openModal;       // Mapped to generic openModal
window.closeDoctorModal = closeDoctorModal;
window.openGalleryModal = openGalleryModal;
window.closeGalleryModal = closeGalleryModal;


// Close modal when clicking outside (on the modal overlay)
window.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal') && e.target.classList.contains('active')) {
        e.target.classList.remove('active');
        document.body.style.overflow = 'auto';
    }
});

// Close modal with Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const activeModal = document.querySelector('.modal.active');
        if (activeModal) {
            activeModal.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    }
});


// ----------------------------------------------------------------------
// MAIN EXECUTION LOGIC (Runs after all HTML is loaded)
// ----------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {

    // ----------------------------------------------------------------------
    // 1. MOBILE MENU & SMOOTH SCROLLING
    // ----------------------------------------------------------------------
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });
    }

    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
        });
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (this.getAttribute('href').length > 1) { 
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // ----------------------------------------------------------------------
    // 2. DOCTOR MODAL ACTIVATION FIX (Reliable Event Listener)
    // ----------------------------------------------------------------------
   const doctorProfileButtons = document.querySelectorAll('.doctor-card .view-profile-btn');
    
doctorProfileButtons.forEach(button => {
    
    // 1. Try to get modal ID from the reliable data-modal-id attribute
    let modalId = button.getAttribute('data-modal-id'); 

    // 2. Fallback: If data-modal-id is missing, try to get it from the onclick attribute
    if (!modalId) {
        const onclickAttr = button.getAttribute('onclick');
        if (onclickAttr) {
            // Use regex to extract the ID (e.g., 'doctor1') from onclick="openDoctorModal('doctor1')"
            const modalMatch = onclickAttr.match(/'([^']+)'/); 
            if (modalMatch && modalMatch.length > 1) {
                modalId = modalMatch[1];
            }
        }
    }
    
    // Attach listener using the found modalId
    if (modalId) {
        button.addEventListener('click', (e) => {
            e.stopPropagation(); // Stop click events from affecting parent elements
            if (window.openModal) { // Ensure openModal is globally available
                window.openModal(modalId);
            }
        });
        
        
    }
});
    // ----------------------------------------------------------------------
    // 3. GALLERY MODAL ACTIVATION FIX
    // ----------------------------------------------------------------------
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Get the image source either from the data attribute or the onclick parameter
            const onclickAttr = item.getAttribute('onclick');
            if (onclickAttr) {
                const srcMatch = onclickAttr.match(/'([^']+)'/);
                if (srcMatch && srcMatch.length > 1) {
                    const imageSrc = srcMatch[1];
                    openGalleryModal(imageSrc);
                }
            }
        });
    });


    // ----------------------------------------------------------------------
    // 4. TESTIMONIALS CAROUSEL
    // ----------------------------------------------------------------------
    let currentTestimonial = 0;
    const testimonials = document.querySelectorAll('.testimonial-card');
    const prevBtn = document.querySelector('.carousel-btn.prev');
    const nextBtn = document.querySelector('.carousel-btn.next');

    function showTestimonial(index) {
        testimonials.forEach((testimonial, i) => {
            testimonial.classList.remove('active');
            if (i === index) {
                testimonial.classList.add('active');
            }
        });
    }

    if (prevBtn && nextBtn && testimonials.length > 0) {
        showTestimonial(currentTestimonial);
        
        prevBtn.addEventListener('click', () => {
            currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
            showTestimonial(currentTestimonial);
        });

        nextBtn.addEventListener('click', () => {
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
            showTestimonial(currentTestimonial);
        });

        setInterval(() => {
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
            showTestimonial(currentTestimonial);
        }, 5000);
    }
    
    // ----------------------------------------------------------------------
    // 5. NAVBAR SCROLL EFFECT
    // ----------------------------------------------------------------------
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 100) {
            navbar.style.boxShadow = '0 4px 20px rgba(46, 204, 113, 0.15)';
        } else {
            navbar.style.boxShadow = '0 2px 15px rgba(46, 204, 113, 0.1)';
        }
    });
    
    console.log('Pulse Multispeciality Hospital Bhandara - JavaScript Core Initialized');
});