<script>
  import { onMount } from "svelte";
export let data = [];
export let cssVarStyles;
  
    onMount(() => {
      function draw() {
        
        let count=0;
        let cnt =0;
        const markers = data.length;
        const samples = data[0].length;
  
        const canvas = document.getElementById("canvas");
        const markerScoreColors = cssVarStyles.split(";")
        

        if (canvas.getContext) {
          const ctx = canvas.getContext("2d");
         
          for( let j =0 ; j< markers;j++){
            for(let i=0; i< samples; i++){
            
            if(data[i][j]==="0"){
               ctx.fillStyle= markerScoreColors[2].split(":")[1];
               ctx.fillRect(i+5, j+2, 5, 2);
            }
            else if(data[i][j]==="1"){
            ctx.fillStyle= markerScoreColors[1].split(":")[1];
            ctx.fillRect(i+5, j+2, 5, 2);

            }
            else if(data[i][j]==="2"){
             ctx.fillStyle= markerScoreColors[0].split(":")[1];
             ctx.fillRect(i+5, j+2, 5, 2);
            }

            else if(data[i][j]==="-"){
               ctx.fillStyle= markerScoreColors[3].split(":")[1];
               ctx.fillRect(i+5, j+2, 5, 2);
            }
         
          

          }
        }
          
          
        }
      }
      draw();
    });
    </script>
     <canvas id="canvas" width="1000" height="1000"></canvas>
  
