$(document).ready(function()
{

		

  

    $myFunction = function(id1){ 

        
    	var id = $(id1).attr('id');
     
  		var selid="selid"+id;
      //var sel = $('<select id='+selid+'  class="form-control" >')\
      var sel = $('<select class="form-control sel_auto sel_" id='+selid+'>');
          $(sites).each(function() {
           sel.append($("<option>").attr('value',this.id).text(this.name));
          });  
          


         var row = $("<tr/>");
         sel =  $("<td/>").append(sel)
         var sel1id="sel1id"+id;
         var sel1 = $('<select class="form-control" id='+sel1id+'>');
         sel1.append($("<option>").attr('value',"3200").text("3200"));
         sel1.append($("<option>").attr('value',"3100").text("3100"));
         sel1.append($("<option>").attr('value',"1").text("Specify in Loads"));
         sel1 =  $("<td/>").append(sel1)

         
         var inpid="inpid"+id
         var inp = $("<td/>").append("<input type='text' placeholder='Unit price' value='"+sites[0].Unit_price+"' class='form-control' id="+inpid+" readonly>");
         

         var lodid="lodid"+id
         var lod = $("<td/>").append("<input type='text' placeholder='No of Loads'  class='form-control textinput' id="+lodid+" required>");
         

         var totid="totid"+id
         var tot = $("<td/>").append("<input type='text' placeholder='Total price'  class='form-control' id="+totid+" readonly>");
         

         var rm_button = $("<td/>").append("<button   class='btn btn-danger remove_b' >Remove</button>");
         row.append(sel);
         row.append(sel1);
         row.append(lod);
         row.append(inp);
         row.append(tot);
         row.append(rm_button);

        
         
       $("#ttb").append(row);
    
     id=parseInt(id)+1
     $(id1).attr('id',id);
    change_sel();

    $(document).on('click', '.remove_b',function(){
        $(this).closest ('tr').remove ();
    });
    $('input.textinput').on('input',function(e){
        var i= $(this).attr('id');
        tot_id=i.replace('lod','tot');
        unit_price_id= i.replace('lod','inp');
        up= $('input[id='+unit_price_id+']').val();
        sel1_id=i.replace('lod','sel1');
        sel1=$('select[id='+sel1_id+']').children("option:selected").val();

    
        console.log(sel1)
        $('input[id='+tot_id+']').val(up*$(this).val()*sel1)
       });
  
    }


 

    function change_sel () {
    $('.sel_').on('change', function() {
    var i= $(this).attr('id');
    i=i.replace('sel','inp');
    console.log(i);
    var sel_id = $(this).children("option:selected").val();
    console.log(sel_id);
    var price=1
     $(sites).each(function() {
     if (this.id == sel_id) { 
     price=this.Unit_price
   	  }
     });
    console.log(price);
    $('input[id='+i+']').val(price)
    
});
  }
    $myFunction(document.getElementById(0));
   // this.attr("id","2");
   
    


    
    

  

   
});