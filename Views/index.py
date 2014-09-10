from static import *
from time import ctime
from sqlite3 import connect

main = """
<div id='main' class='site-main container_16'>
			<div class='inner'>
				<div id='primary' class='grid_11 suffix_1'>
					
					<!-- Articles -->								
                                                %s
					<!-- Pagination 
					<ul class='pagination'>
						<li><a class='active radius' href='#'>1</a></li>
						<li><a class='radius' href='#'>2</a></li>
						<li><a class='radius' href='#'>3</a></li>
						<li><a class='radius' href='#'>4</a></li>
						<li><a class='radius' href='#'>5</a></li>
					</ul>
					-->
				</div>
	
				<div id='secondary' class='grid_4 widget-area' role='complementary'>
                    <!-- replace with appropriate content-->
                        %s %s %s
				</div>
				<div class='clear'></div>
			</div>
		</div>
""" 
article = """

					<article class='list vevent'>
						<div class='short-content'>
							
							<h1 class='entry-header'>
								<a class='url summary' href='single?%s'> %s </a>
							</h1>

							<div class='short-description description'>
								<p> %s </p>
							</div>

							<div class='entry-meta'>
								<time class='dtstart'><a class='buttons time fleft' href='/'> %s </a></time>  <a class='buttons fright' href='single?%s'>Read more...</a>
							</div>
							<div class='clear'></div>

						</div>
						<div class='clear'></div>
					</article>

					"""


def view(uid = " ", name = " ", success = False):
    articles = ""
    con = connect('Models/blog.db')
    c = con.cursor()
    c.execute("SELECT * FROM posts LIMIT 10")
    posts  = c.fetchall()
    if len(posts) == 0:
        pass
    else:
        for row in posts:
            articles += article % (row[1], row[2], row[3], row[4], row[1])
    content = header % ("Home", "Blog Posts", "Blog Posts")
    if success:
        content += main %(articles, signup % ('none' , name), login % ('none' , name), profile % ('', name, uid)) + footer
    else:
        content += main %(articles , signup % ('' , name) , login % ('none' , name), profile % ('none', " ", '')) + footer
    return content
