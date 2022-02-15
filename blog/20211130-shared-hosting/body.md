title: Shared hosting
author: David Houseman
date: 2021-11-30

Shared hosting is the cheapest and simplest option for a simple website.
My hosting provider, `ventraip.com.au`, charges $5 AUD per month for its
smallest package. The configuration is handled by `cPanel` and it has
support for this python/flask (WSGI) application. SSL is now handled
automatically and for free with signed certificates provided by `cPanel`.
This means `http` access can be redirected to `https` access, by adding
the following lines to `.htaccess`:

    RewriteCond %{SERVER_PORT} 80
    RewriteCond %{HTTP_HOST} ^(www\.)?grey-house\.net
    RewriteRule ^(.*)$ https://www.grey-house.net/$1 [R,L]
