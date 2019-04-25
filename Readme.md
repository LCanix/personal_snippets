This program launch a process which create a new folder named with current timestamp (format : NAME_+yy-mm-dd_HH-MM-SS) and put a html file inside with the word OK or FAILED. 
When the process is ending, program will find if the created file contain OK or FAILED then exit with OK or KO status.

generated html file : 
<html>
   <head>
      <title>foo bar</title>
   </head>
   <body>
      <div id="bar">
         OK
      </div>
      <div id="foo">
         Another word
      </div>
   </body>
</html>

-----------------------
<html>
   <head>
      <title>foo bar</title>
   </head>
   <body>
      <div id="bar">
         FAILED
      </div>
      <div id="foo">
         Another word
      </div>
   </body>
</html>