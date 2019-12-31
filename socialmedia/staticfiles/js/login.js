                 function Captcha(){
                     var alpha = new Array('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z');
                     var i;
                     for (i=0;i<6;i++){
                       var a = alpha[Math.floor(Math.random() * alpha.length)];
                       var b = alpha[Math.floor(Math.random() * alpha.length)];
                       var c = alpha[Math.floor(Math.random() * alpha.length)];
                       var d = alpha[Math.floor(Math.random() * alpha.length)];
                       var e = alpha[Math.floor(Math.random() * alpha.length)];
                       var f = alpha[Math.floor(Math.random() * alpha.length)];
                       var g = alpha[Math.floor(Math.random() * alpha.length)];
                      }
                    var code = a + ' ' + b + ' ' + ' ' + c + ' ' + d + ' ' + e + ' '+ f + ' ' + g;
                    document.getElementById("mainCaptcha").value = code
                  }
                  function ValidCaptcha(form){
                      var string1 = removeSpaces(document.getElementById('mainCaptcha').value);
                      var string2 = removeSpaces(document.getElementById('txtInput').value);
                      if (string1 == string2){
                        return true;
                      }
                      else{ 
					        
                              alert("Incorrect captcha");
	               	     				form.text.focus();
                  						return false;
                            }
                       }
				  
 function removeSpaces(string){
	 return string.split(' ').join('');
                  }
  function checkPassword(str)
  {
    var re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/;
    return re.test(str);
  }
function password()
{
	 if(!checkPassword(document.getElementById("id_password").value)) {
       
		document.getElementById("pasw").innerHTML="The password you have entered is not valid!";
        form.id_password.focus();
        return false;
      }
    
	else
	{
		document.getElementById("pasw").innerHTML=null;
		}
	return true;
}
function checkmatch()
{
	if(document.getElementById("id_password").value != document.getElementById("password2").value)
	 { 
	  document.getElementById("check").innerHTML="Please check that you've entered and confirmed your password!";
      form.password2.focus();
      return false;
    }
	else
	{
		document.getElementById("check").innerHTML=null;
		}
	}


  function firstname() 
{
    var x = document.getElementById('f').value;
    var match= /^[a-zA-Z]+$/;
    if (x == null || x == "") 
    {   
      document.getElementById("demo").innerHTML="First Name must be filled out";
        return false;
    }
    else if (x.search(match)!=0 )
    {       
             document.getElementById("demo").innerHTML="Invalid Character"; 
              return false;
    }
    else if (x.length > 35) 
    {
       document.getElementById("demo").innerHTML="Enter less than 35 characters"; 
       return false;
    }
  else
  {
      document.getElementById("demo").innerHTML=null;
      return true;    
   }     
}

function validateEmail(email) 
{
    var re=/\S+@\S+\.\S+/;
    return re.test(email);
}


