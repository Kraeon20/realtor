const header = document.querySelector("header");
const menu = document.querySelector("#menu-icon");
const body = document.body;
const formBtn = document.querySelector("#bookTripBtn");
const formContainer = document.querySelector("#formContainer");
const endFormContainer = document.querySelector("#EndformContainer");

window.addEventListener("scroll", function () {
    header.classList.toggle("sticky", window.scrollY > 60);
});

menu.addEventListener("click", function () {
    body.classList.toggle("menu-open");
});

formBtn.addEventListener("click", function (e) {
  e.preventDefault();
  if (window.innerWidth < 768) {
    if (window.scrollY < endFormContainer.offsetTop) {
      window.scrollTo({
        top: endFormContainer.offsetTop,
        behavior: "smooth",
      });
    } else {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    }
  } else {
    formContainer.style.display = "block";
  }
});

// Close the menu when a menu item is clicked (optional)
const navbarItems = document.querySelectorAll(".navbar a");

navbarItems.forEach((item) => {
    item.addEventListener("click", function () {
        body.classList.remove("menu-open");
        body.classList.remove("showForm");
    });
});
