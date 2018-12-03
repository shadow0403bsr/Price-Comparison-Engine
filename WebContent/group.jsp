<%@page import="java.sql.*"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
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
<title><%=request.getParameter("cat").trim()%> </title>
</head>
<body>
<a href='home.jsp'><img src="images/logo.jpg" alt="Price Comparison Logo" height="158" width="280" class="center">
</a>
<h1 align="center"> <%=request.getParameter("cat").trim()%> Titles</h1>
			<%
			String genre = request.getParameter("cat").trim();
			try{
				Class.forName("com.mysql.cj.jdbc.Driver");
				String url = "jdbc:mysql://localhost:3306/project";
				String userId = "root";
				String password = "admin";
				Connection conn = DriverManager.getConnection(url, userId, password);
				Statement st = conn.createStatement();
				String sqlqry = "Select * from book, author where (genre1 = \'" + genre + "\' OR genre2 = \'" + genre + "\' OR genre3 = \'" + genre +"\') AND author_id = authorID ORDER BY rating desc LIMIT 12";
				ResultSet rs = st.executeQuery(sqlqry);
				int count=0;
				%>
				<h1></h1>
				<div class="row">
				<%
				while(rs.next())
				{					
					count++;
					String image = rs.getString("image_url");
					String nexturl = "view.jsp?id=" + rs.getString("isbn13");
				%>
			<div class="column">
			<img src="<%=image %>" width="100" height="150">
			<p><a href='<%=nexturl %>'> <!--link -->
				<%=rs.getString("title") %> <!--title -->
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