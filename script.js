// JavaScript code for handling login and logout
document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    
    // Add code to validate login credentials and redirect to the dashboard
    // For simplicity, we're just redirecting to dashboard.html here
    window.location.href = 'dashboard.html';
});

document.getElementById('logout-btn').addEventListener('click', function () {
    // Add code to log the user out and redirect to the login page
    window.location.href = 'index.html';
});


function isStrongPassword(password) {
    const lowercaseRegex = /[a-z]/;
    const uppercaseRegex = /[A-Z]/;
    const digitRegex = /[0-9]/;
    const specialRegex = /[^A-Za-z0-9]/; // Matches any character that is not a letter or digit
    
    const hasLowercase = lowercaseRegex.test(password);
    const hasUppercase = uppercaseRegex.test(password);
    const hasDigit = digitRegex.test(password);
    const hasSpecial = specialRegex.test(password);
    
    const isLengthValid = password.length >= 8;

    return hasLowercase && hasUppercase && hasDigit && hasSpecial && isLengthValid;
}
function logic(){
    var choose = document.getElementById("Choice").value;
    console.log(choose)
    if (choose == 'y'){
        var password=document.getElementById("password1").value;
        if(isStrongPassword(password)){
            return true;
        }
        else{
            alert("Choose strong password");
            return false;
        }
    }
    else{
        alert("You should agree.")
        return false;
        
    }
}

function mode(){
    var mod = document.getElementById("logout-btn").value;
    console.log(mod)
    // var uname = document.getElementById("").value;
    // var passwrd= document.getElementById("").value;
    $.ajax({
        method: 'POST',
        url:"/logout/",
        data:{"name":uname,"password":passwrd},
        success : function(response){
            console.log(response);
        },

    })
}