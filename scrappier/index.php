<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


   
    <link rel="stylesheet"  href="https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700">
    <link rel="stylesheet"  href="https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.css">

    <link    rel="stylesheet" href="./main.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
     <title></title>
</head>
<body>




<i title="Go to top" onclick="topFunction()" id="myBtn" class="fa fa-arrow-up" aria-hidden="true"></i>
<div class="container">
  <div class="sidebar">
    <div class="sidebar-container">
      <a class="logo-link" href="#" onclick="sortMovies('popularity')">
        <img src="https://i.imgur.com/AYldSBG.png" class="logo-image">
      </a>
      <h2 class="title-genre">Discover</h2>
      <a class="category-link current" href="#" onclick="sortMovies('popularity')">
        <div class="genre">Popular</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('rating')">
        <div class="genre">Top Rated</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('grossing')">
        <div class="genre">Grossing</div>
      </a>
      <h2 class="title-genre">Genres</h2>
      <a class="category-link" href="#" onclick="sortMovies('action')">
        <div class="genre">Action</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('adventure')">
        <div class="genre">Adventure</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('animation')">
        <div class="genre">Animation</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('comedy')">
        <div class="genre">Comedy</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('crime')">
        <div class="genre">Crime</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('documentary')">
        <div class="genre">Documentary</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('drama')">
        <div class="genre">Drama</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('family')">
        <div class="genre">Family</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('fantasy')">
        <div class="genre">Fantasy</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('history')">
        <div class="genre">History</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('horror')">
        <div class="genre">Horror</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('music')">
        <div class="genre">Music</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('mystery')">
        <div class="genre">Mystery</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('romance')">
        <div class="genre">Romance</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('science fiction')">
        <div class="genre">Science Fiction</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('tv movie')">
        <div class="genre">TV Movie</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('thriller')">
        <div class="genre">Thriller</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('war')">
        <div class="genre">War</div>
      </a>
      <a class="category-link" href="#" onclick="sortMovies('western')">
        <div class="genre">Western</div>
      </a>
      <a target="_blank" rel="noopener noreferrer" href="#" onclick="window.open('https://ko-fi.com/vincenzopiromalli')" class="coffee"><img src="https://i.imgur.com/WP4kgsA.png" alt="Buy me a coffee">
        <span style="margin-left: 5px;">Buy me a coffee</span>
      </a>

    </div>
  </div>
  <div class="search">
    <form class="search-form"><button type="submit" class="search-button"><i class="fa fa-search"></i></button><input id="search" onKeyPress="return checkSubmit(event)" type="search" placeholder="&nbsp;Search for a movie..." class="search-input" value=""></form>
  </div>
  <div class="content">
    <div class="inner-container">
      <div class="titles">
        <h1>Popular</h1>
        <h2>movies</h2>
      </div>
      <div class="item-container">
      </div>
      <div class="load-more"><i class="fa fa-plus-circle more" aria-hidden="true"></i></div>
    </div>
  </div>
</div>

<script src="./app.js"></script>
    
</body>
</html>