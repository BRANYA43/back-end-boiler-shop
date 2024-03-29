document.addEventListener("DOMContentLoaded", function() {
    var rows = document.querySelectorAll('.row');
    rows.forEach(function(row) {
        if (!row.parentElement.classList.contains('total-sum')) {
            var label = row.querySelector('.label');
            var value = row.querySelector('.value');
            var availableSpace = row.clientWidth - label.clientWidth - value.clientWidth;
            var dotsCount = Math.floor(availableSpace / 1);
            var dotsText = '.'.repeat(dotsCount);
            label.textContent += dotsText;
        }
    });
});