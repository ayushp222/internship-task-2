<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<form action="includes/login.php" method="POST">
    <h2>Login</h2>
    <input type="text" name="username_email" placeholder="Username or Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
    <p>Don't have an account? <a href="signup.html">Sign up</a></p>
</form>
</body>
</html>