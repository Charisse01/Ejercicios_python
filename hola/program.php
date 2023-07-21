 
<html>
<body>
    <?php
    $A=$_GET['A'];
    $B=$_GET['B'];
    $C=$_GET['C'];

if (($A==$B) && ($B==$C)){
     print "Hay 3 numeros iguales a $A";
}else{
     if ($A==$B){
         print "Hay 2 numeros iguales a $A";
     }else{
         if ($A==$C){
               print "Hay 2 numeros iguales a $A";
	 }else{
	     if ($B==$C){
	        print "Hay 2 numeros iguales a $B";
	     }else{
	        print "No hay numeros iguales";
             }
	  }
     }
}
?>
</body>
</html>