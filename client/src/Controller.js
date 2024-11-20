export default class Controller{
   
      
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
     
       const response= await fetch('http://127.0.0.1:5000/upload_file',{
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
  
  async sortData (metadata, sort_order) {
    let post_data = {"metadata":metadata, "sortorder": sort_order}        
       let data;
       await fetch('http://127.0.0.1:5000/sort_data',{
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