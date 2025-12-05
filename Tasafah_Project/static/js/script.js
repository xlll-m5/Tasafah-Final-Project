document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const booksContainer = document.getElementById('books-container');
    const allBooks = Array.from(document.querySelectorAll('.book-card'));

    searchInput.addEventListener('keyup', function() {
        const query = searchInput.value.toLowerCase();
        
        allBooks.forEach(bookCard => {
            const title = bookCard.getAttribute('data-title').toLowerCase();
            const author = bookCard.getAttribute('data-author').toLowerCase();

            if (title.includes(query) || author.includes(query)) {
                bookCard.style.display = 'block';
            } else {
                bookCard.style.display = 'none';
            }
        });

        console.log("تم تصفية الكتب بناءً على البحث:", query);
    });
});
