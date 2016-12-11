 d3.csv("datos/datos.csv",function(d){
      var cat = d.categorias.split("|#|")
      var sis = d.sistemas.split("|#|")
      var fam = d.familia.split("|#|")
      return {
        anio : d.anio,
        jugadores : d.jugadores,
        tiempo : d.tiempo,
        edad : d.edad,
        nombre : d.nombre,
        categorias : cat,
        sistemas : sis,
        familia : fam,
        nota : +d.nota/1000,
        cantidad : +d.cantidad,
        desviacion : +d.desviacion
      };
    }, function(data){
    	var cat = [];
    	var prom = [];
    	var cant = [];
    	for (i=0;i<555;i++){
    		for(j=0;j<data[i].categorias.length;j++){
    			var pos = cat.indexOf(data[i].categorias[j]);
        		if (pos!=-1){
        			prom[pos] = prom[pos] + data[i].nota;
        			cant[pos] = cant[pos] + 1;
        		}
        		else{
        			cat.push(data[i].categorias[j]);
        			prom.push(data[i].nota);
        			cant.push(1);
        		}
        	}
    	}
        for(i = 0;i<cat.length;i++){
        	console.log(cat[i]);
        	console.log(prom[i]/cant[i]);
        }
    });