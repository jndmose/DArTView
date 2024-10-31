<script>
  import { onMount } from "svelte";
export let data = [];
export let cssVarStyles;
const width =  window.innerWidth;


const markers = data.length;
  const samples = data[0].length;
  const height=markers/2 + "px";
  
    onMount(() => {
   
        
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
    <div class="zoom-div" >
     <canvas id="canvas" width={width} height={height}></canvas>
</div>

<style>
.zoom-div{
	  padding: 20px;
	  height: calc(105vh - 15em);
      overflow-y: scroll;
}
</style>
  
