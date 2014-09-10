from static import *
from Models.Users import Users
main = """<div id="main" class="site-main container_16">
			<div class="inner">
				<div id="primary" class="grid_11 suffix_1">
					<article class="single">
						
						<div class="entry-content">
							
							<div class="long-description">
                                                            <h5> %s </h5>
                                                            <h3>Share your thoughts:</h3><br />
								<form action="post" id="contact-form" method="post">

									<p>
										<label for="title"></label>
										<input class="radius" type="text" name="title" id="title" value="" placeholder="Post Title*" required/>
										
										<span class="clear"></span>
									</p>
										<input class="radius" type="hidden" name="uid" id="title" value="%s" placeholder="Post Title*" required/>									
									<p>
										<label for="content"></label>
										<textarea class="contactme-text required requiredField radius" name="content" cols="10" rows="10" placeholder="Post Contents" required="required"></textarea>
										<span class="clear"></span>
									</p>
									<p>
										<input  class="buttons radius send" value="Post It!" type="submit"></input >
									</p>
								</form>
	
							
							<div class="clear"></div>
							
						</div>

						<div class="clear"></div>
					
					</article>

					
				</div>
	
				<div id="secondary" class="grid_4 widget-area" role="complementary">

                                %s

				</div>
				<div class="clear"></div>
			</div>
		</div>
""" 
content = header % ("Create Post", "New Post", "Create Post") + main + footer
def view(path=' ', uid = ' ', success = False):
    if '?' in path:
        temp = path.split('?')
        uid = temp[1]
        if uid == ' ':
            return "Refresh 0; url=%s" % '/index.do'
    u = Users()
    uid, name = u.getUser(uid)
    print uid, name
    if success:
        return content % ('Created Successfully', uid, profile % ('', name, uid))
    else:
        return content % ('', uid, profile % ('', name, uid))
