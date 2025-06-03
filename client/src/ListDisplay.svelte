<script>
import VirtualList from './VirtualList.svelte';
import Modal, { bind } from 'svelte-simple-modal';
import Sort from './Sort.svelte';
import {geno_data, modal, sample_list, marker_list, marker_metadata} from './data.js';
import { onMount } from "svelte";

import { loader } from './loader';
import { writable  }from 'svelte/store';
import canvasSize from 'canvas-size';


// let start;
// let end;
let start1;
let end1;
let start2;
let end2;
let checkedX= false;
let checkedY = false;
let canvas;
let y=0;
let canvas_element;
const max_height= '35000';
let mtdata = [];
let styles = {
		'allele2': '#e74c3c',
		'allele1': '#2ecc71',
		'allele0': '#3498db',
      'allele-': '#f0f8ff'
	};

   $: cssVarStyles = Object.entries(styles)
		.map(([key, value]) => `--${key}:${value}`)
		.join(';');


     let SNP_metadata = ["CallRate", "OneRatioRef", "OneRatioSnp", "FreqHomRef", "FreqHomSnp", "FreqHets", "PICRef", "PICSnp", "AvgPIC", "AvgCountRef", "AvgCountSnp", "RepAvg"]
      for(let i=0; i<$marker_metadata.length;i++){
         if(SNP_metadata.includes($marker_metadata[i])){
            mtdata.push($marker_metadata[i])
         }
      }


  
  const sortData = () => modal.set(bind(Sort, {metadata:mtdata}));

  const handleClickZoom = ((which) => {
   start1=0;
   start2=0;
   end1=0;
   end2=0;
   if(which=='zoomX'){
      checkedX=!checkedX;
      handleZoomXaxis();
   }
   else{
      checkedY=!checkedY;
      handleZoomYaxis();
   }
   
   
  })

const handleZoomXaxis = (() => {
   handleDisplayNone();

})

const handleZoomYaxis = (() => {
   handleDisplayNone();
   
})

const handleDisplayNone = (() => {
   if(!checkedX || !checkedY){
      canvas_element.style.display='none';
   }

})

const markers = $geno_data.length;

const samples = $geno_data[0].length;

//width changes when zoom x is pressed
const height=markers;

const handleLongHeight = (() => {
   if(height > max_height){

   }
})

let loading = writable(false);

async function test_canvas (){
 // Optimized tests
canvasSize.maxArea({
  onSuccess({ width, height, testTime, totalTime }) {
    console.log('Success:', width, height, testTime, totalTime);
  },
});

}

function runUpdate(val) {
		loading.update(n => n=val);
  
  }
  


onMount(() => {

   
   
 canvas = document.getElementById("canvas");
 canvas_element = document.getElementById("zoom-div");
 test_canvas()
 

});

function hexToRGB(hex) {
  const bigint = parseInt(hex.replace("#", ""), 16);
  return [
    (bigint >> 16) & 255, // R
    (bigint >> 8) & 255,  // G
    bigint & 255          // B
  ];
}


$: if (checkedX & checkedY || checkedY & !checkedX) {
   runUpdate(true);

const blockWidth = checkedX ? 2 : 20;
const blockHeight = 1;
const width = samples * blockWidth;
const height = markers * blockHeight;

canvas.width = width;
canvas.height = height;

if (canvas_element) {
  canvas_element.style.display = 'block';
}

if (canvas.getContext) {
  const ctx = canvas.getContext("2d");

  // Convert hex to RGB arrays
  const alleleMap = {
    "0": hexToRGB(styles["allele0"]),
    "1": hexToRGB(styles["allele1"]),
    "2": hexToRGB(styles["allele2"]),
    "-": hexToRGB(styles["allele-"])
  };


  const imageData = ctx.createImageData(width, height);
  const data = imageData.data;

  for (let j = 0; j < markers; j++) {
    for (let i = 0; i < samples; i++) {
      const allele = $geno_data[j][i] ?? "-";
      const color = alleleMap[allele] || alleleMap["-"];

      for (let dx = 0; dx < blockWidth; dx++) {
        for (let dy = 0; dy < blockHeight; dy++) {
          const x = i * blockWidth + dx;
          const y = j * blockHeight + dy;
          const index = (y * width + x) * 4;
          data[index] = color[0];     // R
          data[index + 1] = color[1]; // G
          data[index + 2] = color[2]; // B
          data[index + 3] = 255;      // A
        }
      }
    }
  }

  ctx.putImageData(imageData, 0, 0);
}

   runUpdate(false);
}

const handleFilterData = () => {
   // Add functionality for the new button here
};
   
</script>
<div id='geno-map'  style="{cssVarStyles}">

<div class="controls">
	<span> Samples : {$geno_data[0].length}</span> &nbsp; <span>Markers : {$geno_data.length}</span> &nbsp;
	<!-- <button class="top-buttons" on:click={sortData} > Sort Data</button> -->
   <Modal show={$modal}>
      <button class="control-buttons" on:click={sortData}>Sort Data</button>
    </Modal>

    <div class="btn-group">
      <button type="button" class="btn btn-primary dropdown-toggle control-buttons" data-bs-toggle="dropdown" aria-expanded="false">
        Color Scheme
      </button>
      <ul class="dropdown-menu">
         <label>
            <input  style="padding:0" type="color" bind:value={styles['allele2']} />
            Hets
          </label>
          
          <label>
            <input  style="padding:0" type="color" bind:value={styles['allele0']} /> 
            Hom0
          </label>
          
            <label>
            <input  style="padding:0" type="color" bind:value={styles['allele1']} /> 
              Hom1
            </label>
          
            <label>
              <input style="padding:0" type="color" bind:value={styles['allele-']} /> 
                Missing
              </label>
       
               
       
      </ul>
    </div>

        <button class="control-buttons" style="position:relative; padding-left:26px;" on:click={ () => handleClickZoom('zoomX')}>
         <input type="checkbox" bind:checked={checkedX} style="position: absolute; top:10px; left: 4px;"> Zoom X-axis
        </button>

        <button class="control-buttons" style="position:relative; padding-left:26px;" on:click={() => handleClickZoom('zoomY')}>
         <input type="checkbox" bind:checked={checkedY} style="position: absolute; top:10px; left: 4px;"> Zoom Y-axis
        </button>

        <button class="control-buttons" style="position:relative; padding-left:26px;" on:click={handleFilterData}>
         Filter Data
        </button>

        

        
        
       
	</div>

  
<!-- {#if checkedY & checkedX} -->

<div id="zoom-div" style="display: none;"  use:loader={loading} >
   <canvas id="canvas"></canvas>
</div>

    <!-- <Zoom cssVarStyles= {cssVarStyles} /> -->

    {#if checkedX & !checkedY}
    <VirtualList  items= {$geno_data} bind:start={start1} bind:end={end1} let:item>
      <div class="row-data" style="border-bottom: none;">
       {#each item as score}
        <span  class="allele{score} data" style="min-width:2px;"></span>
        {/each}
  
        
     </div>
     
     </VirtualList>
     <div class="footer"><p>Showing {start1}-{end1} of {$geno_data.length} Markers</p></div>
     {/if}
     
{#if !checkedX & !checkedY }
<VirtualList  items= {$geno_data} bind:start={start2} bind:end={end2} let:item>
  
    <div class="row-data">
     {#each item as score , i}
      <span title="Sample: {$sample_list[i]}" class="allele{score} data">{score}</span>
      {/each}

      
   </div>
   
   
   </VirtualList>
   
   <div class="footer"><p>Showing {start2}-{end2} of {$geno_data.length} Markers</p></div>
   {/if}
   
    </div>

   
   

   <style>

.row-data{
      display: flex;
      border-bottom: 1pt solid #bebebe ;
      
      
   }

   .btn-group{
      margin: 6px;
   }
 

   .allele0{
      background-color: var(--allele0, #3498db);
   }

   .allele1{
      background-color: var(--allele1,#2ecc71);
   }

   .allele2{
      background-color: var(--allele2,#e74c3c);
   }

   .allele-{
      background-color: var(--allele-,aliceblue);

   }
   .alleleid{
      display: block;
   }

   .data{
      font-family: 'Source Code Pro', monospace;
      text-align: center;
      min-height: 20px;
      align-items: center;
      justify-content: center;
      min-width: 20px;
      font-size: 13px;
      display: flex;
      

   }
 
   .footer{
	margin-bottom: 5px;
	margin-top: 5px;
	font-family: 'Source Code Pro', monospace;
    text-align-last: center;
   }

   .top-buttons{
	display: inline-block;
                outline: 0;
                cursor: pointer;
                border: none;
                padding: 0 56px;
                height: 45px;
                line-height: 45px;
                border-radius: 7px;
                font-weight: 400;
                font-size: 16px;
                color: #696969;
                box-shadow: 0 4px 14px 0 rgb(0 0 0 / 10%);
                transition: background 0.2s ease,color 0.2s ease,box-shadow 0.2s ease;
   }

   .top-buttons:hover{

	background: rgba(255,255,255,0.9);
	box-shadow: 0 6px 20px rgb(93 93 93 / 23%);

   }


   #geno-map {
      width: 100%;
	  padding-left: 40px;
     padding-right: 20px;
     padding-top: 20px;
     padding-bottom: 20px;
	  height: calc(105vh - 15em);
      max-width: 1850px;
      display: inline-block;
     
	}

    .controls{
	padding-left: 20px;
   height: 80px;
   margin-bottom: 10px;
   margin-top: 5px;
}
#zoom-div{
	  padding: 20px;
	  height: calc(105vh - 15em);
      overflow-y: scroll;
}
.control-buttons{
   border-radius: 12px;
}

   </style>

