
 // Toggle nav for mobile
      const toggle = document.getElementById("menu-toggle");
      const links = document.getElementById("nav-links");
      toggle.addEventListener("click", () => {
        links.classList.toggle("active");
      });



// courses
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modalImg');
const closeBtn = document.getElementById('closeBtn');
const thumbnails = document.querySelectorAll('.thumbnail');

thumbnails.forEach(function(thumbnail) {
  thumbnail.onclick = function() {
    modal.style.display = "block";
    modalImg.src = this.src;
  }
});

closeBtn.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
