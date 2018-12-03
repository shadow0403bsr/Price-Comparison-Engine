<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<script type="text/javascript">
function validate(form)
{
	if(document.getElementById("isbn-radio-btn").checked){
		var qry = document.form.getElementById("searchform");
		if(qry.value.length==10 || qry.value.length==13){
			if(qry.value.match(/^[0-9]+$/))
				return true;
			else{
				document.form.query.focus();
      			return false;
			}
		}
		else{
			alert("make sure length is 10 or 13");
			document.form.query.focus();
			return false;
		}
	}
}
</script>
<style>
img.center 
{
display: block;
margin-left: auto;
margin-right: auto;
}

div.form
{
    display: block;
    text-align: center;
}

form
{
    display: inline-block;
    margin-left: auto;
    margin-right: auto;
    text-align: left;
}

{
    box-sizing: border-box;
}
.column 
{
    float: left;
    display: inline-block; 
    margin: 0 25px;
    width: 25%;
    padding: 2px;
    position: relative;
  	left: 12.5%;
}

/* Clearfix (clear floats) */
.row::after 
{
    content: "";
    clear: both;
    display: table;
}

/* Responsive layout - makes the columns stack on top of each other instead of next to each other */
@media screen and (max-width: 500px) 
{
    .column 
    {
        width: 100%;
    }
}

.image 
{
  opacity: 1;
  display: block;
  width: 100%;
  height: auto;
  transition: .5s ease;
  backface-visibility: hidden;
}

.middle 
{
  transition: .5s ease;
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 30%;
  transform: translate(-65%, -60%);
  -ms-transform: translate(-50%, -50%);
  text-align: left;
}

.column:hover .image 
{
  opacity: 0.5;
}

.column:hover .middle 
{
  opacity: 1;
}

.text
{
  color: white;
  font-size: 12px;
  padding: 12px 24px;
}
</style>
<head>
<meta charset="ISO-8859-1">
<title>Price Comparison Engine</title>
</head>
<body>
<a href='home.jsp'><img src="images/logo.jpg" alt="Price Comparison Logo" height="158" width="280" class="center">
</a>
<div class="form">
<form name="libgen" action="search.jsp">
	<input name="query" id="searchform" size="60" maxlength="200" value="">
<input type="submit" onclick="this.disabled=" disabled';="" document.forms.item(0).submit();'="" value="Search"><br>
<input type="radio" name="column" value="title" checked>Title
<input type="radio" name="column" value="author">Author
<input type="radio" name="column" value="identifier">ISBN
</form>
</div>
<br><br><br><br>
<div class="row">
  <div class="column">
    <img src="images/thriller.png" alt="Thriller" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#22346B;cursor:pointer" onclick="location.href='group.jsp?cat=Thriller'">Thriller</div>
  	</div>
  </div>
  <div class="column">
    <img src="images/nonfiction.png" alt="NonFiction" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#5A73A7;cursor:pointer" onclick="location.href='group.jsp?cat=Nonfiction'">NonFiction</div>
  	</div>
  </div>
  <div class="column">
    <img src="images/romance.png" alt="Romance" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#D92238;cursor:pointer" onclick="location.href='group.jsp?cat=Romance'">Romance</div>
  	</div>
  </div>
</div>
<div class="row">
  <div class="column">
    <img src="images/mystery.png" alt="Mystery" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#74BB88;cursor:pointer" onclick="location.href='group.jsp?cat=Mystery'">Mystery</div>
  	</div>
  </div>
  <div class="column">
    <img src="images/fantasy.png" alt="Fantasy" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#791F52;cursor:pointer" onclick="location.href='group.jsp?cat=Fantasy'">Fantasy</div>
  	</div>
  </div>
  <div class="column">
    <img src="images/horror.png" alt="Horror" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#718B40;cursor:pointer" onclick="location.href='group.jsp?cat=Horror'">Horror</div>
  	</div>
  </div>
</div>
<div class="row">
  <div class="column">
    <img src="images/science_fiction.png" alt="Science Fiction" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#151515;cursor:pointer" onclick="location.href='group.jsp?cat=Science+Fiction'">Science Fiction</div>
  	</div>
  </div>
  <div class="column">
    <img src="images/travel.png" alt="Travel" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#5972A5;cursor:pointer" onclick="location.href='group.jsp?cat=Travel'">Travel</div>
  	</div>
  </div>
  <div class="column">
    <img src="images/young_adult.png" alt="Young Adult" class = "image" style="width:50%">
    <div class="middle">
    <div class="text" style="background-color:#FEFE2D;cursor:pointer" onclick="location.href='group.jsp?cat=Young+Adult'">Young Adult</div>
  	</div>
  </div>
</div>
</body>
</html>