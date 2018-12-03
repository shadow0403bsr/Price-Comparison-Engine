<%@page import="java.sql.*"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
	<title><%=request.getParameter("query") + " - Search Results" %></title>
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

		.t1,td{
			position: left;
			margin-left: 10px;
		}
		.checked {
    	color: orange;}
	</style>
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
					<form name="libgen" action="search.jsp" method="GET">
						<input name="query" id="searchform" size="60" maxlength="200" value="">
						<input type="submit" onclick="this.disabled=" disabled';="" document.forms.item(0).submit();'="" value="Search"><br>
						<input type="radio" name="column" value="title" checked>Title
						<input type="radio" name="column" value="author">Author
						<input type="radio" name="column" value="identifier">ISBN
					</form>
				</div>
			</td>
		</tr>
	</table>

	<!-- table for search results -->
	<table>
		
		<%
			String data_type = (String)request.getParameter("column").trim();
			String qry = request.getParameter("query").trim();
			try{
				Class.forName("com.mysql.cj.jdbc.Driver");
				String url = "jdbc:mysql://localhost:3306/project";
				String userId = "root";
				String password = "admin";
				Connection conn = DriverManager.getConnection(url, userId, password);
				Statement st = conn.createStatement();
				ResultSet rs = null;
				int count = 0;
				if(data_type.equals("title"))
				{
					String sqlqry = "Select * from book, author where title like \'%" + qry + "%\' AND author_id = authorID";
					rs = st.executeQuery(sqlqry);	
				}
				else if(data_type.equals("identifier"))
				{
					String sqlqry = "Select * from book, author where (isbn=\'" + qry+ "\' or isbn13=\'" + qry + "\') AND author_id = authorID";
					rs = st.executeQuery(sqlqry);	
				}
				else if(data_type.equals("author"))
				{
					String sqlqry = "Select * from book, author where author_id=(Select authorID from author where authorName like \'%"+ qry +"%\') AND author_id = authorID order by rating desc";
					rs = st.executeQuery(sqlqry);	
				}
				
				//ResultSetMetaData rsmd = rs.getMetaData();
				//int columnsNumber = rsmd.getColumnCount();
				//out.print("column" + columnsNumber);
				while(rs.next())
				{		
					count++;
					String image = rs.getString("image_url");
					String nexturl = "view.jsp?id=" + rs.getString("isbn13");
				%>
					<tr>
						<td>
							<img src="<%=image %>" width="200" height="300">
						</td>
						<td>
							<!--  if below <a> tag or above img tag doesnt pick url, do this - https://stackoverflow.com/questions/6501265/simple-error-due-to-use-of-double-quotes-in-a-jsp-file/6501305 -->
							<h3><a href='<%=nexturl %>'> <!--link -->
								<%=rs.getString("title") %> <!--title -->
							</a></h3><!--hyperlink on title  -->
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
							<p><%=rs.getString("genre1") %></p><!-- genre -->
							<p><%=rs.getString("genre2") %></p><!-- genre -->
							<p><%=rs.getString("genre3") %></p><!-- genre -->
							<p>ISBN13: <%=rs.getString("isbn13") %>; ISBN10: <%=rs.getString("isbn") %></p>
						</td>
					</tr>	
					<%
		}
		if(count==0)
		{
			out.print("<img src=\"images/spider.jpg\" width=\"300\" height=\"300\" class=\"center\">");
			out.print("<p align=\"center\" style=\"font-size:300%;\">No books found.</p>");
			out.print("<p align=\"center\" style=\"font-size:150%;\">Try another search term.</p>");			
		}
		conn.close();
		%>
		<%
			
			}
			catch(Exception e){
				out.print(e);
				e.printStackTrace();
			}

		%>
	</table>
</body>
</html>