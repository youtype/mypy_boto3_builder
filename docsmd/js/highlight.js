document$.subscribe(() => {
    const navbar = document.querySelector('.md-sidebar--secondary')
    if (navbar.querySelectorAll('.md-nav__item').length > 1000) {
        navbar.style.display = 'none';
    }

    document.querySelectorAll('code').forEach(el => {
        setTimeout(() => {
            hljs.highlightElement(el)
            el.classList.remove('hljs')
        }, 0)
    })
})
