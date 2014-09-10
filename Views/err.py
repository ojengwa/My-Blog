from static import *

main = """


		<div class="item teaser-page-404">
			<div class="container_16">
				<aside class="grid_16">
					<h1 class="page-title">404 - Calabar Meat!!</h1>
					<h2>The page you were looking for could not be found.</h2>
				</aside>
			</div>
		</div>

		<div id="main" class="site-main container_16">
			<div class="inner">
				<div id="primary" class="grid_16">
					<article class="single-404">
						
						<a target="_self" style='color:#fff' class="box medium red square" href="/">Go Home</a>

					</article>
					
				</div>
	
				<div class="clear"></div>
			</div>
		</div>

"""

def view():
    return header % ("404", "Not Found", "404 - Not Found") + main + footer
