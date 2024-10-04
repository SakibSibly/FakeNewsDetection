document.addEventListener('DOMContentLoaded', function () {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    dropdownToggle.addEventListener('click', function (event) {
        event.preventDefault();
        dropdownMenu.classList.toggle('show');
        
        adjustDropdownPosition();
    });

    window.addEventListener('click', function (event) {
        if (!dropdownToggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove('show');
        }
    });

    function adjustDropdownPosition() {
        const menuRect = dropdownMenu.getBoundingClientRect();
        const toggleRect = dropdownToggle.getBoundingClientRect();

        if (menuRect.bottom > window.innerHeight) {
            dropdownMenu.style.top = `${toggleRect.top - menuRect.height}px`;
        } else {
            dropdownMenu.style.top = `${toggleRect.bottom}px`;
        }
    }
});