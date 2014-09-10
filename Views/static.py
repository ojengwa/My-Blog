#HEADER
header = """
<!DOCTYPE html>
<html dir='ltr' lang='en-US'>
<head>
	
	<!--  Basic Page Needs -->
	<meta charset='UTF-8' />
	<title>Pythonic | %s </title>
	<meta name='description' content=''>
	<meta name='author' content=''>

	<!-- Favicon -->
	<link rel='shortcut icon' href='favicon.ico' />
	<link rel='apple-touch-icon' href='apple-touch-icon.png' />
	
	<!-- Mobile Specific Meta -->
	<meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1'>

	<!-- CSS -->
	<link rel='stylesheet' type='text/css' media='all' href='static/style.css' />
	<link rel='stylesheet' type='text/css' media='all' href='static/css/font-awesome.min.css' />
	<link rel='stylesheet' type='text/css' media='all' href='static/css/flexslider.css' />
	<link rel='stylesheet' type='text/css' media='all' href='static/css/font-awesome-ie7.min.css' />
	<link rel='stylesheet' type='text/css' media='all' href='static/css/keyframes.css' />
	<link rel='stylesheet' type='text/css' media='all' href='static/css/grid.css' />
	<link rel='stylesheet' type='text/css' media='all' href='static/css/meanmenu.css' />
	
	<!-- Scripts -->
	<script type='text/javascript' src='static/js/jquery.min.js'></script>
	<script type='text/javascript'>
            $(document).ready(function(){
                $(".toggle").click(function(){
                    if($("#wpltfb-2").css("display") != 'none'){
                        $("#wpltfb-2").hide();
                        $("#wpltfb-1").show();
                    }
                    else{
                        $("#wpltfb-1").hide();
                        $("#wpltfb-2").show();
                    }
                });
                return false;
            });
        </script>
	<script type='text/javascript' src='static/js/html5.js'></script>
	<script src='static/js/base.js'></script>

	<!-- Scripts for plugins -->
	<script src='static/js/jquery.fitvids.js'></script>
	<script src='static/js/jquery.meanmenu.js'></script>
	<script src='static/js/jquery.flexslider-min.js'></script>
	<script src='static/js/jquery.inview.js'></script>
	<script src='static/js/jquery.scrollParallax.min.js'></script>
</head>
<body class='home blog two-column right-sidebar' data-twttr-rendered='true'>
	<div id='page'>

		<header id='branding' class='site-header' role='banner'>
			<div id='sticky_navigation'>
				<div class='container_16'>
					<hgroup class='fleft grid_5'>
						<h1 id='site-title'><a href='index.do' title='Charitas - Foundation' rel='home'>Pythonic</a></h1>
						<h2 id='site-description'>Little Blog</h2>
					</hgroup>

					<nav role='navigation' class='site-navigation main-navigation grid_11' id='site-navigation'>
						<div class='menu-main-menu-container'>
							<ul id='menu-main-menu' class='nav-menu'>
								<li class='menu-item '><a href='index.do'>Home</a></li>
								<!--li class='menu-item '><a href='contact.do'>Contacts</a></li -->
							</ul>
						</div>
					</nav>
					<!-- .site-navigation .main-navigation -->
					<div class='grid_16 mob-nav'></div>
					<div class='clear'></div>
				</div>
			</div>
		</header>
		<!-- #masthead .site-header -->


		<div class='item teaser-page-list'>
			<div class='container_16'>
				<aside class='grid_10'>
					<h1 class='page-title'> %s </h1>
				</aside>
				<div class='grid_6'>
					<div id='rootline'>
						<a href='/'>Home Page</a> | <span class='current'> %s </span>	
					</div>
				</div>
				<div class='clear'></div>
			</div>
		</div>



"""
#LOGIN
login = """


					<aside id='wpltfb-1' class='widget WPlookCauses' style='display: %s '>	
						<div class='widget-title'>
							<h3 class='toggle'>Login</h3>
							<div class='clear'></div>
						</div>
						<span style="color:red"> %s </span>
						<div class='widget-event-body'>
							<article class='event-item'>
								<form action='auth' id='contact-form' method='post'>

									<p>
										<input class='radius span'  type='email' name='user' id='user' value='' placeholder='Email Address*' required/>
										<span class='clear'></span>
									</p>
									<p>
										<input class='radius' type='password' name='pass' id='pass' value='' placeholder='Your Password*' required/>
										<span class='clear'></span>
									</p>
									<p>
										<input  class='buttons radius send' value='Login!' type='submit'></input >
										<input  class='buttons radius red toggle' value='Create Account!' type='submit'></input >
									</p>
								</form>
								
							</article>

							<!-- Second Event -->
							<article class='event-item'>
							</article>
						</div>
					</aside>

"""
#SIGNUP
signup = """


					<aside id='wpltfb-2' class='widget WPlookCauses' style='display: %s '>	
						<div class='widget-title'>
							<h3 cls>Signup</h3>
							<div class='clear'></div>
						</div>
						
                                                    <span style="color:red"> %s </span>
						<div class='widget-event-body'>
							<article class='event-item'>
								<form action='auth' id='contact-form' method='post'>

									<p>
										<input class='radius span'  type='text' name='fname' id='fname' value='' placeholder='First Name*' required/>
										<span class='clear'></span>
									</p>
									<p>
										<input class='radius span'  type='text' name='lname' id='lname' value='' placeholder='Last Name*' required/>
										<span class='clear'></span>
									</p>
									<p>
										<input class='radius span'  type='email' name='user' id='user' value='' placeholder='Email Address*' required/>
										<span class='clear'></span>
									</p>
									<p>
										<input class='radius' type='password' name='pass' id='pass' value='' placeholder='Your Password*' required/>
										<span class='clear'></span>
									</p>
									<p>
										<input  class='buttons radius send' value='Register Now!' type='submit'></input >
										<input  class='buttons radius red toggle' value='I Have Account' type='submit'></input >
									</p>
								</form>
								
							</article>

							<!-- Second Event -->
							<article class='event-item'>
							</article>
						</div>
					</aside>

"""
#PROFILE
profile = """

					<aside id="archives" class="widget" style='display: %s '>
						<div class="widget-title">	
							<h3>Profile</h3>
							<div class="clear"></div>
						</div>
						<ul>
							<li><strong>Welcome, </strong><a name="" > %s </a></li>
							<li><a href="post.do?%s" class=' grey' title="Create a New Post"> Publish a new Article </a></li>
							<li><a href="logout" class='red disabled' disabled> Logout </a></li>
						</ul>
						<br>
						
						
						
					</aside>

"""
#FOOTER
footer = """
		<footer id='colophon' class='site-footer' role='contentinfo'>


			<!-- Site Info -->
			<div class='site-info'>
				<div class='container_16'>
					
					<!-- CopyRight -->
					<div class='grid_8'>
						<p class='copy'>Copyright &copy  2014.  All Rights reserved.  </p>
					</div>

					<!-- Design By -->
					<div class='grid_8'>
						<p class='designby'>Designed by <a href='http://github.com/ojengwa'>Bernard</a></p>
					</div>

					<div class='clear'></div>
				</div>
			</div><!-- .site-info -->
		</footer><!-- #colophon .site-footer -->

	</div>
	<!-- /#page -->
</body>
</html>"""
