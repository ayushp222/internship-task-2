<?php
include 'db.php';
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST["username_email"];
    $pass = $_POST["password"];

    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ? OR email = ?");
    $stmt->bind_param("ss", $user, $user);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows === 1) {
        $row = $result->fetch_assoc();
        if (password_verify($pass, $row["password"])) {
            $_SESSION["user"] = $row["username"];
            header("Location: ../dashboard.php");
            exit();
        }
    }
    echo "Incorrect username/email or password.";
}
?>