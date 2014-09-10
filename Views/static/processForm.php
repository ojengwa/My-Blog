<?php

// Define some constants
define( "RECIPIENT_NAME", "John Smith" );
define( "RECIPIENT_EMAIL", "your@email.com" );
define( "EMAIL_SUBJECT", "Visitor Message" );

// Read the form values
$success = false;
$contactName = isset( $_POST['contactName'] ) ? preg_replace( "/[^\.\-\' a-zA-Z0-9]/", "", $_POST['contactName'] ) : "";
$email = isset( $_POST['email'] ) ? preg_replace( "/[^\.\-\_\@a-zA-Z0-9]/", "", $_POST['email'] ) : "";
$message = isset( $_POST['message'] ) ? preg_replace( "/(From:|To:|BCC:|CC:|Subject:|Content-Type:)/", "", $_POST['message'] ) : "";

// If all values exist, send the email
if ( $contactName && $email && $message ) {
	$recipient = RECIPIENT_NAME . " <" . RECIPIENT_EMAIL . ">";
	$headers = "From: " . $contactName . " <" . $email . ">";
	$success = mail( $recipient, EMAIL_SUBJECT, $message, $headers );
}

// Return an appropriate response to the browser
?>
<html>
	<head>
	 <title>Thanks!</title>
	</head>
	<body>
	<?php if ( $success ) echo "<p>Thanks for sending your message! We'll get back to you shortly.</p>" ?>
	<?php if ( !$success ) echo "<p>There was a problem sending your message. Please try again.</p>" ?>
	<p>Click your browser's Back button to return to the page.</p>
	</body>
</html>
