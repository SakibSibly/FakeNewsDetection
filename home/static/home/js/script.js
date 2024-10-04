const loder = document.querySelector('#preloader');
const analyze = document.querySelector('#analyze');
const process = document.querySelector('#process');

analyze.addEventListener("click", function() {

    // Show preloader
    loder.style.display = "block";
    process.style.display = "block";

    setTimeout(() => {
        // Hide preloader after loading is done
        loder.style.display = "none";
        process.style.display = "none";

    }, 10000); // Adjust the time as needed
});