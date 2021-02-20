function myFunc(){
      var text = "";
      var i;
      for (i = 0; i < 10; i++) {
        text += i + "<br>";
      }
      document.getElementById("demo").innerHTML = text;
	}
