py-lagerhythm 0.1
==============

This is a simple Python/Flask app which uses the 'tweepy' library
to captures text via CGI then passes it along to twitter.

It will also collect your GPS geolocation coordinates and upload
them as well if your browser supports it (you'll also need to enable
this in your twitter account).

There is also a Perl/CGI version called "Lagerhythm" which was initially
written before porting this to Python.

In order to utilize this you'd need to create a developer account
for twitter and then obtain the various secret keys needed.

This was originally hosted on Red Hat's 'Open Shift'
(http://www.openshift.com) and used to track the amount
of draft beer (pivo tocene) I consumed while in the Czech Republic
on work assignment.

This is released under the BSD license so do anything you want with it,
just remember to have fun.  Thanks to @djipko for helping me
hack this to completion in a very short timeframe.

Name credit goes to Nancy Benninger for "lagerhythm" :)
