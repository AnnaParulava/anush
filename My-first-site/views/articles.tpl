% rebase('layout.tpl', title=title, year=year)
%import json

<head>
<title> Articles </title>
<style>
    .content{
        width:400px;
        height:200px;
        border:1px;
        display:inline-block;
    }
     p {
    font-family: Verdana, Arial, Helvetica, sans-serif; 
    font-size: 12pt; 
   }

    </style>
</head>
<body>

<div class="jumbotron">
    <h1>Articles to read</h1>
</div>

     <style>
    .jumbotron{
        background-color: #FFCC33  
    }
    </style>

%with open('./articles.json') as articles:
%data=json.load(articles)
%for key, value in data.items():
    <div style="border-bottom: 1px solid Snow">
        <h3 style="margin-top:40px">
        {{value['title']}}
        </h3>
        <p>
        {{value['description']}}
        </p>
        <p style="font-size:10pt">
        By {{value['author']}}
        </p>
        <p style="font-size:10pt">
        Published on {{value['published_date']}}, written on {{value['written_date']}}
        </p>
        <p style="font-size:10pt">
        Phone {{value['phone']}}
        </p>
        <p style="font-size:10pt">
        Email {{value['author_email']}}
        </p>
    </div>
%end


<h2> Add your own article</h2>

<form action="/articles" method="post">
        <p><input rows="2" cols="55" name="TITLE" placeholder="Your article's title"></p>
        <p><textarea type="text" size="55" name="DESCRIPTION" placeholder="Your article's description"></textarea></p>
        <p><input rows="2" cols="55" name="AUTHOR" placeholder="Enter your name.."></p>
        <p><input rows="2" cols="55" name="PHONE" placeholder="Enter your phone.."></p>
        <p><input rows="2" cols="55" name="AUTHOR_EMAIL" placeholder="Enter your email.."></p> 
        <p><input rows="2" cols="55" name="WRITTEN_DATE" placeholder="Date of writing of the article"></p> 
        <p><input type="submit" value="Add" class="btn btn-default"></p>
</form>

</body>