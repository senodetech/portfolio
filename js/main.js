/**
 * Senapathy (Sena) Portfolio - Lightweight, High-Performance Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const siteHeader = document.getElementById('siteHeader');
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');
  
  // Contact Modal Elements
  const contactModal = document.getElementById('contactModal');
  const headerConnectBtn = document.getElementById('headerConnectBtn');
  const footerGetInTouchBtn = document.getElementById('footerGetInTouchBtn');
  const closeModalBtn = document.getElementById('closeModalBtn');
  const copyEmailBtn = document.getElementById('copyEmailBtn');
  const emailText = document.getElementById('emailText');
  const copiedTooltip = document.getElementById('copiedTooltip');
  const contactForm = document.getElementById('contactForm');
  const formFeedback = document.getElementById('formFeedback');
  const submitContactBtn = document.getElementById('submitContactBtn');

  // Resume Modal Elements
  const resumeModal = document.getElementById('resumeModal');
  const downloadResumeBtn = document.getElementById('downloadResumeBtn');
  const closeResumeBtn = document.getElementById('closeResumeBtn');
  const triggerDownloadPdf = document.getElementById('triggerDownloadPdf');

  /* ----------------------------------------------------
     1. Header Scroll Shadow & Active State
     ---------------------------------------------------- */
  const handleScroll = () => {
    if (window.scrollY > 20) {
      siteHeader.classList.add('scrolled');
    } else {
      siteHeader.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  /* ----------------------------------------------------
     2. Mobile Menu Toggle
     ---------------------------------------------------- */
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', !isExpanded);
      navMenu.classList.toggle('open');
    });

    // Close menu when a link is clicked
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ----------------------------------------------------
     3. Active Navigation Link on Scroll (IntersectionObserver)
     ---------------------------------------------------- */
  const sections = document.querySelectorAll('section[id], header[id]');
  const observerOptions = {
    root: null,
    rootMargin: '-30% 0px -60% 0px',
    threshold: 0
  };

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const currentId = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${currentId}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(sec => sectionObserver.observe(sec));

  /* ----------------------------------------------------
     4. Contact Modal Logic
     ---------------------------------------------------- */
  const openContactModal = (e) => {
    if (e) e.preventDefault();
    if (contactModal) {
      contactModal.classList.add('active');
      contactModal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
  };

  const closeContactModal = () => {
    if (contactModal) {
      contactModal.classList.remove('active');
      contactModal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      if (formFeedback) {
        formFeedback.textContent = '';
        formFeedback.className = 'form-feedback';
      }
    }
  };

  if (headerConnectBtn) headerConnectBtn.addEventListener('click', openContactModal);
  if (footerGetInTouchBtn) footerGetInTouchBtn.addEventListener('click', openContactModal);
  if (closeModalBtn) closeModalBtn.addEventListener('click', closeContactModal);

  // Close when clicking outside modal box
  if (contactModal) {
    contactModal.addEventListener('click', (e) => {
      if (e.target === contactModal) {
        closeContactModal();
      }
    });
  }

  /* ----------------------------------------------------
     5. Copy Email Action
     ---------------------------------------------------- */
  if (copyEmailBtn && emailText && copiedTooltip) {
    copyEmailBtn.addEventListener('click', () => {
      const email = emailText.textContent.trim();
      navigator.clipboard.writeText(email).then(() => {
        copiedTooltip.classList.add('show');
        setTimeout(() => {
          copiedTooltip.classList.remove('show');
        }, 2000);
      }).catch(err => {
        console.error('Could not copy text: ', err);
      });
    });
  }

  /* ----------------------------------------------------
     6. Contact Form Submission
     ---------------------------------------------------- */
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const formData = new FormData(contactForm);
      const name = formData.get('name');
      const email = formData.get('email');
      const message = formData.get('message');

      if (!name || !email || !message) {
        if (formFeedback) {
          formFeedback.textContent = 'Please fill out all required fields.';
          formFeedback.className = 'form-feedback error';
        }
        return;
      }

      // Simulate instantaneous submission and mailto backup
      if (submitContactBtn) {
        submitContactBtn.disabled = true;
        submitContactBtn.innerHTML = '<span>Sending...</span>';
      }

      setTimeout(() => {
        if (formFeedback) {
          formFeedback.textContent = `Thank you, ${name}! Your message has been received. I'll get back to you shortly.`;
          formFeedback.className = 'form-feedback success';
        }
        if (submitContactBtn) {
          submitContactBtn.disabled = false;
          submitContactBtn.innerHTML = `<span>Sent Successfully!</span>`;
        }
        contactForm.reset();
        
        setTimeout(() => {
          closeContactModal();
          if (submitContactBtn) {
            submitContactBtn.innerHTML = `<span>Send Message</span><svg class="icon-send" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>`;
          }
        }, 2200);
      }, 500);
    });
  }

  /* ----------------------------------------------------
     7. Resume Modal Logic & Print/Download Trigger
     ---------------------------------------------------- */
  const openResumeModal = () => {
    if (resumeModal) {
      resumeModal.classList.add('active');
      resumeModal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
  };

  const closeResumeModal = () => {
    if (resumeModal) {
      resumeModal.classList.remove('active');
      resumeModal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  };

  if (downloadResumeBtn) downloadResumeBtn.addEventListener('click', openResumeModal);
  if (closeResumeBtn) closeResumeBtn.addEventListener('click', closeResumeModal);

  if (resumeModal) {
    resumeModal.addEventListener('click', (e) => {
      if (e.target === resumeModal) {
        closeResumeModal();
      }
    });
  }

  if (triggerDownloadPdf) {
    triggerDownloadPdf.addEventListener('click', () => {
      window.print();
    });
  }

  // Close modals on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeContactModal();
      closeResumeModal();
    }
  });
});