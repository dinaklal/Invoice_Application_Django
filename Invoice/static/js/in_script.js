$(document).ready(function()
{

    $myFunction = function(id){ 
        
        var tbody= document.getElementById("ttb")
        
          var selid="selid"+id
          var sel = $('<select id='+selid+'>');
          
          $(sites).each(function() {
           sel.append($("<option>").attr('value',this.id).text(this.name));
          });   
        
         var markup = "<tr><td>"+sel+"</td>dfdf<td></td><td></td></tr>";
         console.log(markup)

         $("#ttb").append(sel);
        alert('You have successfully defined the function!'); 

    }
    $myFunction(0);
    

  

   
});