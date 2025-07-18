<?php
include 'db.php';
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $email = $_POST["email"];
    $password = $_POST["password"];
    $confirm = $_POST["confirm_password"];

    if ($password != $confirm) {
        die("Passwords do not match.");
    }

    $hashed = password_hash($password, PASSWORD_DEFAULT);

    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ? OR email = ?");
    $stmt->bind_param("ss", $username, $email);
    $stmt->execute();
    $result = $stmt->get_result();
    if ($result->num_rows > 0) {
        die("Username or Email already exists.");
    }

    $stmt = $conn->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $email, $hashed);
    if ($stmt->execute()) {
        echo "Signup successful. <a href='../index.php'>Login here</a>";
    } else {
        echo "Signup failed.";
    }
}
?>