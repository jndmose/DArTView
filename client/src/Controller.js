export default class Controller{
   
  static url = 'http://localhost:3000';
      
     async openFile (fl) {
        let data;
        var file;
         if (typeof fl.name !== 'undefined'){
           file= fl;
         }
         else{
         file = document.getElementById("upload").files[0];
         }
          const formData = new FormData();
          formData.append('file', file)
      try{
     
       const response= await fetch(Controller.url + '/upload_file',{
               method: 'POST',
               body: formData
                    });
                    if(!response.ok){
              
                      return new Error(`Response status: ${response.status}`);
                    }
                      
                   const json = await response.json();

                   return json;
                               
  }  catch(error){
    console.error(error.message);
    return error;
  }

     }
  
  async sortData (metadata1, sort_order1, metadata2, sort_order2, metadata3, sort_order3) {
       
    if(metadata1==='-unsorted-'){
      sort_order1="-unsorted-";
    }
    if(metadata2==='-unsorted-'){
      sort_order2="-unsorted-";
    }

    if(metadata3==='-unsorted-'){
      sort_order3="-unsorted-";
    }
        
    let post_data = {"metadata1":metadata1, 
      "sortorder1": sort_order1,
      "metadata2":metadata2, 
      "sortorder2": sort_order2,
        "metadata3":metadata3, 
        "sortorder3": sort_order3}       
       let data;
       await fetch(Controller.url + '/sort_data',{
               method: 'POST',
               headers:{
                'Content-Type': 'application/json',
               },
               body: JSON.stringify(post_data),
       })
                   .then(response => response.json())
                   .then(obj => 
                   {
                     data= obj;
                      
                    
                   });
                   return data;
                                  
    
  }
  

}