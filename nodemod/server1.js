var express = require('express');
var fs      = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var app     = express();

app.get('/scrape', function(req, res){
  url = 'http://www.imdb.com/title/tt1229340/';

  request(url, function(error, response, html){
    if(!error){
      var $ = cheerio.load(html);
      console.log(html);

      var title, release_details, rating;
      var json = { title : "", release_details : "", rating : ""};

      $('.title_wrapper').filter(function(){
        var data = $(this);
        
	title = data.children().first().text();
	
	release_details = data.children().last().children().text();

	})
	$('.ratingValue').filter(function(){
                var data = $(this);

                // The .star-box-giga-star class was exactly where we wanted it to be.
                // To get the rating, we can simply just get the .text(), no need to traverse the DOM any further

                rating = data.text();

        json.rating = rating;
	json.title = title;
        json.release_details = release_details;
      })

    }

    fs.writeFile('output1.json', JSON.stringify(json, null, 4), function(err){
      console.log('File successfully written! - Check your project directory for the output.json file');
    })

    res.send('Check your console!')
  })
})

app.listen('8081')
console.log('Magic happens on port 8081');
exports = module.exports = app;