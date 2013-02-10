/*global jQuery escape*/
jQuery(function($, undefined) {
    "use strict";
    var twitterLinkUrl = 'https://twitter.com/intent/tweet?button_hashtag=neigefr&text='
      , reverseGeocodingService = 'http://nominatim.openstreetmap.org/reverse';

    function tweet(text, postcode) {
        if (postcode) text += ' ' + postcode;
        window.location.href = twitterLinkUrl + encodeURIComponent(text);
    }

    $('#levels').find('a').each(function(level) {
        // append level/10 info to link label
        $(this).data('level', level).text($(this).text() + ' ' + level + '/10');
    }).on('click', function(event) {
        var $link = $(this), href = $link.attr('href'), tweetText = $link.text();
        event.preventDefault();
        if (!navigator.geolocation) return tweet(tweetText, '!CODE_POSTAL!');
        navigator.geolocation.getCurrentPosition(function(position) {
            $.getJSON(reverseGeocodingService, {
                format: 'json',
                lat: position.coords.latitude,
                lon: position.coords.longitude,
                addressdetails: 1
            }, function(data) {
                tweet(tweetText, data.address.postcode);
            });
        }, function(msg) {
            tweet(tweetText, '!CODE_POSTAL!');
        });
    });
});
