<script>
  import { onMount } from "svelte";
export let data = [];
export let cssVarStyles;
const height=window.innerHeight;
const width =  window.innerWidth;
  
    onMount(() => {
   
        const markers = data.length;
        const samples = data[0].length;
        console.log(height,width)
        
  
        const canvas = document.getElementById("canvas");
        const markerScoreColors = cssVarStyles.split(";");

        if (canvas.getContext) {
          const ctx = canvas.getContext("2d");
         
          for( let j =0 ; j< markers;j++){
            for(let i=0; i< samples; i++){
              
            
            if(data[j][i]==="0"){
              
               ctx.fillStyle= markerScoreColors[2].split(":")[1];
        
            }
            else if(data[j][i]==="1"){
            ctx.fillStyle= markerScoreColors[1].split(":")[1];

            }
            else if(data[j][i]==="2"){
             ctx.fillStyle= markerScoreColors[0].split(":")[1];

            }

            else {
               ctx.fillStyle= markerScoreColors[3].split(":")[1];

            }

            ctx.fillRect(i*2, j*2, 2, 2);

          }
        }

        }

      
    });

    </script>
     <canvas id="canvas" width={width} height={height}></canvas>
  
