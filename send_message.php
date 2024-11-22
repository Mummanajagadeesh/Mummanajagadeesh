<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    $dateTime = date("Y-m-d H:i:s");

    // Validate input
    if (empty($name) || empty($email) || empty($message)) {
        echo "All fields are required.";
        exit;
    }

    // Email settings
    $to = "mummanajagadeesh97@gmail.com";
    $subject = "New Contact Form Submission";
    $body = "You have received a new message:\n\n" .
            "Name: $name\n" .
            "Email: $email\n" .
            "Message: $message\n" .
            "Date & Time: $dateTime\n";

    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";

    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "Your message has been sent successfully!";
    } else {
        echo "There was an error sending your message. Please try again.";
    }
}
?>
