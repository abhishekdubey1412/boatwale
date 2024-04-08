document.addEventListener('DOMContentLoaded', function () {
    const imgs = document.querySelectorAll('.img-select a');
    const imgBtns = [...imgs];
    let imgId = 1;
    let intervalId;

    imgBtns.forEach((imgItem) => {
        imgItem.addEventListener('click', (event) => {
            event.preventDefault();
            imgId = parseInt(imgItem.dataset.id);
            slideImage();
        });
    });

    function slideImage() {
        const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;
        const showcase = document.querySelector('.img-showcase');
        showcase.style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
    }

    function startAutoSlide() {
        intervalId = setInterval(() => {
            imgId = (imgId % imgBtns.length) + 1;
            slideImage();
        }, 3000);
    }

    function stopAutoSlide() {
        clearInterval(intervalId);
    }

    startAutoSlide();

    document.querySelector('.product_imgs').addEventListener('mouseenter', stopAutoSlide);
    document.querySelector('.product_imgs').addEventListener('mouseleave', startAutoSlide);

    window.addEventListener('resize', slideImage);
});