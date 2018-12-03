<%@page import="java.sql.*"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<script type="text/javascript">
function validate()
{
	if(document.getElementById("isbn-radio-btn").checked)
	{
		var qry = document.getElementById("searchform");
		if(qry.value.length==10)
		{
			if(qry.value.match(/^[0-9X]+$/))
				return true;
			else
			{
				alert("ISBN10 contains only numbers or X");
				return false;
			}
		}
		else if(qry.value.length==13)
		{
			if(qry.value.match(/^[0-9]+$/))
				return true;
			else
			{
				alert("ISBN13 only consists numbers");
				return false;
			}
			
		}
		else
		{
			alert("ISBN is 10 or 13 characters long");
			return false;
		}
	}
	return true;
}
</script>
<%
			String qry = request.getParameter("id").trim();
			String authorquery = ""; 
			String author = "";
			String genre = "";
			try{
				Class.forName("com.mysql.cj.jdbc.Driver");
				String url = "jdbc:mysql://localhost:3306/project";
				String userId = "root";
				String password = "admin";
				Connection conn = DriverManager.getConnection(url, userId, password);
				Statement st = conn.createStatement();
				String sqlqry = "Select * from book, author where (isbn=\'" + qry+ "\' or isbn13=\'" + qry + "\') AND author_id = authorID";
				ResultSet rs = st.executeQuery(sqlqry);
				while(rs.next())
				{					
					String image = rs.getString("image_url");
					authorquery = rs.getString("author_id");
					author = rs.getString("authorName");
					genre = rs.getString("genre1");
				%>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style type="text/css">
		img.center 
		{
		display: block;
		margin-left: auto;
		margin-right: auto;
		}
		img.left
		{
			display: block;
			mrg
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
		.column {
  		float: left;
  		width: 20%;
  		padding: 1px;
		}

		/* Clear floats after image containers */
		.row::after {
  		content: "";
  		clear: both;
 		display: table;
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

		.t1,td{
			position: left;
			margin-left: 10px;
		}
		.checked {
    	color: orange;}
	</style>
<meta charset="ISO-8859-1">
<title><%=rs.getString("title") + " - Product Page" %></title>
</head>
<body>
	<table class="t1">
		<tr>
			<td width="20%" align="left">
				<a href='home.jsp'><img src="images/logo.jpg" alt="Price Comparison Logo" height="158" width="280" class="center">
				</a>
			</td>
			<td width="80%" align="left">
				<div class="form">
					<form name="libgen" action="search.jsp" onsubmit="return validate()">
						<input name="query" id="searchform" size="60" maxlength="200" value=""/>
						<input type="submit" value="Search"/><br>
						<input type="radio" name="column" value="title" checked/>Title
						<input type="radio" name="column" value="author"/>Author
						<input type="radio" name="column" id="isbn-radio-btn" value="identifier"/>ISBN
					</form>
				</div>
			</td>
		</tr>
	</table>
	<table>
		<tr>
						<td>
							<img src="<%=image %>" width="200" height="300">
						</td>
						<td>
							<h3><%=rs.getString("title") %></h3><!--hyperlink on title  -->
							<h4><%=rs.getString("authorName") %></h4><!-- author -->
							<%
							int i;
							String r = rs.getString("rating");
							float rating = Float.parseFloat(r);
							for(i=0; i<Math.round(rating); i++)
							{
								out.print("<span class=\"fa fa-star checked\"></span>");
							}
							for(;i<5;i++)
							{
								out.print("<span class=\"fa fa-star\"></span>");
							}
							%>
							&nbsp;&nbsp;<%=rs.getString("rating") %>
							<p><%=rs.getString("genre1") %>; <%=rs.getString("genre2") %>; <%=rs.getString("genre3") %></p>
							<p><b>ISBN13:</b> <%=rs.getString("isbn13") %>; <b>ISBN10:</b> <%=rs.getString("isbn") %></p>
						</td>
						<td></td><td></td><td></td><td></td><td></td>
						<td>
							<a href='<%=rs.getString("amazon_url")%>' target="_blank">
								<img src="images/amazon_logo.png" width="50" height="50">
							</a>							
							<p>Amazon Price:</p> 
							<p> &#x20b9; <b><%=rs.getString("amazon_price") %></b> </p>
						</td>
						<td></td><td></td><td></td></td><td></td><td></td>
						<td>
							<a href='<%=rs.getString("flipkart_url")%>' target="_blank">
								<img src="images/flipkart_logo.png" width="50" height="50">
							</a>							
							<p>Flipkart Price:</p> 
							<p> &#x20b9; <b><%=rs.getString("flipkart_price") %></b> </p>
						</td>
						<td></td><td></td><td></td></td><td></td><td></td>
						<td>
							<a href='<%=rs.getString("infibeam_url")%>' target="_blank">
								<img src="images/infibeam_logo.png" width="50" height="50">
							</a>							
							<p>Infibeam Price:</p> 
							<p> &#x20b9; <b><%=rs.getString("infibeam_price") %></b> </p>
						</td>
						<td></td><td></td><td></td></td><td></td><td></td>
						<td>
							<a href='<%=rs.getString("snapdeal_url")%>' target="_blank">
								<img src="images/snapdeal_logo.png" width="50" height="50">
							</a>							
							<p>Snapdeal Price:</p> 
							<p> &#x20b9; <b><%=rs.getString("snapdeal_price") %></b> </p>
						</td>
						<td>
						</td>
		</tr>
		<%
				}
				conn.close();			
			}
			catch(Exception e){
				out.print(e);
				e.printStackTrace();
			}	
			
		%>
	</table>
	<%
	try{
		Class.forName("com.mysql.cj.jdbc.Driver");
		String url = "jdbc:mysql://localhost:3306/project";
		String userId = "root";
		String password = "admin";
		Connection conn = DriverManager.getConnection(url, userId, password);
		Statement st = conn.createStatement();
		String sqlqry = "Select * from book, author where author_id = \'" + authorquery + "\' AND author_id = authorID AND isbn13 <> " + qry + " ORDER BY rating desc LIMIT 4";
		ResultSet rs1 = st.executeQuery(sqlqry);
		int count = 0;
		%>
		<h1>More from <%=author %> </h1>
		<div class="row">
		<%
		while(rs1.next())
		{		
			count++;
			String image = rs1.getString("image_url");
			String nexturl = "view.jsp?id=" + rs1.getString("isbn13");
		%>	
			<div class="column">
			<img src="<%=image %>" width="100" height="150">
			<p><a href='<%=nexturl %>'> <!--link -->
				<%=rs1.getString("title") %> <!--title -->
				</a>
			</p>
			</div>
		
		<%
		}
		if(count==0)
		{
			out.print("<img src=\"images/spider.jpg\" width=\"100\" height=\"100\" class=\"center\">");
			out.print("<p align=\"center\">No other books from this author</p>");
		}
		conn.close();
		%>
		</div>		
		<%	
			}
			catch(Exception e){
				out.print(e);
				e.printStackTrace();
			}	
		%>
	<%
	try{
		Class.forName("com.mysql.cj.jdbc.Driver");
		String url = "jdbc:mysql://localhost:3306/project";
		String userId = "root";
		String password = "admin";
		Connection conn = DriverManager.getConnection(url, userId, password);
		Statement st = conn.createStatement();
		String sqlqry = "Select * from book, author where (genre1 = \'" + genre + "\' OR genre2 = \'" + genre + "\' OR genre3 = \'" + genre +"\') AND author_id = authorID AND isbn13 <> " + qry + " ORDER BY rating desc LIMIT 4";
		ResultSet rs1 = st.executeQuery(sqlqry);
		int count = 0;
		%>
		<h1>More in <%=genre %> </h1>
		<div class="row">
		<%
		while(rs1.next())
		{		
			count++;
			String image = rs1.getString("image_url");
			String nexturl = "view.jsp?id=" + rs1.getString("isbn13");
		%>	
			<div class="column">
			<img src="<%=image %>" width="100" height="150">
			<p><a href='<%=nexturl %>'> <!--link -->
				<%=rs1.getString("title") %> <!--title -->
				</a>
			</p>
			</div>
		
		<%
		}
		if(count==0)
		{
			out.print("<img src=\"images/spider.jpg\" width=\"100\" height=\"100\" class=\"center\">");
			out.print("<p align=\"center\">No other books from this author</p>");
		}
		conn.close();
		%>
		</div>		
		<%	
			}
			catch(Exception e){
				out.print(e);
				e.printStackTrace();
			}	
		%>	
</body>
</html>