document.addEventListener('DOMContentLoaded', getComments);

function getComments() {
  // Send a GET request to the IMDb comments API endpoint
  fetch('https://api.imdb.com/comments')
    .then(response => response.json())
    .then(data => {
      // Process the comments data
      displayComments(data.comments);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function displayComments(comments) {
  // Get the comments container element
  var commentsContainer = document.getElementById('comments');

  // Iterate through the comments and create HTML elements to display them
  comments.forEach(comment => {
    var commentElement = document.createElement('div');
    commentElement.classList.add('comment');
    commentElement.textContent = comment.text;
    commentsContainer.appendChild(commentElement);
  });
}
