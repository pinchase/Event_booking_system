document.addEventListener("DOMContentLoaded", function () {
    const carouselContainer = document.querySelector(".carousel-container");
    const prevButton = document.querySelector(".carousel-button.prev");
    const nextButton = document.querySelector(".carousel-button.next");

    let offset = 0;

    const moveCarousel = (direction) => {
        const itemWidth = document.querySelector(".carousel-item").offsetWidth;
        const maxOffset = -(carouselContainer.scrollWidth - carouselContainer.offsetWidth);

        if (direction === "next" && offset > maxOffset) {
            offset -= itemWidth + 20; // Adjust for gap
        } else if (direction === "prev" && offset < 0) {
            offset += itemWidth + 20;
        }

        carouselContainer.style.transform = `translateX(${offset}px)`;
    };

    prevButton.addEventListener("click", () => moveCarousel("prev"));
    nextButton.addEventListener("click", () => moveCarousel("next"));
});
