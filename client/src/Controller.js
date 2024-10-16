export default class Controller{
async  genotypic_map(){
    await fetch('http://127.0.0.1:5000/upload_file')
                .then(response => {
                    return response.json()
                });
               
 }

}