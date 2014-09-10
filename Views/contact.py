from static import *
sign = signup % ('none' , '')
main = """	<div id="main" class="site-main container_16">
			<div class="inner">
				<div id="primary" class="grid_11 suffix_1">
				<article class="single">
						
						<div class="entry-content">
							
							<div class="long-description">
								<h3>Drop a note with me.</h3>
								<br/>
							</div>
								<form action="contact.do" id="contact-form" method="post">

									<p>
										<label for="contactName"></label>
										<input class="radius"  type="text" name="contactName" id="contactName" value="" placeholder="Name*" required/>
										<span class="clear"></span>
									</p>
									<p>
										<label for="email"></label>
										<input class="radius" type="email" name="email" id="email" value="" placeholder="Email Adress*" required/>
										<span class="clear"></span>
									</p>
									<p>
										<label for="commentsText"></label>
										<textarea class="contactme-text required requiredField radius" name="message" cols="10" rows="10" placeholder="Message" required="required"></textarea>
										<span class="clear"></span>
									</p>
									<p>
										<input  class="buttons radius send" value="Send !" type="submit"></input >
										<input type="hidden" name="submitted" id="submitted" value="true" />
									</p>
								</form>
	
							
							<div class="clear"></div>
							
						</div>

						<div class="clear"></div>
					
					</article>
					
				</div>
	
				<div id="secondary" class="grid_4 widget-area" role="complementary">

				    %s %s

				</div>
				<div class="clear"></div>
			</div>
		</div>
""" % (sign, login % ('none' , ''))

content = header % ("Content Me", "Contact Page", "Contact Us")

content += main + footer

def view():
    return content
