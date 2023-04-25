Quotely API Documentation
==========================

Quotely is a simple API that allows you to fetch random quotes. It's very easy to set up and can be used with any language that supports GET requests.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   text-responses
   json-responses

Text Responses
--------------

To fetch a quote in plain text format, you can make a GET request to the following endpoint:

GET https://quotely-api.codesoftgames.repl.co/api/text

This will return a random quote as a plain text string. For example:

Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett

JSON Responses
--------------

If you prefer to receive your quote as JSON, you can make a GET request to the following endpoint:

GET https://quotely-api.codesoftgames.repl.co/api/json

This will return a JSON object containing the quote content and author. For example:
{
  "content": "If you want to make your dreams come true, the first thing you have to do is wake up.",
  "author": "J.M. Power"
}
That's it! Quotely is a simple API that you can use to add some inspiration to your applications.
