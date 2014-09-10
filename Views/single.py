from static import *
from time import ctime
from sqlite3 import connect

main = """

        <!-- Local content -->
		<div id="main" class="site-main container_16">
			<div class="inner">
				<div id="primary" class="grid_11 suffix_1">
					<article class="single">
						
						<div class="entry-content">
							
							<div class="clear"></div>

							<div class="long-description">
								<h3> %s </h3>
								<br /><p> %s </p>
							</div>

							
							<div class="clear"></div>
							
							<div class="entry-meta-press">

								<time class="entry-date fleft" >
									%s
								</time>


								<div class="author-i">
									<a href="/"> 'Bernard' </a>
								</div>
								<div class="clear"></div>
							</div>

						</div>

						<div class="clear"></div>
	
					</article>"""

comments = """        
                    <div class="alert grey">Grey Message</div>
                    <form action="processForm.php" id="contact-form" method="post">
                        <p>
                            <textarea class="contactme-text required requiredField radius" name="message" cols="10" rows="5" placeholder="Message" required="required"></textarea>
                            <span class="clear"></span>
                        </p>
                        <p>
                            <input  class="buttons radius send" value="Send !" type="submit"></input >
                            <input type="hidden" name="submitted" id="submitted" value="true" />
                        </p>
                    </form>

				"""
prof = """
				</div>
	
				<div id="secondary" class="grid_4 widget-area" role="complementary">
                                    %s %s 
				</div>
				<div class="clear"></div>
			</div>
    	</div>
""" 


def view(path):
    temp = path.split('?')
    uid = temp[1]
    f = "Models/blog.db"
    con = connect(f)
    c = con.cursor()
    c.execute("SELECT * FROM posts WHERE pid = '%s'" % uid)
    post = c.fetchone()
    head = header % (post[2], "Blog Posts", post[2])

    pro = prof % (login % ('none' , '') , signup % ('none' , ''))
    content = head + main % (post[2], post[3], post[4]) + pro + footer
    return content
