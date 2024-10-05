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


function openNav() {
    document.getElementById("sidebar").style.width = "250px";
}

function closeNav() {
    document.getElementById("sidebar").style.width = "0";
}

function toggleProfileMenu() {
    var profileMenu = document.getElementById("profile-menu");
    if (profileMenu.style.display === "block") {
        profileMenu.style.display = "none";
    } else {
        profileMenu.style.display = "block";
    }
}

function checkWindowSize() {
    if (window.innerWidth > 768) {
        closeNav();
    }
}

window.addEventListener('resize', checkWindowSize);
window.addEventListener('load', checkWindowSize);


document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll("nav a");

   
    links.forEach(link => {
        link.addEventListener("click", function () {
            
            links.forEach(link => link.classList.remove("active"));
            this.classList.add("active");
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll("nav a");

    
    const currentUrl = window.location.href;

    links.forEach(link => {
        if (link.href === currentUrl) {
            link.classList.add("active");
        }

        link.addEventListener("click", function () {
            links.forEach(link => link.classList.remove("active"));
            this.classList.add("active");
        });
    });
});
