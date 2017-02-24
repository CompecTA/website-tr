<?php
session_cache_limiter('nocache');
header('Expires: ' . gmdate('r', 0));
header('Content-type: application/json');

$Recipient = 'ekrem.seren@compecta.com,sasmaz@compecta.com,info@compecta.com'; // <-- Set your email here

$subject = $_POST['subject'];

if($Recipient) {

	$Name = htmlspecialchars($_POST['name'], ENT_QUOTES);
	$Email = htmlspecialchars($_POST['email'], ENT_QUOTES);
	$Subject = "[WEBSITE] ";
	$Subject .= htmlspecialchars($_POST['subject'], ENT_QUOTES);
	$Message = htmlspecialchars($_POST['message'], ENT_QUOTES);

	$Email_body = "";
	$Email_body .= "<strong>Message from CompecTA website contact form</strong>" . "\n<br>" .
				   "<strong>From:</strong> " . $Name . "\n<br>" .
				   "<strong>Email:</strong> " . $Email . "\n<br>" .
				   "<strong>Subject:</strong> " . $Subject . "\n<br>" .
				   "<strong>Message:</strong> " . $Message . "\n";

	$Email_headers = "";
	$Email_headers .= "Content-Type: text/html; charset=UTF-8";
	$Email_headers .= 'From: ' . $Name . ' <' . $Email . '>' . "\r\n".
					  "Reply-To: " .  $Email . "\r\n";

	$sent = mail($Recipient, $Subject, $Email_body, $Email_headers);

	if ($sent){
		$emailResult = array ('sent'=>'yes');
	} else{
		$emailResult = array ('sent'=>'no');
	}

	echo json_encode($emailResult);

} else {

	$emailResult = array ('sent'=>'no');
	echo json_encode($emailResult);

}
?>
